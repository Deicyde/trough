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
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Finite product of metric spaces](../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Finiteness of the class number](finiteness-of-the-class-number.md)
- [Lebesgue measure (Measures and integral calculus)](../../analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Periodic points](../../dynamics/general-theory/periodic-points.md)
- [Product of finitely many measures](../../analysis/measures-and-integral-calculus/part-02/product-of-finitely-many-measures.md)
- [Roots of a polynomial](../polynomials-and-power-series/roots-of-a-polynomial.md)
- [Self-adjoint operator](../../analysis/hilbert-spaces/self-adjoint-operator.md)

## Sources

- [Mathlib documentation: `NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/DedekindZeta.html#NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT)
- [Source of `NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT` in Mathlib/NumberTheory/NumberField/DedekindZeta.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/NumberField/DedekindZeta.lean#L75)
- [Mathlib overview: General algebra › Algebraic Number Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L159)
