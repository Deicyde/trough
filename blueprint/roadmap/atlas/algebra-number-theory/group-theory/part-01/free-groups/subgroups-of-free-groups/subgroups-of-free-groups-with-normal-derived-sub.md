---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeGroupDerivedNormalSubgroupKourovka11Problem124Wanted.derivedNormalImpliesNormal, MathlibExt.GroupTheory.FreeGroupDerivedNormalSubgroupKourovka11Problem124Wanted.derivedNormalImpliesNormal_holds
statement: formalized
---

# Subgroups of free groups with normal derived subgroup

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/subgroups-of-free-groups-with-normal-derived-sub/index.html).

## Kourovka Problem 11.124 (free-group subgroups with normal derived subgroup)

The
statement that for every set $X$ such that the free group $F$ on $X$ is not cyclic, every subgroup
$R$ of $F$ that is not cyclic and whose derived subgroup $[R, R]$ is normal in $F$ is itself
normal in $F$.

Formalized by `MathlibExt.GroupTheory.FreeGroupDerivedNormalSubgroupKourovka11Problem124Wanted.derivedNormalImpliesNormal`, a definition declared in [WantedExt/GroupTheory/FreeGroupDerivedNormalSubgroupKourovka11Problem124Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeGroupDerivedNormalSubgroupKourovka11Problem124Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/subgroups-of-free-groups-with-normal-derived-sub/index.html#derived-normal-implies-normal).

## A non-cyclic subgroup of a free group with normal derived subgroup is normal

Let $F$ be a
free group on an arbitrary set of generators, and suppose that $F$ is not cyclic. Then every
subgroup $R$ of $F$ that is not cyclic and whose derived subgroup $[R, R]$ is normal in $F$ is
itself normal in $F$.

Resolved true: Tursunbaev proves that subgroups $H$, $K$ of a free group of arbitrary rank whose
derived subgroups $H' = [H, H]$ and $K' = [K, K]$ are equal and nontrivial coincide; for a
non-cyclic $R$ with $R' = [R, R]$ normal in $F$ and any $f \in F$, the conjugate
$R^f = f^{-1} R f$ satisfies $(R^f)' = (R')^f = R' \ne 1$, so $R^f = R$. The Kourovka Notebook
(21st issue) marks 11.124 solved, "Yes, it is true".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 11.124 (V. E. Shpilrain); resolution: A. Tursunbaev, Subgroups of free groups with the same derived subgroup, arXiv:2609.06755 (2026), main theorem (subgroups `H`, `K` of a free group of arbitrary rank with `H' = K' ≠ 1` are equal) and its corollary answering 11.124; the Kourovka Notebook (21st issue) marks 11.124 solved, https://arxiv.org/abs/2609.06755.

Stated but not proved: `MathlibExt.GroupTheory.FreeGroupDerivedNormalSubgroupKourovka11Problem124Wanted.derivedNormalImpliesNormal_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeGroupDerivedNormalSubgroupKourovka11Problem124Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeGroupDerivedNormalSubgroupKourovka11Problem124Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/subgroups-of-free-groups-with-normal-derived-sub/index.html#derived-normal-implies-normal-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgroups of free groups with normal derived subgroup](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/subgroups-of-free-groups-with-normal-derived-sub/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/subgroups-of-free-groups-with-normal-derived-sub)
