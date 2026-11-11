---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.RetractIntersectionFreeGroupKourovka17Problem19Wanted.IsRetract, MathlibExt.GroupTheory.RetractIntersectionFreeGroupKourovka17Problem19Wanted.retractIntersectionIsRetract, MathlibExt.GroupTheory.RetractIntersectionFreeGroupKourovka17Problem19Wanted.retractIntersectionIsRetract_refuted
statement: formalized
---

# Retracts of free groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/retracts-of-free-groups/index.html).

## Retract of a group

A subgroup $R$ of a group $F$ is a retract of $F$ when there is an
endomorphism $r \colon F \to F$ whose image is $R$ and which fixes every element of $R$.

Formalized by `MathlibExt.GroupTheory.RetractIntersectionFreeGroupKourovka17Problem19Wanted.IsRetract`, a definition declared in [WantedExt/GroupTheory/RetractIntersectionFreeGroupKourovka17Problem19Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RetractIntersectionFreeGroupKourovka17Problem19Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/retracts-of-free-groups/index.html#is-retract).

## Bergman's retract intersection question (Kourovka Problem 17.19)

The statement that for
every natural number $n$, every retract $R$ of the free group $F_n$ on $n$ generators and every
finitely generated subgroup $H$ of $F_n$, the intersection $H \cap R$ is a retract of $H$.

A subgroup of a free group is finitely generated exactly when it has finite rank.

Formalized by `MathlibExt.GroupTheory.RetractIntersectionFreeGroupKourovka17Problem19Wanted.retractIntersectionIsRetract`, a definition declared in [WantedExt/GroupTheory/RetractIntersectionFreeGroupKourovka17Problem19Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RetractIntersectionFreeGroupKourovka17Problem19Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/retracts-of-free-groups/index.html#retract-intersection-is-retract).

## Negative answer to Bergman's retract intersection question (Kourovka Problem 17.19)

It is not
the case that for every natural number $n$, every retract $R$ of the free group $F_n$ on $n$
generators and every finitely generated subgroup $H$ of $F_n$, the intersection $H \cap R$ is a
retract of $H$.

Snopce, Tanushevski and Zalesskii (2022) give a free group $F$ of finite rank, a retract $R$ of $F$
and a finitely generated subgroup $H$ of $F$ such that $H \cap R$ is not a retract of $H$; the
Kourovka Archive answers 17.19 "No, it need not".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.19 (G. M. Bergman); resolution: I. Snopce, S. Tanushevski and P. Zalesskii, Int. Math. Res. Notices 2022, no. 11 (2022), 8280-8294, Kourovka Archive, Problem 17.19 (No, it need not).

Stated but not proved: `MathlibExt.GroupTheory.RetractIntersectionFreeGroupKourovka17Problem19Wanted.retractIntersectionIsRetract_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/RetractIntersectionFreeGroupKourovka17Problem19Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RetractIntersectionFreeGroupKourovka17Problem19Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/retracts-of-free-groups/index.html#retract-intersection-is-retract-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Retracts of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/retracts-of-free-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/retracts-of-free-groups)
