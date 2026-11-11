---
declaration: section
origin: cited
lean: SimpleGraph.IsDegenerateOn, SimpleGraph.IsDegenerate, SimpleGraph.IsDegenerateOn.mono, SimpleGraph.IsDegenerateOn.of_subset, SimpleGraph.IsDegenerate.isDegenerateOn, SimpleGraph.IsDegenerateOn.exists_small_vertex, SimpleGraph.isDegenerate_bot, SimpleGraph.IsDegenerate.mono
statement: formalized
proof: formalized
---

# Degeneracy and greedy coloring

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html).

## Degeneracy on a vertex set

Let $G$ be a simple graph on a finite vertex type $V$, let
$U \subseteq V$ and let $k$ be a natural number. Then $G$ is $k$-degenerate on $U$ if every
nonempty subset $W \subseteq U$ contains a vertex $v$ with at most $k$ neighbors in $W$.

Formalized by `SimpleGraph.IsDegenerateOn`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#is-degenerate-on).

## Degenerate graph

A simple graph $G$ on a finite vertex type $V$ is $k$-degenerate, for a
natural number $k$, if it is $k$-degenerate on the full vertex set $V$: every nonempty set $W$ of
vertices contains a vertex with at most $k$ neighbors in $W$.

Formalized by `SimpleGraph.IsDegenerate`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#is-degenerate).

## Degeneracy on a vertex set is monotone in the degree bound

Let $G$ be a simple graph on
a finite vertex type $V$, let $U \subseteq V$, and let $k \le l$ be natural numbers. If $G$ is
$k$-degenerate on $U$, then $G$ is $l$-degenerate on $U$.

Formalized by `SimpleGraph.IsDegenerateOn.mono`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#mono).

## Degeneracy on a vertex set passes to subsets

Let $G$ be a simple graph on a finite
vertex type $V$, let $T \subseteq U \subseteq V$ and let $k$ be a natural number. If $G$ is
$k$-degenerate on $U$, then $G$ is $k$-degenerate on $T$.

Formalized by `SimpleGraph.IsDegenerateOn.of_subset`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#of-subset).

## A degenerate graph is degenerate on every vertex set

Let $G$ be a simple graph on a
finite vertex type $V$ and let $k$ be a natural number. If $G$ is $k$-degenerate, then $G$ is
$k$-degenerate on every subset $U \subseteq V$.

Formalized by `SimpleGraph.IsDegenerate.isDegenerateOn`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Degeneracy.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#is-degenerate-on-2).

## A degenerate vertex set has a vertex of small degree

Let $G$ be a simple graph
on a finite vertex set $V$ and let $s \subseteq V$ be nonempty. If $G$ is
$k$-degenerate on $s$, then some vertex $v \in s$ has at most $k$ neighbors in $s$.

Formalized by `SimpleGraph.IsDegenerateOn.exists_small_vertex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#exists-small-vertex).

## The edgeless graph is degenerate

For every natural number $k$, the edgeless
graph on a finite vertex set is $k$-degenerate.

Formalized by `SimpleGraph.isDegenerate_bot`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#is-degenerate-bot).

## Degeneracy is monotone in the bound

Let $G$ be a simple graph on a finite
vertex set. If $G$ is $k$-degenerate and $k \le l$, then $G$ is $l$-degenerate.

Formalized by `SimpleGraph.IsDegenerate.mono`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#mono-2).

## Bounded maximum degree implies degeneracy

Let $G$ be a simple graph on a
finite vertex set. If every vertex of $G$ has degree at most $k$, then $G$ is
$k$-degenerate.

Formalized by `SimpleGraph.IsDegenerate.of_forall_degree_le`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#of-forall-degree-le).

## Degeneracy ordering

Let $G$ be a simple graph on a finite vertex set $V$ and
let $k$ be a natural number. A map $e : V \to \mathbb{N}$ is a degeneracy ordering of
$G$ with bound $k$ if $e$ is injective and every vertex $v$ has at most $k$ neighbors
$w$ with $e(v) < e(w)$.

Formalized by `SimpleGraph.IsDegeneracyOrdering`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#is-degeneracy-ordering).

## Degeneracy orderings of a vertex set

Let $G$ be a simple graph on a finite
vertex set $V$ and let $s \subseteq V$. If $G$ is $k$-degenerate on $s$, then there is
a map $e : V \to \mathbb{N}$, injective on $s$, such that every $v \in s$ has at most
$k$ neighbors $w \in s$ with $e(v) < e(w)$.

The proof removes a vertex of small degree in $s$ and labels it $0$.

Formalized by `SimpleGraph.IsDegenerateOn.exists_injOn_ordering`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#exists-inj-on-ordering).

## Degenerate graphs have degeneracy orderings

If $G$ is a $k$-degenerate simple
graph on a finite vertex set $V$, then $G$ has a degeneracy ordering with bound $k$:
an injective map $e : V \to \mathbb{N}$ such that every vertex $v$ has at most $k$
neighbors $w$ with $e(v) < e(w)$.

Formalized by `SimpleGraph.IsDegenerate.exists_degeneracyOrdering`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#exists-degeneracy-ordering).

## Coloring a $k$-degenerate vertex set with $k + 1$ colors

Let $G$ be a simple graph
on a finite vertex set $V$, let $s \subseteq V$ and let $k$ be a natural number. If $G$ is
$k$-degenerate on $s$, then there is a map $f : V \to \{0, 1, \dots, k\}$ such that
$f(a) \ne f(b)$ for all adjacent vertices $a, b \in s$.

The proof removes a vertex of small degree and gives it a color absent from its
neighborhood.

Formalized by `SimpleGraph.IsDegenerateOn.exists_coloringFun`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#exists-coloring-fun).

## $k$-degenerate graphs are $(k + 1)$-colorable

Let $k$ be a natural number. Every
$k$-degenerate simple graph on a finite vertex set is $(k + 1)$-colorable.

## Sources

- Diestel, §5.1–5.2.

Formalized by `SimpleGraph.IsDegenerate.colorable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#colorable).

## Chromatic number of a degenerate graph

Let $k$ be a natural number. If $G$ is a
$k$-degenerate simple graph on a finite vertex set, then the chromatic number of $G$ is at
most $k + 1$.

Formalized by `SimpleGraph.IsDegenerate.chromaticNumber_le`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/DegeneracyColoring.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html#chromatic-number-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Degeneracy and greedy coloring](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-coloring/part-01/degeneracy-and-greedy-coloring)
