#!/usr/bin/env bash
# SessionStart hook: put the writing rules in context so every reply follows
# them without the agent having to remember to load the skill. Voice covers
# most replies, so unslop.md loads too. STE.md loads on demand.
dir="$(cd "$(dirname "$0")/.." && pwd)/skills/writing"
[ -r "$dir/SKILL.md" ] || exit 0
echo "Write every reply, doc, ticket, commit message and code comment by these rules from the first draft."
echo "The files the rules link to live in $dir."
echo
awk 'f>=2{print} /^---$/{f++}' "$dir/SKILL.md"
echo
cat "$dir/unslop.md"
