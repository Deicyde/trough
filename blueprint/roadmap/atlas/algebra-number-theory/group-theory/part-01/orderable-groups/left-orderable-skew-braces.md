---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SkewBraceLeftOrderableKourovka19Problem49Wanted.LeftOrderableMul, MathlibExt.GroupTheory.SkewBraceLeftOrderableKourovka19Problem49Wanted.LeftOrderableAdd, MathlibExt.GroupTheory.SkewBraceLeftOrderableKourovka19Problem49Wanted.skewBraceAdditiveLeftOrderable, MathlibExt.GroupTheory.SkewBraceLeftOrderableKourovka19Problem49Wanted.skewBraceAdditiveLeftOrderable_refuted
statement: formalized
---

# Left-orderable skew braces

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/left-orderable-skew-braces/index.html).

## Left-orderable multiplication

The multiplication of a set $B$ is left-orderable when there
is a strict total order $<$ on $B$ that is invariant under left multiplication: for all
$a, b, c \in B$, if $b < c$ then $a b < a c$.

Formalized by `MathlibExt.GroupTheory.SkewBraceLeftOrderableKourovka19Problem49Wanted.LeftOrderableMul`, a definition declared in [WantedExt/GroupTheory/SkewBraceLeftOrderableKourovka19Problem49Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SkewBraceLeftOrderableKourovka19Problem49Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/left-orderable-skew-braces/index.html#left-orderable-mul).

## Left-orderable addition

The addition of a set $B$ is left-orderable when there is a strict
total order $<$ on $B$ that is invariant under left addition: for all $a, b, c \in B$, if $b < c$
then $a + b < a + c$.

Formalized by `MathlibExt.GroupTheory.SkewBraceLeftOrderableKourovka19Problem49Wanted.LeftOrderableAdd`, a definition declared in [WantedExt/GroupTheory/SkewBraceLeftOrderableKourovka19Problem49Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SkewBraceLeftOrderableKourovka19Problem49Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/left-orderable-skew-braces/index.html#left-orderable-add).

## Left-orderability of the additive group of a skew brace (Kourovka 19.49)

The statement
that for every skew brace $B$, that is, a set with two group structures, an addition $+$ (not
necessarily commutative) and a multiplication $\cdot$, satisfying
$a \cdot (b + c) = a \cdot b - a + a \cdot c$ for all $a, b, c \in B$: if the multiplication of
$B$ is left-orderable, then the addition of $B$ is left-orderable.

Formalized by `MathlibExt.GroupTheory.SkewBraceLeftOrderableKourovka19Problem49Wanted.skewBraceAdditiveLeftOrderable`, a definition declared in [WantedExt/GroupTheory/SkewBraceLeftOrderableKourovka19Problem49Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SkewBraceLeftOrderableKourovka19Problem49Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/left-orderable-skew-braces/index.html#skew-brace-additive-left-orderable).

## A skew brace whose additive group is not left-orderable

There is a skew brace $B$, that is, a
set with two group structures, an addition $+$ and a multiplication $\cdot$, satisfying
$a \cdot (b + c) = a \cdot b - a + a \cdot c$ for all $a, b, c \in B$, whose multiplication is
left-orderable but whose addition is not left-orderable. That is, the statement of Kourovka
Problem 19.49 fails.

Nasybullov's example (Example 3.1) is $\mathbb{Z}$ with addition $a \oplus b = a + (-1)^a b$ and
multiplication $a \odot b = a + b$: the multiplicative group is infinite cyclic, hence
left-orderable, while the additive group is infinite dihedral and has an element of order $2$, so
it is not left-orderable. The Kourovka Archive answers 19.49 "No, not always".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.49 (V. Lebed, L. Vendramin); resolution: T. Nasybullov, Connections between properties of the additive and the multiplicative groups of a two-sided skew brace, J. Algebra 540 (2019), 156-167 (arXiv:1809.09418), Example 3.1: on ℤ, a ⊕ b = a + (−1)^a b and a ⊙ b = a + b define a skew brace with infinite cyclic multiplicative group and infinite dihedral additive group, which has 2-torsion and so is not left-orderable, answering Problem 19.49; Kourovka Archive, Problem 19.49: No, not always, https://arxiv.org/abs/1809.09418.

Stated but not proved: `MathlibExt.GroupTheory.SkewBraceLeftOrderableKourovka19Problem49Wanted.skewBraceAdditiveLeftOrderable_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SkewBraceLeftOrderableKourovka19Problem49Wanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SkewBraceLeftOrderableKourovka19Problem49Wanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/left-orderable-skew-braces/index.html#skew-brace-additive-left-orderable-refut).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Left-orderable skew braces](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/left-orderable-skew-braces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orderable-groups/left-orderable-skew-braces)
