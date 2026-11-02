---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Field.exists_primitive_element
mathlib_file: Mathlib/FieldTheory/PrimitiveElement.lean
---

# Primitive element theorem

**Primitive element theorem**: a finite separable field extension `E` of `F` has a
primitive element, i.e. there is an `α ∈ E` such that `F⟮α⟯ = (⊤ : Subalgebra F E)`.

```lean
Field.exists_primitive_element.{u_1, u_2} (F : Type u_1) (E : Type u_2) [Field F] [Field E]
  [Algebra F E] [FiniteDimensional F E] [Algebra.IsSeparable F E] : ∃ α, F⟮α⟯ = ⊤
```

## Depends on

- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Minimal polynomial](../../../overview/linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Separable polynomial](../../../overview/general-algebra/polynomials-and-power-series/separable-polynomial.md)
- [Subfield](../../../overview/general-algebra/field-theory/subfield.md)

## Proof depends on

- [$A\[X\]$ has gcd and lcm if $A$ does](../../../overview/general-algebra/polynomials-and-power-series/a-x-has-gcd-and-lcm-if-a-does.md)
- [$K\[X\]$ is Euclidean](../../../overview/general-algebra/polynomials-and-power-series/k-x-is-euclidean.md)
- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in.md)
- [Cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md)
- [Euler's totient function ($\varphi$)](../../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function.md)
- [Field of fractions of an integral domain](../../../overview/general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)
- [Greatest Common Divisor Algorithm](../../../hundred-theorems/part-04/greatest-common-divisor-algorithm.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Localization](../../../overview/general-algebra/rings/localization.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Quotient group](../../../overview/general-algebra/group-theory/part-01/quotient-group.md)
- [Quotient space](../../../undergraduate/group-theory/basic-definitions/quotient-space.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Roots of a polynomial](../../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Splitting field](../../../overview/general-algebra/field-theory/splitting-field.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Field.exists_primitive_element`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/PrimitiveElement.html#Field.exists_primitive_element)
- [Source of `Field.exists_primitive_element` in Mathlib/FieldTheory/PrimitiveElement.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/PrimitiveElement.lean#L206)
- [1000+ theorems list: Q2093886](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2007)
- [1000+ theorems project: Q2093886](https://1000-plus.github.io/?length=-1#Q2093886)
- [Wikipedia: Primitive element theorem](https://en.wikipedia.org/wiki/Primitive_element_theorem)
- [Wikidata: Q2093886](https://www.wikidata.org/wiki/Q2093886)
