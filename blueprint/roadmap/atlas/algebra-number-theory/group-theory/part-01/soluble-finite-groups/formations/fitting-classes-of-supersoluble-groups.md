---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.GroupClass, MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.IsFitting, MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.IsSupersoluble, MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.IsMinimalNormal, MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.fittingSupersolubleMinimalNormalCentral, MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.fittingSupersolubleMinimalNormalCentral_refuted
statement: formalized
---

# Fitting classes of supersoluble groups

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups/index.html).

## Isomorphism-closed classes of groups (Kourovka 12.91)

A class of groups is a property of
groups (in the lowest type universe) that is closed under isomorphism: whenever a group $H$ has the
property and $H$ is isomorphic to a group $K$, then $K$ has the property. Only the finite members of
a class are used in Kourovka Problem 12.91.

Formalized by `MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.GroupClass`, a structure declared in [WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups/index.html#group-class).

## Fitting classes (Kourovka 12.91)

A class $\mathfrak{X}$ of groups is a Fitting class (of
finite groups) if, for every finite group $G$: whenever $G \in \mathfrak{X}$, every normal subgroup
of $G$ belongs to $\mathfrak{X}$; and whenever $N_1$ and $N_2$ are normal subgroups of $G$ that
belong to $\mathfrak{X}$, the subgroup $N_1 N_2$ they generate belongs to $\mathfrak{X}$.

Formalized by `MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.IsFitting`, a definition declared in [WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups/index.html#is-fitting).

## Supersoluble groups (Kourovka 12.91)

A group $G$ is supersoluble if it has a chain of
subgroups $1 = G_0 \le G_1 \le \cdots \le G_k = G$, each normal in $G$, such that for every $i < k$
there is an element $x \in G_{i+1}$ with $G_{i+1} = \langle x \rangle G_i$; that is, every factor
$G_{i+1}/G_i$ is cyclic.

Formalized by `MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.IsSupersoluble`, a definition declared in [WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups/index.html#is-supersoluble).

## Minimal normal subgroups (Kourovka 12.91)

A subgroup $N$ of a group $G$ is minimal normal
if $N$ is a nontrivial normal subgroup of $G$ and every nontrivial normal subgroup $M$ of $G$ with
$M \le N$ equals $N$.

Formalized by `MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.IsMinimalNormal`, a definition declared in [WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups/index.html#is-minimal-normal).

## Heineken's question on Fitting classes of supersoluble groups

The proposition that for
every class $\mathfrak{X}$ of groups that is a Fitting class and all of whose finite members are
supersoluble, every minimal normal subgroup of every finite group $G \in \mathfrak{X}$ is contained
in the center of $G$.

This is Kourovka Problem 12.91 (H. Heineken).

Formalized by `MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.fittingSupersolubleMinimalNormalCentral`, a definition declared in [WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups/index.html#fitting-supersoluble-minimal-normal-cent).

## A Fitting class of supersoluble groups with a non-central minimal normal subgroup

There
exist a class $\mathfrak{X}$ of groups that is a Fitting class and all of whose finite members are
supersoluble, a finite group $G \in \mathfrak{X}$, and a minimal normal subgroup $N$ of $G$ that is
not contained in the center of $G$.

This answers Kourovka Problem 12.91 in the negative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.91 (H. Heineken); resolution: H. Heineken, Rend. Sem. Mat. Univ. Padova 98 (1997), 241-251, Kourovka Archive, Problem 12.91: No, it does not.

Stated but not proved: `MathlibExt.GroupTheory.FittingSupersolubleCentralKourovka12Problem91Wanted.fittingSupersolubleMinimalNormalCentral_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FittingSupersolubleCentralKourovka12Problem91Wanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups/index.html#fitting-supersoluble-minimal-normal-cent-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fitting classes of supersoluble groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/formations/fitting-classes-of-supersoluble-groups)
