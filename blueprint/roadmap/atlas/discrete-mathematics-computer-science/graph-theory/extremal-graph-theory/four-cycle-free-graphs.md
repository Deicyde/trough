---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.FourCycleExtremalValuesWanted.extremalNumber_cycleGraph_four_one_to_twenty, MathlibExt.Combinatorics.SimpleGraph.FourCycleExtremalValuesWanted.extremalNumber_cycleGraph_four_projectivePlane_order
statement: formalized
---

# Four-cycle-free graphs

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/four-cycle-free-graphs/index.html).

## Extremal numbers of the four-cycle up to twenty vertices

For a natural number $n$, let
$\mathrm{ex}(n; C_4)$ be the largest number of edges of a simple graph on $n$ vertices that
contains no four-cycle $C_4$ as a (not necessarily induced) subgraph. For
$n = 1, 2, \dots, 20$ the values of $\mathrm{ex}(n; C_4)$ are, in order,
$0, 1, 3, 4, 6, 7, 9, 11, 13, 16, 18, 21, 24, 27, 30, 33, 36, 39, 42, 46$.

## Sources

- C. R. J. Clapham, A. Flockhart, and J. Sheehan, *Graphs without four-cycles*, J. Graph Theory 13 (1989), 29–47 (`n ≤ 21`); OEIS A006855; listed in leansolving/SqueezeBench `SqueezeBench/Problems/ExC4/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.FourCycleExtremalValuesWanted.extremalNumber_cycleGraph_four_one_to_twenty` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/FourCycleExtremalValuesWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/FourCycleExtremalValuesWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/four-cycle-free-graphs/index.html#extremal-number-cycle-graph-four-one-to).

## Füredi's theorem on four-cycle-free graphs

For a natural number $n$, let
$\mathrm{ex}(n; C_4)$ be the largest number of edges of a simple graph on $n$ vertices that
contains no four-cycle $C_4$ as a (not necessarily induced) subgraph. For every prime power
$q > 13$, $\mathrm{ex}(q^2 + q + 1; C_4) = q (q + 1)^2 / 2$; the division is exact because
$q (q + 1)$ is even.

The bound is attained by the polarity graph of the projective plane of order $q$.

## Sources

- Z. Füredi, *On the number of edges of quadrilateral-free graphs*, J. Combin. Theory Ser. B 68 (1996), 1–6; listed in SqueezeBench `SqueezeBench/Problems/ExC4/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.FourCycleExtremalValuesWanted.extremalNumber_cycleGraph_four_projectivePlane_order` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/FourCycleExtremalValuesWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/FourCycleExtremalValuesWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/four-cycle-free-graphs/index.html#extremal-number-cycle-graph-four-project).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Four-cycle-free graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/four-cycle-free-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/extremal-graph-theory/four-cycle-free-graphs)
