---
declaration: section
origin: cited
lean: SimpleGraph.IsUniqueSubgraph, SimpleGraph.uniqueSubgraphCount, MathlibExt.GraphTheory.ErdosProblem426Wanted.conjecture, MathlibExt.GraphTheory.ErdosProblem426Wanted.disprovedForm, MathlibExt.GraphTheory.ErdosProblem426Wanted.conjecture_refuted
statement: formalized
---

# Unique subgraphs

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/unique-subgraphs/index.html).

## Unique subgraph

Let $G$ and $H$ be graphs on the same vertex set $V$. Then $G$ is a
unique subgraph of $H$ if exactly one subgraph of $H$ is isomorphic to $G$. Here a subgraph of
$H$ means a spanning subgraph: a graph on $V$ all of whose edges are edges of $H$ (not
necessarily induced).

Formalized by `SimpleGraph.IsUniqueSubgraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SubgraphIsomorphism.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/SubgraphIsomorphism.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/unique-subgraphs/index.html#is-unique-subgraph).

## Number of unique subgraphs

Let $H$ be a graph on a finite vertex set $V$. The number of
unique subgraphs of $H$ is the number of spanning subgraphs $G$ of $H$ (graphs on $V$ all of
whose edges are edges of $H$) that are unique subgraphs of $H$, that is, isomorphic to no other
spanning subgraph of $H$.

Equivalently, it is the number of isomorphism classes of graphs on $V$ that occur exactly once
as a spanning subgraph of $H$: sending each such $G$ to its isomorphism class is a bijection onto
these classes. In particular, isomorphic copies do not inflate the count: if two distinct
spanning subgraphs of $H$ are isomorphic, neither is a unique subgraph of $H$, so neither is
counted.

Formalized by `SimpleGraph.uniqueSubgraphCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SubgraphIsomorphism.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/SubgraphIsomorphism.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/unique-subgraphs/index.html#unique-subgraph-count).

## Many unique subgraphs (Erdős Problem 426)

For a graph $H$ on a finite vertex set, let
$u(H)$ be the number of spanning subgraphs of $H$ that are isomorphic to no other spanning
subgraph of $H$ (its unique subgraphs). The statement is that there is a real constant $c > 0$
such that for infinitely many $n$ some graph $H$ on $n$ vertices has
$u(H) \ge c \cdot 2^{\binom{n}{2}} / n!$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem426Wanted.conjecture`, a definition declared in [WantedExt/GraphTheory/ErdosProblem426Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem426Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/unique-subgraphs/index.html#conjecture).

## Negation of the Erdős Problem 426 statement

For a graph $H$ on a finite vertex set, let
$u(H)$ be the number of spanning subgraphs of $H$ that are isomorphic to no other spanning
subgraph of $H$. This is the proposition that there is no real constant $c > 0$ such that for
infinitely many $n$ some graph $H$ on $n$ vertices has $u(H) \ge c \cdot 2^{\binom{n}{2}} / n!$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem426Wanted.disprovedForm`, a definition declared in [WantedExt/GraphTheory/ErdosProblem426Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem426Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/unique-subgraphs/index.html#disproved-form).

## Erdős Problem 426 is false (Bradač–Christoph)

For a graph $H$ on a finite vertex set, let
$u(H)$ be the number of spanning subgraphs of $H$ that are isomorphic to no other spanning
subgraph of $H$ (its unique subgraphs). There is no real constant $c > 0$ such that for infinitely
many $n$ some graph $H$ on $n$ vertices has $u(H) \ge c \cdot 2^{\binom{n}{2}} / n!$.

## Sources

- Bradač and Christoph [BrCh24] (f(n) = o(2^C(n,2)/n!)), per erdosproblems.com/426, https://www.erdosproblems.com/426.

Stated but not proved: `MathlibExt.GraphTheory.ErdosProblem426Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/GraphTheory/ErdosProblem426Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem426Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/unique-subgraphs/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unique subgraphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/unique-subgraphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/extremal-graph-theory/unique-subgraphs)
