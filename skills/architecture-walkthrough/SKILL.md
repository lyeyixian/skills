---
name: architecture-walkthrough
description: Settle the architecture of an app with the user, one design topic at a time. List the open topics, then for each topic give two or three options with their trade-offs and a recommendation, ask the user, record the answer as an ADR, and update the architecture docs and diagrams before the next topic. Use when the user wants to design or decide the architecture of an app before it is built, asks to go through the open technical decisions, or asks which stack or design to use for a new app or a new step.
---

# Architecture walkthrough

A walkthrough turns a feature spec, or an idea, into an agreed design. You bring the options and a recommendation. The user makes each decision. Each decision is written down before the next topic starts, so the docs are correct at each point and nothing is left only in the conversation.

This skill uses two other skills. Load each one before you do its part.

- `adr` records each decision in `docs/adr/`.
- `architecture-docs` writes the pages and the diagrams in `docs/architecture/`.

Do not write app code in a walkthrough.

## Process

1. Read what is there: the feature spec in `docs/features/`, the ADRs, the architecture docs, the `README.md`, and the code if there is code.
2. Write the list of topics. See "The topic list".
3. Show the list to the user, in the order in which you will ask. Ask if a topic is missing. Start the first topic in the same message. If the answer is only about the first topic, no topic is missing.
4. For each topic, do "One topic". Do not start a topic before the topic before it is recorded.
5. When the list is empty, do "Finish".

## The topic list

A topic is one decision that the user must make, and that changes how the app is built.

- Include a topic only if it is open. A choice that an accepted ADR records, or that the user said as a decision, is not a topic.
- If the user said a choice as a decision and no ADR records it, record it before the first topic. Do not ask about it again.
- Put a topic before each topic that depends on it. The language comes before the test tools. Where the parts run comes before how a release gets there.
- Make a topic small enough for one question. "The backend" is too large. "Where the API runs" is a topic.
- Leave out a choice that is cheap to change later and that the user is not likely to care about. Select a default for it. See "Defaults".
- For a small app, a full subject from the table below can be a default. Tell the user which subjects you made defaults.
- If the user adds a topic, put it in the list where its dependencies permit.

These subjects are common. Use the list to find topics, and leave out each subject that does not apply to the app.

| Subject | Example topics |
|---|---|
| Shape | One process or more than one. How the parts talk. Where the data is. |
| Stack | The language and the framework for each part. The UI library. |
| Code layout | One repo or more. The folders and what each can import. |
| Addresses | The page URLs and the API paths. |
| Data | The store, the schema changes, the backups. |
| Access | Who can sign in, and how. Where the secrets are. |
| Deployment | Where each part runs. How a release gets there. |
| Testing | The layers of tests and the tool for each. |
| Local development | How to start the app on a laptop. Test data. |
| Checks | What runs on each pull request or before each release, and what must pass. |
| Errors and logging | The shape of an error. What is logged, and where. |

## One topic

1. Find the facts that the topic needs. Read the code, the docs and the documentation of each tool. Do not ask the user for a fact that you can find. Ask for a fact that only the user has, such as the size of a server, with the topic that needs it.
2. Write the options. See "Options".
3. Ask the user to select. If you have a tool that shows a choice with buttons, use it, and mark your recommendation.
4. Wait for the answer. Do not record a decision that the user did not make.
5. Record the answer as an accepted ADR, with the `adr` skill. Include the options that lost and why. If the user gave a reason, record that reason.
6. Update each page and each diagram that the answer changes, with the `architecture-docs` skill.
7. Tell the user in one or two sentences what you recorded, with a link. In the same message, start the next topic.

If the user asks a question and does not select, answer the question and ask again. If the user selects an option that you did not give, use that option.

## The docs between topics

- Start `docs/architecture/` after the first answer that names a part of the system. Before that, the ADRs are the only docs.
- A page holds what is agreed, and what you propose with the status "Proposed". Leave out a section that has nothing to show yet.
- When a diagram needs a part that is not agreed, draw the part that you will recommend, and say below the question that it is a proposal.

## Options

- Give two or three options. Give one option only if no second option is reasonable, and say so.
- Name each option by what it is, in a few words: "Inside the Next.js app", "A separate backend service".
- For each option, say what it does in this app, what it costs, and what it makes easy or hard later.
- Use the facts of this app: its size, its users, its server, the decisions before this one. Do not describe a tool in general.
- Recommend one option, and give the reason that decides it. Say when a different option is the better choice, such as "select the second option if you want the repo to show a separate backend".
- If the topic has a clear default, give the recommendation first and the lighter or heavier option after it.
- If you do not know a fact that matters, say so. Do not write a guess as a fact.
- If your recommendation disagrees with what you said before, say so, and say what changed.

Write each message to the user by the `writing` skill, in its voice register. Write the ADRs and the docs in the technical register.

## When an answer changes an earlier decision

An answer can remove the reason for an earlier decision. A second service, for example, removes the reason for "one language for all code".

1. Tell the user which decision is open again, and why.
2. Make that decision the next topic, before you update the diagrams.
3. If the user changes the decision, write a new ADR that supersedes the old one. If the user keeps it, record the new reason in the new ADR of this topic.
4. Update the docs one time, after the two answers.

If the option that the user selected already says how the earlier decision changes, do not ask again. Change the earlier ADR by the rules of the `adr` skill, and tell the user what you changed.

## Defaults

A default is a small choice that you made and the user did not discuss, such as a library that reads a file format.

- Write each default in the docs with the status "Proposed". Do not write an ADR for it.
- Do not ask about each default as a topic.
- If the user asks about a default, or disagrees with it, handle it as a topic.

## When the user gives you the remaining topics

The user can say "use your recommendations for the others". Then do not ask about each topic.

1. Write your recommendation for each remaining topic in the docs, with the status "Proposed". Do not write the ADRs yet.
2. Send one message. List each recommendation with its reason in one sentence, in the order of the topics.
3. In that message, give the full options for each topic that the user can regret: a choice that can lose data, that opens access, that costs money, or that is hard to reverse.
4. Ask for each fact that only the user has. Ask the user to agree to the others as a set.
5. When the user agrees, write one accepted ADR for each topic, and remove the "Proposed" status.

## Finish

1. Tell the user that the list is empty. Give the number of ADRs and the pages that you wrote.
2. List each default that is "Proposed". Ask the user to agree to the defaults or to change them.
3. When the user agrees, change each "Proposed" status in the docs to agreed, and record an ADR for each default that limits how the code is written.
4. Ask if a topic is missing.
5. Do the checks of the `adr` skill and the `architecture-docs` skill on all the files.

The walkthrough is complete when no topic is open and no status is "Proposed".

## Checks

1. Each topic on the list has an accepted ADR, or the user removed the topic or made it a default.
2. Each ADR records a decision that the user made. No ADR records your recommendation as the decision of the user.
3. The docs and the diagrams agree with each ADR.
4. Each choice that the user did not discuss is "Proposed" in the docs and is in your last list of defaults.
5. No app code changed.
