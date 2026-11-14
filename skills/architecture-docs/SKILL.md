---
name: architecture-docs
description: Write the architecture docs of an app in docs/architecture/, or draw one architecture diagram. The diagrams are Mermaid blocks from five fixed templates with a dark theme - C4 system context, C4 containers, C4 components, deployment, and sequence. The pages are an overview, components, deployment and a stack table. Use when the user asks to document the architecture or the technical design of an app, asks for an architecture, C4, deployment or sequence diagram, asks for a stack list, or asks to update those pages or diagrams after the design changed.
---

# Architecture docs

The architecture docs say how the app is built: its parts, where the parts run, and how they talk. The docs do not say why. Each reason is in an ADR.

The docs are a folder, `docs/architecture/`, unless the user names a different folder.

```text
docs/architecture/
├── README.md        # the list of pages, the system context, the containers
├── components.md    # the parts inside one container, and the main flows
├── deployment.md    # where each part runs, and how a release gets there
└── stack.md         # the frameworks and libraries, each with its job
```

[DIAGRAMS.md](DIAGRAMS.md) has the rules for each diagram, and [TEMPLATES.md](TEMPLATES.md) has the five templates. Read the two files before you draw the first diagram.

The `adr` skill records each decision. Load it before you write an ADR.

## One diagram only

If the user asks for a diagram and not for the docs, do "Draw a diagram" in [DIAGRAMS.md](DIAGRAMS.md). Put the diagram in the file that the user names. Do not write the other pages.

## Process

1. Read the docs that are in the repo: `docs/features/`, `docs/adr/`, `docs/architecture/` and the `README.md`. Read the project glossary, `CONTEXT.md` or `GLOSSARY.md`, if there is one.
2. Read the code, if there is code. The docs must agree with the code.
3. List the containers. A container is a part that runs or holds data, such as a web app, a database or a folder of files.
4. Sort each technical choice into agreed or not agreed. A choice is agreed if an accepted ADR records it or the user said it as a decision. A choice that the user gave as an idea, such as "I'm thinking", is not agreed.
5. If an agreed choice has no ADR, write the ADR with the `adr` skill. Do not write an ADR for a choice that is not agreed, unless the user asks for one.
6. Write the pages. Use the page sections below.
7. Do the checks at the end of this file.
8. In your reply, list each choice that is not agreed, so that the user can decide. List each name that you gave to a thing, and each thing that you added and the user did not say.

Write the prose by the `writing` skill, in its technical register. Load that skill before you write. Write the question above a diagram as a question.

The docs are about the app. Do not mention this skill, its rules or your instructions in the docs.

## Rules for all pages

- Start each page with one or two sentences that say what the page shows.
- Describe the app as it is, or as the design says it will be for the version that you document. Name that version on the README page.
- Mark each thing that is not agreed. Write "Proposed" in a status column, or say in a sentence that the part is a proposal.
- Use one name for one thing on all pages and in all diagrams. Use the words of the project glossary.
- Do not give the reason for a choice. Link to the ADR where a reader will ask why.
- Do not copy a list that the code can generate, such as the endpoints of an API. Link to the generated document.
- Write only what the user said, what the repo shows, and what follows from those as a fact. If a section needs a thing that you do not know, leave the thing out and ask in your reply.
- Do not put a secret, a real hostname or personal data in the docs.

## README.md

The overview page. A reader who reads only this page knows what the system is and what its parts are.

<readme-template>

# Architecture

One or two sentences. Say what the folder covers and which version of the app it describes. Link to the feature spec and to the ADRs if the repo has them.

| Page | What it shows |
|---|---|
| This page | C4 level 1 and 2: the system and its containers |
| [Components](components.md) | C4 level 3, and what happens in the main flows |
| [Deployment](deployment.md) | Where each part runs, and how a release reaches the server |
| [Stack](stack.md) | The frameworks and libraries, each with its job |

## Level 1: system context

The question, the diagram from template 1, and a table.

| Element | Kind | Job |
|---|---|---|
| Name | Person, this system, or outside system | What it does, in one sentence |

## Level 2: containers

The question, the diagram from template 2, and a table.

| Container | Technology | Job |
|---|---|---|
| Name | The technology | What it does, in one sentence |

## What stays out of this repo

The things that the repo must not hold, such as keys or private data. Remove this section if the user and the repo name none.

## Later steps

1. The version that this folder covers.
2. A later step, in one sentence.

</readme-template>

- List only the pages that are in the folder.
- `Later steps` lists the planned versions in order. Do not design them here. Remove the section if the user gave no plan.

## components.md

Write this page if a container has parts with rules about which part can call which. If each container is one simple part, do not write the page.

- `## Level 3: components of <container>`: the question, the diagram from template 3, and a table with the columns `Component` and `Job`.
- Write one such section for each container that has components.
- `## Sequence: <flow>`: one section for each main flow, with the question and a diagram from template 5. A main flow is a thing that the person does often, or a flow that can fail in a way that the person sees.
- If the split into components is not agreed, say so in the first paragraph.

## deployment.md

- `## Deployment: <version or environment>`: the question, the diagram from template 4, and a table with the columns `Node`, `Runs` and `Holds`. A node is a machine or a service that runs things.
- `## Sequence: a release`: what happens between a merge and the new version on the server. Use template 5.
- `## Settings`: a table with the columns `Setting`, `Where it is set` and `Purpose`. List each environment variable and each mounted file that the code or the design names. Do not write the value of a secret. Remove the section if no setting has a name yet.
- `## One-time setup`: the numbered steps to prepare a new server. Remove the section if the user and the repo give no steps.
- If the app has more than one environment, write one `Deployment` section for each environment.

## stack.md

One table. Each row is one framework, library or tool, with the job that it does in this app.

<stack-template>

# Stack

The frameworks and libraries, each with its job. A row marked "Proposed" is not agreed yet.

| Layer | Choice | Job | Status |
|---|---|---|---|
| Language | TypeScript | All app code | [ADR-0001](../adr/0001-nextjs-with-typescript.md) |
| Unit tests | Vitest | The vault module against made-up notes | Proposed |

</stack-template>

- `Layer` is the role, such as "Framework", "Styling" or "Unit tests". `Choice` is the name of the tool.
- `Job` says what the tool does in this app, in a few words. Do not describe the tool in general.
- `Status` is a link to the accepted ADR that records the choice. If there is no accepted ADR, write "Proposed".
- Order the rows from the code out: language, framework, libraries, tests, build, then all that runs or serves the app.
- When the code is there, give the version of each tool from the lock file.
- List a tool only if the app uses it or the design names it.

## Update the docs

When the design or the code changes:

1. Record the change as an ADR first, with the `adr` skill.
2. Change each diagram, table and sentence that the change makes wrong. Search all pages for the old name.
3. Change the status in `stack.md` for each choice that is now agreed.

## Checks

1. The README lists each page in the folder, and each link opens a file that is there.
2. Each diagram passes the checks in [DIAGRAMS.md](DIAGRAMS.md).
3. Each container in the level 2 diagram is in the container table and in the deployment diagram. Its technology is in the stack table.
4. Each name is the same on all pages.
5. Each `Status` in `stack.md` is a link to an accepted ADR or the word "Proposed".
6. No page gives the reason for a choice.
7. No page lists a thing that the code generates.
8. Run the self-check of the `writing` skill on the prose. Do not include the Mermaid blocks in its searches.
