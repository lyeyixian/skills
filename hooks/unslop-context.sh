#!/usr/bin/env bash
# SessionStart hook: put the unslop rules in context so every reply follows
# them without the agent having to remember to load the skill.
skill="$(cd "$(dirname "$0")/.." && pwd)/skills/unslop/SKILL.md"
[ -r "$skill" ] || exit 0
echo "Write every reply, doc, ticket, commit message and code comment by these rules from the first draft."
echo
awk 'f>=2{print} /^---$/{f++}' "$skill"
