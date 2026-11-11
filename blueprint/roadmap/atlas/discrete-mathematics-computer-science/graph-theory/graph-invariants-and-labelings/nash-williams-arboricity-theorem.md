---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.NashWilliamsWanted.IsArboricityColoring, MathlibExt.Combinatorics.SimpleGraph.NashWilliamsWanted.nash_williams_arboricity
statement: formalized
proof: formalized
---

# Nash-Williams arboricity theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/nash-williams-arboricity-theorem/index.html).

## Arboricity colorings

Let $G$ be a simple graph and $k$ a natural number. A labeling of the
edges of $G$ with labels in $\{0, 1, \dots, k - 1\}$ is an arboricity coloring when, for each
label $i$, the graph on the vertices of $G$ whose edges are the edges of $G$ labeled $i$ is
acyclic, that is, a forest.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.NashWilliamsWanted.IsArboricityColoring`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/NashWilliams.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/NashWilliams.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/nash-williams-arboricity-theorem/index.html#is-arboricity-coloring).

## Nash–Williams arboricity theorem

Let $G$ be a simple graph on a finite vertex set $V$ and let
$k$ be a natural number. Then $G$ has an arboricity coloring with $k$ labels, that is, its edges
can be labeled with $k$ labels so that the edges of each label form a forest, if and only if for
every nonempty set $U \subseteq V$, the number of edges of $G$ with both endpoints in $U$ is at
most $k(|U| - 1)$.

## Sources

- C. St. J. A. Nash-Williams, J. London Math. Soc. 39 (1964), DOI 10.1112/jlms/s1-39.1.12.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.NashWilliamsWanted.nash_williams_arboricity`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/NashWilliams.lean, line 885](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/NashWilliams.lean#L885). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/nash-williams-arboricity-theorem/index.html#nash-williams-arboricity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nash-Williams arboricity theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/nash-williams-arboricity-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-invariants-and-labelings/nash-williams-arboricity-theorem)
