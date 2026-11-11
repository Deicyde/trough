---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.IsGPermutable, MathlibExt.GroupTheory.AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.alternatingGroupNoProperPermutableSubgroups, MathlibExt.GroupTheory.AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.alternatingGroupNoProperPermutableSubgroups_holds
statement: formalized
---

# Permutable subgroups of alternating groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/permutable-subgroups-of-alternating-groups/index.html).

## $G$-permutable subgroups

A subgroup $A$ of a group $G$ is $G$-permutable when for every
subgroup $B$ of $G$ there is $x \in G$ such that $A B^x = B^x A$, where $B^x = x B x^{-1}$ is the
conjugate of $B$ by $x$ and the products are products of subsets of $G$.

Formalized by `MathlibExt.GroupTheory.AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.IsGPermutable`, a definition declared in [WantedExt/GroupTheory/AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/permutable-subgroups-of-alternating-groups/index.html#is-gpermutable).

## Kourovka Problem 17.37 on permutable subgroups of alternating groups

This proposition
asserts that there is a natural number $n$ such that for every $m > n$, every $A_m$-permutable
subgroup of the alternating group $A_m$ is either the trivial subgroup or $A_m$ itself. Here a
subgroup $A$ of a group $G$ is $G$-permutable when for every subgroup $B$ of $G$ there is $x \in G$
with $A B^x = B^x A$, where $B^x = x B x^{-1}$ is the conjugate of $B$ by $x$ and products of
subgroups are products of subsets of $G$.

The trivial subgroup and $A_m$ itself are always $A_m$-permutable.

Formalized by `MathlibExt.GroupTheory.AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.alternatingGroupNoProperPermutableSubgroups`, a definition declared in [WantedExt/GroupTheory/AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/permutable-subgroups-of-alternating-groups/index.html#alternating-group-no-proper-permutable-s).

## Permutable subgroups of large alternating groups are trivial or the whole group

There is a
natural number $n$ such that for every $m > n$, every $A_m$-permutable subgroup of the alternating
group $A_m$ is either the trivial subgroup or $A_m$ itself. Here a subgroup $A$ of a group $G$ is
$G$-permutable when for every subgroup $B$ of $G$ there is $x \in G$ with $A B^x = B^x A$, where
$B^x = x B x^{-1}$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 17.37 (A. F. Vasil'ev, A. N. Skiba); resolution: N. Yang and A. Galt, Bull. Malays. Math. Sci. Soc. (2) 46 (2023), no. 5, Paper no. 177, as stated in S. Zhang, Ordinary G-permutable subgroups of finite simple groups, preprint, arXiv:2610.12329 (2026), Zhang, Introduction (Yang and Galt proved that there is N ≥ 7 such that no A_n with n ≥ N has a proper nontrivial A_n-permutable subgroup, with A_n-permutable as in Problem 17.112); the Kourovka Notebook (21st issue) marks 17.37 solved (Yes, there is), https://arxiv.org/abs/2610.12329.

Stated but not proved: `MathlibExt.GroupTheory.AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.alternatingGroupNoProperPermutableSubgroups_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AlternatingGroupPermutableSubgroupsKourovka17Problem37Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/permutable-subgroups-of-alternating-groups/index.html#alternating-group-no-proper-permutable-s-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutable subgroups of alternating groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/permutable-subgroups-of-alternating-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/subgroup-embedding/permutable-subgroups-of-alternating-groups)
