# skills

My agent skills. Each folder under `skills/` is one skill: a `SKILL.md` plus the files it reads.

The dotfiles setup clones this repo to `~/.skills` and links every skill into `~/.agents/skills` (any agent) and `~/.claude/skills` (Claude Code). See `setup/common/skills.sh` in [dotfiles](https://github.com/lyeyixian/dotfiles). Edit a skill here and every agent sees the change on its next session.

## Forked skills

Seven skills started as copies of [mattpocock/skills](https://github.com/mattpocock/skills), MIT licensed (`skills/LICENSE-mattpocock`). `UPSTREAM` pins the commit each one came from. To see how far a skill has drifted from its upstream:

```sh
scripts/diff-upstream.sh            # every forked skill
scripts/diff-upstream.sh grilling   # one skill
```

It exits 1 when any skill differs. A difference is expected once I edit a skill. The script shows what I changed, it doesn't enforce anything.

## Known gaps

- `to-spec`, `to-tickets` and `code-review` call `/setup-matt-pocock-skills`, which isn't forked. It writes per-repo config to `docs/agents/*.md`. Repos that already have those files work.
- `code-review` has the same name as a Claude Code built-in skill, and the built-in wins. `implement` calls `/code-review`, so it gets the built-in too. It needs a rename.
