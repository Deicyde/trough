---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.HasRankIntervalDecomposition, MathlibExt.Combinatorics.AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.acyclicLinksIntervalDecomposition, MathlibExt.Combinatorics.AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.acyclicLinksIntervalDecomposition_refuted, MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.IsCohenMacaulayOverRat, MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.IsPure, MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.IsPartitionable, MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.cohenMacaulayPartitionable, MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.cohenMacaulayPartitionable_refuted
statement: formalized
---

# Partitionable and interval-decomposable complexes

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html).

## Rank-$k$ interval decomposition with a subcomplex of bottoms

For a natural number $k$, a
finite family $K$ of finite subsets of $\mathbb{N}$ has a rank-$k$ interval decomposition with a
subcomplex of bottoms if there are a finite family $B$ of finite subsets of $\mathbb{N}$, closed
under taking subsets, and an assignment of a finite set $\mathrm{top}(F) \subseteq \mathbb{N}$ to
each finite set $F \subseteq \mathbb{N}$, such that every $F \in B$ satisfies
$F \subseteq \mathrm{top}(F)$, $|\mathrm{top}(F)| = |F| + k$ and $\mathrm{top}(F) \in K$, and every
$\sigma \in K$ lies in the interval $[F, \mathrm{top}(F)] = \{G : F \subseteq G \subseteq
\mathrm{top}(F)\}$ for exactly one $F \in B$.

Formalized by `MathlibExt.Combinatorics.AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.HasRankIntervalDecomposition`, a definition declared in [WantedExt/Combinatorics/AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html#has-rank-interval-decomposition).

## Stanley's interval-decomposition conjecture for complexes with acyclic links

The statement
that for every integer $k \ge 1$ and every finite simplicial complex $K$ on the vertex set
$\mathbb{N}$ (a finite family of finite subsets of $\mathbb{N}$ closed under taking subsets): if the
link $\mathrm{lk}_K(F) = \{G \in K : G \cap F = \emptyset,\ G \cup F \in K\}$ of every face
$F \in K$ with fewer than $k$ vertices (including $\mathrm{lk}_K(\emptyset) = K$) is acyclic over
$\mathbb{Q}$ (all of its reduced rational homology vanishes), then $K$ has a rank-$k$ interval
decomposition with a subcomplex of bottoms: there are a family $B$ of finite subsets of
$\mathbb{N}$, closed under taking subsets, and faces $\mathrm{top}(F) \in K$ for $F \in B$ with
$F \subseteq \mathrm{top}(F)$ and $|\mathrm{top}(F)| = |F| + k$, such that every face of $K$ lies
in the interval $[F, \mathrm{top}(F)]$ for exactly one $F \in B$.

This is Stanley's Problem 5 (Positivity Problems; Conjecture 2.4 of Stanley, Discrete Math. 120
(1993)) with $k = j + 2$: the faces with fewer than $k$ vertices are the faces of dimension at most
$j$, and for an interval $[F, F']$ with $F' = \mathrm{top}(F)$, the condition $|F'| = |F| + k$
means $\dim F' - \dim F = k$.

Formalized by `MathlibExt.Combinatorics.AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.acyclicLinksIntervalDecomposition`, a definition declared in [WantedExt/Combinatorics/AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html#acyclic-links-interval-decomposition).

## Stanley's interval-decomposition conjecture for complexes with acyclic links is false

It is
not true that for every integer $k \ge 1$ and every finite simplicial complex $K$ on the vertex set
$\mathbb{N}$ (a finite family of finite subsets of $\mathbb{N}$ closed under taking subsets) such
that the link $\mathrm{lk}_K(F) = \{G \in K : G \cap F = \emptyset,\ G \cup F \in K\}$ of every
face $F \in K$ with fewer than $k$ vertices is acyclic over $\mathbb{Q}$ (all of its reduced
rational homology vanishes), there are a family $B$ of finite subsets of $\mathbb{N}$, closed under
taking subsets, and faces $\mathrm{top}(F) \in K$ for $F \in B$ with $F \subseteq \mathrm{top}(F)$
and $|\mathrm{top}(F)| = |F| + k$, such that every face of $K$ lies in the interval
$[F, \mathrm{top}(F)]$ for exactly one $F \in B$.

Doolittle and Goeckner constructed a complex with $k = 2$ (a $2$-fold acyclic complex) that cannot
be partitioned into intervals $[F, F']$ with $|F'| = |F| + 2$ at all; the case $k = 1$ is
Stanley's theorem.

## Sources

- R. P. Stanley, Positivity Problems and Conjectures in Algebraic Combinatorics (1999), Problem 5 (interval decompositions of complexes with acyclic links); resolution: J. Doolittle and B. Goeckner, Resolving Stanley's conjecture on k-fold acyclic complexes, FPSAC 2019 (Sém. Lothar. Combin. 82B, Article 46), arXiv:1811.08518, §3: Theorem 3.2 (gluing N copies of Δ along Γ preserves k-fold acyclicity and non-decomposability for N > ℓ/2^k) with Theorem 3.4 (Φ = (Δ, Γ) is not rank 2 boolean decomposable); "Ω₁₇ is a counterexample to Conjecture 1.3" (Stanley's Conjecture 2.4 = Problem 5 of the 1999 list, k = 2), https://arxiv.org/abs/1811.08518.

Stated but not proved: `MathlibExt.Combinatorics.AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.acyclicLinksIntervalDecomposition_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AcyclicLinksIntervalDecompositionAMR156Problem0004Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html#acyclic-links-interval-decomposition-ref).

## Cohen–Macaulay complexes over $\mathbb{Q}$

A finite family $K$ of finite subsets of
$\mathbb{N}$ is Cohen–Macaulay over $\mathbb{Q}$ when for every member $F$ of $K$ (the empty face
included, if it belongs to $K$) the link
$L = \operatorname{lk}_K F = \{G \in K : G \cap F = \emptyset,\ G \cup F \in K\}$ satisfies
$\tilde\beta_i(L) = 0$ for every integer $i$ with $-1 \le i < \dim L$. Here $\dim L$ is one less
than the largest number of elements of a member of $L$, taken to be $-1$ when $L$ has no nonempty
member, and $\tilde\beta_i(L)$ is the number of members of $L$ with $i + 1$ elements minus the
ranks of the augmented rational simplicial boundary maps (vertices ordered as in $\mathbb{N}$) out
of and into the span of these members; when $L$ is a simplicial complex,
$\tilde\beta_i(L) = \dim \tilde H_i(L; \mathbb{Q})$.

For a simplicial complex this is Reisner's criterion.

Formalized by `MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.IsCohenMacaulayOverRat`, a definition declared in [WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html#is-cohen-macaulay-over-rat).

## Pure complexes

A finite family $K$ of finite subsets of $\mathbb{N}$ is pure when all
its facets (maximal members) have the same number of elements.

Formalized by `MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.IsPure`, a definition declared in [WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html#is-pure).

## Partitionable complexes

A finite family $K$ of finite subsets of $\mathbb{N}$ is
partitionable when there is a map $r$ assigning to each facet $F$ of $K$ a set $r(F) \subseteq F$
such that for every member $\sigma$ of $K$ there is exactly one facet $F$ of $K$ with
$r(F) \subseteq \sigma \subseteq F$.

For a simplicial complex this says that its faces are partitioned into the intervals
$[r(F), F] = \{\sigma : r(F) \subseteq \sigma \subseteq F\}$, one for each facet $F$.

Formalized by `MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.IsPartitionable`, a definition declared in [WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html#is-partitionable).

## Stanley–Garsia partitionability conjecture

Every finite simplicial complex on the vertex
set $\mathbb{N}$ that is pure and Cohen–Macaulay over $\mathbb{Q}$ is partitionable.

## Sources

- R. P. Stanley, Positivity Problems and Conjectures in Algebraic Combinatorics, Problem 6 (partitionability conjecture of Stanley and Garsia).

Formalized by `MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.cohenMacaulayPartitionable`, a definition declared in [WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html#cohen-macaulay-partitionable).

## The Stanley–Garsia partitionability conjecture is false

There is a finite simplicial complex
on the vertex set $\mathbb{N}$ that is pure and Cohen–Macaulay over $\mathbb{Q}$ but not
partitionable.

Duval, Goeckner, Klivans and Martin constructed explicit pure $3$-dimensional Cohen–Macaulay
simplicial complexes that are not partitionable.

## Sources

- R. P. Stanley, Positivity Problems and Conjectures in Algebraic Combinatorics (1999), Problem 6 (Stanley–Garsia partitionability conjecture); resolution: A. M. Duval, B. Goeckner, C. J. Klivans and J. L. Martin, A non-partitionable Cohen-Macaulay simplicial complex, Adv. Math. 299 (2016), 381-395, arXiv:1504.04279, Theorem 3.5 (arXiv numbering): the complex C₃ obtained by gluing three copies of X along A is Cohen-Macaulay and non-partitionable (Theorem 3.4: likewise C₂₅, by the gluing Theorem 3.1); abstract: "We disprove the conjecture by constructing an explicit counterexample", https://arxiv.org/abs/1504.04279.

Stated but not proved: `MathlibExt.Combinatorics.CohenMacaulayPartitionabilityAMR156Problem0005Wanted.cohenMacaulayPartitionable_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CohenMacaulayPartitionabilityAMR156Problem0005Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html#cohen-macaulay-partitionable-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partitionable and interval-decomposable complexes](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/polytopes-simplicial-complexes/partitionable-and-interval-decomposable-complexe)
