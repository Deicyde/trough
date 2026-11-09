# Product of rings

Mathlib states this as `Pi.ring`.

```lean
Pi.ring.{u, v} {I : Type u} {f : I → Type v} [(i : I) → Ring (f i)] : Ring ((i : I) → f i)
```

## Depends on

- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `Pi.ring`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Pi.html#Pi.ring)
- [Source of `Pi.ring` in Mathlib/Algebra/Ring/Pi.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Ring/Pi.lean#L89)
- [Mathlib undergraduate list: Ring Theory › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L130)
