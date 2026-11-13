---
name: feature-spec
description: Write a feature spec in plain language, one file per user-facing feature in docs/features/. Each file has a short description, a user story, numbered Given/When/Then acceptance criteria, and the assumptions and decisions behind the feature. Use when the user asks for a feature spec, a product spec, acceptance criteria, or a description of what an app does for the person who uses it.
---

# Feature spec

A feature spec says what the app does for the person who uses it. It does not say how to build the app. The reader can be someone who never saw the code, so the spec has no technical terms.

A spec is a folder, `docs/features/`, unless the user names a different folder. The folder holds one file for each feature and a `README.md` for the full spec.

```text
docs/features/
├── README.md              # what the app is, the list of features, what applies to every feature
├── application-board.md   # one feature
└── application-page.md    # one feature
```

[EXAMPLE.md](EXAMPLE.md) is a feature file that the user approved. Read it before you write the first feature file, and match its shape.

## Process

1. Read the project glossary, if there is one. Look for `CONTEXT.md` or `GLOSSARY.md` at the top of the repo. Read the files that are already in `docs/features/`.
2. List the features. A feature is one thing that the person can see or do, and it has a result that the person cares about. If a feature needs more than about ten acceptance criteria, divide it into two features.
3. If the user did not give the list of features, show your list to the user before you write the files.
4. Write one file for each feature. Use the template in the next section.
5. Write `README.md`, or update it if it is there. Use the README template.
6. Do the checks at the end of this file.

Write the prose by the `writing` skill, in its technical register. Load that skill before you write.

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
- Each **Then** must be a thing that the person can see or check when they use the app. "The page feels fast" fails this test. "I see the page in less than two seconds" passes.
- Use exact values. Write the number, the order, or the name of each item that the person sees.
- An assumption is a thing that is not confirmed. A decision is a choice that someone made, with its reason. If the user rejected an alternative, name the alternative in the decision.
- Record a thing that the feature does not do yet as a decision. See the last decision in the example.
- If a feature has no assumptions, remove the `Assumptions` heading. Do the same for `Decisions`.
- Do not invent a decision. If you do not know the answer to a question, write your best answer as an assumption.

## No technical terms

Describe what the person sees and does. Do not describe how the app does it.

- Do not name code, files, folders, databases, frameworks, libraries, services or data formats.
- Do not use words for the parts of a program, such as "endpoint", "component", "query", "cache", "state", "sync" or "render".
- Replace a technical cause with its visible result. "The app reads the vault on each build" becomes "The board shows the change the next time the app updates".
- Use the words of the project glossary for the things in the app. Use one word for one thing in every file.
- Copy the exact values that the person sees, such as a status or a label, and put them in code format: `applied`, `strong-fit`.

Test each sentence with this question: can a person who uses the app, and who cannot read code, check that the sentence is true? If the answer is no, write the sentence again or remove it.

## README

<readme-template>

# App name

Two to four sentences. Say what the app is, who uses it, and what they use it for.

## Features

- [Feature name](feature-name.md). One sentence about what the person does with the feature.

## What applies to every feature

- A rule that is true for all the features, such as "You can use each page on a phone".

</readme-template>

Rules for the README:

- List each feature file one time, in the order in which a new person meets the features.
- Put a rule in "What applies to every feature" only if it is true for all the features. Then remove the rule from the feature files, unless a feature has its own criteria for it.
- The README has no acceptance criteria.

## Checks

1. Each feature has one file, and the README lists each file.
2. Each file has a description, a user story and numbered acceptance criteria.
3. Each criterion has a **Given**, a **When** and a **Then**.
4. Search each file for technical terms and remove them.
5. Compare the names of things with the project glossary and with the other feature files.
6. Run the self-check of the `writing` skill.
