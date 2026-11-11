---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.shift, MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.Lamplighter, MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.IsNonZeroDivisor, MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.IsOreRing, MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lamplighterGroupAlgebraOre, MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lamplighterGroupAlgebraOre_refuted
statement: formalized
---

# Ore condition for group algebras

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras/index.html).

## Shift of the lamplighter base group

For a natural number $p$, the shift is the
automorphism $f \mapsto f(\cdot - 1)$ of the base group $\bigoplus_{i \in \mathbb{Z}} \mathbb{Z}/p$,
the additive group of finitely supported functions $\mathbb{Z} \to \mathbb{Z}/p$, viewed as a
multiplicative group.

Formalized by `MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.shift`, a definition declared in [WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras/index.html#shift).

## Lamplighter group

For a natural number $p$, the lamplighter group
$\mathbb{Z}/p \wr \mathbb{Z}$ is the semidirect product
$\left(\bigoplus_{i \in \mathbb{Z}} \mathbb{Z}/p\right) \rtimes \mathbb{Z}$, in which
$n \in \mathbb{Z}$ acts on the base group by the $n$-th power of the shift
$f \mapsto f(\cdot - 1)$.

Formalized by `MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.Lamplighter`, an abbreviation declared in [WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras/index.html#lamplighter).

## Non-zero-divisor

An element $s$ of a ring $R$ is a non-zero-divisor when it is neither a
left nor a right zero divisor: for every $z \in R$, $zs = 0$ implies $z = 0$ and $sz = 0$ implies
$z = 0$.

Formalized by `MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.IsNonZeroDivisor`, a definition declared in [WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras/index.html#is-non-zero-divisor).

## Right Ore ring

A ring $R$ satisfies the right Ore condition for its non-zero-divisors, so
that it has a classical right ring of quotients, when for all $s, t \in R$ with $s$ a
non-zero-divisor there are $x, y \in R$ with $x$ a non-zero-divisor and $sy = tx$.

For group algebras the left and right conditions agree.

Formalized by `MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.IsOreRing`, a definition declared in [WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras/index.html#is-ore-ring).

## Kourovka Problem 12.47: some lamplighter group algebra is Ore

There are a field $k$ and a
prime $p$ such that the group algebra $k[\mathbb{Z}/p \wr \mathbb{Z}]$ of the lamplighter group
$\mathbb{Z}/p \wr \mathbb{Z}$ satisfies the right Ore condition for its non-zero-divisors, that
is, has a classical right ring of quotients.

Kourovka 12.47 (P. A. Linnell) asks this for a given field and prime; the existential form makes
its refutation cover every field and every prime.

Formalized by `MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lamplighterGroupAlgebraOre`, a definition declared in [WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras/index.html#lamplighter-group-algebra-ore).

## Lamplighter group algebras are not Ore

For every field $k$ and every prime $p$, the group
algebra $k[\mathbb{Z}/p \wr \mathbb{Z}]$ of the lamplighter group $\mathbb{Z}/p \wr \mathbb{Z}$
does not satisfy the right Ore condition for its non-zero-divisors: there are $s$ and $t$ in it,
with $s$ a non-zero-divisor, such that $sy = tx$ holds for no $x$ and $y$ with $x$ a
non-zero-divisor.

Resolved false: Linnell, Lück and Schick (Theorem 3, with W. Dicks's argument) prove that $kG$ is
not an Ore ring for every field $k$ and every group $G$ containing $H \wr \mathbb{Z}$ with
$H \ne 1$ finite, in particular for $G = \mathbb{Z}/p \wr \mathbb{Z}$ and every prime $p$; the
Kourovka Archive answers 12.47 "No, it does not".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.47 (P. A. Linnell); resolution: P. A. Linnell, W. Lück and T. Schick, The Ore condition, affiliated operators, and the lamplighter group, in: High-dimensional manifold topology (Trieste, 2001), World Scientific, 2003, 315-321, Theorem 3: kG is not an Ore ring for every field k and every group G containing H ≀ ℤ with H ≠ 1 finite; Kourovka Archive, Problem 12.47, http://him-lueck.uni-bonn.de/data/lamplighter.pdf.

Stated but not proved: `MathlibExt.GroupTheory.LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lamplighterGroupAlgebraOre_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LamplighterGroupAlgebraOreKourovka12Problem47Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras/index.html#lamplighter-group-algebra-ore-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ore condition for group algebras](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/group-rings/ore-condition-for-group-algebras)
