---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Cardinal
mathlib_file: Mathlib/SetTheory/Cardinal/Defs.lean
---

# Cardinal

`Cardinal.{u}` is the type of cardinal numbers in `Type u`,
defined as the quotient of `Type u` by existence of an equivalence
(a bijection with explicit inverse).

```lean
Cardinal.{u} : Type (u + 1)
```

## Depends on

- [Array](../../../data-structures/list-like-structures/array.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Cardinal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Defs.html#Cardinal)
- [Source of `Cardinal` in Mathlib/SetTheory/Cardinal/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/SetTheory/Cardinal/Defs.lean#L78)
- [Mathlib overview: Logic and computation › Set theory › Cardinals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L630)
