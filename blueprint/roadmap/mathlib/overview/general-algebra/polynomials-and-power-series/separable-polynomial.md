---
article_id: af_3b9bf4ffe681f50a269fc85f
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Polynomial.Separable
mathlib_file: Mathlib/FieldTheory/Separable.lean
---

# Separable polynomial

A **separable polynomial** over a [field](../field-theory/field.md) is a nonzero [polynomial](polynomial-in-one-indeterminate.md) without
repeated roots: in any field over which it factors into linear factors, its roots are pairwise
distinct. Separability can be decided inside the base field, without finding a single root, by
checking that the polynomial and its [formal derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md) have no common
factor of positive degree. The notion is basic to field theory: separable extensions, built from roots of separable
polynomials, are the setting of the [primitive element theorem](../../../thousand-plus/algebra/12-field-theory-and-polynomials/primitive-element-theorem.md)
and of Galois theory. In [characteristic zero](../field-theory/characteristic-zero.md) every irreducible polynomial is
separable, so the subtleties live in [characteristic $p$](../field-theory/characteristic-p.md).

## Definition

Let $R$ be a commutative ring, $f \in R[X]$, and $f'$ its formal derivative. The polynomial $f$ is
[separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.Separable) when $f$ and $f'$ are [coprime](../divisibility-in-integral-domains/coprime-element.md) in the sense
of Bézout: [$f$ is separable exactly when there are polynomials $a, b \in R[X]$ with $af + bf' = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.separable_def').

Over a field $F$ the ring $F[X]$ is a Euclidean domain, so the condition says that $f$ and $f'$ have
no common factor of positive degree, which the Euclidean algorithm decides. The connection with
[roots](roots-of-a-polynomial.md) is the following:
[if a nonzero polynomial $f$ over $F$ splits into linear factors over an extension field $K$, then $f$ is separable if and only if its roots in $K$ are pairwise distinct](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.nodup_aroots_iff_of_splits),
that is, each root has [multiplicity](multiplicity.md) one. Taking $K$ to be a
[splitting field](../field-theory/splitting-field.md) of $f$ gives the definition by roots. The reason
is the product rule: if $(X - \alpha)^2$ divides $f$, then $X - \alpha$ divides $f'$; conversely, if
$f = (X - \alpha)g$ and $f'(\alpha) = 0$, then $g(\alpha) = 0$, so $\alpha$ is a repeated root. Since $f$ splits over $K$, any common factor of
positive degree of $f$ and $f'$ has a root in $K$, which is then a common root of $f$ and $f'$.

For an [irreducible](../divisibility-in-integral-domains/irreducible-element.md) polynomial the test is simpler, since the only candidate for a
common factor of $f$ and $f'$ is $f$ itself, up to a nonzero constant factor, which can divide $f'$ only if $f' = 0$, because
$f'$ has smaller degree than $f$:
[an irreducible polynomial $f$ over a field is separable if and only if $f' \neq 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.separable_iff_derivative_ne_zero).

## Examples

- **Linear and constant polynomials.** Over a commutative ring,
  [$X - c$ is separable for every $c$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.separable_X_sub_C), its derivative being $1$.
  [A constant polynomial $c$ is separable if and only if $c$ is a unit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.separable_C),
  so over any ring other than the zero ring
  [the zero polynomial is not separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.not_separable_zero).
- **A repeated factor.** The polynomial $(X - 1)^2 = X^2 - 2X + 1$ has derivative $2(X - 1)$, and the
  two share the factor $X - 1$. In general
  [a separable polynomial is squarefree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.Separable.squarefree): if $g^2$ divides it,
  then $g$ is a unit.
- **Binomials.** Over a field $F$,
  [$X^n - a$ is separable whenever $a \neq 0$ and the natural number $n$ is nonzero in $F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.separable_X_pow_sub_C),
  and [$X^n - 1$ is separable if and only if $n$ is nonzero in $F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.X_pow_sub_one_separable_iff).
  Over the complex numbers, for $n \ge 1$, $X^n - 1$ has $n$ distinct roots, the $n$th roots of unity; over a field of characteristic
  $p$, the polynomial $X^p - 1$ equals $(X - 1)^p$.
- **Finite fields.** Over a commutative ring of characteristic $p$,
  [$X^q - X$ is separable whenever $p$ divides $q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/GaloisField.html#galois_poly_separable), since its derivative
  is $qX^{q-1} - 1 = -1$. When $p$ is prime and $q = p^n$ with $n \ge 1$, the roots of this polynomial in
  a splitting field over $\mathbb{F}_p$ form the field with $q$ elements (see [finite fields](../../../undergraduate/ring-theory/field-theory/part-01/finite-fields.md)).
- **An inseparable irreducible polynomial.** Let $F = \mathbb{F}_p(t)$ be the field of rational
  functions over the field with $p$ elements, and $f = X^p - t$. It is irreducible in
  $\mathbb{F}_p[t][X]$ by [Eisenstein's criterion](eisensteins-criterion.md)
  at the prime $t$, hence over $\mathbb{F}_p(t)$ by Gauss's lemma, since $f$ is monic; but $f' = pX^{p-1} = 0$, so $f$ is not separable. If $s^p = t$ in a splitting field, then
  $X^p - t = (X - s)^p$, so $f$ has one root, of multiplicity $p$.
- **Dependence on the coefficient ring.** Over $\mathbb{Q}$, $X^2 + 1$ is separable, because
  $(X^2 + 1) - \tfrac{X}{2}\cdot 2X = 1$. Over $\mathbb{Z}$ it is not:
  [separability is preserved by every ring homomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.Separable.map), and modulo
  $2$ the polynomial becomes $(X + 1)^2$, which is not separable over $\mathbb{F}_2$.

## Properties

- **Base change over a field.** For a polynomial $f$ over a field $F$ and a
  [ring homomorphism](../rings/ring-morphism.md) $F \to S$ into a nonzero commutative ring,
  [the image of $f$ is separable if and only if $f$ is](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.separable_map). In
  particular, enlarging the field does not change whether $f$ is separable.
- **Roots.** Over an integral domain,
  [a separable polynomial has no repeated roots in that domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.nodup_roots). If a separable
  polynomial over $F$ splits over an extension field $K$, then
  [its number of distinct roots in $K$ equals its degree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.card_rootSet_eq_natDegree).
- **Factors.** [A divisor of a separable polynomial is separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.Separable.of_dvd),
  and [if $fg$ is separable then $f$ and $g$ are coprime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.Separable.isCoprime).
  Conversely, over a commutative ring,
  [the product of two coprime separable polynomials is separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.Separable.mul).
- **Characteristic zero.** A nonconstant polynomial has nonzero derivative in characteristic zero,
  so [every irreducible polynomial over a field of characteristic zero is separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Irreducible.separable).
- **Characteristic $p$.** Here $f' = 0$ exactly when $f$ is a polynomial in $X^p$. Over a field of
  characteristic $p > 0$,
  [every irreducible $f$ can be written as $f(X) = g(X^{p^n})$ with $n \ge 0$ and $g$ separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.exists_separable_of_irreducible),
  and [$n$ and $g$ are uniquely determined by $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.unique_separable_of_irreducible).

## Related concepts

- **Separable elements and extensions.** For an algebra over $F$,
  [an element is separable when its minimal polynomial over $F$ is separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#IsSeparable)
  (see [minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md)), and
  [the algebra is separable over $F$ when all of its elements are](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Algebra.IsSeparable). By the
  primitive element theorem,
  [every finite separable field extension is generated by a single element](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/PrimitiveElement.html#Field.exists_primitive_element).
  Galois extensions are the separable normal ones, the setting of the
  [Galois correspondence](../field-theory/galois-correspondence.md).
- **Perfect fields.** [A field is perfect when every irreducible polynomial over it is separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#PerfectField);
  in characteristic $p$ this amounts to surjectivity of the [Frobenius](../field-theory/frobenius-morphism.md) map.
  [Every field of characteristic zero is perfect](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#PerfectField.ofCharZero), as is
  [every finite field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#PerfectField.ofFinite), while $\mathbb{F}_p(t)$ is not, by the example
  above. [Over a perfect field a polynomial is separable if and only if it is squarefree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#PerfectField.separable_iff_squarefree),
  and [every algebraic extension of a perfect field is separable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#Algebra.IsAlgebraic.isSeparable_of_perfectField).
  See also [perfect closure](../field-theory/perfect-closure.md).

## In Mathlib

Mathlib defines separability for polynomials over any commutative semiring, directly as Bézout
coprimality of the polynomial and its formal derivative; roots play no part in the definition, and
the description by distinct roots over a field is a theorem. The definition fixes the edge cases:
the zero polynomial is not separable over a nonzero ring, nonzero constants over a field are
separable because they are units, and over the zero ring every polynomial is separable. It is the
strict notion, under which a polynomial with a repeated irreducible factor, such as $(X - 1)^2$, is
not separable; some texts instead call a polynomial separable when each of its irreducible factors
has distinct roots, and under that convention $(X - 1)^2$ would count as separable. Separable
elements are defined for algebras over a commutative ring through the minimal polynomial. Since
Mathlib gives a non-integral element the minimal polynomial $0$,
[a separable element is automatically integral](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#IsSeparable.isIntegral), and separable
extensions are algebraic.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)
- [Polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Coprime element](../divisibility-in-integral-domains/coprime-element.md)
- [Roots of a polynomial](roots-of-a-polynomial.md)

## Sources

- [Mathlib documentation: `Polynomial.Separable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.Separable)
- [Source of `Polynomial.Separable` in Mathlib/FieldTheory/Separable.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/Separable.lean#L41)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L99)
