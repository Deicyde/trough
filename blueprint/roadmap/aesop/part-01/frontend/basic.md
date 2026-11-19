---
catalog: module
lean: Aesop.Frontend.elabBoolLit
statement: formalized
proof: formalized
---

# Frontend/Basic

`Aesop.Frontend.Basic`, in [Aesop/Frontend/Basic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Basic.lean), by Jannis Limperg.

`Aesop.Frontend.elabBoolLit` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Basic.lean#L23))

```lean
def elabBoolLit [Monad m] [MonadRef m] [MonadExceptOf Exception m]
    (stx : TSyntax `Aesop.bool_lit) : m Bool
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Frontend/Basic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Basic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Frontend.Basic.json)
