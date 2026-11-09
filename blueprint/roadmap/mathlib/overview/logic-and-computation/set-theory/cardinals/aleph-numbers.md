# Aleph numbers

The `aleph` function gives the infinite cardinals listed by their ordinal index. `aleph 0 = ℵ₀`,
`aleph 1 = succ ℵ₀` is the first uncountable cardinal, and so on.

For a version including finite cardinals, see `Cardinal.preAleph`.

Conventions for notations in identifiers:

 * The recommended spelling of `ℵ_` in identifiers is `aleph`.

```lean
Cardinal.aleph.{u_1} : Ordinal.{u_1} ↪o Cardinal.{u_1}
```

## Depends on

- [Cofinality](cofinality.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Ordinal](../ordinals/ordinal.md)

## Sources

- [Mathlib documentation: `Cardinal.aleph`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Aleph.html#Cardinal.aleph)
- [Source of `Cardinal.aleph` in Mathlib/SetTheory/Cardinal/Aleph.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/SetTheory/Cardinal/Aleph.lean#L404)
- [Mathlib overview: Logic and computation › Set theory › Cardinals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L631)
