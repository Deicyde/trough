---
catalog: module
lean: Aesop.LevelIndex
statement: formalized
proof: formalized
---

# LevelIndex

`Aesop.Forward.LevelIndex`, in [Aesop/Forward/LevelIndex.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/LevelIndex.lean), by Jannis Limperg.

`Aesop.LevelIndex` (structure, [line 12](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/LevelIndex.lean#L12))

```lean
structure LevelIndex where
  toNat : Nat
  deriving Inhabited, BEq, Hashable, DecidableEq, Ord
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Forward/LevelIndex.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/LevelIndex.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Forward.LevelIndex.json)
