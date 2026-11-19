---
catalog: module
lean: Aesop.Tree, Aesop.mkInitialTree, Aesop.TreeM.Context, Aesop.TreeM.State, Aesop.TreeM, Aesop.TreeM.run', Aesop.getRootMVarCluster, Aesop.getRootMetaState, Aesop.getRootGoal, Aesop.getRootMVarId, Aesop.incrementNumGoals, Aesop.incrementNumRapps, Aesop.getAllIntroducedMVars, Aesop.getAndIncrementNextGoalId, Aesop.getAndIncrementNextRappId
statement: formalized
proof: formalized
---

# TreeM

`Aesop.Tree.TreeM`, in [Aesop/Tree/TreeM.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean), by Jannis Limperg.

`Aesop.Tree` (structure, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L19))

```lean
structure Tree where
  root : MVarClusterRef
  rootMetaState : Meta.SavedState
  numGoals : Nat
  numRapps : Nat
  nextGoalId : GoalId
  nextRappId : RappId
  /--
  Union of the mvars introduced by all rapps.
  -/
  allIntroducedMVars : Std.HashSet MVarId
```

`Aesop.mkInitialTree` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L31))

```lean
def mkInitialTree (goal : MVarId) (rs : LocalRuleSet) : BaseM Tree
```

`Aesop.TreeM.Context` (structure, [line 72](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L72))

```lean
structure TreeM.Context where
  currentIteration : Iteration
  ruleSet : LocalRuleSet
```

`Aesop.TreeM.State` (structure, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L76))

```lean
structure TreeM.State where
  tree : Tree
```

`Aesop.TreeM` (abbreviation, [line 79](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L79))

```lean
abbrev TreeM
```

`Aesop.TreeM.run'` (definition, [line 98](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L98))

```lean
def run' (ctx : TreeM.Context) (tree : Tree) (x : TreeM α) :
    BaseM (α × TreeM.State)
```

`Aesop.getRootMVarCluster` (definition, [line 104](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L104))

```lean
def getRootMVarCluster : TreeM MVarClusterRef
```

`Aesop.getRootMetaState` (definition, [line 107](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L107))

```lean
def getRootMetaState : TreeM Meta.SavedState
```

`Aesop.getRootGoal` (definition, [line 110](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L110))

```lean
def getRootGoal : TreeM GoalRef
```

`Aesop.getRootMVarId` (definition, [line 118](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L118))

```lean
def getRootMVarId : TreeM MVarId
```

`Aesop.incrementNumGoals` (definition, [line 122](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L122))

```lean
def incrementNumGoals (increment := 1) : TreeM Unit
```

`Aesop.incrementNumRapps` (definition, [line 125](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L125))

```lean
def incrementNumRapps (increment := 1) : TreeM Unit
```

`Aesop.getAllIntroducedMVars` (definition, [line 128](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L128))

```lean
def getAllIntroducedMVars : TreeM (Std.HashSet MVarId)
```

`Aesop.getAndIncrementNextGoalId` (definition, [line 131](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L131))

```lean
def getAndIncrementNextGoalId : TreeM GoalId
```

`Aesop.getAndIncrementNextRappId` (definition, [line 136](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean#L136))

```lean
def getAndIncrementNextRappId : TreeM RappId
```

## Depends on

- [Initial](../forward/state-2/initial.md)
- [Data](data.md)

## Sources

- [Aesop/Tree/TreeM.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/TreeM.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.TreeM.json)
