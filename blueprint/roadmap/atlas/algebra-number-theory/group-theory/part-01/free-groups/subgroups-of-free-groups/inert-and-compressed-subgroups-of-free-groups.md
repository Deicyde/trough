---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.subgroupRank, MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.IsInert, MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.IsCompressed, MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.compressedSubgroupsInert, MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.compressedSubgroupsInert_holds, MathlibExt.GroupTheory.CompressedSubgroupIntersectionKourovka19Problem103Wanted.subgroupRank, MathlibExt.GroupTheory.CompressedSubgroupIntersectionKourovka19Problem103Wanted.IsCompressed, MathlibExt.GroupTheory.CompressedSubgroupIntersectionKourovka19Problem103Wanted.intersectionOfCompressedCompressed
statement: formalized
---

# Inert and compressed subgroups of free groups

18 results, 14 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html).

## Rank of a subgroup

For a subgroup $H$ of a group $G$, the rank
$r(H) \in \mathbb{N} \cup \{\infty\}$ is the least size of a finite subset of $G$ that generates
$H$, with $r(H) = \infty$ when $H$ is not finitely generated.

Formalized by `MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.subgroupRank`, a definition declared in [WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#subgroup-rank).

## Inert subgroup of a free group of finite rank

Let $F_n$ be the free group on $n$
generators and $r(K) \in \mathbb{N} \cup \{\infty\}$ the rank of a subgroup $K$. A subgroup $H$ of
$F_n$ is inert when $r(H \cap K) \le r(K)$ for every subgroup $K$ of $F_n$.

Formalized by `MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.IsInert`, a definition declared in [WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#is-inert).

## Compressed subgroup of a free group of finite rank

Let $F_n$ be the free group on $n$
generators and $r(K) \in \mathbb{N} \cup \{\infty\}$ the rank of a subgroup $K$. A subgroup $H$ of
$F_n$ is compressed when $r(H) \le r(K)$ for every subgroup $K$ of $F_n$ containing $H$.

Formalized by `MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.IsCompressed`, a definition declared in [WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#is-compressed).

## Ventura's compressed-implies-inert problem in finite rank (Kourovka 19.102)

The
proposition that for every $n \in \mathbb{N}$, every compressed subgroup of the free group $F_n$ on
$n$ generators is inert.

Formalized by `MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.compressedSubgroupsInert`, a definition declared in [WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#compressed-subgroups-inert).

## Compressed subgroups of free groups of finite rank are inert (Kourovka 19.102)

For every
$n \in \mathbb{N}$, every compressed subgroup $H$ of the free group $F_n$ on $n$ generators is
inert.

The Kourovka Notebook (21st issue) answers 19.102 "Yes, it is true" (A. Jaikin-Zapirain, 2024),
whose Corollary 1.2 proves that compressed and inert are equivalent for finitely generated
subgroups of a free group.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.102 (E. Ventura); resolution: A. Jaikin-Zapirain, Free groups are L^2-subgroup rigid, preprint, arXiv:2403.09515 (2024), abstract and Corollary 1.2: for a finitely generated subgroup H of a free group F, H is compressed iff H is inert iff H is L²-independent, answering the question of Dicks and Ventura (Kourovka 19.102); the Kourovka Notebook (21st issue) marks 19.102 solved, https://arxiv.org/abs/2403.09515.

Stated but not proved: `MathlibExt.GroupTheory.CompressedSubgroupInertKourovka19Problem102Wanted.compressedSubgroupsInert_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupInertKourovka19Problem102Wanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#compressed-subgroups-inert-holds).

## Rank of a subgroup (Kourovka 19.103)

For a subgroup $H$ of a group $G$, the rank
$r(H) \in \mathbb{N} \cup \{\infty\}$ is the least number of elements of a finite subset of $G$ that
generates $H$, with $r(H) = \infty$ when $H$ is not finitely generated.

Formalized by `MathlibExt.GroupTheory.CompressedSubgroupIntersectionKourovka19Problem103Wanted.subgroupRank`, a definition declared in [WantedExt/GroupTheory/CompressedSubgroupIntersectionKourovka19Problem103Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupIntersectionKourovka19Problem103Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#subgroup-rank-2).

## Compressed subgroup of a free group (Kourovka 19.103)

A subgroup $H$ of the free group
$F_n$ on $n$ generators is compressed when $r(H) \le r(K)$ for every subgroup $K$ of $F_n$ that
contains $H$, where $r$ denotes the rank of a subgroup.

Formalized by `MathlibExt.GroupTheory.CompressedSubgroupIntersectionKourovka19Problem103Wanted.IsCompressed`, a definition declared in [WantedExt/GroupTheory/CompressedSubgroupIntersectionKourovka19Problem103Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupIntersectionKourovka19Problem103Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#is-compressed-2).

## Kourovka Problem 19.103 for two compressed subgroups

The statement that for every
natural number $n$ and all subgroups $H$ and $K$ of the free group $F_n$ on $n$ generators, if $H$
and $K$ are compressed, then $H \cap K$ is compressed.

Formalized by `MathlibExt.GroupTheory.CompressedSubgroupIntersectionKourovka19Problem103Wanted.intersectionOfCompressedCompressed`, a definition declared in [WantedExt/GroupTheory/CompressedSubgroupIntersectionKourovka19Problem103Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupIntersectionKourovka19Problem103Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#intersection-of-compressed-compressed).

## The intersection of two compressed subgroups of a finite-rank free group is compressed

For
every natural number $n$ and all subgroups $H$ and $K$ of the free group $F_n$ on $n$
generators, if $H$ and $K$ are compressed, then $H \cap K$ is compressed. That is, Kourovka
Problem 19.103 has a positive answer for the intersection of two subgroups of a free group of
finite rank.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.103 (E. Ventura); resolution: A. Jaikin-Zapirain, Free groups are L^2-subgroup rigid, preprint, arXiv:2403.09515 (2024), Corollary 1.3(1) (citing Kourovka 19.103): the intersection of two compressed subgroups of a free group is again compressed, from Corollary 1.2 (compressed iff inert for finitely generated subgroups); the Kourovka Notebook (21st issue) marks 19.103 solved, https://arxiv.org/abs/2403.09515.

Stated but not proved: `MathlibExt.GroupTheory.CompressedSubgroupIntersectionKourovka19Problem103Wanted.intersectionOfCompressedCompressed_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/CompressedSubgroupIntersectionKourovka19Problem103Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompressedSubgroupIntersectionKourovka19Problem103Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#intersection-of-compressed-compressed-ho).

## Rank of a subgroup

For a subgroup $H$ of a group $G$, the rank $r(H)$ is the least size of
a finite subset of $G$ that generates $H$, or $\infty$ if $H$ is not finitely generated.

Formalized by `MathlibExt.GroupTheory.EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.subgroupRank`, a definition declared in [WantedExt/GroupTheory/EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#subgroup-rank-3).

## Inert subgroups of a free group

Let $F_n$ be the free group on $n$ generators and let
$r(K)$ denote the rank of a subgroup $K$. A subgroup $H \le F_n$ is inert if
$r(H \cap K) \le r(K)$ for every subgroup $K \le F_n$.

Formalized by `MathlibExt.GroupTheory.EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.IsInert`, a definition declared in [WantedExt/GroupTheory/EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#is-inert-2).

## Kourovka Problem 19.105 (Ventura) for free groups of finite rank

The statement that for
every $n \in \mathbb{N}$ and every endomorphism $\varphi$ of the free group $F_n$ on $n$ generators,
the fixed subgroup $\{x \in F_n \mid \varphi(x) = x\}$ of $\varphi$ is inert in $F_n$.

Formalized by `MathlibExt.GroupTheory.EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.endomorphismFixedSubgroupInert`, a definition declared in [WantedExt/GroupTheory/EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#endomorphism-fixed-subgroup-inert).

## Fixed subgroups of endomorphisms of free groups are inert

Let $n \in \mathbb{N}$, let $F_n$ be
the free group on $n$ generators, and for a subgroup $H \le F_n$ let $r(H)$ be its rank, the least
size of a finite generating set of $H$, or $\infty$ if $H$ is not finitely generated. For every
endomorphism $\varphi$ of $F_n$, the fixed subgroup $\{x \in F_n \mid \varphi(x) = x\}$ of
$\varphi$ is inert in $F_n$: its intersection with every subgroup $K \le F_n$ has rank at most
$r(K)$. This answers Kourovka Problem 19.105 (E. Ventura) in the affirmative.

The Kourovka Notebook (21st issue) answers 19.105 "Yes, it is true", citing A. Jaikin-Zapirain
(2024), whose Corollary 1.2 proves that compressed and inert are equivalent for finitely generated
subgroups of a free group.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.105 (E. Ventura); resolution: A. Jaikin-Zapirain, Free groups are L^2-subgroup rigid, preprint, arXiv:2403.09515 (2024), Corollary 1.2: for a finitely generated subgroup of a free group, compressed iff inert; the Kourovka Notebook (21st issue) answers 19.105 "Yes, it is true" citing this preprint, https://arxiv.org/abs/2403.09515.

Stated but not proved: `MathlibExt.GroupTheory.EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.endomorphismFixedSubgroupInert_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismFixedSubgroupInertKourovka19Problem105Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#endomorphism-fixed-subgroup-inert-holds).

## Rank of a subgroup, possibly infinite

For a subgroup $H$ of a group $G$, the rank
$r(H) \in \mathbb{N} \cup \{\infty\}$ is the least size of a finite subset of $G$ that generates
$H$, and $r(H) = \infty$ if $H$ is not finitely generated.

Formalized by `MathlibExt.GroupTheory.InertSubgroupDecidableKourovka19Problem104Wanted.subgroupRank`, a definition declared in [WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#subgroup-rank-4).

## Inert subgroup of a free group of finite rank

A subgroup $H$ of the free group $F_n$ on
$n$ generators is inert if $r(H \cap K) \le r(K)$ for every subgroup $K$ of $F_n$, where the rank
$r(L)$ of a subgroup $L$ is the least size of a finite generating set of $L$, and $\infty$ when $L$
is not finitely generated.

Formalized by `MathlibExt.GroupTheory.InertSubgroupDecidableKourovka19Problem104Wanted.IsInert`, a definition declared in [WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#is-inert-3).

## Subgroup of a free group generated by a list of words

Let $F_n$ be the free group on
generators $x_0, \dots, x_{n-1}$. A word is a finite list of letters $(i, b)$ with $i < n$ and $b$
a boolean, where $(i, \mathrm{true})$ stands for $x_i$ and $(i, \mathrm{false})$ for $x_i^{-1}$.
Given a finite list of words, this is the subgroup of $F_n$ generated by the elements of $F_n$
that the words represent, each word representing the product of its letters.

Formalized by `MathlibExt.GroupTheory.InertSubgroupDecidableKourovka19Problem104Wanted.generatedBy`, a definition declared in [WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#generated-by).

## Kourovka Problem 19.104 (statement): deciding inertness

The statement that for every
natural number $n$ there is an algorithm deciding, for a finite list of words in the generators
$x_0, \dots, x_{n-1}$ of the free group $F_n$ and their inverses, whether the subgroup of $F_n$
they generate is inert; that is, the predicate on lists of words is computable.

Formalized by `MathlibExt.GroupTheory.InertSubgroupDecidableKourovka19Problem104Wanted.inertSubgroupDecidable`, a definition declared in [WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#inert-subgroup-decidable).

## Inertness is decidable in free groups of finite rank (Kourovka Problem 19.104)

For every
natural number $n$, let $F_n$ be the free group on generators $x_0, \dots, x_{n-1}$, and give a
finitely generated subgroup of $F_n$ by a finite list of generating words in the letters
$x_i^{\pm 1}$. Then there is an algorithm deciding, for such a list, whether the subgroup $H$ it
generates is inert, that is, whether $r(H \cap K) \le r(K)$ for every subgroup $K$ of $F_n$. Here
the rank $r(L)$ of a subgroup $L$ is the least size of a finite generating set of $L$, and
$r(L) = \infty$ when $L$ is not finitely generated; "an algorithm" means that the predicate on
lists of words is computable.

Jaikin-Zapirain proved that a finitely generated subgroup of a free group is inert if and only if
it is compressed, and compressedness is known to be decidable.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.104 (E. Ventura); resolution: A. Jaikin-Zapirain, Free groups are L^2-subgroup rigid, preprint, arXiv:2403.09515 (2024), Corollary 1.3(2) (citing Kourovka 19.104): it is algorithmically decidable, for a finitely generated subgroup of a free group, whether it is inert (compressedness is decidable and equivalent to inertness by Corollary 1.2); the Kourovka Notebook (21st issue) marks 19.104 solved, https://arxiv.org/abs/2403.09515.

Stated but not proved: `MathlibExt.GroupTheory.InertSubgroupDecidableKourovka19Problem104Wanted.inertSubgroupDecidable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/InertSubgroupDecidableKourovka19Problem104Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html#inert-subgroup-decidable-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inert and compressed subgroups of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/inert-and-compressed-subgroups-of-free-groups)
