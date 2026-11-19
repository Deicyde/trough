---
catalog: module
lean: Aesop.Script.TacticState, Aesop.Script.TacticState.mkInitial, Aesop.Script.TacticState.getVisibleGoalIndex?, Aesop.Script.TacticState.getVisibleGoalIndex, Aesop.Script.TacticState.getMainGoal?, Aesop.Script.TacticState.visibleGoalsHaveMVars, Aesop.Script.TacticState.solveVisibleGoals, Aesop.Script.TacticState.eraseSolvedGoals, Aesop.Script.TacticState.applyTactic, Aesop.Script.TacticState.focus, Aesop.Script.TacticState.onGoalM
statement: formalized
proof: formalized
---

# TacticState

`Aesop.Script.TacticState`, in [Aesop/Script/TacticState.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean), by Jannis Limperg.

`Aesop.Script.TacticState` (structure, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L20))

```lean
structure TacticState where
  visibleGoals : Array GoalWithMVars
  invisibleGoals : Std.HashSet MVarId
  deriving Inhabited
```

`Aesop.Script.TacticState.mkInitial` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L27))

```lean
def mkInitial (goal : MVarId) : MetaM TacticState
```

`Aesop.Script.TacticState.getVisibleGoalIndex?` (definition, [line 36](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L36))

```lean
def getVisibleGoalIndex? (ts : TacticState) (goal : MVarId) : Option Nat
```

`Aesop.Script.TacticState.getVisibleGoalIndex` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L39))

```lean
def getVisibleGoalIndex (ts : TacticState) (goal : MVarId) : m Nat
```

`Aesop.Script.TacticState.getMainGoal?` (definition, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L45))

```lean
def getMainGoal? (ts : TacticState) : Option MVarId
```

`Aesop.Script.TacticState.visibleGoalsHaveMVars` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L48))

```lean
def visibleGoalsHaveMVars (ts : TacticState) : Bool
```

`Aesop.Script.TacticState.solveVisibleGoals` (definition, [line 51](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L51))

```lean
def solveVisibleGoals (ts : TacticState) : TacticState
```

`Aesop.Script.TacticState.eraseSolvedGoals` (definition, [line 66](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L66))

```lean
def eraseSolvedGoals (ts : TacticState) (preMCtx postMCtx : MetavarContext) :
    TacticState
```

`Aesop.Script.TacticState.applyTactic` (definition, [line 77](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L77))

```lean
def applyTactic (ts : TacticState) (inGoal : MVarId)
    (outGoals : Array GoalWithMVars) (preMCtx postMCtx : MetavarContext) :
    m TacticState
```

`Aesop.Script.TacticState.focus` (definition, [line 88](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L88))

```lean
def focus (ts : TacticState) (goal : MVarId) : m TacticState
```

`Aesop.Script.TacticState.onGoalM` (definition, [line 98](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean#L98))

```lean
def onGoalM (ts : TacticState) (g : MVarId)
    (f : TacticState → m (α × TacticState)) : m (α × TacticState)
```

## Depends on

- [GoalWithMVars](goalwithmvars.md)

## Sources

- [Aesop/Script/TacticState.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/TacticState.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.TacticState.json)
