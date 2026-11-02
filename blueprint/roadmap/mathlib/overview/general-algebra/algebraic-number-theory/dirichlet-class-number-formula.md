---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT
mathlib_file: Mathlib/NumberTheory/NumberField/DedekindZeta.lean
---

# Dirichlet class number formula

**Dirichlet class number formula**

```lean
NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT.{u_1} (K : Type u_1) [Field K] [NumberField K] :
  Filter.Tendsto (fun s => (↑s - 1) * NumberField.dedekindZeta K ↑s) (nhdsWithin 1 (Set.Ioi 1))
    (nhds ↑(NumberField.dedekindZeta_residue K))
```

## Depends on

- [Almost sure convergence](../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Determinant](../../linear-algebra/matrices/determinant.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Finite product of metric spaces](../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Finiteness of the class number](finiteness-of-the-class-number.md)
- [Lebesgue measure](../../analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Periodic points](../../dynamics/general-theory/periodic-points.md)
- [Product of finitely many measures](../../analysis/measures-and-integral-calculus/part-02/product-of-finitely-many-measures.md)
- [Roots of a polynomial](../polynomials-and-power-series/roots-of-a-polynomial.md)
- [Self-adjoint operator](../../analysis/hilbert-spaces/self-adjoint-operator.md)

## Proof depends on

- [Cauchy-Schwarz inequality](../../analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Change of variables to polar co-ordinates](../../../undergraduate/measures-and-integral-calculus/integration/change-of-variables-to-polar-co-ordinates.md)
- [Chinese remainder theorem](../ideals-and-quotients/chinese-remainder-theorem.md)
- [Class formula](../group-theory/part-01/class-formula.md)
- [Compactness in terms of open covers (Borel-Lebesgue)](../../topology/general-topology/part-01/compactness-in-terms-of-open-covers-borel-lebesg.md)
- [Connected components](../../../undergraduate/topology/topology-and-metric-spaces/connected-components.md)
- [Connectedness](../../topology/general-topology/part-01/connectedness.md)
- [Continuity of the sum of a series of functions](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Cramer’s Rule](../../../hundred-theorems/part-05/cramers-rule.md)
- [Derivative of the inverse of a function](../../analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Direct product of groups](../../../undergraduate/group-theory/basic-definitions/direct-product-of-groups.md)
- [Dirichlet's unit theorem](../../../thousand-plus/number-theory/part-02/dirichlets-unit-theorem.md)
- [Dominated convergence theorem](../../analysis/measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Existence of algebraic closure of a field](../field-theory/existence-of-algebraic-closure-of-a-field.md)
- [Fundamental theorem of algebra](../../analysis/complex-analysis/fundamental-theorem-of-algebra.md)
- [Gershgorin circle theorem](../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/gershgorin-circle-theorem.md)
- [Integral root theorem](../../../thousand-plus/algebra/12-field-theory-and-polynomials/integral-root-theorem.md)
- [Matrix representation](../../linear-algebra/bilinear-and-quadratic-forms/matrix-representation.md)
- [Minkowski’s Fundamental Theorem](../../../hundred-theorems/part-02/minkowskis-fundamental-theorem.md)
- [Path connectedness](../../../undergraduate/topology/topology-and-metric-spaces/path-connectedness.md)
- [Prime spectrum](../../geometry/algebraic-geometry/prime-spectrum.md)
- [Primitive element theorem](../../../thousand-plus/algebra/12-field-theory-and-polynomials/primitive-element-theorem.md)
- [Relationship between the coefficients and the roots of a split polynomial](../../../undergraduate/ring-theory/polynomial-rings/relationship-between-the-coefficients-and-the-ro.md)
- [Transcendental elements](../../../undergraduate/ring-theory/field-theory/part-01/transcendental-elements.md)
- [Transpose of a linear map](../../../undergraduate/linear-algebra/duality/transpose-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/DedekindZeta.html#NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT)
- [Source of `NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT` in Mathlib/NumberTheory/NumberField/DedekindZeta.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/NumberField/DedekindZeta.lean#L75)
- [Mathlib overview: General algebra › Algebraic Number Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L159)
