---
catalog: module
lean: Aesop.runRuleTac
statement: formalized
proof: formalized
---

# Expansion/Basic

`Aesop.Search.Expansion.Basic`, in [Aesop/Search/Expansion/Basic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Basic.lean), by Jannis Limperg.

`Aesop.runRuleTac` (definition, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Basic.lean#L17))

```lean
def runRuleTac (tac : RuleTac) (ruleName : RuleName)
    (preState : Meta.SavedState) (input : RuleTacInput) :
    BaseM (Except Exception RuleTacOutput)
```

## Depends on

- [Rule Tactic Types](../../ruletac/basic.md)

## Sources

- [Aesop/Search/Expansion/Basic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Basic.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Search.Expansion.Basic.json)
