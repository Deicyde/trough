# Beth numbers

The Beth function is defined so that `beth 0 = ℵ₀`, `beth (succ o) = 2 ^ beth o`, and that for a
limit ordinal `o`, `beth o` is the supremum of `beth a` for `a < o`.

Assuming the generalized continuum hypothesis, which is undecidable in ZFC, we have `ℶ_ o = ℵ_ o`
for all ordinals.

For a version which starts at zero, see `Cardinal.preBeth`.

```lean
Cardinal.beth.{u} (o : Ordinal.{u}) : Cardinal.{u}
```

## Depends on

- [Cardinal](cardinal.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Ordinal](../ordinals/ordinal.md)

## Sources

- [Mathlib documentation: `Cardinal.beth`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Aleph.html#Cardinal.beth)
- [Source of `Cardinal.beth` in Mathlib/SetTheory/Cardinal/Aleph.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/SetTheory/Cardinal/Aleph.lean#L682)
- [Mathlib overview: Logic and computation › Set theory › Cardinals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L632)
