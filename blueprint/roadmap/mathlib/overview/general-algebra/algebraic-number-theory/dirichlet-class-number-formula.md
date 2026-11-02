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
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Determinant](../../linear-algebra/matrices/determinant.md)
- [Finiteness of the class number](finiteness-of-the-class-number.md)
- [Lebesgue measure (Measures and integral calculus)](../../analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Periodic points](../../dynamics/general-theory/periodic-points.md)
- [Product of sigma-algebras](../../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)
- [Self-adjoint operator](../../analysis/hilbert-spaces/self-adjoint-operator.md)

## Proof depends on

- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)

## Sources

- [Mathlib documentation: `NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/DedekindZeta.html#NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT)
- [Source of `NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT` in Mathlib/NumberTheory/NumberField/DedekindZeta.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/NumberField/DedekindZeta.lean#L75)
- [Mathlib overview: General algebra › Algebraic Number Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L159)
