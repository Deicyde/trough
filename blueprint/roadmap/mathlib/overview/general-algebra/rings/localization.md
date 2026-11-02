---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Localization
mathlib_file: Mathlib/GroupTheory/MonoidLocalization/Basic.lean
---

# Localization

The localization of a `CommMonoid` at one of its submonoids (as a quotient type).

```lean
Localization.{u_1} {M : Type u_1} [CommMonoid M] (S : Submonoid M) : Type u_1
```

## Depends on

- [Group action](../group-theory/part-01/group-action.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Localization`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/MonoidLocalization/Basic.html#Localization)
- [Source of `Localization` in Mathlib/GroupTheory/MonoidLocalization/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/MonoidLocalization/Basic.lean#L207)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L69)
