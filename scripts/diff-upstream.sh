#!/usr/bin/env bash
# Diff each forked skill against its upstream commit. Exit 1 if any differ.
# Usage: scripts/diff-upstream.sh [skill...]   (default: every skill in UPSTREAM)
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
status=0
while read -r name repo sha path; do
  [[ -z "$name" || "$name" == \#* ]] && continue
  [[ $# -gt 0 && ! " $* " =~ " $name " ]] && continue
  src="$tmp/$repo@$sha"
  if [[ ! -d "$src" ]]; then
    git clone -q --filter=blob:none --no-checkout "https://github.com/$repo.git" "$src"
    git -C "$src" checkout -q "$sha"
  fi
  if diff -ru "$src/$path" "$root/skills/$name" >"$tmp/$name.diff"; then
    echo "same     $name"
  else
    echo "changed  $name ($(grep -c '^[-+][^-+]' "$tmp/$name.diff") lines)"
    status=1
  fi
done <"$root/UPSTREAM"
exit $status
