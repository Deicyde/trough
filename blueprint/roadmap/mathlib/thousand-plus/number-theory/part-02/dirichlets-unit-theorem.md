---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: NumberField.Units.basisModTorsion, NumberField.Units.exist_unique_eq_mul_prod
mathlib_file: Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean
---

# Dirichlet's unit theorem

Mathlib records this with 2 declarations.

`NumberField.Units.basisModTorsion`: A basis of the quotient `(𝓞 K)ˣ ⧸ (torsion K)` seen as an additive ℤ-module.

```lean
NumberField.Units.basisModTorsion.{u_1} (K : Type u_1) [Field K] [NumberField K] :
  Module.Basis (Fin (NumberField.Units.rank K)) ℤ
    (Additive ((NumberField.RingOfIntegers K)ˣ ⧸ NumberField.Units.torsion K))
```

`NumberField.Units.exist_unique_eq_mul_prod`: **Dirichlet Unit Theorem**. Any unit `x` of `𝓞 K` can be written uniquely as the product of
a root of unity and powers of the units of the fundamental system `fundSystem`.

```lean
NumberField.Units.exist_unique_eq_mul_prod.{u_1} (K : Type u_1) [Field K] [NumberField K]
  (x : (NumberField.RingOfIntegers K)ˣ) :
  ∃! ζe, x = ↑ζe.1 * ∏ i, NumberField.Units.fundSystem K i ^ ζe.2 i
```

## Depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Euclidean domain](../../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Minimal polynomial](../../../overview/linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Periodic points](../../../overview/dynamics/general-theory/periodic-points.md)
- [Quotient group](../../../overview/general-algebra/group-theory/part-01/quotient-group.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)
- [Roots of a polynomial](../../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [Subring](../../../overview/general-algebra/rings/subring.md)

## Proof depends on

- [Aleph numbers](../../../overview/logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Ball](../../../overview/topology/metric-spaces/ball.md)
- [Cayley-Hamilton theorem](../../../overview/linear-algebra/endomorphism-polynomials/cayley-hamilton-theorem.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Fundamental sequences](../../../overview/logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Hilbert basis theorem](../../../overview/general-algebra/polynomials-and-power-series/hilbert-basis-theorem.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Isomorphism with $K^n$](../../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Polynomial in several indeterminates](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Well-ordering theorem](../../general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `NumberField.Units.basisModTorsion`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.basisModTorsion)
- [Source of `NumberField.Units.basisModTorsion` in Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean#L465)
- [Mathlib documentation: `NumberField.Units.exist_unique_eq_mul_prod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.exist_unique_eq_mul_prod)
- [Source of `NumberField.Units.exist_unique_eq_mul_prod` in Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean#L504)
- [1000+ theorems list: Q1227702](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1547)
- [1000+ theorems project: Q1227702](https://1000-plus.github.io/?length=-1#Q1227702)
- [Wikipedia: Dirichlet's unit theorem](https://en.wikipedia.org/wiki/Dirichlet's_unit_theorem)
- [Wikidata: Q1227702](https://www.wikidata.org/wiki/Q1227702)
