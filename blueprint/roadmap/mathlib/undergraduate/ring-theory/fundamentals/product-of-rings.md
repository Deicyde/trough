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
- [Source of `Pi.ring` in Mathlib/Algebra/Ring/Pi.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Algebra/Ring/Pi.lean#L89)
- [Mathlib undergraduate list: Ring Theory › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L130)
