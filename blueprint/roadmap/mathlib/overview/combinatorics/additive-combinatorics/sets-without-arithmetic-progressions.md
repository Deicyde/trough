# Sets without arithmetic progressions

A set is **3AP-free** if it does not contain any non-trivial arithmetic
progression of length three.

This is also sometimes called a **non-averaging set** or **Salem-Spencer set**.

```lean
ThreeAPFree.{u_2} {α : Type u_2} [AddMonoid α] (s : Set α) : Prop
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `ThreeAPFree`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/AP/Three/Defs.html#ThreeAPFree)
- [Source of `ThreeAPFree` in Mathlib/Combinatorics/Additive/AP/Three/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/AP/Three/Defs.lean#L69)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L539)
