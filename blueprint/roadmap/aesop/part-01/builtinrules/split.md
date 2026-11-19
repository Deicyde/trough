---
catalog: module
lean: Aesop.BuiltinRules.splitTarget, Aesop.BuiltinRules.splitHypothesesCore, Aesop.BuiltinRules.splitHypotheses
statement: formalized
proof: formalized
---

# Split

`Aesop.BuiltinRules.Split`, in [Aesop/BuiltinRules/Split.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Split.lean), by Sebastian Ullrich, Jannis Limperg.

`Aesop.BuiltinRules.splitTarget` (definition, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Split.lean#L18))

```lean
meta def splitTarget : RuleTac
```

`Aesop.BuiltinRules.splitHypothesesCore` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Split.lean#L24))

```lean
meta partial def splitHypothesesCore (goal : MVarId) :
    ScriptM (Option (Array MVarId))
```

`Aesop.BuiltinRules.splitHypotheses` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Split.lean#L38))

```lean
meta def splitHypotheses : RuleTac
```

## Depends on

- [Rule Tactic Types](../ruletac/basic.md)
- [SpecificTactics](../script/specifictactics.md)

## Sources

- [Aesop/BuiltinRules/Split.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Split.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.BuiltinRules.Split.json)
