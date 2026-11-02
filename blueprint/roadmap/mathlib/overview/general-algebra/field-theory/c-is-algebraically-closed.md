---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.exists_root
mathlib_file: Mathlib/Analysis/Complex/Polynomial/Basic.lean
---

# $\C$ is algebraically closed

**Fundamental theorem of algebra**: every nonconstant complex polynomial
has a root.

```lean
Complex.exists_root {f : Polynomial ℂ} (hf : 0 < f.degree) : ∃ z, f.IsRoot z
```

## Depends on

- [Complex number](../numbers/complex-number.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)

## Proof depends on

- [Characteristic zero](characteristic-zero.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Differentiable functions](../../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Sources

- [Mathlib documentation: `Complex.exists_root`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/Basic.html#Complex.exists_root)
- [Source of `Complex.exists_root` in Mathlib/Analysis/Complex/Polynomial/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/Polynomial/Basic.lean#L35)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L128)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L180)
- [Freek Wiedijk's 100 theorems, no. 2](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L12)
