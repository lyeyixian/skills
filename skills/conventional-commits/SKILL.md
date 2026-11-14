---
name: conventional-commits
description: Write a commit message or a pull request title in the Conventional Commits 1.0.0 format, type(scope) and subject, with a body, a breaking change mark and footers when they apply. Use when the user asks to commit, asks for a commit message or a pull request title, or when you commit work in a repo that uses Conventional Commits.
---

# Conventional Commits

A Conventional Commit starts with a type, so a person or a tool can sort the history without reading each diff. This skill gives the format. The [writing](../writing/SKILL.md) skill gives the words: the technical register for the subject and the voice register for the body.

```text
type(scope)!: subject

body

footers
```

Only `type: subject` is necessary. Add each other part only when its section below says so.

## Process

1. Read the staged diff with `git diff --staged`. Do not write the message from memory of the work.
2. Find the rules of the repo. Read `AGENTS.md`, `CLAUDE.md` and `CONTRIBUTING.md`, then run `git log --oneline -20`. A type list or a scope list in the repo replaces the list in this skill.
3. If the diff holds two changes that need different types, make two commits. Remove the files of the second change from the index with `git restore --staged <file>`, commit, then add them and commit again. Tests and docs for a change go in the same commit as the change. Changes that do not work apart are one change.
4. Select the type, then the scope.
5. Write the subject. Add a body and footers if they apply.
6. Do the checks at the end of this skill.

If the history of the repo uses a different format and no rule or user request asks for Conventional Commits, use the format of the repo for the first line. The Body section and the 72-character limit still apply. Skip checks 1 and 3.

## Type

Use the first row that is true for the change.

| Type | The change |
|---|---|
| `feat` | Adds to or changes what the user of the software can do or must do: a new page, endpoint, option or command, a renamed option, a new required setting |
| `fix` | Corrects behaviour that was wrong |
| `perf` | Makes the software faster or smaller, with the same behaviour |
| `refactor` | Changes the code structure, with the same behaviour |
| `docs` | Changes only documentation or comments |
| `test` | Changes only tests |
| `build` | Changes the build, the packaging or the dependencies |
| `ci` | Changes only the CI configuration |
| `chore` | Is none of the above, for example a `.gitignore` entry |

- The user of the software can be a person, a caller of an API, or an agent that loads a skill. A new skill in a skills repo is `feat`.
- A feature that arrives with its tests and docs is `feat`.
- A dependency update is `build`. If you know that the update is there to correct a bug, it is `fix`. If you do not know the purpose, use `build` with no body.
- A new version of an action in a CI workflow is `ci`, not `build`.
- Do not use `chore` for a change that a row above describes.

## Scope

The scope is one noun for the part of the repo that changed: an app, a package, a module or a skill. Write it in lower case.

- Use a scope from the list of the repo. If there is no list, use a scope that `git log` shows for the same part.
- If the repo has no scopes, do not start them.
- If the change is in two or more parts, or in none, omit the scope. Do not write `feat(web,api)`.
- Tests and docs that arrive with a change are not a second part. The scope is the part that holds the code.

## Subject

- Start with a verb in the imperative: `add`, `remove`, `show`, `stop`. Not `added` or `adds`.
- Start with a lower-case letter. Do not end with a period.
- For `feat`, `fix` and `perf`, say what the software does after the change, in the words of its user. `fix(api): return 404 for an unknown application`, not `fix(api): update handler`. For the other types, say what the change does: `build: update hono to 4.7.2`.
- Keep the full first line to 72 characters or fewer.
- Do not repeat the type or the scope in the subject. `docs: update docs` says nothing.

## Body

Add a body when the diff does not show the reason for the change. Put one empty line after the subject. Write the cause of the change and the choice that you made, in sentences. Do not list the files, because the diff shows them. Wrap the lines at 72 characters.

A change that explains itself, such as a corrected typo, has no body.

## Breaking change

A breaking change makes a caller or a user change something on their side: a removed endpoint, a renamed option, a new required setting.

1. Put `!` before the colon: `feat(api)!: remove the v1 routes`.
2. Add a `BREAKING CHANGE:` footer that says what broke and what to do. If the footer gives the full reason, the commit needs no body.

A breaking change can have any type.

## Footers

Footers come last, after one empty line. Each footer starts with `Token: value` on a new line. Wrap a long value at 72 characters.

- `Closes #12` when the commit completes an issue. `Refs #12` when it only relates to the issue.
- `BREAKING CHANGE: <what broke and what to do>`.
- Trailers that the environment requires, such as `Co-Authored-By:`, stay at the end.

## Pull request titles

When a repo squash merges, the pull request title becomes the commit subject on the main branch. Write the title in the same format. Select the type and the scope from the full diff of the pull request, not from its last commit.

## Examples

```text
feat(web): show the application board
```

```text
fix(api): return 404 for an unknown application

The handler threw when the slug was not in the index, and the client
got a 500 with a stack trace. An unknown slug is a normal case, so it
now gets the same not_found error as the other routes.

Closes #31
```

```text
feat(api)!: require a token on each request

BREAKING CHANGE: requests without an Authorization header get 401.
Set API_TOKEN in the environment of the Web service.
```

## Checks

1. The first line matches `type(scope)!: subject`, with a type from the list and one space after the colon. The scope and the `!` are there only when they apply.
2. The first line is 72 characters or fewer.
3. The subject starts with an imperative verb in lower case and has no period at the end.
4. If the commit breaks a caller, it has `!` and a `BREAKING CHANGE:` footer.
5. The message passes the self-check of the writing skill.
