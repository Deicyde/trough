---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: PadicInt
mathlib_file: Mathlib/NumberTheory/Padics/PadicIntegers.lean
---

# $p$-adic integer

The `p`-adic integers `ℤ_[p]` are the `p`-adic numbers with norm `≤ 1`.

```lean
PadicInt (p : ℕ) [hp : Fact (Nat.Prime p)] : Type
```

## Depends on

- [$p$-adic number](p-adic-number.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Subring](../rings/subring.md)

## Sources

- [Mathlib documentation: `PadicInt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt)
- [Source of `PadicInt` in Mathlib/NumberTheory/Padics/PadicIntegers.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Padics/PadicIntegers.lean#L70)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L29)
