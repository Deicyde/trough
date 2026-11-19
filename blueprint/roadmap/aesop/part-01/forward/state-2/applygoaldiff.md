---
catalog: module
lean: Aesop.ForwardState.applyGoalDiff
statement: formalized
proof: formalized
---

# ApplyGoalDiff

`Aesop.Forward.State.ApplyGoalDiff`, in [Aesop/Forward/State/ApplyGoalDiff.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State/ApplyGoalDiff.lean), by Jannis Limperg.

`Aesop.ForwardState.applyGoalDiff` (definition, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State/ApplyGoalDiff.lean#L19))

> Apply a goal diff to the state, adding and removing hypotheses as indicated
> by the diff.

```lean
def applyGoalDiff (rs : LocalRuleSet) (diff : GoalDiff) (fs : ForwardState) :
    BaseM ForwardState
```

## Depends on

- [Forward/State](../state.md)
- [RuleSet](../../../part-02/ruleset.md)

## Sources

- [Aesop/Forward/State/ApplyGoalDiff.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State/ApplyGoalDiff.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Forward.State.ApplyGoalDiff.json)
