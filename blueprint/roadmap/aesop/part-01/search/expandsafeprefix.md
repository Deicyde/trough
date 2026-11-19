---
catalog: module
lean: Aesop.SafeExpansionM.State, Aesop.SafeExpansionM, Aesop.expandSafePrefix
statement: formalized
proof: formalized
---

# ExpandSafePrefix

`Aesop.Search.ExpandSafePrefix`, in [Aesop/Search/ExpandSafePrefix.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/ExpandSafePrefix.lean), by Jannis Limperg.

`Aesop.SafeExpansionM.State` (structure, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/ExpandSafePrefix.lean#L21))

```lean
structure SafeExpansionM.State where
  numRapps : Nat := 0
```

`Aesop.SafeExpansionM` (abbreviation, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/ExpandSafePrefix.lean#L24))

```lean
abbrev SafeExpansionM Q [Queue Q]
```

`Aesop.expandSafePrefix` (definition, [line 74](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/ExpandSafePrefix.lean#L74))

```lean
def expandSafePrefix : SearchM Q Bool
```

## Depends on

- [SearchM](searchm.md)

## Proof depends on

- [Expansion](expansion.md)

## Sources

- [Aesop/Search/ExpandSafePrefix.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/ExpandSafePrefix.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Search.ExpandSafePrefix.json)
