# Diagrams

The diagram rules of the [architecture-docs](SKILL.md) skill.

Each diagram starts from one of five templates, so a shape, a colour or an arrow means the same thing in every diagram. A diagram is a Mermaid block in a markdown file. GitHub shows the block as a picture. Do not make image files.

[TEMPLATES.md](TEMPLATES.md) holds the five templates. Read it before you draw the first diagram.

| Template | Question it answers |
|---|---|
| 1. C4 level 1, system context | Who uses the system, and which outside systems does it depend on? |
| 2. C4 level 2, containers | Which parts that run or hold data make up the system, and how do they talk? |
| 3. C4 level 3, components | Which parts make up one container, and which part can call which? |
| 4. Deployment | On which machine does each container run, and what connects the machines? |
| 5. Sequence | What happens, in order, when one thing occurs? |

A container is a part that runs or holds data, such as a web app, a database or a folder of files. It is not only a Docker container.

## Draw a diagram

1. Find the question that the diagram must answer. One diagram answers one question.
2. Select the template for that question. If no template fits, see "Other diagram types".
3. Read the diagrams that are already in the repo. Use the same name for a thing that they use.
4. Copy the template. Keep the `%%{init}%%` line and all the `classDef` lines as they are.
5. Replace the nodes, the subgraphs and the arrows. Obey the rules in the sections below.
6. Write the text around the diagram. See "Around the diagram".
7. Do the checks at the end of this file.

## Around the diagram

- Put a heading above the diagram. The heading names the diagram type and its subject, such as "Level 2: containers" or "Sequence: a release".
- Below the heading, write the question that the diagram answers, as one sentence.
- Below the diagram, put a table. The first column is the name of an element. The other columns say what the element is and what it does.
- The table lists the nodes of our system. The table of a level 1 diagram also lists the persons and the outside systems.
- Leave the table out if the diagram has fewer than four nodes, and for a sequence diagram.
- The table holds the full description of each element. The node holds the short one.
- If a diagram shows a part that is not agreed, say which part in a sentence below the question. Do not give that part a different look.

## Node labels

Each node has three lines. Mermaid wraps a long line, and a wrapped box is hard to read, so each line has a limit.

| Line | Content | Format | Limit |
|---|---|---|---|
| 1 | The name | Bold, `<b>` | 25 characters |
| 2 | The kind and the technology, in brackets | Normal | 28 characters |
| 3 | What it does | Small, `<small>` | 28 characters |

```text
"<b>Name</b><br/>[Kind: technology]<br/><small>What it does</small>"
```

- Do not put a `<br/>` inside a line. If the text does not fit, make it shorter. The table below the diagram holds the full description.
- Line 2 starts with the kind: `Person`, `Software system`, `Container`, `Component`, `Volume`, `File` or `External`.
- If there is no technology, leave it out, as in `[Person]`.
- Write `[External: technology]` for a system that is outside this system.
- A node has the same three lines in each diagram that shows it.

## Shapes and classes

| Element | Shape | Class | Look |
|---|---|---|---|
| Person | Stadium `([ ])` | `person` | Bright blue, white text |
| This system, on level 1 | Rectangle `[ ]` | `system` | Bright blue, white text |
| Container | Rectangle `[ ]` | `container` | Dark blue, light text |
| Component | Rectangle `[ ]` | `component` | Dark blue, light text |
| Data store, volume or file | Cylinder `[( )]` | `store` | Dark blue, light text |
| System or person outside this system | Rectangle, stadium or cylinder | `external` | Dark grey, dashed outline |
| Server, device or boundary | Subgraph | none | Near-black box |

- Give each node one class, with `:::class` at the end of the node line. Do not add a class, a colour or a `style` line.
- The class shows who owns the part, not where the part runs. A database of this system that a cloud service runs is a `store`.
- A person who uses the system is a `person`. A person who only gets something from it, or who has no access, is `external`.

## Subgraphs

- A subgraph for the system, for a container or for a group of components has one line: the name.
- A group of components can add the rule that the group obeys, after a comma: `Vault module, no Next.js code`.
- A subgraph in a deployment diagram has the name, a comma, then the kind: `Home server, server`.
- The kinds are `device`, `server`, `runtime`, `region` and `external service`. If a part runs as more than one copy, use the count as the kind: `API app, 2 machines`.
- Keep the label of a subgraph to 40 characters or fewer.
- Do not put a subgraph around one `external` node. The node already names the service.
- The groups in template 3 are optional. Use a group when some components obey a rule that the others do not.

## Arrows

| Meaning | Arrow | Label |
|---|---|---|
| A call, a request, a read or a write | Solid `-->` | A verb, then the protocol if it matters: `"git pull, SSH"` |
| A file mount, or data that one part is built from | Dotted `-.->` | A verb |
| No access, or a call that is not permitted | Dotted with a cross `-.-x` | What is blocked: `"no route"`, `"must not call"` |

- Each arrow has a label of 20 characters or fewer. If the full words do not fit, use fewer words. The table holds the full description.
- A solid arrow points away from the part that starts the action.
- A dotted arrow points away from the data, to the part that uses the data.

## Theme

- Templates 1 to 4 are Mermaid flowcharts that go from top to bottom, `flowchart TB`.
- The first line of each flowchart is the `%%{init}%%` line from the template. It sets the font, the line colour, straight lines and the dark background of a subgraph.
- The colours are for GitHub's dark mode. Each box and each label has its own dark background, so the diagram is also clear on a light page.
- A sequence diagram has no `%%{init}%%` line and no `classDef` lines. GitHub changes its colours for dark mode.
- Do not change the theme for one diagram. If the user wants a different look, change the templates, then change every diagram.

## Deployment diagrams

- Show the containers of level 2, each in the subgraph of the machine or the service that runs it.
- Do not show the persons, unless the diagram must show who has no access.
- Show the device that the person uses as a subgraph, with the client inside, as in template 4.

## Sequence diagrams

- The person or the system that starts the flow is the first participant, as an `actor`.
- The participants are persons, containers, components, outside systems or machines from the other diagrams, with the same names.
- Keep `autonumber` on.
- A solid arrow `->>` is a call. A dashed arrow `-->>` is the answer to a call. A call that gets no answer has no dashed arrow.
- Put each way that the flow can fail in a branch of an `alt` block. Put the failure before the usual case. An `alt` block can be inside a different `alt` block.
- Write each message as what the sender does, in a few words: "asks for a rebuild", "runs git pull".
- If you do not know what occurs after a failure, draw only what you know. Ask the user about the remainder in your reply.

## Other diagram types

The templates cover five types. For a different type, such as a class diagram or a state diagram:

- Use the default look of Mermaid, with no `%%{init}%%` line.
- Obey the rules in "Around the diagram".
- Tell the user in your reply that the type has no template.

## Checks

1. Each flowchart starts with the `%%{init}%%` line of the template, and ends with the six `classDef` lines.
2. Each node has three lines and one class.
3. Run `python3 check-labels.py <file>` from the folder of this skill. It finds each label that is longer than its limit. Make each label that it finds shorter.
4. Each arrow has a label.
5. Each diagram has a heading and a question above it. A diagram with four or more nodes has a table below it.
6. Each thing has one name in all the diagrams, in the tables and in the text.
