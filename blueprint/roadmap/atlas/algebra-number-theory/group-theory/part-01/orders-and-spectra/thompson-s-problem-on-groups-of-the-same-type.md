---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.Kourovka21Problem134bWanted.SamePowerEquationType, MathlibExt.GroupTheory.Kourovka21Problem134bWanted.IsAlmostSimple, MathlibExt.GroupTheory.Kourovka21Problem134bWanted.conjecture, MathlibExt.GroupTheory.Kourovka21Problem134bWanted.conjecture_refuted, MathlibExt.GroupTheory.SolubleTypeRecognitionKourovka12Problem37Wanted.SameType, MathlibExt.GroupTheory.SolubleTypeRecognitionKourovka12Problem37Wanted.solubleOfSameTypeAsSoluble, MathlibExt.GroupTheory.SolubleTypeRecognitionKourovka12Problem37Wanted.solubleOfSameTypeAsSoluble_refuted
statement: formalized
---

# Thompson's problem on groups of the same type

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html).

## Same power-equation type

Two groups $G$ and $H$ have the same power-equation type when,
for every positive integer $n$, the equation $x^n = 1$ has the same number of solutions in $G$ as
in $H$. An infinite set of solutions is counted as $0$, so the notion is meant for finite
groups.

Formalized by `MathlibExt.GroupTheory.Kourovka21Problem134bWanted.SamePowerEquationType`, a definition declared in [WantedExt/GroupTheory/Kourovka21Problem134bWanted.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/Kourovka21Problem134bWanted.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html#same-power-equation-type).

## Almost simple group

A group $G$ is almost simple when there is a nonabelian finite simple
group $S$ such that $G$ is isomorphic to a subgroup $A$ of the automorphism group
$\mathrm{Aut}(S)$ that contains the inner automorphism group $\mathrm{Inn}(S)$.

Formalized by `MathlibExt.GroupTheory.Kourovka21Problem134bWanted.IsAlmostSimple`, a definition declared in [WantedExt/GroupTheory/Kourovka21Problem134bWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/Kourovka21Problem134bWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html#is-almost-simple).

## Characterization of almost simple groups by power-equation type (Kourovka 21.134(b))

The conjecture that for all finite groups $G$ and $H$, if $G$ is almost simple and $G$ and $H$
have the same power-equation type, then $G$ is isomorphic to $H$.

Formalized by `MathlibExt.GroupTheory.Kourovka21Problem134bWanted.conjecture`, a definition declared in [WantedExt/GroupTheory/Kourovka21Problem134bWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/Kourovka21Problem134bWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html#conjecture).

## Power-equation type does not characterize almost simple groups

There exist finite
groups $G$ and $H$ such that $G$ is almost simple, $G$ and $H$ have the same power-equation type,
and $G$ is not isomorphic to $H$. That is, the conjecture of Kourovka Problem 21.134(b) is false.

Kourovka Notebook v46 records that J. G. Thompson had already given a negative answer to part (b).

## Sources

- Yu Li and Wujie Shi, A Note on Thompson Problem, arXiv:2303.09460v1 (2023); published in Ricerche di Matematica 74(1) (2025), 559-563, https://arxiv.org/abs/2303.09460v1; The Kourovka Notebook: Unsolved Problems in Group Theory, 21st edition, Problem 21.134, arXiv:1401.0300v46, https://arxiv.org/abs/1401.0300v46.

Stated but not proved: `MathlibExt.GroupTheory.Kourovka21Problem134bWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/Kourovka21Problem134bWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/Kourovka21Problem134bWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html#conjecture-refuted).

## Groups of the same type

Two groups $G$ and $H$ have the same type when, for every integer
$n \ge 1$, the equation $x^n = 1$ has the same number of solutions in $G$ as in $H$, where an
infinite set of solutions counts as having $0$ elements.

Formalized by `MathlibExt.GroupTheory.SolubleTypeRecognitionKourovka12Problem37Wanted.SameType`, a definition declared in [WantedExt/GroupTheory/SolubleTypeRecognitionKourovka12Problem37Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleTypeRecognitionKourovka12Problem37Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html#same-type).

## Kourovka Problem 12.37 (J. G. Thompson)

Every finite group of the same type as a finite
soluble group is soluble: if $G$ and $H$ are finite groups of the same type and $H$ is soluble,
then $G$ is soluble.

Formalized by `MathlibExt.GroupTheory.SolubleTypeRecognitionKourovka12Problem37Wanted.solubleOfSameTypeAsSoluble`, a definition declared in [WantedExt/GroupTheory/SolubleTypeRecognitionKourovka12Problem37Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleTypeRecognitionKourovka12Problem37Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html#soluble-of-same-type-as-soluble).

## Solubility is not determined by the type

The answer to Kourovka Problem 12.37 is negative:
there are finite groups $G$ and $H$ of the same type such that $H$ is soluble and $G$ is not
soluble.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 12.37 (J. G. Thompson; A. S. Kondratiev, W. J. Shi); resolution: P. Piwek, Algebra Number Theory 19 (2025), no. 8, 1663-1670, the Kourovka Notebook (21st issue) marks 12.37 solved: No, not always.

Stated but not proved: `MathlibExt.GroupTheory.SolubleTypeRecognitionKourovka12Problem37Wanted.solubleOfSameTypeAsSoluble_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SolubleTypeRecognitionKourovka12Problem37Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleTypeRecognitionKourovka12Problem37Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html#soluble-of-same-type-as-soluble-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thompson's problem on groups of the same type](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orders-and-spectra/thompson-s-problem-on-groups-of-the-same-type)
