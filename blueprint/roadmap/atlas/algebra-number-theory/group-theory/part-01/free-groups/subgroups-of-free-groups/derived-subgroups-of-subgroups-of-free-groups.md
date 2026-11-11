---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DerivedSubgroupInclusionFreeGroupKourovka13Problem62Wanted.derivedInclusionImpliesInclusion, MathlibExt.GroupTheory.DerivedSubgroupInclusionFreeGroupKourovka13Problem62Wanted.derivedInclusionImpliesInclusion_refuted
statement: formalized
---

# Derived subgroups of subgroups of free groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/derived-subgroups-of-subgroups-of-free-groups/index.html).

## Inclusion of derived subgroups in free groups (Kourovka 13.62)

The conjecture of
V. P. Shaptala that for every free group $F$ and all non-cyclic subgroups $U$ and $V$ of $F$, if
the commutator subgroup $[U, U]$ is contained in the commutator subgroup $[V, V]$, then $U$ is
contained in $V$.

Formalized by `MathlibExt.GroupTheory.DerivedSubgroupInclusionFreeGroupKourovka13Problem62Wanted.derivedInclusionImpliesInclusion`, a definition declared in [WantedExt/GroupTheory/DerivedSubgroupInclusionFreeGroupKourovka13Problem62Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DerivedSubgroupInclusionFreeGroupKourovka13Problem62Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/derived-subgroups-of-subgroups-of-free-groups/index.html#derived-inclusion-implies-inclusion).

## Inclusion of derived subgroups does not imply inclusion in free groups

There exist a free
group $F$ and non-cyclic subgroups $U$ and $V$ of $F$ such that the commutator subgroup $[U, U]$
is contained in the commutator subgroup $[V, V]$ but $U$ is not contained in $V$. That is, the
conjecture of Kourovka Problem 13.62 is false; the Kourovka Archive credits this answer to
M. J. Dunwoody.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.62 (V. P. Shaptala); resolution: M. J. Dunwoody, Arch. Math. 16 (1965), 153-157, Kourovka Archive, Problem 13.62 (answer: No, it does not).

Stated but not proved: `MathlibExt.GroupTheory.DerivedSubgroupInclusionFreeGroupKourovka13Problem62Wanted.derivedInclusionImpliesInclusion_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DerivedSubgroupInclusionFreeGroupKourovka13Problem62Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DerivedSubgroupInclusionFreeGroupKourovka13Problem62Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/derived-subgroups-of-subgroups-of-free-groups/index.html#derived-inclusion-implies-inclusion-refu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Derived subgroups of subgroups of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/derived-subgroups-of-subgroups-of-free-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/derived-subgroups-of-subgroups-of-free-groups)
