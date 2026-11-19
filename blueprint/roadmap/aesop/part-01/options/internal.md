---
catalog: module
lean: Aesop.Options', Aesop.Options.toOptions'
statement: formalized
proof: formalized
---

# Internal

`Aesop.Options.Internal`, in [Aesop/Options/Internal.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Options/Internal.lean), by Jannis Limperg.

`Aesop.Options'` (structure, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Options/Internal.lean#L18))

```lean
structure Options' extends Options where
  generateScript : Bool
  forwardMaxDepth? : Option Nat
  deriving Inhabited
```

`Aesop.Options.toOptions'` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Options/Internal.lean#L23))

```lean
def Options.toOptions' [Monad m] [MonadOptions m] (opts : Options)
    (forwardMaxDepth? : Option Nat := none) : m Options'
```

## Depends on

- [Aesop/Check](../check.md)
- [Public](public.md)

## Sources

- [Aesop/Options/Internal.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Options/Internal.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Options.Internal.json)
