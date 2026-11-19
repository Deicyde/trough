---
catalog: module
lean: Aesop.SlotIndex
statement: formalized
proof: formalized
---

# SlotIndex

`Aesop.Forward.SlotIndex`, in [Aesop/Forward/SlotIndex.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/SlotIndex.lean), by Jannis Limperg.

`Aesop.SlotIndex` (structure, [line 12](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/SlotIndex.lean#L12))

```lean
structure SlotIndex where
  toNat : Nat
  deriving Inhabited, BEq, Hashable, DecidableEq, Ord
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Forward/SlotIndex.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/SlotIndex.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Forward.SlotIndex.json)
