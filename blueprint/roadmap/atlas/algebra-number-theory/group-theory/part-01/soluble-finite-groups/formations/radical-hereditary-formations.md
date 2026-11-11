---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.GroupClass, MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.QuotMem, MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsFormation, MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsRadical, MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsHereditary, MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsSolubleRadical, MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsComposition, MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.radicalHereditaryFormationIsComposition
statement: formalized
---

# Radical hereditary formations

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html).

## Isomorphism-closed class of groups

A class of groups $X$ is a property of groups that is
invariant under isomorphism: if a group $H$ belongs to $X$ and $K$ is a group isomorphic to $H$,
then $K$ belongs to $X$.

Infinite groups may belong to a class; apart from isomorphism invariance, the conditions imposed
on classes below concern only finite groups.

Formalized by `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.GroupClass`, a structure declared in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#group-class).

## Quotient lying in a class

For a class of groups $X$, a group $G$ and a subgroup $N$ of $G$,
this holds when $N$ is normal in $G$ and the quotient group $G/N$ belongs to $X$.

Formalized by `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.QuotMem`, a definition declared in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#quot-mem).

## Formation of finite groups

A class of groups $X$ is a formation if it contains the trivial
group, for every finite group $G$ in $X$ and every normal subgroup $N$ of $G$ the quotient $G/N$
belongs to $X$, and for every finite group $G$ with normal subgroups $N_1, N_2$ such that
$G/N_1$ and $G/N_2$ belong to $X$, the quotient $G/(N_1 \cap N_2)$ belongs to $X$.

Formalized by `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsFormation`, a definition declared in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#is-formation).

## Radical (Fitting) class

A class of groups $X$ is radical if, for every finite group $G$,
every normal subgroup of $G$ belongs to $X$ whenever $G$ does, and whenever $N_1, N_2$ are normal
subgroups of $G$ that belong to $X$, their product $N_1 N_2$ belongs to $X$.

Formalized by `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsRadical`, a definition declared in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#is-radical).

## Hereditary class of groups

A class of groups $X$ is hereditary if every subgroup of a
finite group in $X$ belongs to $X$.

Formalized by `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsHereditary`, a definition declared in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#is-hereditary).

## Soluble radical

A subgroup $R$ of a group $G$ is the soluble radical of $G$ if $R$ is a
soluble normal subgroup of $G$ that contains every soluble normal subgroup of $G$.

Formalized by `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsSolubleRadical`, a definition declared in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#is-soluble-radical).

## Solubly saturated class

A class of groups $X$ is solubly saturated (a composition class)
if, for every finite group $G$ with soluble radical $R$, whenever the Frattini subgroup $\Phi(R)$
of $R$ is normal in $G$ and $G/\Phi(R)$ belongs to $X$, the group $G$ belongs to $X$.

A formation with this property is a composition (solubly saturated, Baer-local) formation.

Formalized by `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.IsComposition`, a definition declared in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#is-composition).

## Kourovka Problem 12.7 (Vasil'ev)

The statement that every radical hereditary formation of
finite groups is a composition formation: every class of groups that is a formation, a radical
class and a hereditary class is solubly saturated.

Formalized by `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.radicalHereditaryFormationIsComposition`, a definition declared in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#radical-hereditary-formation-is-composit).

## Radical hereditary formations need not be composition formations

It is not true that every
radical hereditary formation of finite groups is a composition formation: some class of groups
that is a formation, a radical class and a hereditary class is not solubly saturated.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.7 (A. F. Vasil'ev); resolution: S. F. Kamornikov, Math. Notes 55 (1994), no. 6, 586-588, Kourovka Archive, Problem 12.7: No, it is not.

Stated but not proved: `MathlibExt.GroupTheory.RadicalHereditaryFormationKourovka12Problem7Wanted.radicalHereditaryFormationIsComposition_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RadicalHereditaryFormationKourovka12Problem7Wanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html#radical-hereditary-formation-is-composit-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Radical hereditary formations](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/formations/radical-hereditary-formations)
