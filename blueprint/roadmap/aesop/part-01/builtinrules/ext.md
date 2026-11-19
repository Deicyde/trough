---
catalog: module
lean: Aesop.BuiltinRules.extCore, Aesop.BuiltinRules.ext
statement: formalized
proof: formalized
---

# BuiltinRules/Ext

`Aesop.BuiltinRules.Ext`, in [Aesop/BuiltinRules/Ext.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Ext.lean), by Jannis Limperg.

`Aesop.BuiltinRules.extCore` (definition, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Ext.lean#L16))

```lean
meta def extCore (goal : MVarId) : ScriptM (Option (Array MVarId))
```

`Aesop.BuiltinRules.ext` (definition, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Ext.lean#L25))

```lean
meta def ext : RuleTac
```

## Depends on

- [Rule Tactic Types](../ruletac/basic.md)
- [SpecificTactics](../script/specifictactics.md)

## Sources

- [Aesop/BuiltinRules/Ext.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Ext.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.BuiltinRules.Ext.json)
