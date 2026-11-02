---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.isPrimitiveRoot_iff
mathlib_file: Mathlib/RingTheory/RootsOfUnity/Complex.lean
---

# Primitive complex roots of unity

Mathlib states this as `Complex.isPrimitiveRoot_iff`.

```lean
Complex.isPrimitiveRoot_iff (ζ : ℂ) (n : ℕ) (hn : n ≠ 0) :
  IsPrimitiveRoot ζ n ↔
    ∃ i < n, ∃ (_ : i.Coprime n), Complex.exp (2 * ↑Real.pi * Complex.I * (↑i / ↑n)) = ζ
```

## Depends on

- [Cos (extension of trigonometric functions to the complex plane)](../../single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Coprime element](../../../overview/general-algebra/divisibility-in-integral-domains/coprime-element.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `Complex.isPrimitiveRoot_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_iff)
- [Source of `Complex.isPrimitiveRoot_iff` in Mathlib/RingTheory/RootsOfUnity/Complex.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/RootsOfUnity/Complex.lean#L97)
- [Mathlib undergraduate list: Group Theory › Abelian group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L97)
