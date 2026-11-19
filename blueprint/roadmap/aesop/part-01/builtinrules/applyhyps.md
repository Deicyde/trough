---
catalog: module
lean: Aesop.BuiltinRules.applyHyp, Aesop.BuiltinRules.applyHyps
statement: formalized
proof: formalized
---

# ApplyHyps

`Aesop.BuiltinRules.ApplyHyps`, in [Aesop/BuiltinRules/ApplyHyps.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/ApplyHyps.lean), by Jannis Limperg.

`Aesop.BuiltinRules.applyHyp` (definition, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/ApplyHyps.lean#L17))

```lean
meta def applyHyp (hyp : FVarId) (goal : MVarId) (md : TransparencyMode) :
    BaseM RuleApplication
```

`Aesop.BuiltinRules.applyHyps` (definition, [line 36](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/ApplyHyps.lean#L36))

```lean
meta def applyHyps : RuleTac
```

## Depends on

- [Rule Tactic Types](../ruletac/basic.md)
- [SpecificTactics](../script/specifictactics.md)

## Sources

- [Aesop/BuiltinRules/ApplyHyps.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/ApplyHyps.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.BuiltinRules.ApplyHyps.json)
