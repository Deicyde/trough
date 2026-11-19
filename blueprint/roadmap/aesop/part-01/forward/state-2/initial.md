---
catalog: module
lean: Aesop.LocalRuleSet.mkInitialForwardState
statement: formalized
proof: formalized
---

# Initial

`Aesop.Forward.State.Initial`, in [Aesop/Forward/State/Initial.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State/Initial.lean), by Jannis Limperg.

`Aesop.LocalRuleSet.mkInitialForwardState` (definition, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State/Initial.lean#L17))

```lean
def mkInitialForwardState (goal : MVarId) (rs : LocalRuleSet) :
    BaseM (ForwardState × Array ForwardRuleMatch)
```

## Depends on

- [Forward/State](../state.md)
- [RuleSet](../../../part-02/ruleset.md)

## Sources

- [Aesop/Forward/State/Initial.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State/Initial.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Forward.State.Initial.json)
