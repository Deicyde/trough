---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NilpotentSubgroupsTrivialIntersectionKourovka15Problem40Wanted.nilpotentSubgroupsTrivialConjugateIntersection, MathlibExt.GroupTheory.NilpotentSubgroupsTrivialIntersectionKourovka15Problem40Wanted.nilpotentSubgroupsTrivialConjugateIntersection_holds, MathlibExt.GroupTheory.NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.fittingSubgroup, MathlibExt.GroupTheory.NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.nilpotentThreeConjugatesInFitting, MathlibExt.GroupTheory.NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.nilpotentThreeConjugatesInFitting_holds, MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.tripleIntersections, MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.inclusionMinimalIntersectionJoin, MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.minimalOrderIntersectionJoin
statement: formalized
---

# Intersections of conjugate nilpotent subgroups

17 results, 11 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html).

## Kourovka Problem 15.40

The assertion, in the two-subgroup form of its resolution, that for
every finite non-abelian simple group $G$ and all nilpotent subgroups $A$ and $B$ of $G$ there is
$x \in G$ with $A \cap x B x^{-1} = 1$.

The case $A = B$ is the problem as posed.

Formalized by `MathlibExt.GroupTheory.NilpotentSubgroupsTrivialIntersectionKourovka15Problem40Wanted.nilpotentSubgroupsTrivialConjugateIntersection`, a definition declared in [WantedExt/GroupTheory/NilpotentSubgroupsTrivialIntersectionKourovka15Problem40Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentSubgroupsTrivialIntersectionKourovka15Problem40Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#nilpotent-subgroups-trivial-conjugate-in).

## Nilpotent subgroups of a finite simple group have conjugates meeting trivially

Let $G$ be a
finite non-abelian simple group and let $A$ and $B$ be nilpotent subgroups of $G$. Then there is
$x \in G$ with $A \cap x B x^{-1} = 1$.

Burness and Huang proved this (for alternating groups using work of Kurmazov and Zenkov); the case
$A = B$ answers Kourovka Problem 15.40 positively.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 15.40 (E. P. Vdovin); resolution: T. C. Burness and H. Y. Huang, On the intersections of nilpotent subgroups in simple groups, arXiv:2508.03479 (2025), abstract (Vdovin's conjecture and its stronger form: A ∩ B^x = 1 for nilpotent subgroups A, B of a simple group, combined with work of Kurmazov and Zenkov on alternating groups); the Kourovka Notebook (21st issue) marks 15.40 solved, https://arxiv.org/abs/2508.03479.

Stated but not proved: `MathlibExt.GroupTheory.NilpotentSubgroupsTrivialIntersectionKourovka15Problem40Wanted.nilpotentSubgroupsTrivialConjugateIntersection_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/NilpotentSubgroupsTrivialIntersectionKourovka15Problem40Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentSubgroupsTrivialIntersectionKourovka15Problem40Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#nilpotent-subgroups-trivial-conjugate-in-2).

## Fitting subgroup

The Fitting subgroup `F(G)`: the join of the nilpotent normal subgroups of `G` (for finite `G`
the largest nilpotent normal subgroup).

Formalized by `MathlibExt.GroupTheory.NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.fittingSubgroup`, a definition declared in [WantedExt/GroupTheory/NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#fitting-subgroup).

## Kourovka Problem 17.40

The assertion that for every finite group $G$ and every nilpotent
subgroup $N$ of $G$ there are $x, y \in G$ with $N \cap x N x^{-1} \cap y N y^{-1} \le F(G)$, where
$F(G)$ is the Fitting subgroup of $G$.

Formalized by `MathlibExt.GroupTheory.NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.nilpotentThreeConjugatesInFitting`, a definition declared in [WantedExt/GroupTheory/NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#nilpotent-three-conjugates-in-fitting).

## Three conjugates of a nilpotent subgroup meet inside the Fitting subgroup

For every finite
group $G$ and every nilpotent subgroup $N$ of $G$ there are $x, y \in G$ with
$N \cap x N x^{-1} \cap y N y^{-1} \le F(G)$, where $F(G)$ is the Fitting subgroup of $G$.

This answers Kourovka Problem 17.40 positively; it is due to Zenkov (2021) and uses the
classification of finite simple groups.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.40 (E. P. Vdovin); resolution: V. I. Zenkov, Siberian Math. J. 62 (2021), 621-637, Kourovka Archive, Problem 17.40 (Yes, such elements always exist, mod CFSG).

Stated but not proved: `MathlibExt.GroupTheory.NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.nilpotentThreeConjugatesInFitting_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentThreeConjugatesFittingKourovka17Problem40Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#nilpotent-three-conjugates-in-fitting-ho).

## Triple intersections with conjugates

For subgroups $A$, $B$, $C$ of a group $G$, this is
the set of all subgroups of $G$ of the form $A \cap xBx^{-1} \cap yCy^{-1}$ with $x, y \in G$,
that is, the intersections of $A$ with a conjugate of $B$ and a conjugate of $C$.

Formalized by `MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.tripleIntersections`, a definition declared in [WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#triple-intersections).

## Subgroup generated by the inclusion-minimal triple intersections

For subgroups $A$, $B$,
$C$ of a group $G$, the subgroup $\mathrm{Min}_G(A, B, C)$ is the subgroup of $G$ generated by
those intersections $A \cap xBx^{-1} \cap yCy^{-1}$ ($x, y \in G$) that are minimal by inclusion
among all such intersections, that is, that contain no other intersection of this form.

Formalized by `MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.inclusionMinimalIntersectionJoin`, a definition declared in [WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#inclusion-minimal-intersection-join).

## Subgroup generated by the triple intersections of least order

For subgroups $A$, $B$, $C$
of a group $G$, the subgroup $\min_G(A, B, C)$ is the subgroup of $G$ generated by those
intersections $A \cap xBx^{-1} \cap yCy^{-1}$ ($x, y \in G$) whose order is at most the order of
every such intersection.

Orders are taken as natural numbers, so an infinite subgroup counts as having order $0$; the
notion is intended for finite $G$.

Formalized by `MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.minimalOrderIntersectionJoin`, a definition declared in [WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#minimal-order-intersection-join).

## Minimal-order triple intersections and the Fitting subgroup (Kourovka 20.122(a), (c))

The
statement that for every finite soluble group $G$ and all nilpotent subgroups $A$, $B$, $C$ of $G$,
the subgroup $\min_G(A, B, C)$ generated by the intersections $A \cap xBx^{-1} \cap yCy^{-1}$
($x, y \in G$) of least order is contained in the Fitting subgroup $F(G)$, the join of all
nilpotent normal subgroups of $G$.

The question is due to V. I. Zenkov.

Formalized by `MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.minimalOrderIntersectionsInFitting`, a definition declared in [WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#minimal-order-intersections-in-fitting).

## Inclusion-minimal triple intersections and the Fitting subgroup (Kourovka 20.122(b), (c))

The statement that for every finite soluble group $G$ and all nilpotent subgroups $A$, $B$, $C$ of
$G$, the subgroup $\mathrm{Min}_G(A, B, C)$ generated by those intersections
$A \cap xBx^{-1} \cap yCy^{-1}$ ($x, y \in G$) that are minimal by inclusion among all such
intersections is contained in the Fitting subgroup $F(G)$, the join of all nilpotent normal
subgroups of $G$.

Formalized by `MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.inclusionMinimalIntersectionsInFitting`, a definition declared in [WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#inclusion-minimal-intersections-in-fitti).

## Minimal-order triple intersections need not lie in the Fitting subgroup

It is not true that
for every finite soluble group $G$ and all nilpotent subgroups $A$, $B$, $C$ of $G$, the subgroup
$\min_G(A, B, C)$ generated by the intersections $A \cap xBx^{-1} \cap yCy^{-1}$ ($x, y \in G$)
of least order is contained in the Fitting subgroup $F(G)$, the join of all nilpotent normal
subgroups of $G$.

Kinyon and Urban (Section 3.38) give a soluble group $G$ of order $36864$ with nilpotent subgroups
$A$ of order $16$ and $B = C$ of order $2048$ such that $\min_G(A, B, B) = A$ while $F(G)$ does not
contain $A$. Since this group is soluble, it answers part (c), and hence part (a), in the negative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.122 (V. I. Zenkov); resolution: M. Kinyon and J. Urban, Results on problems from the Kourovka Notebook, preprint, version 4, 19 September 2026, Kinyon-Urban, Section 3.38 (Problem 20.122(a)-(c)): G = E ⋊ Q soluble of order 512 · 72 = 36864, A = Z × H of order 16 and B = C the stabilizer of order 2048 are nilpotent, min_G(A, B, B) = Min_G(A, B, B) = A and F(G) = E does not contain A; the Kourovka Notebook (21st issue) marks 20.122 solved, "No, it is not always true in all three cases" (AI solution confirmed by V. I. Zenkov), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.minimalOrderIntersectionsInFitting_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#minimal-order-intersections-in-fitting-r).

## Inclusion-minimal triple intersections need not lie in the Fitting subgroup

It is not true
that for every finite soluble group $G$ and all nilpotent subgroups $A$, $B$, $C$ of $G$, the
subgroup $\mathrm{Min}_G(A, B, C)$ generated by those intersections
$A \cap xBx^{-1} \cap yCy^{-1}$ ($x, y \in G$) that are minimal by inclusion among all such
intersections is contained in the Fitting subgroup $F(G)$, the join of all nilpotent normal
subgroups of $G$.

Kinyon and Urban (Section 3.38) give a soluble group $G$ of order $36864$ with nilpotent subgroups
$A$ of order $16$ and $B = C$ of order $2048$ such that $\mathrm{Min}_G(A, B, B) = A$ while $F(G)$
does not contain $A$. Since this group is soluble, it answers part (c), and hence part (b), in the
negative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.122 (V. I. Zenkov); resolution: M. Kinyon and J. Urban, Results on problems from the Kourovka Notebook, preprint, version 4, 19 September 2026, Kinyon-Urban, Section 3.38 (Problem 20.122(a)-(c)): G = E ⋊ Q soluble of order 512 · 72 = 36864, A = Z × H of order 16 and B = C the stabilizer of order 2048 are nilpotent, min_G(A, B, B) = Min_G(A, B, B) = A and F(G) = E does not contain A; the Kourovka Notebook (21st issue) marks 20.122 solved, "No, it is not always true in all three cases" (AI solution confirmed by V. I. Zenkov), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.MinimalIntersectionsFittingKourovka20Problem122Wanted.inclusionMinimalIntersectionsInFitting_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalIntersectionsFittingKourovka20Problem122Wanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#inclusion-minimal-intersections-in-fitti-2).

## Nilpotent injector

A subgroup $H$ of a group $G$ is a nilpotent injector when, for every
subnormal subgroup $K$ of $G$, the intersection $H \cap K$ is nilpotent and is a maximal nilpotent
subgroup of $K$: every nilpotent subgroup $L$ of $G$ with $H \cap K \le L \le K$ equals
$H \cap K$.

Formalized by `MathlibExt.GroupTheory.NilpotentInjectorConjugatesKourovka19Problem37Wanted.IsNilpotentInjector`, a definition declared in [WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#is-nilpotent-injector).

## Kourovka Problem 19.37(a)

The assertion that there is a natural number $k$ such that for
every finite group $G$ and every nilpotent injector $H$ of $G$ there are elements
$g_1, \dots, g_k \in G$, not necessarily distinct, with
$g_1 H g_1^{-1} \cap \dots \cap g_k H g_k^{-1} = F(G)$, where $F(G)$ is the Fitting subgroup of
$G$.

Formalized by `MathlibExt.GroupTheory.NilpotentInjectorConjugatesKourovka19Problem37Wanted.nilpotentInjectorBoundedConjugates`, a definition declared in [WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#nilpotent-injector-bounded-conjugates).

## Kourovka Problem 19.37(b)

The assertion that for every finite group $G$ and every
nilpotent injector $H$ of $G$ there are elements $g_1, g_2, g_3 \in G$, not necessarily distinct,
with $g_1 H g_1^{-1} \cap g_2 H g_2^{-1} \cap g_3 H g_3^{-1} = F(G)$, where $F(G)$ is the Fitting
subgroup of $G$.

Formalized by `MathlibExt.GroupTheory.NilpotentInjectorConjugatesKourovka19Problem37Wanted.nilpotentInjectorThreeConjugates`, a definition declared in [WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#nilpotent-injector-three-conjugates).

## Boundedly many conjugates of a nilpotent injector meet in the Fitting subgroup

There is a
natural number $k$ such that for every finite group $G$ and every nilpotent injector $H$ of $G$
there are elements $g_1, \dots, g_k \in G$, not necessarily distinct, with
$g_1 H g_1^{-1} \cap \dots \cap g_k H g_k^{-1} = F(G)$, where $F(G)$ is the Fitting subgroup of
$G$.

Zenkov proved, using the classification of finite simple groups, that $k = 3$ works, which answers
Kourovka Problem 19.37(a) positively.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.37 (S. F. Kamornikov); resolution: V. I. Zenkov, Intersections of three nilpotent subgroups in a finite group, Siberian Math. J. 62 (2021), no. 4, 621-637, doi:10.1134/S0037446621040066, Kourovka Archive, Problem 19.37: Yes, one can choose k = 3 as such a constant, mod CFSG, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.NilpotentInjectorConjugatesKourovka19Problem37Wanted.nilpotentInjectorBoundedConjugates_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#nilpotent-injector-bounded-conjugates-ho).

## Three conjugates of a nilpotent injector meet in the Fitting subgroup

For every finite group
$G$ and every nilpotent injector $H$ of $G$ there are elements $g_1, g_2, g_3 \in G$, not
necessarily distinct, with $g_1 H g_1^{-1} \cap g_2 H g_2^{-1} \cap g_3 H g_3^{-1} = F(G)$, where
$F(G)$ is the Fitting subgroup of $G$.

This answers Kourovka Problem 19.37(b) positively; it is due to Zenkov and uses the classification
of finite simple groups, the soluble case being due to Passman and Mann.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.37 (S. F. Kamornikov); resolution: V. I. Zenkov, Intersections of three nilpotent subgroups in a finite group, Siberian Math. J. 62 (2021), no. 4, 621-637, doi:10.1134/S0037446621040066, Kourovka Archive, Problem 19.37: Yes, one can choose k = 3 as such a constant, mod CFSG, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.NilpotentInjectorConjugatesKourovka19Problem37Wanted.nilpotentInjectorThreeConjugates_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentInjectorConjugatesKourovka19Problem37Wanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html#nilpotent-injector-three-conjugates-hold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Intersections of conjugate nilpotent subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/subgroup-embedding/intersections-of-conjugate-nilpotent-subgroups)
