---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: CircleDeg1Lift.translationNumber
mathlib_file: Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean
---

# Translation number

The translation number of a `CircleDeg1Lift`, $τ(f)=\lim_{n→∞}\frac{f^n(x)-x}{n}$. We use
an auxiliary sequence `\frac{f^{2^n}(0)}{2^n}` to define `τ(f)` because some proofs are simpler
this way.

```lean
CircleDeg1Lift.translationNumber (f : CircleDeg1Lift) : ℝ
```

## Depends on

- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Uniform space](../../topology/uniform-notions/uniform-space.md)

## Sources

- [Mathlib documentation: `CircleDeg1Lift.translationNumber`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.html#CircleDeg1Lift.translationNumber)
- [Source of `CircleDeg1Lift.translationNumber` in Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean#L547)
- [Mathlib overview: Dynamics › Circle dynamics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L557)
