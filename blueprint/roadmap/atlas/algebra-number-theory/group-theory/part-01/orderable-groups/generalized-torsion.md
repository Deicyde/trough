---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.GeneralizedTorsionFreeProductKourovka16Problem49Wanted.IsGeneralizedTorsion, MathlibExt.GroupTheory.GeneralizedTorsionFreeProductKourovka16Problem49Wanted.freeProductNoGeneralizedTorsion, MathlibExt.GroupTheory.GeneralizedTorsionFreeProductKourovka16Problem49Wanted.freeProductNoGeneralizedTorsion_holds, MathlibExt.GroupTheory.GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.IsGeneralizedTorsion, MathlibExt.GroupTheory.GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.rightOrders, MathlibExt.GroupTheory.GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.noGeneralizedTorsionRightOrderable, MathlibExt.GroupTheory.GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.noGeneralizedTorsionRightOrderable_refuted
statement: formalized
---

# Generalized torsion

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html).

## Generalized torsion element (Kourovka 16.49)

An element $h$ of a group $H$ is a generalized
torsion element when $h \ne 1$ and some nonempty product of conjugates of $h$ is trivial, that is,
$x_1^{-1} h x_1 \cdots x_k^{-1} h x_k = 1$ for some $k \ge 1$ and some $x_1, \dots, x_k \in H$.

Formalized by `MathlibExt.GroupTheory.GeneralizedTorsionFreeProductKourovka16Problem49Wanted.IsGeneralizedTorsion`, a definition declared in [WantedExt/GroupTheory/GeneralizedTorsionFreeProductKourovka16Problem49Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GeneralizedTorsionFreeProductKourovka16Problem49Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html#is-generalized-torsion).

## Kopytov–Medvedev question on generalized torsion in free products (Kourovka 16.49)

The
statement that for every family of groups $(G_i)_{i \in I}$ none of which contains a generalized
torsion element (an element $h \ne 1$ such that some nonempty product of conjugates of $h$ is
trivial), the free product of the family contains no generalized torsion element either.

Formalized by `MathlibExt.GroupTheory.GeneralizedTorsionFreeProductKourovka16Problem49Wanted.freeProductNoGeneralizedTorsion`, a definition declared in [WantedExt/GroupTheory/GeneralizedTorsionFreeProductKourovka16Problem49Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GeneralizedTorsionFreeProductKourovka16Problem49Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html#free-product-no-generalized-torsion).

## Free products of groups without generalized torsion have no generalized torsion

For every
family of groups $(G_i)_{i \in I}$ none of which contains a generalized torsion element (an element
$h \ne 1$ such that some nonempty product of conjugates of $h$ is trivial), the free product of the
family contains no generalized torsion element.

The Kourovka Archive answers 16.49 "Yes, it is true", citing Ito, Motegi and Teragaito (2019),
whose Theorem 1.5 shows that a generalized torsion element of a free product
$G_1 \ast \cdots \ast G_n$ of torsion-free groups is conjugate to a generalized torsion element of
some factor.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.49 (V. M. Kopytov, N. Ya. Medvedev); resolution: T. Ito, K. Motegi and M. Teragaito, Generalized torsion and decomposition of 3-manifolds, Proc. Amer. Math. Soc. 147 (2019), no. 11, 4999-5008, arXiv:1811.07532, Theorem 1.5 (a generalized torsion element of a free product G_1 ∗ ⋯ ∗ G_n of torsion-free groups is conjugate to a generalized torsion element of some factor); Kourovka Archive, Problem 16.49 (Yes; moreover the generalized torsion in a free product of torsion-free groups is conjugate to a generalized torsion of one of its factor groups), https://arxiv.org/abs/1811.07532.

Stated but not proved: `MathlibExt.GroupTheory.GeneralizedTorsionFreeProductKourovka16Problem49Wanted.freeProductNoGeneralizedTorsion_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/GeneralizedTorsionFreeProductKourovka16Problem49Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GeneralizedTorsionFreeProductKourovka16Problem49Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html#free-product-no-generalized-torsion-hold).

## Generalized torsion elements (Kourovka 16.48)

An element $h$ of a group $H$ is a
generalized torsion element if $h \ne 1$ and there are $n \ge 1$ elements
$x_1, \dots, x_n \in H$, not necessarily distinct, such that
$(x_1^{-1} h x_1)(x_2^{-1} h x_2) \cdots (x_n^{-1} h x_n) = 1$.

Formalized by `MathlibExt.GroupTheory.GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.IsGeneralizedTorsion`, a definition declared in [WantedExt/GroupTheory/GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html#is-generalized-torsion-2).

## Right orders on a group (Kourovka 16.48)

The right orders of a group $G$ are the binary
relations $\preceq$ on $G$ that are linear orders (reflexive, transitive, antisymmetric and total)
and are invariant under right multiplication: $a \preceq b$ implies $ac \preceq bc$ for all
$a, b, c \in G$.

Formalized by `MathlibExt.GroupTheory.GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.rightOrders`, a definition declared in [WantedExt/GroupTheory/GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html#right-orders).

## The Kopytov–Medvedev question (Kourovka 16.48)

This is the proposition that every group
$H$ with no generalized torsion element is right-orderable, that is, admits a right order.

Formalized by `MathlibExt.GroupTheory.GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.noGeneralizedTorsionRightOrderable`, a definition declared in [WantedExt/GroupTheory/GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html#no-generalized-torsion-right-orderable).

## Some group without generalized torsion is not right-orderable (Kourovka 16.48)

The
Kopytov–Medvedev proposition is false: there is a group $H$ with no generalized torsion element
that admits no right order.

Resolved false: Cai and Clay give a condition ensuring that an amalgam is generalized torsion-free
and use it to construct a group that is generalized torsion-free but not left-orderable (their
Theorem 1.3, proved in Section 7), hence not right-orderable; the Kourovka Notebook (21st issue)
answers 16.48 "No, not every".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.48 (V. M. Kopytov, N. Ya. Medvedev); resolution: T. W. Cai and A. Clay, Generalized torsion in amalgams, preprint, arXiv:2504.08084 (2025), Theorem 1.3 (there exists a group which is generalized torsion-free and not left-orderable; Definition 7.1 and Theorem 7.2); the Kourovka Notebook (21st issue) marks 16.48 solved (No, not every), https://arxiv.org/abs/2504.08084.

Stated but not proved: `MathlibExt.GroupTheory.GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.noGeneralizedTorsionRightOrderable_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GeneralizedTorsionRightOrderableKourovka16Problem48Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html#no-generalized-torsion-right-orderable-r).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized torsion](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/generalized-torsion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orderable-groups/generalized-torsion)
