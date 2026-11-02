---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.hittingBtwn
mathlib_file: Mathlib/Probability/Process/HittingTime.lean
---

# Hitting time

Hitting time: given a stochastic process `u` and a set `s`, `hittingBtwn u s n m` is
the first time `u` is in `s` after time `n` and before time `m` (if `u` does not hit `s`
after time `n` and before `m` then the hitting time is simply `m`).

The hitting time is a stopping time if the process is strongly adapted and discrete.

```lean
MeasureTheory.hittingBtwn.{u_1, u_2, u_3} {Ω : Type u_1} {β : Type u_2} {ι : Type u_3} [Preorder ι]
  [InfSet ι] (u : ι → Ω → β) (s : Set β) (n m : ι) : Ω → ι
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `MeasureTheory.hittingBtwn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Process/HittingTime.html#MeasureTheory.hittingBtwn)
- [Source of `MeasureTheory.hittingBtwn` in Mathlib/Probability/Process/HittingTime.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Process/HittingTime.lean#L52)
- [Mathlib overview: Probability Theory › Stochastic Processes](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L426)
