#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"

if [[ ! -x .tools/zola ]]; then
  python3 scripts/setup-zola.py
fi

nrse_preview_port="${NRSE_PREVIEW_PORT:-8877}"
exec .tools/zola serve --interface 127.0.0.1 --port "$nrse_preview_port" \
  --output-dir ".preview/served-$nrse_preview_port" --store-html --force
