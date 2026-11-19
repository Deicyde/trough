---
catalog: module
lean: Aesop.ExtResult, Aesop.straightLineExt, Aesop.straightLineExtProgress
statement: formalized
proof: formalized
---

# Tactic/Ext

`Aesop.Util.Tactic.Ext`, in [Aesop/Util/Tactic/Ext.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic/Ext.lean), by Jannis Limperg.

`Aesop.ExtResult` (structure, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic/Ext.lean#L18))

```lean
structure ExtResult where
  depth : Nat
  commonFVarIds : Array FVarId
  goals : Array (MVarId × Array FVarId)
```

`Aesop.straightLineExt` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic/Ext.lean#L23))

```lean
partial def straightLineExt (goal : MVarId) : MetaM ExtResult
```

`Aesop.straightLineExtProgress` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic/Ext.lean#L48))

```lean
def straightLineExtProgress (goal : MVarId) : MetaM ExtResult
```

## Depends on

Its statements use no other Aesop module's declarations.

## Proof depends on

- [Aesop/Tracing](../../../part-02/tracing.md)

## Sources

- [Aesop/Util/Tactic/Ext.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic/Ext.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Util.Tactic.Ext.json)
