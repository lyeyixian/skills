# Diagram templates

The five templates of the [architecture-docs](SKILL.md) skill. [DIAGRAMS.md](DIAGRAMS.md) has the rules. Copy a template. Keep the `%%{init}%%` line and the `classDef` lines as they are. Change only the nodes, the subgraphs and the arrows.

## Template 1: C4 level 1, system context

Question it answers: who uses the system, and which outside systems does it depend on?

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"system-ui, sans-serif","fontSize":"14px","lineColor":"#8b949e","clusterBkg":"#161b22","clusterBorder":"#30363d","edgeLabelBackground":"#0d1117","primaryTextColor":"#e6edf3","titleColor":"#e6edf3"},"flowchart":{"curve":"linear","nodeSpacing":40,"rankSpacing":50}}}%%
flowchart TB
    user(["<b>Person name</b><br/>[Person]<br/><small>What they do</small>"]):::person
    system["<b>System name</b><br/>[Software system]<br/><small>What it does</small>"]:::system
    ext[("<b>Outside system</b><br/>[External: technology]<br/><small>What it holds</small>")]:::external

    user -- "verb, protocol" --> system
    system -- "verb, protocol" --> ext

    classDef person fill:#1f6feb,stroke:#58a6ff,color:#ffffff,rx:8,ry:8
    classDef system fill:#1f6feb,stroke:#58a6ff,color:#ffffff,rx:8,ry:8
    classDef container fill:#0c2d6b,stroke:#388bfd,color:#e6edf3,rx:8,ry:8
    classDef component fill:#0c2d6b,stroke:#388bfd,color:#e6edf3,rx:8,ry:8
    classDef store fill:#0c2d6b,stroke:#388bfd,color:#e6edf3
    classDef external fill:#21262d,stroke:#8b949e,color:#c9d1d9,stroke-dasharray:4 3,rx:8,ry:8
```

## Template 2: C4 level 2, containers

Question it answers: which parts that run or hold data make up the system, and how do they talk?

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"system-ui, sans-serif","fontSize":"14px","lineColor":"#8b949e","clusterBkg":"#161b22","clusterBorder":"#30363d","edgeLabelBackground":"#0d1117","primaryTextColor":"#e6edf3","titleColor":"#e6edf3"},"flowchart":{"curve":"linear","nodeSpacing":40,"rankSpacing":50}}}%%
flowchart TB
    user(["<b>Person name</b><br/>[Person]<br/><small>What they do</small>"]):::person

    subgraph system["System name"]
        app["<b>Container name</b><br/>[Container: technology]<br/><small>What it does</small>"]:::container
        db[("<b>Store name</b><br/>[Container: technology]<br/><small>What it holds</small>")]:::store
    end

    ext[("<b>Outside system</b><br/>[External: technology]<br/><small>What it holds</small>")]:::external

    user -- "verb, protocol" --> app
    app -- "verb, protocol" --> db
    app -- "verb, protocol" --> ext

    classDef person fill:#1f6feb,stroke:#58a6ff,color:#ffffff,rx:8,ry:8
    classDef system fill:#1f6feb,stroke:#58a6ff,color:#ffffff,rx:8,ry:8
    classDef container fill:#0c2d6b,stroke:#388bfd,color:#e6edf3,rx:8,ry:8
    classDef component fill:#0c2d6b,stroke:#388bfd,color:#e6edf3,rx:8,ry:8
    classDef store fill:#0c2d6b,stroke:#388bfd,color:#e6edf3
    classDef external fill:#21262d,stroke:#8b949e,color:#c9d1d9,stroke-dasharray:4 3,rx:8,ry:8
```

## Template 3: C4 level 3, components

Question it answers: which parts make up one container, and which part can call which?

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"system-ui, sans-serif","fontSize":"14px","lineColor":"#8b949e","clusterBkg":"#161b22","clusterBorder":"#30363d","edgeLabelBackground":"#0d1117","primaryTextColor":"#e6edf3","titleColor":"#e6edf3"},"flowchart":{"curve":"linear","nodeSpacing":40,"rankSpacing":50}}}%%
flowchart TB
    subgraph container["Container name"]
        subgraph groupA["Group name"]
            a["<b>Component name</b><br/>[Component: technology]<br/><small>What it does</small>"]:::component
        end
        subgraph groupB["Group name"]
            b["<b>Component name</b><br/>[Component: technology]<br/><small>What it does</small>"]:::component
        end
    end

    store[("<b>Store name</b><br/>[Container: technology]<br/><small>What it holds</small>")]:::store

    a -- "calls" --> b
    b -- "reads" --> store

    classDef person fill:#1f6feb,stroke:#58a6ff,color:#ffffff,rx:8,ry:8
    classDef system fill:#1f6feb,stroke:#58a6ff,color:#ffffff,rx:8,ry:8
    classDef container fill:#0c2d6b,stroke:#388bfd,color:#e6edf3,rx:8,ry:8
    classDef component fill:#0c2d6b,stroke:#388bfd,color:#e6edf3,rx:8,ry:8
    classDef store fill:#0c2d6b,stroke:#388bfd,color:#e6edf3
    classDef external fill:#21262d,stroke:#8b949e,color:#c9d1d9,stroke-dasharray:4 3,rx:8,ry:8
```

## Template 4: deployment

Question it answers: on which machine does each container run, and what connects the machines?

A subgraph is a machine, a device or a service that runs things. Put a subgraph for a runtime inside its machine, such as Docker inside a server.

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"system-ui, sans-serif","fontSize":"14px","lineColor":"#8b949e","clusterBkg":"#161b22","clusterBorder":"#30363d","edgeLabelBackground":"#0d1117","primaryTextColor":"#e6edf3","titleColor":"#e6edf3"},"flowchart":{"curve":"linear","nodeSpacing":40,"rankSpacing":50}}}%%
flowchart TB
    subgraph device["Device name, device"]
        client["<b>Client name</b><br/>[Container: technology]<br/><small>What it does</small>"]:::container
    end

    subgraph server["Server name, server"]
        subgraph runtime["Runtime name, runtime"]
            app["<b>Container name</b><br/>[Container: technology]<br/><small>What it does</small>"]:::container
        end
        vol[("<b>Store name</b><br/>[Volume]<br/><small>What it holds</small>")]:::store
    end

    subgraph cloud["Service name, external service"]
        ext[("<b>Outside system</b><br/>[External]<br/><small>What it holds</small>")]:::external
    end

    client -- "verb, protocol" --> app
    vol -. "mounted" .-> app
    app -- "verb, protocol" --> ext

    classDef person fill:#1f6feb,stroke:#58a6ff,color:#ffffff,rx:8,ry:8
    classDef system fill:#1f6feb,stroke:#58a6ff,color:#ffffff,rx:8,ry:8
    classDef container fill:#0c2d6b,stroke:#388bfd,color:#e6edf3,rx:8,ry:8
    classDef component fill:#0c2d6b,stroke:#388bfd,color:#e6edf3,rx:8,ry:8
    classDef store fill:#0c2d6b,stroke:#388bfd,color:#e6edf3
    classDef external fill:#21262d,stroke:#8b949e,color:#c9d1d9,stroke-dasharray:4 3,rx:8,ry:8
```

## Template 5: sequence

Question it answers: what happens, in order, when one thing occurs?

- The person or the system that starts the flow is the first participant, as an `actor`.
- The participants are persons, containers, components, outside systems or machines from the other diagrams, with the same names.
- `autonumber` is on.
- A solid arrow `->>` is a call. A dashed arrow `-->>` is its answer.
- Each way the flow can fail is a branch of an `alt` block, with the failure first.

```mermaid
sequenceDiagram
    autonumber
    actor User as Person name
    participant A as Component name
    participant B as Component name

    User->>A: does something
    A->>B: asks for something
    alt the call fails
        B-->>A: error
        A-->>User: what the person sees
    else the call works
        B-->>A: result
        A-->>User: what the person sees
    end
```
