---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NoProperPronormalSubgroupsKourovka19Problem74Wanted.existsInfiniteGroupWithoutProperPronormal, MathlibExt.GroupTheory.NoProperPronormalSubgroupsKourovka19Problem74Wanted.existsInfiniteGroupWithoutProperPronormal_holds
statement: formalized
---

# Pronormal subgroups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/pronormal-subgroups/index.html).

## Infinite groups without nontrivial proper pronormal subgroups (Kourovka 19.74, Revin)

The statement that there is an infinite group $G$ in which every pronormal subgroup is trivial or
equal to $G$. Here a subgroup $H$ of $G$ is pronormal when, for every $g \in G$, the subgroups $H$
and $H^g = gHg^{-1}$ are conjugate by an element of $\langle H, H^g \rangle$.

Formalized by `MathlibExt.GroupTheory.NoProperPronormalSubgroupsKourovka19Problem74Wanted.existsInfiniteGroupWithoutProperPronormal`, a definition declared in [WantedExt/GroupTheory/NoProperPronormalSubgroupsKourovka19Problem74Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NoProperPronormalSubgroupsKourovka19Problem74Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/pronormal-subgroups/index.html#exists-infinite-group-without-proper-pro).

## An infinite group without nontrivial proper pronormal subgroups exists

There is an infinite
group $G$ in which every pronormal subgroup is trivial or equal to $G$. Here a subgroup $H$ of $G$
is pronormal when, for every $g \in G$, the subgroups $H$ and $H^g = gHg^{-1}$ are conjugate by an
element of $\langle H, H^g \rangle$. This answers Kourovka Problem 19.74 in the affirmative.

Corson constructs an infinite simple group with no proper abnormal subgroup, which the problem
states is equivalent (the normalizer of a pronormal subgroup is abnormal); the 21st issue of the
Kourovka Notebook marks 19.74 solved ("Yes, it does").

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.74 (D. O. Revin); resolution: S. M. Corson, Infinite simple groups with no proper abnormal subgroups, Monatsh. Math. (2025), doi:10.1007/s00605-025-02116-8 (arXiv:2505.07330), Theorem 1: there is an infinite group that is simple, torsion-free, has no maximal subgroup and has no proper abnormal subgroup, answering Revin's problem; the Kourovka Notebook (21st issue) marks 19.74 solved: Yes, it does (the problem states the equivalent form: an infinite simple group without proper abnormal subgroups), https://arxiv.org/abs/2505.07330.

Stated but not proved: `MathlibExt.GroupTheory.NoProperPronormalSubgroupsKourovka19Problem74Wanted.existsInfiniteGroupWithoutProperPronormal_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/NoProperPronormalSubgroupsKourovka19Problem74Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NoProperPronormalSubgroupsKourovka19Problem74Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/pronormal-subgroups/index.html#exists-infinite-group-without-proper-pro-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pronormal subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/pronormal-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/subgroup-embedding/pronormal-subgroups)
