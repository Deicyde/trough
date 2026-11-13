---
declaration: section
origin: cited
lean: SimpleGraph.generalizedExtremalNumber, SimpleGraph.generalizedExtremalNumber_eq_sup, SimpleGraph.copyCount_le_generalizedExtremalNumber, SimpleGraph.generalizedExtremalNumber_le_iff, SimpleGraph.exists_free_copyCount_eq_generalizedExtremalNumber
statement: formalized
proof: formalized
---

# Generalized Turán numbers

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/generalized-tur-n-numbers/index.html).

## Generalized Turán number

Let $n$ be a natural number and let $T$ and $H$ be simple graphs,
where $T$ has finitely many vertices. A copy of a graph in a graph $G$ is a subgraph of $G$
isomorphic to it, and $G$ is $H$-free if it contains no copy of $H$. The generalized Turán number
$\mathrm{ex}(n, T, H)$ is the largest number of copies of $T$ in an $H$-free simple graph on the
vertex set $\{0, 1, \dots, n-1\}$, and is $0$ if there is no such graph.

The source considers graphs $T$ and $H$ without isolated vertices; the definition does not require
this.

Formalized by `SimpleGraph.generalizedExtremalNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/generalized-tur-n-numbers/index.html#generalized-extremal-number).

## The generalized Turán number as a supremum

Let $n$ be a natural number and let $T$ and $H$
be simple graphs, where $T$ has finitely many vertices. Then the generalized Turán number
$\mathrm{ex}(n, T, H)$ is the supremum in $\mathbb{N}$, with the supremum of the empty family taken
to be $0$, of the number of copies of $T$ in $G$ over all simple graphs $G$ on the vertex set
$\{0, 1, \dots, n-1\}$ that contain no copy of $H$ (a subgraph isomorphic to $H$).

Formalized by `SimpleGraph.generalizedExtremalNumber_eq_sup`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/generalized-tur-n-numbers/index.html#generalized-extremal-number-eq-sup).

## The generalized Turán number is an upper bound

Let $n$ be a natural number and let $T$ and
$H$ be simple graphs, where $T$ has finitely many vertices. If $G$ is a simple graph on the vertex
set $\{0, 1, \dots, n-1\}$ that contains no copy of $H$ (a subgraph isomorphic to $H$), then the
number of copies of $T$ in $G$ is at most the generalized Turán number $\mathrm{ex}(n, T, H)$.

Formalized by `SimpleGraph.copyCount_le_generalizedExtremalNumber`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/generalized-tur-n-numbers/index.html#copy-count-le-generalized-extremal-numbe).

## Upper bounds for the generalized Turán number

Let $n$ and $m$ be natural numbers and let
$T$ and $H$ be simple graphs, where $T$ has finitely many vertices. Then the generalized Turán
number $\mathrm{ex}(n, T, H)$ is at most $m$ if and only if every simple graph on the vertex set
$\{0, 1, \dots, n-1\}$ that contains no copy of $H$ (a subgraph isomorphic to $H$) has at most $m$
copies of $T$.

Formalized by `SimpleGraph.generalizedExtremalNumber_le_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/generalized-tur-n-numbers/index.html#generalized-extremal-number-le-iff).

## The generalized Turán number is attained

Let $n$ be a natural number and let $T$ and $H$
be simple graphs, where $T$ has finitely many vertices. If some simple graph on the vertex set
$\{0, 1, \dots, n-1\}$ contains no copy of $H$ (a subgraph isomorphic to $H$), then some such graph
$G$ has exactly $\mathrm{ex}(n, T, H)$ copies of $T$, where $\mathrm{ex}(n, T, H)$ is the
generalized Turán number.

Formalized by `SimpleGraph.exists_free_copyCount_eq_generalizedExtremalNumber`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/GeneralizedExtremal.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/generalized-tur-n-numbers/index.html#exists-free-copy-count-eq-generalized-ex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Turán numbers](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/generalized-tur-n-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/extremal-graph-theory/generalized-tur-n-numbers)
