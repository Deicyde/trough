---
catalog: module
lean: Aesop.PremiseIndex
statement: formalized
proof: formalized
---

# PremiseIndex

`Aesop.Forward.PremiseIndex`, in [Aesop/Forward/PremiseIndex.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/PremiseIndex.lean), by Jannis Limperg.

`Aesop.PremiseIndex` (structure, [line 12](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/PremiseIndex.lean#L12))

```lean
structure PremiseIndex where
  toNat : Nat
  deriving Inhabited, BEq, Hashable, DecidableEq, Ord
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Forward/PremiseIndex.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/PremiseIndex.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Forward.PremiseIndex.json)
