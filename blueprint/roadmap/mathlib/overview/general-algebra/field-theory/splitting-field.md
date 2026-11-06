---
article_id: af_da76bb334cf24625cba4ead2
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Polynomial.SplittingField
mathlib_file: Mathlib/FieldTheory/SplittingField/Construction.lean
---

# Splitting field

A **splitting field** of a [polynomial](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) $f$ over a [field](field.md) $K$ is a field extension of $K$ in which $f$ factors completely into linear factors and which is generated over $K$ by the roots of $f$. Every polynomial has one, and any two are isomorphic over $K$, so one may speak of "the" splitting field. Splitting fields are the extensions in which the [roots](../polynomials-and-power-series/roots-of-a-polynomial.md) of a polynomial can all be handled at once, which makes them the basic objects of Galois theory: the finite normal extensions are exactly the splitting fields, and the Galois group of a polynomial is the group of automorphisms of its splitting field over $K$.

## Definition

Let $L$ be a field extension of $K$. A polynomial $f \in K[X]$ *splits* over $L$ if, viewed in $L[X]$, it is a constant times a product of linear factors; equivalently,
[$f$ equals its leading coefficient times a product of factors $X - a_i$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Splits.html#Polynomial.splits_iff_exists_multiset), and also equivalently, for nonzero $f$,
[the number of roots of $f$ in $L$, counted with multiplicity, equals its degree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Splits.html#Polynomial.splits_iff_card_roots). Separately, the zero polynomial counts as split over every field.

The extension $L$ is a [splitting field of $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/IsSplittingField.html#Polynomial.IsSplittingField) if $f$ splits over $L$ and $L$ is generated over $K$ by the roots of $f$. If $f$ has roots $a_1, \dots, a_n$ in $L$, the second condition says $L = K(a_1, \dots, a_n)$; no proper subfield of $L$ containing $K$ is a field over which $f$ splits. Starting from any extension $M$ over which $f$ splits, the
[subfield of $M$ generated over $K$ by the roots of $f$ is a splitting field of $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/IsSplittingField.html#IntermediateField.adjoin_rootSet_isSplittingField).

## Existence

[A splitting field of $f$ can always be constructed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/Construction.html#Polynomial.SplittingField), by induction on the degree. If $f$ has positive degree, choose an [irreducible](../divisibility-in-integral-domains/irreducible-element.md) factor $g$ of $f$ and pass to the [rupture field](rupture-field.md) $K[X]/(g)$, in which the class of $X$ is a root of $g$ and hence of $f$. Over this larger field, $f$ has a linear factor; dividing it out leaves a polynomial of smaller degree, to which the induction applies. After at most $\deg f$ steps one reaches an extension over which $f$ splits, and
[the field built this way is a splitting field of $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/Construction.html#Polynomial.IsSplittingField.splittingField). Since each step has degree at most the current degree of the polynomial, a splitting field of a polynomial of degree $n \ge 1$ has degree at most $n!$ over $K$.

## Examples

- Over $\mathbb{Q}$, the polynomial $X^2 - 2$ has splitting field $\mathbb{Q}(\sqrt 2)$, of degree $2$. Over $\mathbb{R}$, the polynomial $X^2 + 1$ has splitting field $\mathbb{C}$.
- The roots of $X^3 - 2$ over $\mathbb{Q}$ are $\sqrt[3]{2}$, $\omega\sqrt[3]{2}$ and $\omega^2\sqrt[3]{2}$, where $\omega$ is a primitive cube root of unity. The splitting field is $\mathbb{Q}(\sqrt[3]{2}, \omega)$, of degree $6 = 3!$, so the bound above can be attained. The field $\mathbb{Q}(\sqrt[3]{2})$, of degree $3$, contains one root but is not a splitting field, since it lies inside $\mathbb{R}$ and the other two roots do not.
- Let $n \ge 1$. If an extension $L$ of $K$ contains a primitive $n$-th root of unity $\zeta$ and $L = K(\zeta)$ (equivalently, $L$ is generated over $K$ by the $n$-th roots of unity, which is how Mathlib phrases the hypothesis), then
  [$L$ is a splitting field of $X^n - 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Cyclotomic/Basic.html#IsCyclotomicExtension.isSplittingField_X_pow_sub_one), since the roots of $X^n - 1$ are the powers of $\zeta$.
- If $K$ is a finite field with $q$ elements and $F$ is a subfield of $K$, then
  [$K$ is a splitting field of $X^q - X$ over $F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/GaloisField.html#FiniteField.isSplittingField_sub), because every element of $K$ is a root of this polynomial and it has no other roots.

## Properties

- **Uniqueness.** If $L$ is any splitting field of $f$ over $K$, then
  [$L$ is isomorphic over $K$ to the constructed splitting field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/Construction.html#Polynomial.IsSplittingField.algEquiv). The isomorphism is not unique in general: two such isomorphisms differ by an automorphism of $L$ over $K$, and these automorphisms form the Galois group of $f$.
- **Universal property.** If $f$ splits over a field extension $M$ of $K$, then a splitting field $L$ of $f$
  [embeds into $M$ by a homomorphism that is the identity on $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/IsSplittingField.html#Polynomial.IsSplittingField.lift).
- **Finiteness.** A splitting field
  [is a finite-dimensional extension of $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/IsSplittingField.html#Polynomial.IsSplittingField.finiteDimensional), and hence an [algebraic extension](algebraic-extension.md).
- **Normality.** A splitting field of a polynomial
  [is a normal extension of $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Normal/Basic.html#Normal.of_isSplittingField): every irreducible polynomial over $K$ with one root in $L$ splits over $L$. Conversely, a
  [finite normal extension is a splitting field of some polynomial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Normal/Basic.html#Normal.exists_isSplittingField).
- **Galois extensions.** The splitting field of a [separable polynomial](../polynomials-and-power-series/separable-polynomial.md)
  [is a Galois extension of $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.of_separable_splitting_field), and conversely
  [every finite Galois extension is a splitting field of a separable polynomial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.is_separable_splitting_field). The [Galois correspondence](galois-correspondence.md) then applies to such splitting fields.

## Finite fields

For a prime $p$ and a positive integer $n$, the splitting field of $X^{p^n} - X$ over $\mathbb{Z}/p\mathbb{Z}$ is a [finite field](../../../undergraduate/ring-theory/field-theory/finite-fields.md) that
[has exactly $p^n$ elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/GaloisField.html#GaloisField.card): the polynomial has derivative $-1$, so its $p^n$ roots are distinct, and they already form a field. Conversely, a field $K$ with $p^n$ elements, regarded as an algebra over $\mathbb{Z}/p\mathbb{Z}$ (as every field of characteristic $p$ is), is
[a splitting field of $X^{p^n} - X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/GaloisField.html#FiniteField.isSplittingField_of_nat_card_eq), so by uniqueness
[it is isomorphic to the splitting field constructed above](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/GaloisField.html#GaloisField.algEquivGaloisField). Hence any two fields with $p^n$ elements are isomorphic.

## Related concepts

An [algebraic closure](existence-of-algebraic-closure-of-a-field.md) of $K$ is an [algebraically closed](algebraically-closed-field.md) algebraic extension; it plays the role of a splitting field for all polynomials over $K$ at once, and contains a copy of the splitting field of each one. The [rupture field](rupture-field.md) of an irreducible polynomial adjoins only one root and is in general smaller than the splitting field. The [primitive element theorem](../../../thousand-plus/algebra/12-field-theory-and-polynomials/primitive-element-theorem.md) shows that the splitting field of a separable polynomial is generated by a single element.

## In Mathlib

Mathlib separates the property from the construction. Being a splitting field is a predicate on a field extension $L$ of $K$: the polynomial splits over $L$, and $L$ is generated by the roots as a $K$-algebra, which is the same as being generated as a field because the roots are algebraic; an
[equivalent form uses the subfield generated by the roots](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/IsSplittingField.html#isSplittingField_iff_intermediateField). Splitting is defined for polynomials over any semiring, as being a product of constants and monic linear polynomials, so the zero polynomial splits and its splitting field is $K$ itself. The construction is a specific field, built by repeatedly adjoining a root of an irreducible factor and then rewritten as a quotient of a multivariate polynomial ring over $K$, so that it carries well-behaved algebraic structure. Results are mostly stated for an arbitrary field satisfying the predicate, and the constructed field supplies existence. The field with $p^n$ elements is defined in this way, as the constructed splitting field of $X^{p^n} - X$ over $\mathbb{Z}/p\mathbb{Z}$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Field](field.md)
- [Polynomial in one indeterminate](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Roots of a polynomial](../polynomials-and-power-series/roots-of-a-polynomial.md)

## Proof depends on

- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)
- [Rupture field](rupture-field.md)

## Sources

- [Mathlib documentation: `Polynomial.SplittingField`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/SplittingField/Construction.html#Polynomial.SplittingField)
- [Source of `Polynomial.SplittingField` in Mathlib/FieldTheory/SplittingField/Construction.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/SplittingField/Construction.lean#L211)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L132)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L187)
