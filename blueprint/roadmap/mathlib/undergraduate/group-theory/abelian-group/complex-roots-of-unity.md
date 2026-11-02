---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.mem_rootsOfUnity
mathlib_file: Mathlib/RingTheory/RootsOfUnity/Complex.lean
---

# Complex roots of unity

The complex `n`-th roots of unity are exactly the
complex numbers of the form `exp (2 * Real.pi * Complex.I * (i / n))` for some `i < n`.

```lean
Complex.mem_rootsOfUnity (n : ℕ) [NeZero n] (x : ℂˣ) :
  x ∈ rootsOfUnity n ℂ ↔ ∃ i < n, Complex.exp (2 * ↑Real.pi * Complex.I * (↑i / ↑n)) = ↑x
```

## Depends on

- [Cos (extension of trigonometric functions to the complex plane)](../../single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Coprime element](../../../overview/general-algebra/divisibility-in-integral-domains/coprime-element.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)

## Sources

- [Mathlib documentation: `Complex.mem_rootsOfUnity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.mem_rootsOfUnity)
- [Source of `Complex.mem_rootsOfUnity` in Mathlib/RingTheory/RootsOfUnity/Complex.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/RootsOfUnity/Complex.lean#L111)
- [Mathlib undergraduate list: Group Theory › Abelian group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L96)
