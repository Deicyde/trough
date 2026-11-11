---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeGroupPowerAbelianizationKourovka13Problem18Wanted.cartesianPowerAbelianizationTorsionFree, MathlibExt.GroupTheory.FreeGroupPowerAbelianizationKourovka13Problem18Wanted.cartesianPowerAbelianizationTorsionFree_refuted
statement: formalized
---

# Cartesian powers of free groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/cartesian-powers-of-free-groups/index.html).

## Torsion-freeness of abelianized Cartesian powers of free groups (Kourovka 13.18)

The
statement, posed by A. M. Gaglione and D. Spellman, that for every integer $n \ge 2$ the
abelianization of the unrestricted (Cartesian) product $F_n^{\mathbb{N}}$ of countably many copies
of the free group $F_n$ of rank $n$ is torsion-free: none of its nontrivial elements has finite
order.

Formalized by `MathlibExt.GroupTheory.FreeGroupPowerAbelianizationKourovka13Problem18Wanted.cartesianPowerAbelianizationTorsionFree`, a definition declared in [WantedExt/GroupTheory/FreeGroupPowerAbelianizationKourovka13Problem18Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeGroupPowerAbelianizationKourovka13Problem18Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/cartesian-powers-of-free-groups/index.html#cartesian-power-abelianization-torsion-f).

## Abelianized Cartesian powers of free groups can have torsion

For some integer $n \ge 2$, the
abelianization of the unrestricted (Cartesian) product $F_n^{\mathbb{N}}$ of countably many copies
of the free group $F_n$ of rank $n$ contains a nontrivial element of finite order. That is, the
torsion-freeness asked for in Kourovka Problem 13.18 fails.

The Kourovka Archive answers 13.18 "No, it may contain elements of order 2" (O. Kharlampovich and
A. Myasnikov, 2001).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.18 (A. M. Gaglione, D. Spellman); resolution: O. Kharlampovich and A. Myasnikov, in: Knots, braids, and mapping class groups (New York, 1998), Amer. Math. Soc., 2001, 77-83, Kourovka Archive, Problem 13.18: No, it may contain elements of order 2.

Stated but not proved: `MathlibExt.GroupTheory.FreeGroupPowerAbelianizationKourovka13Problem18Wanted.cartesianPowerAbelianizationTorsionFree_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeGroupPowerAbelianizationKourovka13Problem18Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeGroupPowerAbelianizationKourovka13Problem18Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/cartesian-powers-of-free-groups/index.html#cartesian-power-abelianization-torsion-f-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cartesian powers of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/cartesian-powers-of-free-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/cartesian-powers-of-free-groups)
