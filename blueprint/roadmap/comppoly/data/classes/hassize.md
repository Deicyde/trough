---
catalog: module
lean: HasSize
statement: formalized
proof: formalized
---

# `HasSize` class

`CompPoly.Data.Classes.HasSize`, in [CompPoly/Data/Classes/HasSize.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/HasSize.lean), by Quang Dao.

> A type has a size in units of `β` when it embeds into `Vector β size`. A duplex sponge over
> units `β` absorbs and squeezes elements of such a type `size` units at a time.
>
> Ported verbatim from ArkLib (`ArkLib/Data/Classes/HasSize.lean`).

`HasSize` (class, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/HasSize.lean#L23))

> Type class for types that has an injective mapping to a vector of a given length `size` of
> another type (often `UInt8`).

```lean
class HasSize (α : Type*) (β : Type*) where
  size : Nat
  toFun : α ↪ Vector β size
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Classes/HasSize.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/HasSize.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Classes.HasSize.json)
