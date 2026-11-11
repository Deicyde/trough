---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.StronglyMaximalMatchingAMR29Problem0084Wanted.IsMatching, MathlibExt.Combinatorics.StronglyMaximalMatchingAMR29Problem0084Wanted.IsStronglyMaximal, MathlibExt.Combinatorics.StronglyMaximalMatchingAMR29Problem0084Wanted.boundedEdgesStronglyMaximalMatching, MathlibExt.Combinatorics.StronglyMaximalMatchingAMR29Problem0084Wanted.boundedEdgesStronglyMaximalMatching_refuted, MathlibExt.Combinatorics.StronglyMinimalCoverOpenGardenProblem690Wanted.IsVertexCover, MathlibExt.Combinatorics.StronglyMinimalCoverOpenGardenProblem690Wanted.IsStronglyMinimalCover, MathlibExt.Combinatorics.StronglyMinimalCoverOpenGardenProblem690Wanted.boundedEdgesStronglyMinimalCover, MathlibExt.Combinatorics.StronglyMinimalCoverOpenGardenProblem690Wanted.boundedEdgesStronglyMinimalCover_refuted
statement: formalized
---

# Strong matchings and covers in hypergraphs

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html).

## Matching in a hypergraph

For a hypergraph on a vertex set $V$ whose edges form a set $E$
of finite subsets of $V$, a set $M$ is a matching when $M \subseteq E$ and any two distinct
members of $M$ are disjoint.

Formalized by `MathlibExt.Combinatorics.StronglyMaximalMatchingAMR29Problem0084Wanted.IsMatching`, a definition declared in [WantedExt/Combinatorics/StronglyMaximalMatchingAMR29Problem0084Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/StronglyMaximalMatchingAMR29Problem0084Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html#is-matching).

## Strongly maximal matching

For a hypergraph with edge set $E$, a set $M$ is a strongly
maximal matching (Aharoni) when $M$ is a matching of $E$ and every matching $M'$ of $E$
satisfies $|M' \setminus M| \le |M \setminus M'|$, comparing the cardinalities as cardinal
numbers.

Formalized by `MathlibExt.Combinatorics.StronglyMaximalMatchingAMR29Problem0084Wanted.IsStronglyMaximal`, a definition declared in [WantedExt/Combinatorics/StronglyMaximalMatchingAMR29Problem0084Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/StronglyMaximalMatchingAMR29Problem0084Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html#is-strongly-maximal).

## Strongly maximal matchings in hypergraphs with bounded edges

The statement that for
every vertex set $V$ and every set $E$ of finite subsets of $V$ such that some natural number $k$
bounds the number of elements of every edge in $E$, the hypergraph with edge set $E$ has a
strongly maximal matching.

This is the claim from the EGRES list of open problems; it has since been refuted.

Formalized by `MathlibExt.Combinatorics.StronglyMaximalMatchingAMR29Problem0084Wanted.boundedEdgesStronglyMaximalMatching`, a definition declared in [WantedExt/Combinatorics/StronglyMaximalMatchingAMR29Problem0084Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/StronglyMaximalMatchingAMR29Problem0084Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html#bounded-edges-strongly-maximal-matching).

## Bounded edge size does not guarantee a strongly maximal matching

There are a vertex set
$V$, a set $E$ of finite subsets of $V$ and a natural number $k$ such that every edge in $E$ has
at most $k$ elements, but the hypergraph with edge set $E$ has no strongly maximal matching.

Hollom and Randall Shaw (Theorem 1.2) construct a $3$-uniform (infinite) hypergraph with no
strongly maximal matching, so bounded edge size does not suffice.

## Sources

- EGRES Open (Egerváry Research Group), list of open problems, Strongly maximal matchings, https://oldlemon.cs.elte.hu/egres/open/Strongly_maximal_matchings; resolution: L. Hollom and B. Randall Shaw, Counterexamples to conjectures on strong maximality and minimality, Electron. J. Combin. 33(2) (2026), P2.11; arXiv:2511.13709, Theorem 1.2: there is a 3-uniform hypergraph H₁ with no strongly maximal matching (refuting Conjecture 1.1 for matchings and Aharoni's question), https://doi.org/10.37236/14948.

Stated but not proved: `MathlibExt.Combinatorics.StronglyMaximalMatchingAMR29Problem0084Wanted.boundedEdgesStronglyMaximalMatching_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/StronglyMaximalMatchingAMR29Problem0084Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/StronglyMaximalMatchingAMR29Problem0084Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html#bounded-edges-strongly-maximal-matching-2).

## Vertex cover of a hypergraph

Let $E$ be a set of finite subsets of a type $V$, the edges
of a hypergraph. A set $X \subseteq V$ is a (vertex) cover of $E$ if it meets every edge: every
$e \in E$ contains some $v \in X$.

Formalized by `MathlibExt.Combinatorics.StronglyMinimalCoverOpenGardenProblem690Wanted.IsVertexCover`, a definition declared in [WantedExt/Combinatorics/StronglyMinimalCoverOpenGardenProblem690Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/StronglyMinimalCoverOpenGardenProblem690Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html#is-vertex-cover).

## Strongly minimal cover

Let $E$ be a set of finite subsets of a type $V$, the edges of a
hypergraph. A set $X \subseteq V$ is a strongly minimal cover of $E$ (Aharoni) if $X$ is a cover of
$E$, that is, it meets every edge in $E$, and $|X \setminus X'| \le |X' \setminus X|$, as cardinals,
for every cover $X'$ of $E$.

Formalized by `MathlibExt.Combinatorics.StronglyMinimalCoverOpenGardenProblem690Wanted.IsStronglyMinimalCover`, a definition declared in [WantedExt/Combinatorics/StronglyMinimalCoverOpenGardenProblem690Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/StronglyMinimalCoverOpenGardenProblem690Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html#is-strongly-minimal-cover).

## Aharoni's strongly minimal cover conjecture

The statement that for every type $V$, every
set $E$ of finite subsets of $V$ (the edges of a hypergraph, possibly infinitely many) and every
natural number $k$ such that each edge in $E$ is nonempty and has at most $k$ elements, the
hypergraph with edge set $E$ has a strongly minimal cover.

Formalized by `MathlibExt.Combinatorics.StronglyMinimalCoverOpenGardenProblem690Wanted.boundedEdgesStronglyMinimalCover`, a definition declared in [WantedExt/Combinatorics/StronglyMinimalCoverOpenGardenProblem690Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/StronglyMinimalCoverOpenGardenProblem690Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html#bounded-edges-strongly-minimal-cover).

## Aharoni's strongly minimal cover conjecture is false

There are a type $V$, a set $E$ of
finite subsets of $V$ (the edges of a hypergraph) and a natural number $k$ such that every edge in
$E$ is nonempty and has at most $k$ elements, but no strongly minimal cover of $E$ exists. Here a
cover of $E$ is a set $X \subseteq V$ that meets every edge in $E$, and a cover $X$ is strongly
minimal if $|X \setminus X'| \le |X' \setminus X|$, as cardinals, for every cover $X'$ of $E$.

Hollom and Randall Shaw (Section 3.4) show that the graph on $\mathbb{N}$ whose edges are the
pairs $\{u, v\}$ with $2u \le v$ has no strongly minimal vertex cover, so already hypergraphs with
all edges of size $2$ need not have a strongly minimal cover.

## Sources

- Open Problem Garden, Strong matchings and covers (node 690; R. Aharoni), http://www.openproblemgarden.org/op/strong_matchings_and_covers; resolution: L. Hollom and B. Randall Shaw, Counterexamples to conjectures on strong maximality and minimality, Electron. J. Combin. 33(2) (2026), #P2.11, doi:10.37236/14948; arXiv:2511.13709, Section 3.4 (Strongly minimal vertex-covers): the graph G on N with edges {u, v} such that 2u ≤ v has no strongly minimal vertex-cover; the introduction defines strongly minimal vertex-covers by |C \ C'| ≤ |C' \ C| for every vertex-cover C', https://doi.org/10.37236/14948.

Stated but not proved: `MathlibExt.Combinatorics.StronglyMinimalCoverOpenGardenProblem690Wanted.boundedEdgesStronglyMinimalCover_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/StronglyMinimalCoverOpenGardenProblem690Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/StronglyMinimalCoverOpenGardenProblem690Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html#bounded-edges-strongly-minimal-cover-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strong matchings and covers in hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/strong-matchings-and-covers-in-hypergraphs)
