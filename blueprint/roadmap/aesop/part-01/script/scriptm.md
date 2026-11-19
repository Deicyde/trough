---
catalog: module
lean: Aesop.ScriptT, Aesop.ScriptT.run, Aesop.ScriptM, Aesop.recordScriptStep, Aesop.recordScriptSteps, Aesop.withScriptStep, Aesop.withOptScriptStep
statement: formalized
proof: formalized
---

# ScriptM

`Aesop.Script.ScriptM`, in [Aesop/Script/ScriptM.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean), by Jannis Limperg.

`Aesop.ScriptT` (abbreviation, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean#L17))

```lean
abbrev ScriptT m
```

`Aesop.ScriptT.run` (definition, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean#L21))

```lean
protected def run [Monad m] [MonadLiftT (ST IO.RealWorld) m] (x : ScriptT m α) :
    m (α × Array LazyStep)
```

`Aesop.ScriptM` (abbreviation, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean#L27))

```lean
abbrev ScriptM
```

`Aesop.recordScriptStep` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean#L31))

```lean
def recordScriptStep (step : LazyStep) : m Unit
```

`Aesop.recordScriptSteps` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean#L34))

```lean
def recordScriptSteps (steps : Array LazyStep) : m Unit
```

`Aesop.withScriptStep` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean#L37))

```lean
def withScriptStep (preGoal : MVarId) (postGoals : α → Array MVarId)
    (success : α → Bool) (tacticBuilder : α → TacticBuilder) (x : MetaM α) :
    ScriptM α
```

`Aesop.withOptScriptStep` (definition, [line 51](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean#L51))

```lean
def withOptScriptStep (preGoal : MVarId) (postGoals : α → Array MVarId)
    (tacticBuilder : α → TacticBuilder) (x : MetaM (Option α)) :
    ScriptM (Option α)
```

## Depends on

- [BaseM](../basem.md)
- [Step](step.md)

## Sources

- [Aesop/Script/ScriptM.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/ScriptM.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.ScriptM.json)
