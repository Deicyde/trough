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

- [Liouville theorem](../../analysis/complex-analysis/liouville-theorem.md)
- [Polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Roots of a polynomial](../polynomials-and-power-series/roots-of-a-polynomial.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)

## Sources

- [Mathlib documentation: `Complex.exists_root`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/Basic.html#Complex.exists_root)
- [Source of `Complex.exists_root` in Mathlib/Analysis/Complex/Polynomial/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/Polynomial/Basic.lean#L35)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L128)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L180)
- [Freek Wiedijk's 100 theorems, no. 2](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L12)
