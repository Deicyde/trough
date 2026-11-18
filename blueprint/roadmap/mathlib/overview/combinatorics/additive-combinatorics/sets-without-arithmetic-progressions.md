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
- [Source of `ThreeAPFree` in Mathlib/Combinatorics/Additive/AP/Three/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Combinatorics/Additive/AP/Three/Defs.lean#L69)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L539)
