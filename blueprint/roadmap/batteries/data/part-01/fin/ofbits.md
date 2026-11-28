---
catalog: module
lean: Fin.ofBits, Fin.val_ofBits
statement: formalized
proof: formalized
---

# OfBits

`Batteries.Data.Fin.OfBits`, in [Batteries/Data/Fin/OfBits.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/OfBits.lean), by François G. Dorais.

`Fin.ofBits` (abbreviation, [line 17](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/OfBits.lean#L17))

> Construct an element of `Fin (2 ^ n)` from a sequence of bits (little endian).

```lean
abbrev ofBits (f : Fin n → Bool) : Fin (2 ^ n)
```

`Fin.val_ofBits` (theorem, [line 19](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/OfBits.lean#L19))

```lean
theorem val_ofBits (f : Fin n → Bool) : (ofBits f).val = Nat.ofBits f
```

## Depends on

- [Basic lemmas about natural numbers](../nat/lemmas.md)

## Sources

- [Batteries/Data/Fin/OfBits.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/OfBits.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Fin.OfBits.json)
