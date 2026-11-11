---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.HasLargeInverseClosedNormalSubsetWithSmallSquare, MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.finitelyManySimpleGroupsWithLargeNormalSubset, MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.finitelyManyPSL2WithLargeNormalSubset, MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.finitelyManySimpleGroupsWithLargeNormalSubset_refuted, MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.finitelyManyPSL2WithLargeNormalSubset_holds
statement: formalized
---

# Products of large normal subsets

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-large-normal-subsets/index.html).

## Large inverse-closed normal subsets with small square

A group $G$ has this property when it
has a subset $S$ such that $g s g^{-1} \in S$ and $s^{-1} \in S$ for all $g \in G$ and $s \in S$,
$S$ has more than $|G| / \log_2 |G|$ elements, and $S^2 = \{st : s, t \in S\}$ is not all of $G$.

The definition is intended for finite groups $G$.

Formalized by `MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.HasLargeInverseClosedNormalSubsetWithSmallSquare`, a definition declared in [WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-large-normal-subsets/index.html#has-large-inverse-closed-normal-subset-w).

## Pyber's conjecture for finite simple groups (Kourovka 20.74(a))

This proposition states
that there is a natural number $N$ such that every nonabelian finite simple group $G$ that has a
subset $S$ closed under conjugation and under inversion with $|S| > |G| / \log_2 |G|$ and
$S^2 \ne G$, where $S^2 = \{st : s, t \in S\}$, has order $|G| \le N$. Since there are only finitely
many groups of each order, this says that only finitely many such groups exist up to isomorphism.

Formalized by `MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.finitelyManySimpleGroupsWithLargeNormalSubset`, a definition declared in [WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-large-normal-subsets/index.html#finitely-many-simple-groups-with-large-n).

## Pyber's conjecture for $\mathrm{PSL}(2, p)$ (Kourovka 20.74(b))

This proposition states
that there is a natural number $N$ such that $p \le N$ for every prime $p$ for which the group
$G = \mathrm{PSL}(2, p)$, the quotient of $\mathrm{SL}(2, \mathbb{Z}/p\mathbb{Z})$ by its center,
has a subset $S$ closed under conjugation and under inversion with $|S| > |G| / \log_2 |G|$ and
$S^2 \ne G$, where $S^2 = \{st : s, t \in S\}$. In other words, only finitely many groups
$\mathrm{PSL}(2, p)$ with $p$ prime have such a subset.

Formalized by `MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.finitelyManyPSL2WithLargeNormalSubset`, a definition declared in [WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-large-normal-subsets/index.html#finitely-many-psl2-with-large-normal-sub).

## Pyber's conjecture for finite simple groups is false

There is no natural number $N$ such that
every nonabelian finite simple group $G$ that has a subset $S$ with $g s g^{-1} \in S$ and
$s^{-1} \in S$ for all $g \in G$ and $s \in S$, with $|S| > |G| / \log_2 |G|$ and with $S^2 \ne G$,
where $S^2 = \{st : s, t \in S\}$, has order $|G| \le N$.

Sheinfeld (Theorem 1.6) gives, for every odd $n \ge 5$, an inverse-closed normal subset $S$ of the
simple group $G = \mathrm{PSL}_n(5) = \mathrm{SL}_n(5)$ with $|S| \ge |G| / 960$ and $S^2 \ne G$, so
infinitely many nonabelian finite simple groups have such a subset; the paper states that this
disproves Pyber's conjecture, and the 21st issue of the Kourovka Notebook records 20.74(a) as "No,
there are infinitely many such groups".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.74 (L. Pyber); resolution: O. Sheinfeld, On Shalev's quantitative version of Thompson's conjecture, preprint, arXiv:2609.22004 (2026) (part (a)); S. V. Skresanov, Bull. London Math. Soc. 57 (2025), no. 11, 3429-3440 (part (b)), (a) Sheinfeld, Theorem 1.6: for every odd n ≥ 5 there is an inverse-closed normal subset S ⊆ SL_n(5) = PSL_n(5) with |S| ≥ |SL_n(5)|/960 and diag(1, -I_{n-1}) ∉ S², which the paper states disproves Pyber's conjecture; (b) Skresanov, Corollary 3 (arXiv:2406.12506): in a finite simple group of Lie type of bounded rank every inverse-closed normal subset A with |A| > |G|/log₂|G| has A² = G once |G| is large in terms of the rank, and part (b) for PSL(2, p) follows; Kourovka Notebook (21st issue), Problem 20.74: a) No, there are infinitely many such groups; b) The conjecture is proved for the groups PSL(2, p), https://arxiv.org/abs/2609.22004.

Stated but not proved: `MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.finitelyManySimpleGroupsWithLargeNormalSubset_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-large-normal-subsets/index.html#finitely-many-simple-groups-with-large-n-2).

## Pyber's conjecture for $\mathrm{PSL}(2, p)$ holds

There is a natural number $N$ such that for
every prime $p$ the following holds. Let $G = \mathrm{PSL}(2, p)$ be the quotient of
$\mathrm{SL}(2, \mathbb{Z}/p\mathbb{Z})$ by its center. If $G$ has a subset $S$ with
$g s g^{-1} \in S$ and $s^{-1} \in S$ for all $g \in G$ and $s \in S$, with more than
$|G| / \log_2 |G|$ elements, and with $S^2 = \{st : s, t \in S\}$ different from $G$, then
$p \le N$. In other words, only finitely many groups $\mathrm{PSL}(2, p)$ with $p$ prime have such
a subset.

Skresanov (Bull. London Math. Soc. 57 (2025), Corollary 3) proves that in a finite simple group $G$
of Lie type of bounded rank every inverse-closed normal subset $A$ with $|A| > |G| / \log_2 |G|$
satisfies $A^2 = G$ once $|G|$ is large, and notes that this settles the groups
$\mathrm{PSL}(2, p)$; the 21st issue of the Kourovka Notebook records 20.74(b) as proved for the
groups $\mathrm{PSL}(2, p)$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.74 (L. Pyber); resolution: O. Sheinfeld, On Shalev's quantitative version of Thompson's conjecture, preprint, arXiv:2609.22004 (2026) (part (a)); S. V. Skresanov, Bull. London Math. Soc. 57 (2025), no. 11, 3429-3440 (part (b)), (a) Sheinfeld, Theorem 1.6: for every odd n ≥ 5 there is an inverse-closed normal subset S ⊆ SL_n(5) = PSL_n(5) with |S| ≥ |SL_n(5)|/960 and diag(1, -I_{n-1}) ∉ S², which the paper states disproves Pyber's conjecture; (b) Skresanov, Corollary 3 (arXiv:2406.12506): in a finite simple group of Lie type of bounded rank every inverse-closed normal subset A with |A| > |G|/log₂|G| has A² = G once |G| is large in terms of the rank, and part (b) for PSL(2, p) follows; Kourovka Notebook (21st issue), Problem 20.74: a) No, there are infinitely many such groups; b) The conjecture is proved for the groups PSL(2, p), https://arxiv.org/abs/2609.22004.

Stated but not proved: `MathlibExt.GroupTheory.LargeNormalSubsetSquareKourovka20Problem74Wanted.finitelyManyPSL2WithLargeNormalSubset_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LargeNormalSubsetSquareKourovka20Problem74Wanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-large-normal-subsets/index.html#finitely-many-psl2-with-large-normal-sub-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Products of large normal subsets](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-large-normal-subsets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/combinatorics-in-groups/products-of-large-normal-subsets)
