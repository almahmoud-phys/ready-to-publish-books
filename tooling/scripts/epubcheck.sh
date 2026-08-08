#!/usr/bin/env bash
# tooling/scripts/epubcheck.sh — Gate E validator wrapper
# Usage: tooling/scripts/epubcheck.sh path/to/book.epub
set -euo pipefail
EPUB="${1:?usage: epubcheck.sh <file.epub>}"
if command -v epubcheck >/dev/null 2>&1; then
  epubcheck "$EPUB"
else
  JAR="${EPUBCHECK_JAR:-$HOME/tools/epubcheck/epubcheck.jar}"
  [[ -f "$JAR" ]] || { echo "epubcheck not found. Install: brew install epubcheck OR set EPUBCHECK_JAR"; exit 127; }
  java -jar "$JAR" "$EPUB"
fi
