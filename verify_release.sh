#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")" && pwd)"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

python3 "$root/materialize_release.py" "$work"
cd "$work/release"
./verify_release.sh

cd "$root"
python3 scripts/check_release_integrity.py

printf '%s\n' 'R010 RELEASE VERIFICATION PASSED'
