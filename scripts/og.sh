#!/bin/sh
# Rebuild docs/og.png (1280x640) from assets/social.svg with headless Chrome.
# Run after render.py when the rounded project count changes. Upload the same PNG as the
# GitHub social preview (Settings > General > Social preview); GitHub has no API for it.
set -e
cd "$(dirname "$0")/.."
CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,640 \
  --screenshot="$PWD/docs/og.png" "file://$PWD/assets/social.svg"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,640 \
  --screenshot="$PWD/docs/resurrected/og.png" "file://$PWD/assets/resurrected.svg"
