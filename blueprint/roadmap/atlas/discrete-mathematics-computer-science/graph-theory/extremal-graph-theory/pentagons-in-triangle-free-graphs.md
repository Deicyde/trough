---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.ErdosProblem24Wanted.conjecture, MathlibExt.GraphTheory.ErdosProblem24Wanted.conjecture_holds
statement: formalized
---

# Pentagons in triangle-free graphs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/pentagons-in-triangle-free-graphs/index.html).

## Pentagons in triangle-free graphs (Erdős Problem 24)

For every natural number $n$, every
graph on $5n$ vertices with no three pairwise adjacent vertices has at most $n^5$ subgraphs
isomorphic to the $5$-cycle $C_5$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem24Wanted.conjecture`, a definition declared in [WantedExt/GraphTheory/ErdosProblem24Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem24Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/pentagons-in-triangle-free-graphs/index.html#conjecture).

## Pentagon bound for triangle-free graphs (five-cycle case of Erdős Problem 24)

For every
natural number $n$, every graph on $5n$ vertices with no three pairwise adjacent vertices has at
most $n^5$ subgraphs isomorphic to the $5$-cycle $C_5$.

## Sources

- Erdős Problems, Problem 24 (records the Grzesik and Hatami–Hladký–Králʼ–Norine–Razborov resolution), https://www.erdosproblems.com/24; Andrzej Grzesik, On the maximum number of five-cycles in a triangle-free graph, arXiv:1102.0962v3, https://arxiv.org/abs/1102.0962v3; Hamed Hatami, Jan Hladky, Daniel Kral, Serguei Norine, and Alexander Razborov, On the number of pentagons in triangle-free graphs, arXiv:1102.1634v4, https://arxiv.org/abs/1102.1634v4.

Stated but not proved: `MathlibExt.GraphTheory.ErdosProblem24Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/ErdosProblem24Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem24Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/pentagons-in-triangle-free-graphs/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pentagons in triangle-free graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/pentagons-in-triangle-free-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/extremal-graph-theory/pentagons-in-triangle-free-graphs)
