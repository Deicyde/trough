---
catalog: module
lean: Aesop.ExtractScriptM.State, Aesop.ExtractScriptM, Aesop.ExtractScriptM.run, Aesop.ExtractScript.lazyStepToStep, Aesop.ExtractScript.lazyStepsToSteps, Aesop.ExtractScript.recordStep, Aesop.ExtractScript.recordLazySteps, Aesop.ExtractScript.visitGoal, Aesop.ExtractScript.visitRapp, Aesop.MVarClusterRef.extractScriptCore, Aesop.GoalRef.extractScriptCore, Aesop.RappRef.extractScriptCore, Aesop.extractScript, Aesop.MVarClusterRef.extractSafePrefixScriptCore, Aesop.GoalRef.extractSafePrefixScriptCore, Aesop.RappRef.extractSafePrefixScriptCore, Aesop.extractSafePrefixScript
statement: formalized
proof: formalized
---

# ExtractScript

`Aesop.Tree.ExtractScript`, in [Aesop/Tree/ExtractScript.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean), by Jannis Limperg.

`Aesop.ExtractScriptM.State` (structure, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L21))

```lean
structure ExtractScriptM.State where
  script : UScript := #[]
  proofHasMVar : Bool := false
```

`Aesop.ExtractScriptM` (abbreviation, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L25))

```lean
abbrev ExtractScriptM
```

`Aesop.ExtractScriptM.run` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L27))

```lean
def ExtractScriptM.run (x : ExtractScriptM α) : TreeM (UScript × Bool)
```

`Aesop.ExtractScript.lazyStepToStep` (definition, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L33))

```lean
def lazyStepToStep (ruleName : DisplayRuleName) (lstep : LazyStep) :
    MetaM Step
```

`Aesop.ExtractScript.lazyStepsToSteps` (definition, [line 40](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L40))

```lean
def lazyStepsToSteps (ruleName : DisplayRuleName) :
    Option (Array LazyStep) → MetaM (Array Step)
```

`Aesop.ExtractScript.recordStep` (definition, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L45))

```lean
def recordStep (step : Script.Step) : ExtractScriptM Unit
```

`Aesop.ExtractScript.recordLazySteps` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L48))

```lean
def recordLazySteps (ruleName : DisplayRuleName)
    (steps? : Option (Array Script.LazyStep)) : ExtractScriptM Unit
```

`Aesop.ExtractScript.visitGoal` (definition, [line 53](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L53))

```lean
def visitGoal (g : Goal) : ExtractScriptM Unit
```

`Aesop.ExtractScript.visitRapp` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L64))

```lean
def visitRapp (r : Rapp) : ExtractScriptM Unit
```

`Aesop.MVarClusterRef.extractScriptCore` (definition, [line 73](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L73))

```lean
partial def MVarClusterRef.extractScriptCore (cref : MVarClusterRef) :
    ExtractScriptM Unit
```

`Aesop.GoalRef.extractScriptCore` (definition, [line 80](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L80))

```lean
partial def GoalRef.extractScriptCore (gref : GoalRef) : ExtractScriptM Unit
```

`Aesop.RappRef.extractScriptCore` (definition, [line 88](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L88))

```lean
partial def RappRef.extractScriptCore (rref : RappRef) :
    ExtractScriptM Unit
```

`Aesop.extractScript` (definition, [line 96](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L96))

```lean
def extractScript : TreeM (UScript × Bool)
```

`Aesop.MVarClusterRef.extractSafePrefixScriptCore` (definition, [line 101](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L101))

```lean
partial def MVarClusterRef.extractSafePrefixScriptCore
    (mref : MVarClusterRef) : ExtractScriptM Unit
```

`Aesop.GoalRef.extractSafePrefixScriptCore` (definition, [line 105](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L105))

```lean
partial def GoalRef.extractSafePrefixScriptCore (gref : GoalRef) :
    ExtractScriptM Unit
```

`Aesop.RappRef.extractSafePrefixScriptCore` (definition, [line 120](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L120))

```lean
partial def RappRef.extractSafePrefixScriptCore (rref : RappRef) :
    ExtractScriptM Unit
```

`Aesop.extractSafePrefixScript` (definition, [line 132](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean#L132))

```lean
def extractSafePrefixScript : TreeM (UScript × Bool)
```

## Depends on

- [UScript](../script/uscript.md)
- [TreeM](treem.md)

## Sources

- [Aesop/Tree/ExtractScript.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractScript.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.ExtractScript.json)
