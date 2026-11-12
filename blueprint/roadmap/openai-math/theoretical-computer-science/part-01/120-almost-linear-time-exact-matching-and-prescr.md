---
declaration: section
origin: cited
---

# 120. Almost-linear-time exact matching and prescribed-degree factors in general graphs

1 manuscript, with no Lean, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a randomized algorithm finding an exact maximum-cardinality matching in any simple undirected graph in $(n+m)^{1+o(1)}$ word time, with success probability at least 2/3. The time bound holds on every computation path. The same guarantees apply to finding a spanning subgraph with prescribed admissible vertex degrees, or deciding that none exists.

## Almost-Linear-Time Maximum-Cardinality Matching in General Graphs

We prove that maximum-cardinality matching in a simple undirected graph with *n* vertices and *m* edges can be found by one uniform randomized algorithm in $(n+m)^{1+o(1)}$ time. The bound holds on every computation path in a logarithmic-word model, and the algorithm returns an explicit maximum matching with probability at least 2/3. An explicit reduction gives the same time and probability guarantees for deciding whether a simple host graph has a spanning subgraph with prescribed valid vertex degrees, and for finding one when it exists.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/main.pdf).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
