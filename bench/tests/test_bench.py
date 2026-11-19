"""The benchmark's validity checks. Run: python3 -m unittest discover -s bench/tests"""
import os, random, secrets, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from interop_bench import fmt, harness, proto
from interop_bench.core import LEVELS


class Oracle(unittest.TestCase):
    def test_format_answers_are_in_the_bytes(self):
        for _ in range(40):
            seed = secrets.token_hex(16)
            for lv in LEVELS:
                spec = fmt.Spec(seed, lv)
                for data, want in fmt.hidden_tests(seed, lv, 6):
                    self.assertEqual(fmt.score_doc(want, spec.decode(data)), 1.0)

    def test_long_name_is_refused(self):
        seed = secrets.token_hex(16)
        dev = proto.live_unit(seed, 1, "hidden")
        with self.assertRaises(proto.Bad):
            dev.execute(proto.Spec(seed, 1).cmds["rename"], bytes([200]) + b"x" * 200)

    def test_protocol_reference_client_controls_a_live_unit(self):
        for _ in range(10):
            seed = secrets.token_hex(16)
            for lv in LEVELS:
                spec = proto.Spec(seed, lv)
                dev = proto.live_unit(seed, lv, "hidden")
                live = proto.Live(dev)
                sock, c = proto.tcp_client(spec, live.port, random.Random(1))
                c.set_power("on"); c.set_temp("23.5"); c.set_mode("away"); c.rename("x1")
                self.assertEqual(c.status(), {"power": True, "temp": 23.5, "mode": "away", "name": "x1"})
                sock.close()
                live.close()

    def test_same_seed_same_instance(self):
        seed = secrets.token_hex(16)
        for lv in LEVELS:
            self.assertEqual(fmt.instance(seed, lv)[1], fmt.instance(seed, lv)[1])
            self.assertEqual(proto.instance(seed, lv)[1], proto.instance(seed, lv)[1])

    def test_labeled_samples_show_every_code(self):
        for lv in LEVELS:
            for _ in range(20):
                seed = secrets.token_hex(16)
                spec, files = fmt.instance(seed, lv)
                text = b" ".join(v for k, v in files.items() if k.endswith(".json")).decode()
                for word in fmt.MODES + (fmt.CODES if lv >= 3 else []):
                    self.assertIn(f'"{word}"', text, (lv, word))

    def test_firmware_really_contains_the_frame_check(self):
        """Run the generated RISC-V in an emulator: it must agree with what the device enforces."""
        import rv32emu
        from interop_bench import rv32
        for _ in range(25):
            seed = secrets.token_hex(16)
            img, (fn, iv, y), off = rv32.firmware(seed)
            r = random.Random(seed)
            for _ in range(10):
                a, b = r.getrandbits(32), r.getrandbits(32)
                self.assertEqual(rv32emu.call(img, off["mix"], [a, b])[0], rv32.mix(fn, a, b))
            for n in (1, 7, 8, 13, 40):
                data = bytes(r.randrange(256) for _ in range(n))
                self.assertEqual(rv32emu.check(img, off["check"], data), rv32.check(fn, iv, y, data))

    def test_levels_4_and_5_carry_no_secrets(self):
        """Payloads stay readable: a name must appear in the clear in the traffic."""
        for lv in (4, 5):
            text = proto.instance(secrets.token_hex(16), lv)[1]["capture.txt"].decode()
            first = [l for l in text.split("\n") if l.startswith("# user: rename the unit to ")]
            if first:
                self.assertIn(first[0].split()[-1][:5].encode().hex(), text)

    def test_most_sessions_are_unlabeled_from_level_4(self):
        text = proto.instance(secrets.token_hex(16), 4)[1]["capture.txt"].decode()
        labels = [i for i, l in enumerate(text.split("## Session")) if "# user:" in l]
        self.assertEqual(labels, [1])

    def test_hub_refuses_a_bad_checksum(self):
        seed = secrets.token_hex(16)
        spec, files = fmt.instance(seed, 5)
        good = files["samples/log00.bin"]
        spec.validate(good)
        with self.assertRaises(ValueError):
            spec.validate(good[:-1] + bytes([good[-1] ^ 1]))

    def test_new_seed_new_format(self):
        a, b = secrets.token_hex(16), secrets.token_hex(16)
        for lv in LEVELS:
            self.assertNotEqual(fmt.Spec(a, lv).magic, fmt.Spec(b, lv).magic)

    def test_captures_show_every_mode_and_power_state(self):
        for lv in LEVELS:
            text = proto.instance(secrets.token_hex(16), lv)[1]["capture.txt"].decode()
            for m in proto.MODES:
                self.assertIn(f"switch mode to {m}", text)
            self.assertIn("turn power on", text)
            self.assertIn("turn power off", text)


class Scorer(unittest.TestCase):
    """The full path: prepare, install a solution, score it against hidden tests."""

    def run_agent(self, agent, track, lv):
        return harness.run_one(agent, track, lv, secrets.token_hex(16), 60, "/tmp/interop-test")

    def test_reference_scores_100(self):
        for track in ("fmt", "proto"):
            for lv in LEVELS:
                rec = self.run_agent("reference", track, lv)
                self.assertEqual((rec["score"], rec["solved"]), (1.0, True), (track, lv))

    def test_empty_submission_scores_0(self):
        for track in ("fmt", "proto"):
            for lv in LEVELS:
                self.assertEqual(self.run_agent("null", track, lv)["score"], 0.0)

    def test_replaying_samples_does_not_pass(self):
        for track in ("fmt", "proto"):
            for lv in LEVELS:
                rec = self.run_agent("replay", track, lv)
                self.assertFalse(rec["solved"])
                self.assertLess(rec["score"], 0.15, (track, lv))


if __name__ == "__main__":
    unittest.main()
