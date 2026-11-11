---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.GroupClass, MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.IsFormation, MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.residual, MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.pGroupFormationIndecomposable, MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.pGroupFormationIndecomposable_holds, MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.GroupClass, MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.IsFormation, MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.NontrivialClass
statement: formalized
---

# Indecomposable formations

13 results, 11 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html).

## Class of finite groups (Kourovka 10.72)

A class of finite groups is given by a
membership predicate: a proposition $X(G)$ for every finite group $G$. It is not required to be
closed under isomorphisms.

Formalized by `MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.GroupClass`, an abbreviation declared in [WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#group-class).

## Formation of finite groups (Kourovka 10.72)

A class $X$ of finite groups is a formation
when it is closed under isomorphisms, contains the trivial group, contains the quotient $G/N$ of
each of its members $G$ by every normal subgroup $N$, and contains $G/(N_1 \cap N_2)$ whenever
$N_1$ and $N_2$ are normal subgroups of a finite group $G$ with $G/N_1$ and $G/N_2$ in $X$. The
last condition is closure under subdirect products.

Formalized by `MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.IsFormation`, a definition declared in [WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#is-formation).

## Residual of a finite group with respect to a class (Kourovka 10.72)

For a class $X$ of
finite groups and a finite group $G$, the $X$-residual of $G$ is the intersection of all normal
subgroups $N$ of $G$ with $G/N \in X$. When $X$ is a formation, it is the smallest such $N$.

Formalized by `MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.residual`, a definition declared in [WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#residual).

## Indecomposability of the formation of finite $p$-groups (Kourovka 10.72)

The statement
that for every prime $p$, the class $\mathfrak{N}_p$ of all finite $p$-groups is not the Gaschütz
product $\mathfrak{F} \circ \mathfrak{G}$ of two formations $\mathfrak{F}$ and $\mathfrak{G}$ that
consist of $p$-groups, each contain a nontrivial group and each omit some finite $p$-group. Here a
finite group $G$ lies in $\mathfrak{F} \circ \mathfrak{G}$ when its $\mathfrak{G}$-residual lies
in $\mathfrak{F}$.

Omitting some finite $p$-group is part of the reading of "non-trivial": for all formations
$\mathfrak{F}, \mathfrak{G}$ consisting of $p$-groups,
$\mathfrak{N}_p \circ \mathfrak{G} = \mathfrak{F} \circ \mathfrak{N}_p = \mathfrak{N}_p$.

Formalized by `MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.pGroupFormationIndecomposable`, a definition declared in [WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#p-group-formation-indecomposable).

## The formation of finite $p$-groups is indecomposable

For every prime $p$, the class
$\mathfrak{N}_p$ of all finite $p$-groups is not the Gaschütz product $\mathfrak{F} \circ
\mathfrak{G}$ of two formations $\mathfrak{F}$ and $\mathfrak{G}$ that consist of $p$-groups, each
contain a nontrivial group and each omit some finite $p$-group. Here a finite group $G$ lies in
$\mathfrak{F} \circ \mathfrak{G}$ when its $\mathfrak{G}$-residual lies in $\mathfrak{F}$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.72 (L. A. Shemetkov); resolution: A. N. Skiba and L. A. Shemetkov, Dokl. Akad. Nauk BSSR 33 (1989), 581-582 (Russian), Kourovka Archive, Problem 10.72 ("This has been proved").

Stated but not proved: `MathlibExt.GroupTheory.PGroupFormationIndecomposableKourovka10Problem72Wanted.pGroupFormationIndecomposable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupFormationIndecomposableKourovka10Problem72Wanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#p-group-formation-indecomposable-holds).

## Isomorphism-closed classes of groups (Kourovka 12.97)

A class of groups is given by a
membership predicate on groups such that every group isomorphic to a member is again a member.
Only the finite members matter in the formulation of Kourovka Problem 12.97.

Formalized by `MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.GroupClass`, a structure declared in [WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#group-class-2).

## Formations of finite groups (Kourovka 12.97)

A class $X$ of groups is a formation when it
contains the trivial group, the quotient $G/N$ lies in $X$ for every finite group $G$ in $X$ and
every normal subgroup $N$ of $G$, and for every finite group $G$ with normal subgroups $N_1$ and
$N_2$ such that $G/N_1$ and $G/N_2$ lie in $X$, the quotient $G/(N_1 \cap N_2)$ lies in $X$.

Formalized by `MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.IsFormation`, a definition declared in [WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#is-formation-2).

## Classes containing a nontrivial finite group

A class $X$ of groups is nontrivial when it
contains a nontrivial finite group; for a formation this means that $X$ is not the trivial
formation.

Formalized by `MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.NontrivialClass`, a definition declared in [WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#nontrivial-class).

## The residual of a group with respect to a class (Kourovka 12.97)

For a class $X$ of groups
and a group $G$, the $X$-residual of $G$ is the intersection of all normal subgroups $N$ of $G$
such that the quotient $G/N$ lies in $X$.

Formalized by `MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.residual`, a definition declared in [WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#residual-2).

## Groups with a subnormal series whose factors are all isomorphic to a given group

For
groups $T$ and $G$, the group $G$ lies in the class $\mathfrak{F}_T$ when it has a subnormal series
$1 = H_0 \le H_1 \le \dots \le H_n = G$, each $H_i$ normal in $H_{i+1}$, all of whose factors
$H_{i+1}/H_i$ are isomorphic to $T$. For simple $T$ these are the groups all of whose composition
factors are isomorphic to $T$.

Formalized by `MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.AllCompositionFactorsIso`, a definition declared in [WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#all-composition-factors-iso).

## Proper subclass of a formation

`X` is a proper subclass of `𝔉_T`: some finite group of `𝔉_T` does not belong to `X`.

Formalized by `MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.IsProperIn`, a definition declared in [WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#is-proper-in).

## Kourovka Problem 12.97 (Shemetkov)

For a group $T$, write $\mathfrak{F}_T$ for the class
of groups having a subnormal series all of whose factors are isomorphic to $T$. This is the
proposition that, for every finite non-abelian simple group $T$ and all formations $\mathfrak{M}$
and $\mathfrak{H}$ whose finite members lie in $\mathfrak{F}_T$, each containing a nontrivial
finite group and each missing some finite group of $\mathfrak{F}_T$, it is not the case that every
finite group $G$ satisfies: $G \in \mathfrak{F}_T$ if and only if the $\mathfrak{H}$-residual
$G^{\mathfrak{H}}$ of $G$ lies in $\mathfrak{M}$. In other words, $\mathfrak{F}_T$ is not the
Gaschütz product $\mathfrak{M}\mathfrak{H} = \{G : G^{\mathfrak{H}} \in \mathfrak{M}\}$ of two
nontrivial proper subformations.

Formalized by `MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.compositionFactorFormationIndecomposable`, a definition declared in [WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#composition-factor-formation-indecomposa).

## Mel'nikov's theorem on Kourovka Problem 12.97

Let $T$ be a finite non-abelian simple group,
and write $\mathfrak{F}_T$ for the class of groups having a subnormal series all of whose factors
are isomorphic to $T$. Let $\mathfrak{M}$ and $\mathfrak{H}$ be formations whose finite members
lie in $\mathfrak{F}_T$, each containing a nontrivial finite group and each missing some finite
group of $\mathfrak{F}_T$. Then it is not true that, for every finite group $G$, $G$ lies in
$\mathfrak{F}_T$ if and only if its $\mathfrak{H}$-residual $G^{\mathfrak{H}}$ lies in
$\mathfrak{M}$: the formation $\mathfrak{F}_T$ is not the Gaschütz product
$\mathfrak{M}\mathfrak{H}$ of two nontrivial proper subformations.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.97 (L. A. Shemetkov); resolution: O. V. Mel'nikov, Problems in Algebra 9, Gomel', 1996, 42-47 (Russian), Kourovka Archive, Problem 12.97: it is proved.

Stated but not proved: `MathlibExt.GroupTheory.SimpleCompositionFactorFormationKourovka12Problem97Wanted.compositionFactorFormationIndecomposable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleCompositionFactorFormationKourovka12Problem97Wanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html#composition-factor-formation-indecomposa-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Indecomposable formations](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/formations/indecomposable-formations)
