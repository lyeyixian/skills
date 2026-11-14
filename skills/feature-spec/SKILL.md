---
name: feature-spec
description: Write a feature spec in plain language, one file per user-facing feature in docs/features/. Each file has a short description, a user story, numbered Given/When/Then acceptance criteria, and the assumptions and decisions behind the feature. After the app is built, docs/features/ is the baseline, and a new or changed behaviour is a change in docs/changes/ that the user approves before code is written. Use when the user asks for a feature spec, a product spec, acceptance criteria, or a description of what an app does for the person who uses it, or when work adds, changes or removes a behaviour of an app that has a feature spec.
---

# Feature spec

A feature spec says what the app does for the person who uses it. It does not say how to build the app. The reader can be someone who never saw the code, so the spec has no technical terms.

A spec is a folder, `docs/features/`, unless the user names a different folder. The folder holds one file for each feature and a `README.md` for the full spec.

```text
docs/features/
├── README.md              # what the app is, the list of features
├── every-page.md          # the criteria that apply to every feature
├── application-board.md   # one feature
└── application-page.md    # one feature
```

[EXAMPLE.md](EXAMPLE.md) is a feature file that the user approved. Read it before you write the first feature file, and match its shape.

Only the user approves the spec. You write a spec or a change to it as a proposal, and you say so in your reply. If code is already built from the spec, do not edit `docs/features/` to propose a behaviour. See "Change a spec that the app is built from".

## Process

1. Read the project glossary, if there is one. Look for `CONTEXT.md` or `GLOSSARY.md` at the top of the repo. Read the files that are already in `docs/features/`.
2. Compare the request with the project. If the request says a thing that the project does not agree with, write what the person will see and record the difference as an assumption.
3. List the features. A feature is one thing that the person can see or do, and it has a result that the person cares about. If a feature needs more than about twelve acceptance criteria, tell the user in your reply that it can be two features. Do not divide a feature that the user named, and do not write this note in the spec.
4. If the user did not give the list of features, show your list to the user before you write the files.
5. Write one file for each feature. Use the template in the next section.
6. If some criteria apply to every feature, write the file for the whole app. See "Criteria for the whole app".
7. Write `README.md`, or update it if it is there. Use the README template.
8. Do the checks at the end of this file.
9. In your reply, list each criterion that holds a choice of yours, and each assumption. Ask the user to confirm or change each one.

Write the prose by the `writing` skill, in its technical register. Load that skill before you write. That register does not permit "I". This skill does, for the criteria and for the writer in `Assumptions` and `Decisions`.

The spec is about the app. Do not mention this skill, its rules or your instructions in the spec.

## Feature file

Name the file after the feature, in lower case with hyphens: `application-board.md`.

<feature-template>

# Feature name

Two to four sentences. Say what the feature is, where the person finds it, and what the person uses it for. Speak to the person as "you".

**As** the person who has the need,
**I want** the thing that the feature gives me,
**so that** the result I care about.

## Acceptance criteria

### 1. The result, in a few words

- **Given** the situation before the person acts
- **When** the person does one thing
- **Then** the thing that the person sees
- **And** a second thing that the person sees

### 2. The next result

- **Given** ...
- **When** ...
- **Then** ...

## Assumptions

- A thing that you took as true and that the user did not confirm.

## Decisions

- **The choice in a few words.** The reason for the choice. Say who made the choice, and the date if you know it.

</feature-template>

Rules for the feature file:

- Write one user story for each feature. Name the person by what they do, not as "the user".
- Number the acceptance criteria. Give each criterion a title that names its result, such as "The best fits come first".
- Write each criterion in the first person, as the person in the user story.
- Each criterion tests one result. A criterion can have a second **When** and **Then** pair if the second action undoes or completes the first. See criteria 2 and 5 in the example.
- Include the criteria for the cases that are not the usual case: nothing to show, a wrong entry, a small screen.
- Put a condition in a **Given** line. Do not put "if" in a **Then** line or an **And** line.
- Each **Then** must be a thing that the person can see or check when they use the app. "The page feels fast" fails this test. "I see the page in less than two seconds" passes.
- Use exact values. Write the number, the order, or the name of each item that the person sees.
- If the app does not have a label or a message yet, propose one. List all the labels that you proposed in one assumption.
- A thing that the person sees or does in the app is a criterion. This includes an order, a default, a label, what a missing value shows, and what stays after Back or a bookmark. Do not put such a thing only in `Assumptions` or `Decisions`.
- An assumption is a fact about the person or their data that the user did not confirm, such as "The list has about 40 items today". It is not a behaviour of the app.
- If the request has a hole and you fill it with a behaviour, write the behaviour as a criterion and list it in your reply. The user approves it there.
- A decision is a choice that the user made or agreed to, with its reason. If the user rejected an alternative, name the alternative in the decision. A decision can give the reason for a criterion. It can also say what the feature does not do.
- In the criteria, "I" is the person in the user story. In `Assumptions` and `Decisions`, "you" is the user and "I" is the writer of the spec.
- If the user said that the feature does not do a thing yet, record that as a decision. See the last decision in the example. If you only think that the feature does not do the thing, record it as an assumption.
- If a feature has no assumptions, remove the `Assumptions` heading. Do the same for `Decisions`.
- Do not invent a decision. A choice that you made is not a decision until the user agrees to it in words. If you do not know the answer to a question, ask the user. If you cannot wait, write your best answer as an assumption or as a criterion, and list it in your reply.

## No technical terms

Describe what the person sees and does. Do not describe how the app does it.

- Do not name code, files, folders, databases, frameworks, libraries, services or data formats.
- Do not use words for the parts of a program, such as "endpoint", "component", "query", "cache", "state", "sync" or "render".
- Replace a technical cause with its visible result. "The app reads the vault on each build" becomes "The board shows the change the next time the app updates".
- If the user made a technical choice, record its visible result as a decision. "Keep the filters in the URL" becomes "A bookmark of the board keeps your choices". The technical detail goes in the implementation spec, not in this spec.
- Words for things that the person sees in a browser are not technical: "page", "link", "address", "tab", "bookmark", "back button".
- Use the words of the project glossary for the things in the app. Use one word for one thing in every file.
- Copy the exact values that the person sees, such as a status or a label, and put them in code format: `applied`, `strong-fit`.

Test each sentence with this question: can a person who uses the app, and who cannot read code, check that the sentence is true? If the answer is no, write the sentence again or remove it.

## Criteria for the whole app

Some criteria are true for every feature. Examples are a menu on each page, a sign-in, and a page that works on a phone.

- Put these criteria in one feature file for the whole app. Name the file after what the criteria cover, such as `every-page.md`.
- Use the feature template: a description, a user story, numbered criteria, assumptions and decisions.
- Say in the description that the other feature files do not repeat these criteria.
- Put a criterion in this file only if it is true for all the features.
- Remove the criterion from the other feature files. A feature keeps its own criterion when the feature does a specific thing, such as "I can swipe sideways to go to the next column" for a board on a phone.
- If no criterion applies to every feature, do not write this file.

## Change a spec that the app is built from

After code is built from the spec, `docs/features/` is the baseline. The baseline says what the app does now. A behaviour that is not built is a change, and a change has its own folder until its code is merged.

```text
docs/changes/
├── change-status-from-board/     # one open change
│   ├── README.md                 # the reason, the status and the files
│   └── application-board.md      # the changes to one feature file
└── archive/
    └── 2026-11-20-open-the-resume/
```

If the repo has a `docs/changes/README.md`, obey it. If it does not, use these rules.

1. Write the change folder. Name it after the change, in lower case with hyphens.
2. In its `README.md`, write the title, the line `**Status:** Proposed (2026-11-14)`, two to four sentences about what the person can do after the change, and a list of the files in the folder.
3. For a feature that is in the baseline, write a file with the name of the feature file. Use the change template below. Write only the parts that change.
4. For a new feature, write the full feature file in the change folder.
5. Ask the user to approve the change. Do not write code and do not edit `docs/features/` before the user approves in words.
6. When the user approves, set the status to `Approved` with the date.
7. If the build finds a behaviour that no approved criterion covers, stop and ask the user. Add the answer to the change as a criterion.
8. When the code is ready to merge, fold the change. Apply it to the files in `docs/features/`, and move the folder to `docs/changes/archive/` with the date in front of its name. Do this in the same pull request as the code, as its last commit.
9. If the repo gates `docs/features/`, such as with a label on the pull request, the user gives that approval. Do not give it yourself.

<change-template>

# Feature name

Baseline: [feature-name.md](../../features/feature-name.md)

## Added criteria

### 10. The result, in a few words

- **Given** ...
- **When** ...
- **Then** ...

## Changed criteria

### 2. The title of the criterion after the change

The full text of the criterion after the change.

## Removed criteria

### 5. The title of the criterion

One sentence that says why the app stops doing this.

## Other changes

- A change to the description, the user story, an assumption or a decision.

</change-template>

Rules for a change:

- An added criterion takes the next free number of the feature file.
- A criterion keeps its number for as long as it is in the spec. Do not give the number of a removed criterion to a new one. Tests can hold the number.
- Remove a heading of the template that has nothing below it.
- A fix that makes the code do what the baseline already says is not a change. It needs no folder.
- The rules for a feature file apply to each criterion in a change.

## README

<readme-template>

# App name

Two to four sentences. Say what the app is, who uses it, and what they use it for.

## Features

- [Feature name](feature-name.md). One sentence about what the person does with the feature.

</readme-template>

Rules for the README:

- List each feature file one time, in the order in which a new person meets the features.
- If the spec has a file for the whole app, list it first.
- If a feature is in the app and has no file, list its name with no link and add "No spec yet".
- For the title, use the name that the user gives the app. If the app has no name, use a few plain words for what it does.
- The README has no acceptance criteria and no rules for the features. Those go in the file for the whole app.

## Checks

1. Each feature has one file, and the README lists each file.
2. Each file has a description, a user story and numbered acceptance criteria.
3. Each criterion has a **Given**, a **When** and a **Then**.
4. Search each file for technical terms and remove them.
5. A criterion that applies to every feature is in the file for the whole app, and in no other file.
6. Compare the names of things with the project glossary and with the other feature files.
7. No behaviour of the app is only in `Assumptions` or `Decisions`. Each one is a criterion.
8. No decision is in the spec unless the user made it or agreed to it in words.
9. If code is built from the spec, each new behaviour is in `docs/changes/`, and `docs/features/` changes only in a fold.
10. Run the self-check of the `writing` skill.
