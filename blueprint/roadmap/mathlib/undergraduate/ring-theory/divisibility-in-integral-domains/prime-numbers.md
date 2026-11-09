# Prime numbers

An element `p` of a commutative monoid with zero (e.g., a ring) is called *prime*,
if it's not zero, not a unit, and `p ∣ a * b → p ∣ a ∨ p ∣ b` for all `a`, `b`.

```lean
Prime.{u_1} {M : Type u_1} [CommMonoidWithZero M] (p : M) : Prop
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Prime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Prime/Defs.html#Prime)
- [Source of `Prime` in Mathlib/Algebra/Prime/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Prime/Defs.lean#L41)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L153)
