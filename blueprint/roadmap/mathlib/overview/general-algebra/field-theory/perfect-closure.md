---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: PerfectClosure
mathlib_file: Mathlib/FieldTheory/PerfectClosure.lean
---

# Perfect closure

The perfect closure is the smallest extension that makes frobenius surjective.

```lean
PerfectClosure.{u} (K : Type u) [CommRing K] (p : ℕ) [Fact (Nat.Prime p)] [CharP K p] : Type u
```

## Depends on

- [Frobenius morphism](frobenius-morphism.md)
- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `PerfectClosure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/PerfectClosure.html#PerfectClosure)
- [Source of `PerfectClosure` in Mathlib/FieldTheory/PerfectClosure.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/PerfectClosure.lean#L67)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L133)
