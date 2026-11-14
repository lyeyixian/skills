#!/usr/bin/env python3
"""Find the labels in Mermaid flowcharts that are longer than their limits.

Usage: python3 check-labels.py FILE.md [FILE.md ...]

The limits come from DIAGRAMS.md: 25 characters for the name of a node, 28 for
the kind line, 28 for the description line, 20 for the label of an arrow, and
40 for the label of a subgraph.
The exit code is 1 if a label is too long or a node does not have three lines.
"""
import html
import re
import sys

NODE_LIMITS = (25, 28, 28)
ARROW_LIMIT = 20
SUBGRAPH_LIMIT = 40

BLOCK = re.compile(r"```mermaid\n(.*?)```", re.S)
# A node label is a quoted string inside a shape bracket: ["..."], (["..."]) or [("...")].
NODE = re.compile(r'[\[(]"([^"]*)"[\])]')
# An arrow label is a quoted string between the two halves of an arrow.
ARROW = re.compile(r'(?:--|-\.)\s*"([^"]*)"\s*(?:-->|\.->|\.-x|--x|---)')
TAG = re.compile(r"</?(?:b|small)>")


def text_of(line):
    return html.unescape(TAG.sub("", line)).strip()


def check(path):
    problems = []
    with open(path, encoding="utf-8") as f:
        source = f.read()
    for block in BLOCK.finditer(source):
        body = block.group(1)
        if not re.search(r"^\s*flowchart\b", body, re.M):
            continue
        first = source.count("\n", 0, block.start(1)) + 1
        for offset, line in enumerate(body.split("\n")):
            number = first + offset
            subgraph = re.match(r'\s*subgraph\s+\w+\["([^"]*)"\]', line)
            if subgraph:
                if len(subgraph.group(1)) > SUBGRAPH_LIMIT:
                    problems.append(f"{path}:{number}: {len(subgraph.group(1))} characters, limit {SUBGRAPH_LIMIT}: {subgraph.group(1)}")
                continue
            for label in NODE.findall(line):
                parts = [text_of(p) for p in re.split(r"<br\s*/?>", label)]
                if len(parts) != 3:
                    problems.append(f"{path}:{number}: node has {len(parts)} lines, not 3: {label}")
                    continue
                for part, limit in zip(parts, NODE_LIMITS):
                    if len(part) > limit:
                        problems.append(f"{path}:{number}: {len(part)} characters, limit {limit}: {part}")
            for label in ARROW.findall(line):
                if len(label) > ARROW_LIMIT:
                    problems.append(f"{path}:{number}: {len(label)} characters, limit {ARROW_LIMIT}: {label}")
    return problems


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    problems = [p for path in sys.argv[1:] for p in check(path)]
    for problem in problems:
        print(problem)
    if not problems:
        print("All labels are within their limits.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
