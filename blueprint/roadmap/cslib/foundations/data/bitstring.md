---
catalog: module
lean: Cslib.BitString, Cslib.BooleanFunction
statement: formalized
proof: formalized
---

# Fixed-length bit strings and Boolean functions

`Cslib.Foundations.Data.BitString`, in [Cslib/Foundations/Data/BitString.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/BitString.lean), by Samuel Schlesinger.

> A bit string is indexed by its coordinates, so selecting or updating one bit uses the usual
> functions on `Fin n → Bool`.

`Cslib.BitString` (abbreviation, [line 22](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/BitString.lean#L22))

> A string of `n` bits, indexed by its coordinates.

```lean
abbrev BitString (n : ℕ) : Type
```

`Cslib.BooleanFunction` (abbreviation, [line 25](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/BitString.lean#L25))

> A Boolean function of `n` input bits.

```lean
abbrev BooleanFunction (n : ℕ) : Type
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/BitString.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/BitString.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Data.BitString.json)
