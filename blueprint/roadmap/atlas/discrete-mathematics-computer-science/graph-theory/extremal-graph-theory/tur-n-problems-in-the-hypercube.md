---
declaration: section
origin: cited
lean: SimpleGraph.hypercubeGraph, SimpleGraph.hypercubeGraph_adj, SimpleGraph.hypercubeGraph_zero_not_adj, SimpleGraph.hypercubeGraph_one_adj, SimpleGraph.hypercubeGraph_zero_edgeSet, SimpleGraph.hypercubeGraph_subgraph_edgeSet_ncard_le, SimpleGraph.hypercubeTuranNumber, SimpleGraph.le_hypercubeTuranNumber
statement: formalized
---

# Turán problems in the hypercube

15 results, 11 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html).

## Hypercube graph

For a natural number $n$, the $n$-dimensional hypercube $Q_n$ is the
simple graph whose vertices are the functions from $\{0, \dots, n-1\}$ to the Booleans
$\{\mathrm{true}, \mathrm{false}\}$, with an edge between two vertices exactly when they differ
in exactly one coordinate.

Formalized by `SimpleGraph.hypercubeGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-graph).

## Adjacency in the hypercube

For every natural number $n$ and all vertices $x, y$ of the
$n$-dimensional hypercube $Q_n$ (functions from $\{0, \dots, n-1\}$ to the Booleans), $x$ and
$y$ are adjacent in $Q_n$ if and only if there is exactly one coordinate $i$ with
$x_i \ne y_i$.

Formalized by `SimpleGraph.hypercubeGraph_adj`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-graph-adj).

## No two vertices of the zero-dimensional hypercube are adjacent

For all vertices $x, y$
of the $0$-dimensional hypercube $Q_0$, $x$ and $y$ are not adjacent in $Q_0$.

Any two vertices agree on all (zero) coordinates.

Formalized by `SimpleGraph.hypercubeGraph_zero_not_adj`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-graph-zero-not-adj).

## An edge of the one-dimensional hypercube

In the $1$-dimensional hypercube $Q_1$, the
constant vertex $\mathrm{true}$ and the constant vertex $\mathrm{false}$ are adjacent.

Formalized by `SimpleGraph.hypercubeGraph_one_adj`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-graph-one-adj).

## The zero-dimensional hypercube has no edges

The edge set of the $0$-dimensional
hypercube $Q_0$ is empty.

Formalized by `SimpleGraph.hypercubeGraph_zero_edgeSet`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-graph-zero-edge-set).

## Subgraphs of the hypercube have at most as many edges

For every natural number $n$,
every subgraph of the $n$-dimensional hypercube $Q_n$ has at most as many edges as $Q_n$.

Formalized by `SimpleGraph.hypercubeGraph_subgraph_edgeSet_ncard_le`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-graph-subgraph-edge-set-ncard).

## Hypercube Turán number

For a natural number $n$ and a simple graph $H$, let $Q_n$ be the
$n$-dimensional hypercube. The hypercube Turán number $\mathrm{ex}(Q_n, H)$ is the largest number
of edges of a subgraph (not necessarily spanning) of $Q_n$ that contains no copy of $H$, that is,
no subgraph isomorphic to $H$; it is $0$ when no such subgraph exists.

Formalized by `SimpleGraph.hypercubeTuranNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-turan-number).

## The hypercube Turán number bounds every free subgraph

For every natural number $n$ and
every simple graph $H$, let $Q_n$ be the $n$-dimensional hypercube and let $\mathrm{ex}(Q_n, H)$
be the hypercube Turán number of $H$ in $Q_n$. If $S$ is a subgraph of $Q_n$ that contains no
copy of $H$, then $S$ has at most $\mathrm{ex}(Q_n, H)$ edges.

Formalized by `SimpleGraph.le_hypercubeTuranNumber`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#le-hypercube-turan-number).

## Upper bound for the hypercube Turán number

For every natural number $n$ and every
simple graph $H$, writing $Q_n$ for the $n$-dimensional hypercube, the hypercube Turán number
$\mathrm{ex}(Q_n, H)$ is at most the number of edges of $Q_n$.

Formalized by `SimpleGraph.hypercubeTuranNumber_le_edgeSet_ncard`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-turan-number-le-edge-set-ncard).

## Attainment of the hypercube Turán number

Let $n$ be a natural number, $H$ a simple
graph, $Q_n$ the $n$-dimensional hypercube, and $\mathrm{ex}(Q_n, H)$ the hypercube Turán number.
If $Q_n$ has at least one subgraph (not necessarily spanning) that contains no copy of $H$, then
some subgraph $S$ of $Q_n$ contains no copy of $H$ and has exactly $\mathrm{ex}(Q_n, H)$ edges.

Formalized by `SimpleGraph.exists_attains_hypercubeTuranNumber`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#exists-attains-hypercube-turan-number).

## The hypercube Turán number in dimension zero

For every simple graph $H$, writing $Q_0$
for the $0$-dimensional hypercube, the hypercube Turán number $\mathrm{ex}(Q_0, H)$ is $0$.

Formalized by `SimpleGraph.hypercubeTuranNumber_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/HypercubeExtremal.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-turan-number-zero).

## Four-cycle-free subgraphs of the hypercubes of dimensions one to six

For a natural
number $n$, let $Q_n$ be the $n$-dimensional hypercube, let $C_4$ be the cycle on four vertices,
and let $\mathrm{ex}(Q_n, C_4)$ be the largest number of edges of a subgraph of $Q_n$ that
contains no copy of $C_4$. Then for $n = 1, 2, 3, 4, 5, 6$ the value of $\mathrm{ex}(Q_n, C_4)$
is $1$, $3$, $9$, $24$, $56$ and $132$ respectively.

## Sources

- OEIS A245762; `ex(Q₆, C₄) = 132` is H. Harborth and H. Nienborg, *Maximum number of edges in squarefree subgraphs of the n-cube*, Bull. Inst. Combin. Appl. 12 (1994), 55–60; listed in leansolving/SqueezeBench `SqueezeBench/Problems/HypercubeC4/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.HypercubeFourCycleFreeWanted.hypercubeTuranNumber_cycleGraph_four_one_to_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/HypercubeFourCycleFreeWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/HypercubeFourCycleFreeWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-turan-number-cycle-graph-four).

## Lower bound for four-cycle-free subgraphs of the seven-dimensional hypercube

Let $Q_7$
be the $7$-dimensional hypercube and $C_4$ the cycle on four vertices. The largest number
$\mathrm{ex}(Q_7, C_4)$ of edges of a subgraph of $Q_7$ that contains no copy of $C_4$ is at
least $304$.

The bound is witnessed by an explicit construction.

## Sources

- M. Minamoto, *C₄-free subgraphs of the hypercubes Q₆, Q₇, and Q₈*, arXiv:2603.29127 (2026); listed in SqueezeBench `SqueezeBench/Problems/HypercubeC4/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.HypercubeFourCycleFreeWanted.le_hypercubeTuranNumber_seven_cycleGraph_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/HypercubeFourCycleFreeWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/HypercubeFourCycleFreeWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#le-hypercube-turan-number-seven-cycle-gr).

## Upper bound for four-cycle-free subgraphs of the seven-dimensional hypercube

Let $Q_7$
be the $7$-dimensional hypercube and $C_4$ the cycle on four vertices. The largest number
$\mathrm{ex}(Q_7, C_4)$ of edges of a subgraph of $Q_7$ that contains no copy of $C_4$ is at
most $308$.

The bound comes from averaging over the fourteen facets of $Q_7$: each is a copy of $Q_6$ and
each edge lies in six of them, so $\mathrm{ex}(Q_7, C_4) \le 14 \cdot \mathrm{ex}(Q_6, C_4) / 6 =
14 \cdot 132 / 6 = 308$.

## Sources

- the averaging bound applied to `ex(Q₆, C₄) = 132` (Harborth and Nienborg 1994), as stated in SqueezeBench `SqueezeBench/Problems/HypercubeC4/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.HypercubeFourCycleFreeWanted.hypercubeTuranNumber_seven_cycleGraph_four_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/HypercubeFourCycleFreeWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/HypercubeFourCycleFreeWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#hypercube-turan-number-seven-cycle-graph).

## Lower bound for four-cycle-free subgraphs of the eight-dimensional hypercube

Let $Q_8$
be the $8$-dimensional hypercube and $C_4$ the cycle on four vertices. The largest number
$\mathrm{ex}(Q_8, C_4)$ of edges of a subgraph of $Q_8$ that contains no copy of $C_4$ is at
least $682$.

The bound is witnessed by an explicit construction.

## Sources

- M. Minamoto, *C₄-free subgraphs of the hypercubes Q₆, Q₇, and Q₈*, arXiv:2603.29127v5 (2026), which improves the bound `680` of its earlier versions; SqueezeBench `SqueezeBench/Problems/HypercubeC4/README.md` and OEIS A245762 still list `680`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.HypercubeFourCycleFreeWanted.le_hypercubeTuranNumber_eight_cycleGraph_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/HypercubeFourCycleFreeWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/HypercubeFourCycleFreeWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html#le-hypercube-turan-number-eight-cycle-gr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turán problems in the hypercube](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/extremal-graph-theory/tur-n-problems-in-the-hypercube)
