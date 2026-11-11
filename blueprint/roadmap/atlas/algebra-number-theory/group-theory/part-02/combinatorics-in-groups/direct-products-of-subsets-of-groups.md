---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DirectProductFactorCardinalityKourovka21Problem58Wanted.IsDirectProduct, MathlibExt.GroupTheory.DirectProductFactorCardinalityKourovka21Problem58Wanted.existsInfiniteGroupStableFactors, MathlibExt.GroupTheory.DirectProductFactorCardinalityKourovka21Problem58Wanted.existsInfiniteGroupStableFactors_refuted
statement: formalized
---

# Direct products of subsets of groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/direct-products-of-subsets-of-groups/index.html).

## Direct product of subsets

For subsets $A$ and $B$ of a group $G$, the product
$AB = \{ab \mid a \in A,\ b \in B\}$ is direct when each element of $AB$ is $ab$ for unique
$a \in A$ and $b \in B$: whenever $a_1 b_1 = a_2 b_2$ with $a_1, a_2 \in A$ and $b_1, b_2 \in B$,
we have $a_1 = a_2$ and $b_1 = b_2$.

Formalized by `MathlibExt.GroupTheory.DirectProductFactorCardinalityKourovka21Problem58Wanted.IsDirectProduct`, a definition declared in [WantedExt/GroupTheory/DirectProductFactorCardinalityKourovka21Problem58Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DirectProductFactorCardinalityKourovka21Problem58Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/direct-products-of-subsets-of-groups/index.html#is-direct-product).

## Infinite groups with equicardinal maximal direct factors (Kourovka 21.58)

The statement
that there is an infinite group $G$ such that for every subset $A \subseteq G$, any two subsets
$B_1, B_2 \subseteq G$ that are maximal under inclusion among the subsets $B$ for which the
product $AB$ is direct have the same cardinality.

Formalized by `MathlibExt.GroupTheory.DirectProductFactorCardinalityKourovka21Problem58Wanted.existsInfiniteGroupStableFactors`, a definition declared in [WantedExt/GroupTheory/DirectProductFactorCardinalityKourovka21Problem58Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DirectProductFactorCardinalityKourovka21Problem58Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/direct-products-of-subsets-of-groups/index.html#exists-infinite-group-stable-factors).

## No infinite group has equicardinal maximal direct factors

For every infinite group $G$ there
are subsets $A, B_1, B_2 \subseteq G$ such that $B_1$ and $B_2$ are both maximal under inclusion
among the subsets $B$ for which the product $AB$ is direct, but $B_1$ and $B_2$ have different
cardinalities. That is, the answer to Kourovka Problem 21.58 is negative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 21.58 (M. H. Hooshmand); resolution: M. I. Kabenyuk, Factors in infinite groups, preprint, arXiv:2602.22876 (2026); M. H. Hooshmand, preprint, arXiv:2604.08724 (2026), Remark 1.16, Kabenyuk, Section 6, Theorem: every infinite group is unstable, i.e. has a subset A whose maximal subsets U with AU direct do not all have the same cardinality; Kourovka Notebook (21st issue), Problem 21.58: No, there are no such groups, https://arxiv.org/abs/2602.22876.

Stated but not proved: `MathlibExt.GroupTheory.DirectProductFactorCardinalityKourovka21Problem58Wanted.existsInfiniteGroupStableFactors_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DirectProductFactorCardinalityKourovka21Problem58Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DirectProductFactorCardinalityKourovka21Problem58Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/direct-products-of-subsets-of-groups/index.html#exists-infinite-group-stable-factors-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Direct products of subsets of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/direct-products-of-subsets-of-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/combinatorics-in-groups/direct-products-of-subsets-of-groups)
