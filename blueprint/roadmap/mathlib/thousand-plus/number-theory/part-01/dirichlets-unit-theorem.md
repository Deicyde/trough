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

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Orbit](../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Periodic points](../../../overview/dynamics/general-theory/periodic-points.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Proof depends on

- [Quotient group](../../../overview/general-algebra/group-theory/part-01/quotient-group.md)

## Sources

- [Mathlib documentation: `NumberField.Units.basisModTorsion`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.basisModTorsion)
- [Source of `NumberField.Units.basisModTorsion` in Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean#L465)
- [Mathlib documentation: `NumberField.Units.exist_unique_eq_mul_prod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.exist_unique_eq_mul_prod)
- [Source of `NumberField.Units.exist_unique_eq_mul_prod` in Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean#L504)
- [1000+ theorems list: Q1227702](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1547)
- [1000+ theorems project: Q1227702](https://1000-plus.github.io/all.html?length=-1#Q1227702)
- [Wikipedia: Dirichlet's unit theorem](https://en.wikipedia.org/wiki/Dirichlet's_unit_theorem)
- [Wikidata: Q1227702](https://www.wikidata.org/wiki/Q1227702)
