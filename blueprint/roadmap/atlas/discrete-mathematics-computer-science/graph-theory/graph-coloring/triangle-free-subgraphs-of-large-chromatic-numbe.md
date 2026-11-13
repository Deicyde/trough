---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem923Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem923Wanted.conjecture_holds
statement: formalized
---

# Triangle-free subgraphs of large chromatic number

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/triangle-free-subgraphs-of-large-chromatic-numbe/index.html).

## Erdős Problem 923 on triangle-free subgraphs of large chromatic number

The proposition
asserts that for every natural number $n$ there is a natural number $k$ such that every simple
graph $G$, on any vertex set, whose chromatic number is at least $k$ has a triangle-free subgraph
$H$ on the same vertex set whose chromatic number is at least $n$. Chromatic numbers may be
infinite.

Formalized by `MathlibExt.Combinatorics.ErdosProblem923Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem923Wanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem923Wanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/triangle-free-subgraphs-of-large-chromatic-numbe/index.html#conjecture).

## Rödl's theorem on triangle-free subgraphs

For every natural number $n$ there is a natural
number $k$ such that every simple graph $G$, on any vertex set, whose chromatic number is at least
$k$ has a triangle-free subgraph $H$ on the same vertex set whose chromatic number is at least
$n$. Chromatic numbers may be infinite.

This answers Erdős Problem 923 affirmatively; it was proved by Rödl.

## Sources

- Vojtěch Rödl, On the chromatic number of subgraphs of a given graph, Proceedings of the American Mathematical Society 64 (1977), 370–371, https://doi.org/10.1090/S0002-9939-1977-0469806-4.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem923Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem923Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem923Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/triangle-free-subgraphs-of-large-chromatic-numbe/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Triangle-free subgraphs of large chromatic number](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/triangle-free-subgraphs-of-large-chromatic-numbe/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/triangle-free-subgraphs-of-large-chromatic-numbe)
