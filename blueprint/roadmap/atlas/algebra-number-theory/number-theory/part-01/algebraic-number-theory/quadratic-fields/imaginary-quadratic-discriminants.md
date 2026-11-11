---
declaration: section
origin: cited
lean: ImaginaryQuadraticDiscriminant.IsImaginaryQuadraticDiscriminant, ImaginaryQuadraticDiscriminant.IsFundamentalImaginaryQuadraticDiscriminant, ImaginaryQuadraticDiscriminant.imaginaryQuadraticDiscriminants, ImaginaryQuadraticDiscriminant.fundamentalImaginaryQuadraticDiscriminants, ImaginaryQuadraticDiscriminant.ImaginaryQuadraticDiscriminantDecomposition, ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_iff, ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_mk, ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_neg
statement: formalized
proof: formalized
---

# Imaginary quadratic discriminants

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html).

## Imaginary Quadratic Discriminant

## Imaginary quadratic discriminant

An integer $D$ is an imaginary quadratic discriminant
if $D < 0$ and either $D \equiv 0 \pmod 4$ or $D \equiv 1 \pmod 4$.

Formalized by `ImaginaryQuadraticDiscriminant.IsImaginaryQuadraticDiscriminant`, a definition declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-imaginary-quadratic-discriminant).

## Fundamental imaginary quadratic discriminant

An integer $D$ is a fundamental imaginary
quadratic discriminant if $D < 0$ and $D$ is a fundamental discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.IsFundamentalImaginaryQuadraticDiscriminant`, a definition declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-fundamental-imaginary-quadratic-discr).

## Imaginary quadratic discriminants

The set of imaginary quadratic discriminants is the set
of integers $D$ such that $D < 0$ and $D$ is congruent to $0$ or $1$ modulo $4$.

Formalized by `ImaginaryQuadraticDiscriminant.imaginaryQuadraticDiscriminants`, a definition declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#imaginary-quadratic-discriminants).

## Fundamental imaginary quadratic discriminants

The set of fundamental imaginary quadratic
discriminants is the set of integers $D$ with $D < 0$ that are fundamental discriminants.

Formalized by `ImaginaryQuadraticDiscriminant.fundamentalImaginaryQuadraticDiscriminants`, a definition declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#fundamental-imaginary-quadratic-discrimi).

## Conductor decomposition of an imaginary quadratic discriminant

For an integer $D$, a
decomposition of $D$ consists of integers $u$ and $D_K$ such that $u \ge 1$, $D_K$ is a
fundamental imaginary quadratic discriminant, and $D = u^2 D_K$. The integer $u$ is called the
conductor.

Formalized by `ImaginaryQuadraticDiscriminant.ImaginaryQuadraticDiscriminantDecomposition`, a structure declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#imaginary-quadratic-discriminant-decompo).

## Characterization of imaginary quadratic discriminants

An integer $D$ is an imaginary
quadratic discriminant if and only if $D < 0$ and $D$ is congruent to $0$ or $1$ modulo $4$.

Formalized by `ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_iff`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-imaginary-quadratic-discriminant-iff).

## Criterion for an imaginary quadratic discriminant

If an integer $D$ satisfies $D < 0$
and either $D \equiv 0 \pmod 4$ or $D \equiv 1 \pmod 4$, then $D$ is an imaginary quadratic
discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_mk`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-imaginary-quadratic-discriminant-mk).

## Imaginary quadratic discriminants are negative

Every imaginary quadratic discriminant
$D$ satisfies $D < 0$.

Formalized by `ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_neg`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-imaginary-quadratic-discriminant-neg).

## Imaginary quadratic discriminants are congruent to 0 or 1 mod 4

Every imaginary
quadratic discriminant $D$ satisfies $D \equiv 0 \pmod 4$ or $D \equiv 1 \pmod 4$.

Formalized by `ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_mod`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-imaginary-quadratic-discriminant-mod).

## Negative multiples of 4 are imaginary quadratic discriminants

If an integer $D$
satisfies $D < 0$ and $D \equiv 0 \pmod 4$, then $D$ is an imaginary quadratic
discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_of_mod_zero`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-imaginary-quadratic-discriminant-of-m).

## Negative integers congruent to 1 mod 4 are imaginary quadratic discriminants

If an
integer $D$ satisfies $D < 0$ and $D \equiv 1 \pmod 4$, then $D$ is an imaginary quadratic
discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.isImaginaryQuadraticDiscriminant_of_mod_one`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-imaginary-quadratic-discriminant-of-m-2).

## Characterization of fundamental imaginary quadratic discriminants

An integer $D$ is a
fundamental imaginary quadratic discriminant if and only if $D < 0$ and $D$ is a fundamental
discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.isFundamentalImaginaryQuadraticDiscriminant_iff`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-fundamental-imaginary-quadratic-discr-2).

## Negative fundamental discriminants are fundamental imaginary quadratic discriminants

If
an integer $D$ satisfies $D < 0$ and is a fundamental discriminant, then $D$ is a fundamental
imaginary quadratic discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.isFundamentalImaginaryQuadraticDiscriminant_mk`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-fundamental-imaginary-quadratic-discr-3).

## Fundamental imaginary quadratic discriminants are fundamental discriminants

Every
fundamental imaginary quadratic discriminant $D$ is a fundamental discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.isFundamentalImaginaryQuadraticDiscriminant_isFundamentalDiscriminant`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-fundamental-imaginary-quadratic-discr-4).

## Fundamental imaginary quadratic discriminants are imaginary quadratic discriminants

Every fundamental imaginary quadratic discriminant is an imaginary quadratic discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.isFundamentalImaginaryQuadraticDiscriminant_isImaginary`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-fundamental-imaginary-quadratic-discr-5).

## The fundamental part of a conductor decomposition

For every conductor decomposition of
an integer $D$, consisting of an integer $u \ge 1$ and a fundamental imaginary quadratic
discriminant $D_K$ with $D = u^2 D_K$, the integer $D_K$ is a fundamental imaginary quadratic
discriminant.

Formalized by `ImaginaryQuadraticDiscriminant.ImaginaryQuadraticDiscriminantDecomposition.isFundamental`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#is-fundamental).

## The conductor of a discriminant decomposition is at least one

For every decomposition of
an integer $D$ into a conductor $u$ and a fundamental imaginary quadratic discriminant $D_K$,
we have $u \ge 1$.

Formalized by `ImaginaryQuadraticDiscriminant.ImaginaryQuadraticDiscriminantDecomposition.u_ge_one`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#u-ge-one).

## The equation of a discriminant decomposition

For every decomposition of an integer $D$
into a conductor $u$ and a fundamental imaginary quadratic discriminant $D_K$, we have
$D = u^2 D_K$.

Formalized by `ImaginaryQuadraticDiscriminant.ImaginaryQuadraticDiscriminantDecomposition.prop_eq`, a theorem declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#prop-eq).

## Decomposition from a conductor and a fundamental discriminant

Let $D$ be an integer. If
$u \ge 1$ is an integer, $D_K$ is a fundamental imaginary quadratic discriminant and
$D = u^2 D_K$, then $u$ and $D_K$ form a decomposition of $D$ into the conductor $u$ and the
fundamental imaginary quadratic discriminant $D_K$.

Formalized by `ImaginaryQuadraticDiscriminant.ImaginaryQuadraticDiscriminantDecomposition.ofFundamental`, a definition declared in [MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ImaginaryQuadraticDiscriminant.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html#of-fundamental).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Imaginary quadratic discriminants](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/imaginary-quadratic-discriminants)
