---
catalog: module
lean: Aesop.Check, Aesop.Check.get, Aesop.Check.isEnabled, Aesop.Check.name
statement: formalized
proof: formalized
---

# Aesop/Check

`Aesop.Check`, in [Aesop/Check.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Check.lean), by Jannis Limperg.

`Aesop.Check` (structure, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Check.lean#L21))

```lean
structure Check where
  toOption : Lean.Option Bool
```

`Aesop.Check.get` (definition, [line 26](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Check.lean#L26))

```lean
def get (opts : Options) (opt : Check) : Bool
```

`Aesop.Check.isEnabled` (definition, [line 32](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Check.lean#L32))

```lean
def isEnabled [Monad m] [MonadOptions m] (opt : Check) : m Bool
```

`Aesop.Check.name` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Check.lean#L35))

```lean
def name (opt : Check) : Name
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Check.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Check.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.Check.json)
