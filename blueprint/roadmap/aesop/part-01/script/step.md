---
catalog: module
lean: Aesop.Script.mkOneBasedNumLit, Aesop.Script.mkOnGoal, Aesop.Script.Step, Aesop.Script.TacticState.applyStep, Aesop.Script.Step.uTactic, Aesop.Script.Step.sTactic?, Aesop.Script.Step.mkSorry, Aesop.Script.Step.render, Aesop.Script.Step.validate, Aesop.Script.LazyStep, Aesop.Script.LazyStep.runFirstSuccessfulTacticBuilder, Aesop.Script.LazyStep.toStep, Aesop.Script.LazyStep.BuildInput, Aesop.Script.LazyStep.build, Aesop.Script.LazyStep.erasePostStateAssignments
statement: formalized
---

# Step

`Aesop.Script.Step`, in [Aesop/Script/Step.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean), by Jannis Limperg.

`Aesop.Script.mkOneBasedNumLit` (definition, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L25))

```lean
def mkOneBasedNumLit (n : Nat) : NumLit
```

`Aesop.Script.mkOnGoal` (definition, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L28))

```lean
def mkOnGoal (goalPos : Nat) (tac : Syntax.Tactic) : Syntax.Tactic
```

`Aesop.Script.Step` (structure, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L35))

```lean
structure Step where
  preState : Meta.SavedState
  preGoal : MVarId
  tactic : Tactic
  postState : Meta.SavedState
  postGoals : Array GoalWithMVars
```

`Aesop.Script.TacticState.applyStep` (definition, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L42))

```lean
def TacticState.applyStep (tacticState : TacticState) (step : Step) :
    m TacticState
```

`Aesop.Script.Step.uTactic` (definition, [line 49](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L49))

```lean
def uTactic (s : Step) : UTactic
```

`Aesop.Script.Step.sTactic?` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L52))

```lean
def sTactic? (s : Step) : Option STactic
```

`Aesop.Script.Step.mkSorry` (definition, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L59)). Its value holds `sorry`.

```lean
def mkSorry (preGoal : MVarId) (preState : Meta.SavedState) : MetaM Step
```

`Aesop.Script.Step.render` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L68))

```lean
def render (acc : Array Syntax.Tactic) (step : Step)
    (tacticState : TacticState) : m (Array Syntax.Tactic × TacticState)
```

`Aesop.Script.Step.validate` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L76))

```lean
def validate (step : Step) : MetaM Unit
```

`Aesop.Script.LazyStep` (structure, [line 99](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L99))

```lean
structure LazyStep where
  preState : Meta.SavedState
  preGoal : MVarId
  /--
  A nonempty list of tactic builders. During script generation, Aesop tries to
  execute the builders from left to right. It then uses the first builder that
  succceds (in the sense that when run in `preState` on `preGoal` it produces
  the `postState` and `postGoals`). The last builder must succeed and is used
  unconditionally.
  -/
  tacticBuilders : Array TacticBuilder
  tacticBuilders_ne : 0 < tacticBuilders.size := by simp
  postState : Meta.SavedState
  postGoals : Array MVarId
```

`Aesop.Script.LazyStep.runFirstSuccessfulTacticBuilder` (definition, [line 116](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L116))

```lean
def runFirstSuccessfulTacticBuilder (s : LazyStep) : MetaM Tactic
```

`Aesop.Script.LazyStep.toStep` (definition, [line 141](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L141))

```lean
def toStep (s : LazyStep) : MetaM Step
```

`Aesop.Script.LazyStep.BuildInput` (structure, [line 149](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L149))

```lean
structure BuildInput (α) where
  tac : MetaM α
  postGoals : α → Array MVarId
  tacticBuilder : α → TacticBuilder
```

`Aesop.Script.LazyStep.build` (definition, [line 155](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L155))

```lean
def build (preGoal : MVarId) (i : BuildInput α) : MetaM (LazyStep × α)
```

`Aesop.Script.LazyStep.erasePostStateAssignments` (definition, [line 166](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean#L166))

```lean
def erasePostStateAssignments (s : LazyStep) (gs : Array MVarId) : LazyStep
```

## Depends on

- [Script/Tactic](tactic.md)
- [TacticState](tacticstate.md)
- [Aesop/Tracing](../../part-02/tracing.md)
- [EqualUpToIds](../util/equaluptoids.md)

## Proof depends on

- [Util](util.md)

## Sources

- [Aesop/Script/Step.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Step.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.Step.json)
