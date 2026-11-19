---
catalog: module
lean: Aesop.Nanos, Aesop.Nanos.printAsMillis
statement: formalized
proof: formalized
---

# Nanos

`Aesop.Nanos`, in [Aesop/Nanos.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Nanos.lean), by Jannis Limperg.

`Aesop.Nanos` (structure, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Nanos.lean#L16))

```lean
structure Nanos where
  nanos : Nat
  deriving Inhabited, BEq, Ord
```

`Aesop.Nanos.printAsMillis` (definition, [line 46](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Nanos.lean#L46))

```lean
def printAsMillis (n : Nanos) : String
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Nanos.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Nanos.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.Nanos.json)
