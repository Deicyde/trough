---
catalog: module
lean: Aesop.AddRapp, Aesop.AddRapp.consumedForwardRuleMatches, Aesop.findPathForAssignedMVars, Aesop.getGoalsToCopy, Aesop.copyGoals, Aesop.makeInitialGoal, Aesop.addRappUnsafe, Aesop.addRapp
statement: formalized
proof: formalized
---

# AddRapp

`Aesop.Tree.AddRapp`, in [Aesop/Tree/AddRapp.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean), by Jannis Limperg.

`Aesop.AddRapp` (structure, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean#L21))

```lean
structure AddRapp extends RuleApplication where
  parent : GoalRef
  appliedRule : RegularRule
  successProbability : Percent
```

`Aesop.AddRapp.consumedForwardRuleMatches` (definition, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean#L28))

```lean
def consumedForwardRuleMatches (r : AddRapp) : Array ForwardRuleMatch
```

`Aesop.findPathForAssignedMVars` (definition, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean#L33))

```lean
def findPathForAssignedMVars (assignedMVars : UnorderedArraySet MVarId)
    (start : GoalRef) : TreeM (Array RappRef × Std.HashSet GoalId)
```

`Aesop.getGoalsToCopy` (definition, [line 65](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean#L65))

```lean
def getGoalsToCopy (assignedMVars : UnorderedArraySet MVarId)
    (start : GoalRef) : TreeM (Array GoalRef)
```

`Aesop.copyGoals` (definition, [line 87](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean#L87))

```lean
unsafe def copyGoals (assignedMVars : UnorderedArraySet MVarId)
    (start : GoalRef) (parentMetaState : Meta.SavedState)
    (parentSuccessProbability : Percent) (depth : Nat) :
    TreeM (Array Goal)
```

`Aesop.makeInitialGoal` (definition, [line 127](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean#L127))

```lean
def makeInitialGoal (goal : Subgoal) (mvars : UnorderedArraySet MVarId)
    (parent : MVarClusterRef) (parentMetaState : Meta.SavedState)
    (parentForwardState : ForwardState)
    (parentForwardMatches : ForwardRuleMatches)
    (consumedForwardRuleMatches : Array ForwardRuleMatch) (depth : Nat)
    (successProbability : Percent) (origin : GoalOrigin) : TreeM Goal
```

`Aesop.addRappUnsafe` (definition, [line 158](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean#L158))

```lean
unsafe def addRappUnsafe (r : AddRapp) : TreeM RappRef
```

`Aesop.addRapp` (opaque constant, [line 321](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean#L321))

> Adds a new rapp and its subgoals. If the rapp assigns mvars, all relevant
> goals containing these mvars are copied as children of the rapp as well. If
> the rapp drops mvars, these are treated as assigned mvars, in the sense that
> the same goals are copied as if the dropped mvar had been assigned.
>
> Note that adding a rapp may prove the parent goal, but this function does not
> make the necessary changes. So after calling it, you should check whether the
> rapp's parent goal is proven and mark it accordingly.

```lean
opaque addRapp : AddRapp → TreeM RappRef
```

## Depends on

- [ApplyGoalDiff](../forward/state-2/applygoaldiff.md)
- [Traversal](traversal.md)
- [TreeM](treem.md)

## Sources

- [Aesop/Tree/AddRapp.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/AddRapp.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.AddRapp.json)
