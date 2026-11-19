"""Landing pages for search engines: one page per vendor (docs/vendors/<slug>/) and one page per
game platform (docs/games/<slug>/), plus an index page for each. pages.build() calls build().

Matching: each rule is a case-insensitive regex, searched in the entry's name, description and
topics (topic hyphens read as spaces). The rules favour precision over recall: a page lists only
entries whose own text names the vendor or the platform. A page needs MIN entries.

Check the rules after an edit:  python3 scripts/landing.py [slug ...]
(prints the count of each page and 15 random matches for the named pages, or for all pages).
"""
import collections, html, json, os, random, re, shutil, sys

GAMES = "Game Decompilations & Reimplementations"
MIN = 5

# Vendor pages. (slug, name, products, regex[, categories]). The regex is searched in name and description
# only (topics are too loose for brands), after STRIP removes phrases that name a brand only as an API format
# or a side feature ("OpenAI-compatible", "Discord RPC"). Entries in the game category are left out unless
# the slug is in VENDOR_GAMES: game decompilations belong on the platform pages. With categories, only
# entries in those categories count (AI brands are named as formats and backends everywhere else).
AI = ("AI Tools & LLM Clients",)
STRIP = re.compile(
    r"\b(openai|anthropic|claude|gemini|codex)((\s*/\s*|\s+(and|or)\s+)(openai|anthropic|claude|gemini|codex))*"
    r"[- ]?(compatible|format|style|api (format|interfaces?|endpoints?|traffic)|(messages|responses|chat completions) api)\b"
    r"|\b(openai|anthropic|claude|gemini|codex)(\s*/\s*(openai|anthropic|claude|gemini|codex|responses))+\s*(apis?|protocols?|proxy|endpoints?)\b"
    r"|\b(into|to|as) (an? )?(standard )?openai\b|-to-openai\b|\bopenai api (wrapper|proxy|gateway|server)\b|\b(openai|anthropic)(/\w+)* endpoints\b"
    r"|\bdiscord (rpc|rich presence)|\b(on|for) apple silicon macs?|\brunning on apple silicon|\bsteam deck\b|\btelegram bots?\b|\b(to|via) telegram\b|\bdiscord bots?\b", re.I)
VENDOR_NOT = {"lg": r"\bpalm\b", "telegram": r"\bdsmr\b|\bmeters?\b|\bw?m-bus\b", "segway-ninebot": r"copilot|microsoft 365"}  # entries that name the brand but are about something else
VENDOR_HOME = {"apple": "Apple Ecosystem"}  # every entry in this category counts for the vendor
VENDORS = [
    # Smart home and IoT
    ("tuya", "Tuya", "Smart Life devices", r"\btuya|localtuya|tinytuya|smart ?life\b"),
    ("xiaomi", "Xiaomi", "Mi Home, Mijia and Redmi devices", r"xiaomi|\bmijia\b|\bmi ?home\b|\bmiio\b|\bmiot\b|\bmi ?band\b|\bxiaoai|\bredmi\b|\bmiui\b|\bhyperos\b"),
    ("roborock", "Roborock", "robot vacuums", r"roborock"),
    ("dreame", "Dreame", "robot vacuums", r"\bdreame"),
    ("ecovacs", "Ecovacs", "Deebot robot vacuums", r"ecovacs|\bdeebot"),
    ("irobot", "iRobot", "Roomba robot vacuums", r"\birobot\b|roomba"),
    ("eufy", "Eufy", "cameras, doorbells and vacuums", r"\beufy"),
    ("philips-hue", "Philips Hue", "lights and bridges", r"philips ?hue|\bhue (bridge|lights?|bulbs?|api|entertainment|sync|emulator|hub)|\bphue\b|diyhue"),
    ("ikea", "IKEA", "Tradfri and Dirigera smart home", r"\bikea\b|tr[aå]dfri|dirigera"),
    ("sonos", "Sonos", "speakers", r"\bsonos"),
    ("ring", "Ring", "doorbells and cameras", r"\bring (doorbell|camera|alarm|api|app|devices?|intercom)|ring\.com|\bring[ -](client|mqtt)"),
    ("google-nest", "Google Nest", "thermostats, cameras and speakers", r"google nest|\bnest (thermostat|protect|cam|camera|hub|api|learning|wifi|mini|audio|doorbell|devices?|smoke)|nolongerevil|google home\b"),
    ("chromecast", "Chromecast", "Google Cast devices", r"chromecast|google ?cast|\bcastv2"),
    ("amazon-alexa", "Amazon Alexa and Echo", "smart speakers and Fire TV", r"\balexa\b|amazon echo|echo (dot|show)|fire ?tv\b|fire ?stick"),
    ("kindle", "Amazon Kindle", "e-readers and ebook formats", r"kindle|\bazw3?\b|\bkfx\b"),
    ("kobo", "Kobo", "e-readers", r"\bkobo\b"),
    ("remarkable", "reMarkable", "paper tablets", r"(?-i:reMarkable)|\brmapi\b|\bremarkable (tablet|2|pro|paper|cloud)"),
    ("govee", "Govee", "lights", r"\bgovee"),
    ("tp-link", "TP-Link", "Kasa and Tapo devices", r"tp-?link|\bkasa\b|\btapo\b"),
    ("broadlink", "Broadlink", "IR and RF remotes", r"broadlink"),
    ("yeelight", "Yeelight", "lights", r"yeelight"),
    ("aqara", "Aqara", "Zigbee sensors and hubs", r"aqara"),
    ("switchbot", "SwitchBot", "devices", r"switchbot"),
    ("wyze", "Wyze", "cameras", r"\bwyze"),
    ("hikvision", "Hikvision and Ezviz", "cameras and NVRs", r"hikvision|ezviz|\bhik ?connect"),
    ("reolink", "Reolink", "cameras", r"reolink"),
    ("dahua", "Dahua", "cameras and NVRs", r"dahua|\bimou\b"),
    ("somfy", "Somfy", "blinds and TaHoma", r"somfy|\btahoma"),
    ("midea", "Midea", "air conditioners and appliances", r"\bmidea|\bmsmart"),
    ("daikin", "Daikin", "air conditioners and heat pumps", r"daikin"),
    ("mitsubishi", "Mitsubishi", "heat pumps, PLCs and cars", r"mitsubishi"),
    ("lg", "LG", "ThinQ appliances and webOS TVs", r"\blg (thinq|webos|tvs?|smart|washer|ac|electronics|soundbar)|\bthinq|\bwebos\b|lg ?electronics"),
    ("samsung", "Samsung", "phones, TVs and SmartThings", r"samsung|\btizen\b|galaxy (watch|buds)"),
    ("bosch", "Bosch and Siemens", "Home Connect appliances, eBikes and ECUs", r"\bbosch\b|home ?connect\b|siemens home"),
    ("miele", "Miele", "appliances", r"\bmiele"),
    ("dyson", "Dyson", "fans and purifiers", r"\bdyson"),
    # Health and fitness
    ("garmin", "Garmin", "Garmin Connect and watches", r"garmin"),
    ("fitbit", "Fitbit", "trackers", r"fitbit"),
    ("withings", "Withings", "scales and health devices", r"withings|nokia health"),
    ("polar", "Polar", "heart-rate sensors and watches", r"\bpolar (h10|h9|h7|verity|vantage|flow|loop|ignite|grit|pacer|oh1|accesslink|beat|sensors?|watch(es)?|m\d{3})"),
    ("suunto", "Suunto", "watches", r"suunto"),
    ("whoop", "Whoop", "bands", r"\bwhoop\b"),
    ("oura", "Oura", "rings", r"\boura\b"),
    ("peloton", "Peloton", "bikes and treads", r"peloton"),
    ("zwift", "Zwift", "trainers and apps", r"zwift"),
    ("wahoo", "Wahoo", "trainers and bike computers", r"\bwahoo"),
    ("dexcom", "Dexcom", "glucose monitors", r"dexcom"),
    ("freestyle-libre", "FreeStyle Libre", "glucose monitors", r"freestyle ?libre|\blibre ?[23]\b|\blibreview"),
    # Phones, PCs and peripherals
    ("apple", "Apple", "AirPods, Find My, iCloud, iMessage and HomeKit", r"airpods|airtags?\b|\bfind ?my\b|\bicloud|imessage|homekit accessory protocol|\bairplay|\bairdrop|apple silicon|apple (watch|neural engine|id|notes|business chat)|siri remote|\bfacetime"),
    ("huawei", "Huawei", "phones, routers and solar inverters", r"huawei|harmony ?os\b|\bemui\b"),
    ("sony", "Sony", "headphones, cameras, Xperia and Bravia", r"sony (wh|wf|xperia|bravia|alpha|camera|headphones?|tv)|\bxperia|\bbravia|wh-?1000xm|wf-?1000xm"),
    ("bose", "Bose", "headphones and speakers", r"\bbose\b"),
    ("logitech", "Logitech", "mice, keyboards and Harmony remotes", r"logitech|\bg ?hub\b|\bharmony hub|\bunifying\b"),
    ("razer", "Razer", "peripherals", r"\brazer\b|openrazer"),
    ("corsair", "Corsair", "peripherals and iCUE", r"corsair|\bicue\b"),
    ("steelseries", "SteelSeries", "peripherals", r"steelseries"),
    ("elgato", "Elgato", "Stream Deck and capture devices", r"elgato|stream ?deck"),
    ("nvidia", "NVIDIA", "GPUs and drivers", r"nvidia|nouveau"),
    ("broadcom", "Broadcom", "Wi-Fi, Bluetooth and SoCs", r"broadcom|\bbcm\d|\bb43\b"),
    ("qualcomm", "Qualcomm", "Snapdragon SoCs and modems", r"qualcomm|snapdragon|\bqcom\b|\badreno"),
    ("mediatek", "MediaTek", "SoCs and phones", r"mediatek|\bmtk\b"),
    ("realtek", "Realtek", "chips and drivers", r"realtek|\brtl ?\d{4}"),
    ("canon", "Canon", "cameras and printers", r"\bcanon\b|magic ?lantern|\bchdk\b"),
    ("nikon", "Nikon", "cameras", r"\bnikon"),
    ("fujifilm", "Fujifilm", "cameras", r"fujifilm|\binstax\b"),
    ("gopro", "GoPro", "cameras", r"gopro"),
    ("dji", "DJI", "drones and gimbals", r"\bdji\b"),
    # 3D printers
    ("bambu-lab", "Bambu Lab", "3D printers", r"\bbambu"),
    ("creality", "Creality", "3D printers", r"creality|\bender[ -]?[35]|\bsonic pad"),
    # Cars and mobility
    ("tesla", "Tesla", "cars, Powerwalls and APIs", r"\btesla"),
    ("bmw", "BMW", "cars and ConnectedDrive", r"\bbmw|bimmer|connected ?drive|\bmini connected"),
    ("volkswagen", "Volkswagen Group", "VW, Audi, Skoda, Porsche and Cupra cars", r"volkswagen|\bvw\b|\baudi\b|\bskoda\b|\bporsche|\bcupra\b|\bwe connect\b|\bmib ?[23]\b|\bvag\b"),
    ("toyota", "Toyota and Lexus", "cars", r"toyota|\blexus"),
    ("hyundai-kia", "Hyundai and Kia", "cars and Bluelink", r"hyundai|\bkia\b|bluelink|\buvo\b"),
    ("ford", "Ford", "cars and FordPass", r"\bford\b|fordpass"),
    ("mercedes", "Mercedes-Benz", "cars", r"mercedes|\bmbux\b|\bdaimler"),
    ("renault-nissan", "Renault and Nissan", "cars", r"renault|nissan|\bdacia\b"),
    ("volvo", "Volvo and Polestar", "cars", r"\bvolvo|polestar"),
    ("segway-ninebot", "Segway-Ninebot", "scooters", r"ninebot|segway|\bm365\b"),
    # Messaging and social
    ("whatsapp", "WhatsApp", "messaging", r"whatsapp|\bbaileys\b|whatsmeow|yowsup"),
    ("telegram", "Telegram", "messaging", r"telegram|\bmtproto|\btdlib\b|telethon|pyrogram|gramjs"),
    ("signal", "Signal", "messaging", r"signal[ -](messenger|app|protocol|desktop|cli|bot|private)|libsignal|\bsignald\b"),
    ("wechat", "WeChat", "messaging and mini programs", r"wechat|weixin|微信|itchat|wechaty"),
    ("qq", "QQ", "messaging and bots", r"\bqq\b(?![ -]?music)|onebot|napcat|cqhttp"),
    ("qq-music", "QQ Music", "music streaming", r"qq ?music"),
    ("discord", "Discord", "chat", r"discord"),
    ("instagram", "Instagram", "social network", r"instagram|instaloader|instagrapi"),
    ("tiktok-douyin", "TikTok and Douyin", "short video", r"tiktok|douyin|抖音"),
    ("twitter-x", "Twitter / X", "social network", r"twitter|\btweets?\b|\bx\.com\b"),
    ("facebook", "Facebook and Messenger", "social network", r"facebook|\bfb messenger"),
    ("snapchat", "Snapchat", "social network", r"snapchat"),
    ("linkedin", "LinkedIn", "social network", r"linkedin"),
    ("reddit", "Reddit", "social network", r"\breddit"),
    ("xiaohongshu", "Xiaohongshu (RedNote)", "social network", r"xiaohongshu|小红书|\brednote\b"),
    ("weibo", "Weibo", "social network", r"weibo|微博"),
    ("zhihu", "Zhihu", "Q&A site", r"zhihu|知乎"),
    ("bilibili", "Bilibili", "video", r"bilibili|哔哩"),
    ("youtube", "YouTube", "video and music", r"youtube|\byt-dlp\b|\binnertube\b|newpipe|invidious"),
    # Music and media
    ("spotify", "Spotify", "music streaming", r"spotify|librespot|\bspotdl\b|spicetify"),
    ("tidal", "Tidal", "music streaming", r"\btidal\b"),
    ("deezer", "Deezer", "music streaming", r"deezer"),
    ("soundcloud", "SoundCloud", "music streaming", r"soundcloud"),
    ("netease-cloud-music", "NetEase Cloud Music", "music streaming", r"netease|网易云"),
    ("netflix", "Netflix", "video streaming", r"netflix"),
    ("steam", "Steam", "store, client and network", r"\bsteam ?(api|client|guard|workshop|cmd|web|protocol|network|community|market|kit|works|cloud|link)|\bsteam\b(?= (account|library|inventory|trade|friends|chat))"),
    ("blizzard", "Blizzard", "Battle.net, World of Warcraft, Diablo and StarCraft", r"blizzard|battle\.net|world of warcraft|\bwow\b|diablo|starcraft|warcraft|overwatch|hearthstone"),
    # AI services
    ("openai-chatgpt", "OpenAI and ChatGPT", "ChatGPT, Codex and Sora", r"openai|chatgpt|\bsora\b|dall-?e", AI),
    ("anthropic-claude", "Anthropic Claude", "Claude and Claude Code", r"anthropic|\bclaude\b", AI),
    ("google-gemini", "Google Gemini", "Gemini and AI Studio", r"google gemini|gemini (api|cli|web|pro|advanced|nano|code|flash)|\bbard\b|google ai studio|aistudio\.google", AI),
    ("copilot", "GitHub and Microsoft Copilot", "coding and chat assistants", r"copilot", AI),
    ("cursor", "Cursor", "AI code editor", r"\bcursor (ide|editor|ai|api|agent|pro|rules)|cursor\.(sh|com)|\bcursor\b(?=,| and claude| or claude)", AI),
    ("deepseek", "DeepSeek", "chat models", r"deepseek", AI),
    ("perplexity", "Perplexity", "AI search", r"perplexity", AI),
    ("midjourney", "Midjourney", "image generation", r"midjourney", AI),
    ("suno", "Suno", "music generation", r"\bsuno\b", AI),
]
# Game-category entries count only for these vendors (None: every game subcategory).
# Search term for the "search the full index" link when the name's first word is not a good query.
SEARCH = {"kindle": "kindle", "google-nest": "nest", "copilot": "copilot", "amazon-alexa": "alexa", "philips-hue": "hue",
          "segway-ninebot": "ninebot", "anthropic-claude": "claude", "openai-chatgpt": "chatgpt", "google-gemini": "gemini",
          "netease-cloud-music": "netease", "qq-music": "qq music", "bambu-lab": "bambu", "hyundai-kia": "kia",
          "twitter-x": "twitter", "renault-nissan": "nissan", "volvo": "volvo", "volkswagen": "volkswagen"}
VENDOR_GAMES = {"blizzard": None, "steam": {"Launchers & Store Clients", "Game Network Protocols & APIs"}}

# Platform pages, in display order. (slug, name, short name for titles, group, regex, implied subcategories).
# Only game decompilations, static recompilations and PC ports, engine reimplementations and fan patches count.
SUB_KIND = [("Matching Decompilations", "Matching decompilations"), ("Static Recompilations", "Static recompilations and PC ports"),
            ("Engine Reimplementations", "Engine reimplementations"), ("Fan Patches", "Fan patches and enhancements")]
PLATFORMS = [
    ("nes", "NES / Famicom", "NES", "Nintendo", r"\bnes\b|(?<!super )famicom|nintendo entertainment system", ()),
    ("snes", "SNES / Super Famicom", "SNES", "Nintendo", r"\bsnes\b|super nintendo|super famicom|\bsfc\b", ()),
    ("n64", "Nintendo 64", "N64", "Nintendo", r"\bn64\b|nintendo ?64|\bultra ?64\b|\b64dd\b", ("Matching Decompilations — Nintendo 64",)),
    ("gamecube", "GameCube", "GameCube", "Nintendo", r"game ?cube|\bgcn\b", ()),
    ("wii", "Wii", "Wii", "Nintendo", r"\bwii\b(?![ -]?u\b)", ()),
    ("wii-u", "Wii U", "Wii U", "Nintendo", r"\bwii ?u\b", ()),
    ("switch", "Nintendo Switch", "Switch", "Nintendo", r"nintendo ?switch|\(switch\b|\bswitch\)", ("Matching Decompilations — Switch",)),
    ("game-boy", "Game Boy / Game Boy Color", "Game Boy", "Nintendo", r"game ?boy(?! ?advance)|\bgbc\b|\bgb color\b", ()),
    ("gba", "Game Boy Advance", "GBA", "Nintendo", r"game ?boy advance|\bgba\b", ()),
    ("nds", "Nintendo DS", "Nintendo DS", "Nintendo", r"nintendo ds(i)?\b|\bnds\b|\(dsi?\)|\(dsi?,", ()),
    ("3ds", "Nintendo 3DS", "3DS", "Nintendo", r"\b3ds\b(?! ?max)|nintendo 3ds", ()),
    ("ps1", "PlayStation (PS1)", "PS1", "Sony", r"\bps1\b|\bpsx\b|\bpsone\b|playstation ?1\b|\bplaystation\b(?![ -]?(2|3|4|5|portable|vita|network|plus|store|now|move))", ("Matching Decompilations — PlayStation 1",)),
    ("ps2", "PlayStation 2", "PS2", "Sony", r"\bps2\b|playstation ?2\b", ("Matching Decompilations — PlayStation 2",)),
    ("ps3", "PlayStation 3", "PS3", "Sony", r"\bps3\b|playstation ?3\b", ()),
    ("psp", "PSP / PS Vita", "PSP", "Sony", r"\bpsp\b|playstation portable|\((ps ?|playstation )?vita\b", ()),
    ("xbox", "Xbox (original)", "Xbox", "Microsoft", r"\bxbox\b(?![ -]?(360|one|series|live|game pass|app))", ()),
    ("xbox-360", "Xbox 360", "Xbox 360", "Microsoft", r"xbox ?360|\bx360\b", ()),
    ("master-system", "Sega Master System / Game Gear", "Master System", "Sega", r"master system|\bsms\b|game ?gear", ()),
    ("genesis", "Sega Genesis / Mega Drive", "Genesis", "Sega", r"mega ?drive|sega genesis|(?<!neon )\bgenesis\b(?! plus)", ()),
    ("saturn", "Sega Saturn", "Saturn", "Sega", r"\bsaturn\b", ()),
    ("dreamcast", "Dreamcast", "Dreamcast", "Sega", r"dreamcast", ()),
    ("arcade", "Arcade", "arcade", "Other", r"\(arcade\b|\barcade (board|pcb|version|original|rom)", ("Matching Decompilations — Arcade",)),
    ("dos", "MS-DOS", "DOS", "Computers", r"\bms-?dos\b|\bdos\b(?![ -]?(attack|protection))", ()),
    ("amiga", "Amiga", "Amiga", "Computers", r"\bamiga\b|\bcd32\b", ()),
    ("c64", "Commodore 64", "C64", "Computers", r"commodore ?64|\bc64\b", ()),
    ("zx-spectrum", "ZX Spectrum", "ZX Spectrum", "Computers", r"zx ?spectrum|\bspeccy\b", ()),
    ("atari", "Atari", "Atari", "Other", r"\batari\b|\b2600\b|atari jaguar|\(jaguar\b", ()),
    ("mobile", "Mobile (J2ME, iOS, Android)", "mobile", "Other", r"\bj2me\b|\bjava me\b|\((android|ios|mobile|j2me|java me)(,|\)| \d{4})|feature[ -]phone|\bn-gage\b|\bmobile game\b", ("Matching Decompilations — Mobile",)),
]


# Phrases that name a platform as a port target ("port to the Dreamcast", "running natively on Switch",
# "recompilation for Android", "Nintendo DS port of") are removed before the platform rules run.
_PLAT = (r"((the|a|an|original|sony|sega|nintendo|microsoft|new)\s+)*[\w./+-]+"
         r"(\s+(64|360|ds|3ds|u|advance|colou?r|portable|vita|[1-5]|drive|system|gear|cd|one|series)\b)?")
TARGET = re.compile(
    rf"\b(to|onto|on)\s+{_PLAT}(\s*(,\s*(and|or)?|and|or|&|/)\s*{_PLAT})*"
    rf"|\bfor\s+(the\s+)?(new\s+)?(nintendo\s+)?(switch|android|ios|ipados|ps ?vita|vita|ps[45]|playstation [45]|wii u|3ds)\b(\s*(,\s*(and|or)?|and|or|&|/)\s*{_PLAT})*"
    r"|\b(native\s+)?((original|nintendo|sony|sega|new)\s+)*[\w-]+(\s+(64|360|ds|3ds|u|vita))?(\s+[\w-]+)?\s+(port|engine|build)\b", re.I)


NO_TOPICS = {"switch", "3ds", "dreamcast"}  # platforms whose topics mostly tag ports *to* the platform


def topics(e):
    return " ".join(x.replace("-", " ").replace("_", " ") for x in e.get("topics") or [])


def game_kind(e):
    if e.get("category") != GAMES:
        return None
    for prefix, kind in SUB_KIND:
        if (e.get("subcategory") or "").startswith(prefix):
            return kind
    return None


def in_games(s, e):
    """False for a game-category entry, unless VENDOR_GAMES admits its subcategory for vendor s."""
    if e.get("category") != GAMES:
        return True
    return s in VENDOR_GAMES and (VENDOR_GAMES[s] is None or e.get("subcategory") in VENDOR_GAMES[s])


def match(entries):
    """Returns ({vendor slug: [entries]}, {platform slug: [entries]}), each list sorted by stars then name."""
    vr = [(v[0], re.compile(v[3], re.I), set(v[4]) if len(v) > 4 else None,
           re.compile(VENDOR_NOT[v[0]], re.I) if v[0] in VENDOR_NOT else None, VENDOR_HOME.get(v[0])) for v in VENDORS]
    pr = [(s, re.compile(p, re.I), set(subs)) for s, _, _, _, p, subs in PLATFORMS]
    vendors, platforms = collections.defaultdict(list), collections.defaultdict(list)
    for e in entries:
        t = STRIP.sub(" ", (e.get("name") or "") + " " + (e.get("desc") or ""))
        for s, r, cats, no, home in vr:
            if e.get("category") == home or (in_games(s, e) and (not cats or e.get("category") in cats)
                                             and r.search(t) and not (no and no.search(t))):
                vendors[s].append(e)
        if game_kind(e):
            # Platforms read the description only (names often carry the port target, "mario-kart-64-3ds").
            # Topics count too, unless the description names a port target: then the topics tag that target.
            d = e.get("desc") or ""
            gone = " ".join(m.group(0) for m in TARGET.finditer(d))
            t0 = TARGET.sub(" ", d)
            t = t0 if any(r.search(gone) for _, r, _ in pr) else t0 + " " + topics(e)
            for s, r, subs in pr:
                if e.get("subcategory") in subs or r.search(t0 if s in NO_TOPICS else t):
                    platforms[s].append(e)
    key = lambda e: (-(e.get("stars") or 0), e["name"].lower())
    return ({s: sorted(v, key=key) for s, v in vendors.items() if len(v) >= MIN},
            {s: sorted(v, key=key) for s, v in platforms.items() if len(v) >= MIN})


# ---------------------------------------------------------------- pages

esc = lambda s: html.escape(str(s or ""), quote=True)
EXTRA_CSS = """.facts{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px;padding:0;list-style:none}.facts li{font:12px var(--mono);color:var(--ink-2);border:1px solid var(--line);border-radius:999px;padding:4px 10px;background:var(--surface)}
.groups h2{font-size:15px;color:var(--ink-3);text-transform:uppercase;letter-spacing:.6px;margin:28px 0 8px}
.related{margin:32px 0 0;color:var(--ink-2);font-size:14px}.related a{color:var(--accent)}"""


def _ld(title, url, items):
    data = {"@context": "https://schema.org", "@type": "ItemList", "name": title, "url": url, "numberOfItems": len(items),
            "itemListElement": [{"@type": "ListItem", "position": i, "url": e["url"], "name": e["name"]} for i, e in enumerate(items[:50], 1)]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def _top_places(v, slug, n=3):
    c = collections.Counter((e["category"], e["subcategory"]) for e in v)
    return [(cat, sub, k, f"c/{slug(cat)}/{slug(sub)}/") for (cat, sub), k in c.most_common(n)]


def build(root, entries, total, health, page, item, slug, base):
    """Writes docs/vendors/ and docs/games/. page(path, title, desc, body, depth, total) and item(e, health) come from pages.py.
    Returns the list of page paths written."""
    vendors, platforms = match(entries)
    paths = []
    for d in ("vendors", "games"):
        shutil.rmtree(os.path.join(root, "docs", d), ignore_errors=True)

    def write(p, title, desc, body, depth):
        os.makedirs(os.path.join(root, "docs", p), exist_ok=True)
        html_ = page(p, title, desc, f"<style>{EXTRA_CSS}</style>\n" + body, depth, total)
        open(os.path.join(root, "docs", p, "index.html"), "w").write(html_)
        paths.append(p)

    active = lambda v: sum(health(e) == "active" for e in v)
    names = lambda v, n=3: ", ".join(e["name"] for e in v[:n])

    # Vendor pages
    vinfo = {v[0]: (v[1], v[2]) for v in VENDORS}
    for s, (name, what) in vinfo.items():
        v = vendors.get(s)
        if not v:
            continue
        p = f"vendors/{s}/"
        title = f"{name} reverse engineered: {len(v):,} open-source tools, APIs and clients"
        desc = (f"{len(v):,} open-source projects built by reverse engineering {name} {what}: unofficial APIs, local control, "
                f"clients and protocol docs. Includes {names(v)}. Sorted by GitHub stars, refreshed nightly.")
        places = _top_places(v, slug)
        lede = (f"Open-source projects that exist because someone reverse engineered {esc(name)} {esc(what)}. "
                f"{active(v):,} of {len(v):,} had a commit in the last 12 months. Most-starred: {esc(names(v, 5))}.")
        body = [f'<div class="crumbs"><a href="../../">Home</a> / <a href="../">Vendors</a> / {esc(name)}</div>',
                f"<h1>{len(v):,} open-source {esc(name)} projects built by reverse engineering</h1>",
                f'<p class="lede">{lede}</p>',
                '<ul class="facts">' + "".join(f'<li>{esc(sub)} · {k}</li>' for _, sub, k, _ in places) + "</ul>",
                f'<a class="cta" href="../../#q={esc(SEARCH.get(s, name.split()[0].lower()))}">Search and filter in the full index →</a>',
                '<ol class="items">' + "".join(item(e, health) for e in v) + "</ol>",
                '<p class="related">Related: ' + " · ".join(f'<a href="../../{u}">{esc(sub)}</a>' for _, sub, _, u in places)
                + ' · <a href="../">All vendors</a> · <a href="../../games/">Games by console</a></p>',
                _ld(title, base + p, v)]
        write(p, title, desc, "\n".join(body), 2)

    # Vendor index
    order = sorted(vendors, key=lambda s: (-len(vendors[s]), s))
    title = f"Reverse-engineered products by vendor: {len(order)} brands, from Tuya to Tesla"
    desc = (f"Open-source tools built by reverse engineering the devices, apps and services of {len(order)} vendors, "
            f"with project counts: {', '.join(vinfo[s][0] for s in order[:8])} and more.")
    body = ['<div class="crumbs"><a href="../">Home</a> / Vendors</div>',
            f"<h1>Reverse-engineered products by vendor</h1>",
            f'<p class="lede">{len(order)} vendors whose devices, apps or services the open-source community reverse engineered: '
            f"unofficial APIs, local control, alternative clients, drivers and firmware tools. A project can appear under more than one vendor. "
            f'Game consoles are on <a href="../games/">Games by console</a>.</p>',
            '<ul class="subs">' + "".join(f'<li><a href="{s}/">{esc(vinfo[s][0])}<span>{len(vendors[s]):,}</span></a></li>' for s in order) + "</ul>"]
    write("vendors/", title, desc, "\n".join(body), 1)

    # Platform pages
    pinfo = {s: (name, short, group) for s, name, short, group, _, _ in PLATFORMS}
    kinds = [k for _, k in SUB_KIND]
    for s, name, short, group, _, _ in PLATFORMS:
        v = platforms.get(s)
        if not v:
            continue
        p = f"games/{s}/"
        by_kind = collections.OrderedDict((k, [e for e in v if game_kind(e) == k]) for k in kinds)
        counts = [(k, len(x)) for k, x in by_kind.items() if x]
        title = f"{short} decompilations, recompilations and PC ports: {len(v):,} open-source projects"
        desc = (f"{len(v):,} open-source {name} game projects: " + ", ".join(f"{n} {k[0].lower() + k[1:]}" for k, n in counts)
                + f". Includes {names(v)}. Sorted by GitHub stars, refreshed nightly.")
        lede = (f"Open-source projects that decompile, statically recompile or reimplement {esc(name)} games. "
                + ", ".join(f"{n:,} {esc(k[0].lower() + k[1:])}" for k, n in counts) + ". "
                f"{active(v):,} of {len(v):,} had a commit in the last 12 months. Most-starred: {esc(names(v, 5))}.")
        body = [f'<div class="crumbs"><a href="../../">Home</a> / <a href="../">Games by console</a> / {esc(name)}</div>',
                f"<h1>{esc(name)} decompilations, recompilations and PC ports</h1>",
                f'<p class="lede">{lede}</p>',
                f'<a class="cta" href="../../#c={slug(GAMES)}&amp;q={esc(short.lower())}">Search and filter in the full index →</a>',
                '<div class="groups">']
        for k, x in by_kind.items():
            if x:
                body.append(f"<h2>{esc(k)} <span>{len(x):,}</span></h2>")
                body.append('<ol class="items">' + "".join(item(e, health) for e in x) + "</ol>")
        body.append("</div>")
        body.append(f'<p class="related">Related: <a href="../../c/{slug(GAMES)}/">{esc(GAMES)}</a> · <a href="../">All consoles</a> · <a href="../../vendors/">Vendors</a></p>')
        body.append(_ld(title, base + p, v))
        write(p, title, desc, "\n".join(body), 2)

    # Platform index
    order = [s for s, *_ in PLATFORMS if s in platforms]
    n_all = len({e["url"] for v in platforms.values() for e in v})
    title = f"Game decompilations by console: {len(order)} platforms, from NES to Xbox 360"
    desc = (f"Open-source decompilations, static recompilations, PC ports and engine reimplementations of games, by platform: "
            f"{', '.join(pinfo[s][1] for s in order[:10])} and more.")
    body = ['<div class="crumbs"><a href="../">Home</a> / Games by console</div>',
            "<h1>Game decompilations and PC ports by console</h1>",
            f'<p class="lede">{n_all:,} open-source projects that decompile, statically recompile or reimplement games, grouped by the platform '
            f"the game shipped on. A project can appear under more than one platform. "
            f'All game projects, including emulators, mod loaders and private servers: <a href="../c/{slug(GAMES)}/">{esc(GAMES)}</a>.</p>']
    for g in dict.fromkeys(pinfo[s][2] for s in order):
        body.append(f"<h2>{esc(g)}</h2>")
        body.append('<ul class="subs">' + "".join(f'<li><a href="{s}/">{esc(pinfo[s][0])}<span>{len(platforms[s]):,}</span></a></li>'
                                                for s in order if pinfo[s][2] == g) + "</ul>")
    write("games/", title, desc, "\n".join(body), 1)
    return paths


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    entries = json.load(open(os.path.join(here, "..", "data", "entries.json")))
    vendors, platforms = match(entries)
    want = set(sys.argv[1:])
    rnd = random.Random(int(os.environ.get("SEED", 7)))
    for label, got in (("VENDORS", vendors), ("PLATFORMS", platforms)):
        print(f"== {label}: {len(got)} pages")
        for s, v in sorted(got.items(), key=lambda kv: -len(kv[1])):
            print(f"{len(v):6,}  {s}")
            if not want or s in want:
                for e in rnd.sample(v, min(int(os.environ.get("N", 15)), len(v))):
                    print(f"        {e['name'][:40]:40} | {(e.get('desc') or '')[:90]}")
