# skills

My agent skills. Each folder under `skills/` is one skill: a `SKILL.md` plus the files it reads.

The dotfiles setup clones this repo to `~/.skills` and links every skill into `~/.agents/skills` (any agent) and `~/.claude/skills` (Claude Code). See `setup/common/skills.sh` in [dotfiles](https://github.com/lyeyixian/dotfiles). Edit a skill here and every agent sees the change on its next session.

## Hooks

`hooks/writing-context.sh` prints the `writing` skill. The dotfiles Claude Code settings run it on every session start, so replies follow the rules from the first draft instead of relying on the agent to load the skill.

`writing` replaced the older `unslop` skill. It keeps the unslop patterns and adds an ASD-STE100 register for procedures, reference and code comments. In a test of 96 replies, with the unslop rules loaded a blind judge preferred the replies 21 of 24 times for both Opus 5.5 and Fable 5.1. The STE register has no test yet.

## Commit messages

`conventional-commits` gives the format of a commit message or a pull request title: the type, the scope, the breaking change mark and the footers. `writing` still gives the wording. The format is in its own skill because the hook prints `writing` into every session, and most sessions never commit.

A fresh agent followed the skill on seven sample repos: a feature with tests and docs, a fix across two apps, a dependency update, a breaking rename, a diff that needed two commits, a repo with a different format, and a squash-merge title. All seven messages had the type and scope I expected. The agent listed the points where it had to guess, and the skill now answers them. That second version has no test run yet.

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
