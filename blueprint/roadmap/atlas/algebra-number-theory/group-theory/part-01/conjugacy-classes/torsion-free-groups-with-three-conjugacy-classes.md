---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TorsionFreeThreeClassesIndexTwoKourovka11Problem42Wanted.torsionFreeThreeClassesIndexTwo, MathlibExt.GroupTheory.TorsionFreeThreeClassesIndexTwoKourovka11Problem42Wanted.torsionFreeThreeClassesIndexTwo_holds, MathlibExt.GroupTheory.TorsionFreeThreeClassesNoRealKourovka11Problem67Wanted.torsionFreeThreeClassesNoInverseConj, MathlibExt.GroupTheory.TorsionFreeThreeClassesNoRealKourovka11Problem67Wanted.torsionFreeThreeClassesNoInverseConj_holds
statement: formalized
---

# Torsion-free groups with three conjugacy classes

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/torsion-free-groups-with-three-conjugacy-classes/index.html).

## Kourovka Problem 11.42 (statement)

The statement that there is a torsion-free group $G$ (no
element of $G$ other than the identity has finite order) that has exactly three conjugacy classes
and has a subgroup of index $2$.

The problem was posed by A. V. Izosov.

Formalized by `MathlibExt.GroupTheory.TorsionFreeThreeClassesIndexTwoKourovka11Problem42Wanted.torsionFreeThreeClassesIndexTwo`, a definition declared in [WantedExt/GroupTheory/TorsionFreeThreeClassesIndexTwoKourovka11Problem42Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeThreeClassesIndexTwoKourovka11Problem42Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/torsion-free-groups-with-three-conjugacy-classes/index.html#torsion-free-three-classes-index-two).

## Minasyan's theorem (Kourovka Problem 11.42)

There is a torsion-free group $G$ (no element of
$G$ other than the identity has finite order) that has exactly three conjugacy classes and has a
subgroup of index $2$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.42 (A. V. Izosov); resolution: A. Minasyan, Comment. Math. Helv. 84 (2009), 259-296, Kourovka Archive, Problem 11.42: "Yes, there does", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.TorsionFreeThreeClassesIndexTwoKourovka11Problem42Wanted.torsionFreeThreeClassesIndexTwo_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TorsionFreeThreeClassesIndexTwoKourovka11Problem42Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeThreeClassesIndexTwoKourovka11Problem42Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/torsion-free-groups-with-three-conjugacy-classes/index.html#torsion-free-three-classes-index-two-hol).

## Kourovka Problem 11.67 (statement)

The statement that there is a torsion-free group $G$ (no
element of $G$ other than the identity has finite order) with exactly three conjugacy classes in
which no element $g \neq 1$ is conjugate to its inverse $g^{-1}$, that is, no nontrivial conjugacy
class contains a pair of mutually inverse elements.

The problem was posed by B. Neumann.

Formalized by `MathlibExt.GroupTheory.TorsionFreeThreeClassesNoRealKourovka11Problem67Wanted.torsionFreeThreeClassesNoInverseConj`, a definition declared in [WantedExt/GroupTheory/TorsionFreeThreeClassesNoRealKourovka11Problem67Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeThreeClassesNoRealKourovka11Problem67Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/torsion-free-groups-with-three-conjugacy-classes/index.html#torsion-free-three-classes-no-inverse-co).

## Bagayoko's theorem (Kourovka Problem 11.67)

There is a torsion-free group $G$ (no element of
$G$ other than the identity has finite order) with exactly three conjugacy classes in which no
element $g \neq 1$ is conjugate to its inverse $g^{-1}$.

Bagayoko's example is a linearly ordered group with exactly three conjugacy classes, the positive
transseries under composition; an ordered group is torsion-free, and conjugation preserves
positivity, so no $g \neq 1$ is conjugate to $g^{-1}$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 11.67 (B. Neumann); resolution: V. Bagayoko, Ordered groups of formal series, and a conjugacy problem, arXiv:2509.09186 (2025), main result: a linearly ordered group `(𝕋^{>ℝ}, ∘, <)` of transseries under composition with exactly three conjugacy classes; the Kourovka Notebook (21st issue) marks 11.67 solved, https://arxiv.org/abs/2509.09186.

Stated but not proved: `MathlibExt.GroupTheory.TorsionFreeThreeClassesNoRealKourovka11Problem67Wanted.torsionFreeThreeClassesNoInverseConj_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TorsionFreeThreeClassesNoRealKourovka11Problem67Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeThreeClassesNoRealKourovka11Problem67Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/torsion-free-groups-with-three-conjugacy-classes/index.html#torsion-free-three-classes-no-inverse-co-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Torsion-free groups with three conjugacy classes](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/torsion-free-groups-with-three-conjugacy-classes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/conjugacy-classes/torsion-free-groups-with-three-conjugacy-classes)
