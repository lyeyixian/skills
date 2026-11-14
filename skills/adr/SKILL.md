---
name: adr
description: Record an architecture decision as an ADR, one decision per file in docs/adr/, with a status of proposed, accepted or superseded, the options that were considered, and an index in docs/adr/README.md. Use when the user makes or changes a technical decision, asks for an ADR or a decision record, asks why the project chose something, or has an open technical question to settle before work starts.
---

# ADR

An ADR (architecture decision record) is a short file that says what was decided and why. A person or an agent who starts with no memory of the project reads the ADRs and does not propose an option that was rejected before.

The ADRs are in `docs/adr/`, unless the repo already keeps them in a different folder. The folder holds one file for each decision and a `README.md` that lists them.

```text
docs/adr/
├── README.md                          # the list of decisions
├── 0001-nextjs-with-typescript.md     # one decision
└── 0002-in-memory-vault-index.md      # one decision
```

[EXAMPLE.md](EXAMPLE.md) is an ADR that the user approved. Read it before you write the first ADR, and match its length.

## What a status means

| Status | Meaning | Who must obey it |
|---|---|---|
| Proposed | An open question with a recommended answer. The user did not agree to it yet. | No one. Do not build on it. |
| Accepted | The user made the decision or agreed to it. | All work in the repo. |
| Superseded | A later ADR replaced the decision. | No one. Obey the later ADR. |

## Process

1. Read `docs/adr/README.md` and each ADR that is about the same subject.
2. Find the decisions in the request. One ADR holds one decision. If the request has two decisions, write two ADRs. Choices that the user made together, and that change only together, are one decision.
3. Compare each decision with the accepted ADRs. If a decision disagrees with an accepted ADR, see "Change a decision".
4. Select the status. Use `Accepted` only if the user made the decision or agreed to it. If you made the choice, use `Proposed`.
5. Write one file for each decision. Use the template in the next section.
6. Add a row to `docs/adr/README.md` for each new file. See "README".
7. If the repo has an `AGENTS.md` that lists decisions, update that list in the same change.
8. Do the checks at the end of this file.
9. In your reply, ask for each reason and each option that you did not know. Say which parts of a proposed ADR are yours.

Write the prose by the `writing` skill, in its technical register. Load that skill before you write.

The ADR is about the project. Do not mention this skill, its rules or your instructions in the ADR.

## ADR file

Name the file with the next free number, four digits, then the decision in lower case with hyphens: `0004-docker-container.md`. Do not use a number again, and do not change the number of a file.

<adr-template>

# ADR-0004: The decision in a few words

**Status:** Accepted (2026-11-14)

## Context

Two to four sentences. Say what the project needs and what limits the choice. Include only the facts that make one option better than a different option.

Options: the first option, the second option, the third option.

## Decision

One to three sentences. Say what the project does. Use the present tense.

## Consequences

- A thing that is now true, easier or harder because of the decision.
- The reason that decided between the options.
- A cost of the decision.

</adr-template>

Rules for the ADR file:

- The title names the choice, not the question. "Run in a Docker container" is correct. "Where to run the app" is not.
- The status line has the status and the date of that status: `**Status:** Proposed (2026-11-14)`.
- List each option that was considered, in one `Options:` line at the end of `Context`. Include the option that the project chose. If there was only one option, leave the line out.
- `Decision` holds the choice only. Put the reasons in `Context` and `Consequences`.
- In `Consequences`, say why each rejected option lost, if the reason is not clear from `Context`.
- Include one consequence or more that is a cost. A decision with no cost is not a decision.
- Give exact names and values: the library, the command, the port, the path.
- Link to a different ADR by its number, with the file as the target: `[ADR-0002](0002-in-memory-vault-index.md)`.
- Keep the file to about 20 lines. If it grows longer, look for a second decision in it.
- In an accepted ADR, do not invent a reason or an option. If you do not know why the user made the choice, ask the user.
- If you cannot wait for the answer, write the ADR with the facts that you have. Leave the unknown reason out of the file, and ask for it in your reply.
- A consequence that follows from the decision as a fact is not an invented reason. "The app has one server, so a restart stops the app" is such a fact.
- Do not write an ADR for a choice that is easy to reverse and affects one file, such as the name of a variable.

## Proposed ADRs

Use a proposed ADR for an open question, so that the question has a file before the work starts.

- Write the answer that you recommend in `Decision`, and name the other answers in the `Options:` line.
- The recommendation and its reasons are yours. You can add an option that the user did not name.
- When the user agrees, change the status to `Accepted` with the date of that day.
- If the user selects a different option, write that option in `Decision`, correct `Consequences`, and then change the status to `Accepted`.
- Do not write code that depends on a proposed ADR.

## Change a decision

Do not rewrite an accepted ADR when the decision changes. The old file is the record of what was true before.

If a new decision replaces all of an old one:

1. Write a new ADR with the next number. In `Context`, say what changed since the old ADR and link to it.
2. In the old ADR, change only the status line: `**Status:** Superseded by [ADR-0009](0009-sqlite-for-scan-data.md) (2026-12-01)`. The date is the day of the change.
3. In the README, change the row of the old ADR. See "README".
4. If the old ADR holds a part that the new decision does not replace, say in `Consequences` of the new ADR that the part is now open. Ask the user about it in your reply.

If a new decision replaces one part of an old one:

1. Write a new ADR with the next number. In `Consequences`, say which part of the old ADR it replaces.
2. Keep the status of the old ADR as `Accepted`. In the old ADR, change the sentence that is no longer true so that it points to the new ADR.

If the request disagrees with an accepted ADR and the user did not say that the decision changed, stop. Tell the user which ADR the request disagrees with, and ask if the decision changed. Do not do the work and do not change the ADR until the user answers.

You can correct a wrong link or a spelling error in an accepted ADR.

## README

<readme-template>

# Architecture decisions

One file per decision. A decision that changes gets a new file, and the status of the old file names the file that replaces it.

| ADR | Decision | Status |
|---|---|---|
| [0001](0001-nextjs-with-typescript.md) | Next.js with TypeScript | Accepted |
| [0002](0002-parse-per-page.md) | Parse the vault on each page | Superseded by [0003](0003-in-memory-vault-index.md) |
| [0003](0003-in-memory-vault-index.md) | One vault index held in memory | Accepted |
| [0004](0004-rest-api.md) | A REST API for all data | Proposed |

</readme-template>

Rules for the README:

- List each ADR one time, in the order of the numbers.
- The `Decision` column holds the title of the ADR.
- The `Status` column holds the status with no date.
- The link in the `ADR` column shows only the number.
- If the README is there and has no `Status` column, add the column. Keep the other text of the README.

## Checks

1. Each decision has one file, and the README lists each file.
2. Each file has a status line, `Context`, `Decision` and `Consequences`.
3. The status in the README is the same as the status in the file.
4. No ADR is `Accepted` unless the user made the decision or agreed to it.
5. Each superseded ADR names the ADR that replaced it, and that ADR links to the superseded one.
6. Each link to an ADR opens a file that is there.
7. Run the self-check of the `writing` skill.
