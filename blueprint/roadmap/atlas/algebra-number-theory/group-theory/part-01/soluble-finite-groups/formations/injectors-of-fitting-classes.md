---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.GroupClass, MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.IsFitting, MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.IsXMaximalIn, MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.IsInjector, MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.fittingClassWithoutInjectors, MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.fittingClassWithoutInjectors_holds
statement: formalized
---

# Injectors of Fitting classes

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes/index.html).

## Isomorphism-closed classes of groups (Kourovka 12.96)

A class of groups is a property of
groups that is closed under isomorphism: if a group $H$ has the property and $K$ is a group
isomorphic to $H$, then $K$ has it too.

Only finite members matter for Fitting classes and for injectors of finite groups.

Formalized by `MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.GroupClass`, a structure declared in [WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes/index.html#group-class).

## Fitting classes of finite groups

A class $\mathfrak{X}$ of groups is a Fitting class of
finite groups if, for every finite group $G$, every normal subgroup of $G$ lies in $\mathfrak{X}$
whenever $G$ does, and the product $N_1 N_2$ of two normal subgroups $N_1$ and $N_2$ of $G$ lies in
$\mathfrak{X}$ whenever $N_1$ and $N_2$ do.

Formalized by `MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.IsFitting`, a definition declared in [WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes/index.html#is-fitting).

## Maximal subgroups within a class of groups

Let $\mathfrak{X}$ be a class of groups and let
$V$ and $K$ be subgroups of a group $G$. Then $V$ is $\mathfrak{X}$-maximal in $K$ if $V \le K$,
$V$ lies in $\mathfrak{X}$, and no subgroup $W$ of $G$ with $V < W \le K$ lies in $\mathfrak{X}$.

Formalized by `MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.IsXMaximalIn`, a definition declared in [WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes/index.html#is-xmaximal-in).

## Injectors

Let $\mathfrak{X}$ be a class of groups and $G$ a group. A subgroup $V$ of $G$ is
an $\mathfrak{X}$-injector of $G$ if, for every subnormal subgroup $N$ of $G$, the intersection
$V \cap N$ is $\mathfrak{X}$-maximal in $N$.

Formalized by `MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.IsInjector`, a definition declared in [WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes/index.html#is-injector).

## Kourovka Problem 12.96: a Fitting class without injectors

The statement that there are a
Fitting class $\mathfrak{X}$ of finite groups that contains at least one finite group and a finite
non-soluble group $G$ such that no subgroup of $G$ is an $\mathfrak{X}$-injector of $G$.

The problem was posed by L. A. Shemetkov.

Formalized by `MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.fittingClassWithoutInjectors`, a definition declared in [WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes/index.html#fitting-class-without-injectors).

## A Fitting class with no injectors in a non-soluble group

There are a Fitting class
$\mathfrak{X}$ of finite groups that contains at least one finite group and a finite non-soluble
group $G$ such that no subgroup of $G$ is an $\mathfrak{X}$-injector of $G$.

This answers Kourovka Problem 12.96 (L. A. Shemetkov) affirmatively: the Kourovka Archive records
that E. Salomon found such a Fitting class and group; the example is presented in Section 7.1 of
Ballester-Bolinches and Ezquerro, Classes of finite groups (2006).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.96 (L. A. Shemetkov); resolution: E. Salomon (unpublished), presented in A. Ballester-Bolinches and L. M. Ezquerro, Classes of finite groups, Springer, 2006, Section 7.1, Kourovka Archive, Problem 12.96: found by E. Salomon.

Stated but not proved: `MathlibExt.GroupTheory.FittingClassWithoutInjectorKourovka12Problem96Wanted.fittingClassWithoutInjectors_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingClassWithoutInjectorKourovka12Problem96Wanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes/index.html#fitting-class-without-injectors-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Injectors of Fitting classes](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/formations/injectors-of-fitting-classes)
