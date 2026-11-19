---
catalog: module
lean: Aesop.NormSimpContext, Aesop.SearchM.Context, Aesop.SearchM.State, Aesop.SearchM, Aesop.SearchM.run', Aesop.SearchM.run, Aesop.getTree, Aesop.setTree, Aesop.modifyTree, Aesop.getIteration, Aesop.incrementIteration, Aesop.popGoal?, Aesop.enqueueGoals, Aesop.setMaxRuleApplicationDepthReached, Aesop.wasMaxRuleApplicationDepthReached
statement: formalized
proof: formalized
---

# SearchM

`Aesop.Search.SearchM`, in [Aesop/Search/SearchM.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean), by Jannis Limperg.

`Aesop.NormSimpContext` (structure, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L18))

```lean
structure NormSimpContext where
  toContext : Simp.Context
  enabled : Bool
  useHyps : Bool
  configStx? : Option Term
  simprocs : Simp.SimprocsArray
  deriving Inhabited
```

`Aesop.SearchM.Context` (structure, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L28))

```lean
structure Context where
  ruleSet : LocalRuleSet
  normSimpContext : NormSimpContext
  options : Aesop.Options'
  deriving Nonempty
```

`Aesop.SearchM.State` (structure, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L34))

```lean
structure State (Q) [Aesop.Queue Q] where
  iteration : Iteration
  queue : Q
  maxRuleApplicationDepthReached : Bool
  deriving Inhabited
```

`Aesop.SearchM` (abbreviation, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L42))

```lean
abbrev SearchM Q [Aesop.Queue Q]
```

`Aesop.SearchM.run'` (definition, [line 75](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L75))

```lean
protected def run' (ctx : SearchM.Context) (σ : SearchM.State Q) (tree : Tree)
    (x : SearchM Q α) : BaseM (α × SearchM.State Q × Tree)
```

`Aesop.SearchM.run` (definition, [line 81](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L81))

```lean
protected def run (ruleSet : LocalRuleSet) (options : Aesop.Options')
    (simpConfig : Simp.Config) (simpConfigStx? : Option Term)
    (goal : MVarId) (x : SearchM Q α) : BaseM (α × State Q × Tree)
```

`Aesop.getTree` (definition, [line 105](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L105))

```lean
def getTree : SearchM Q Tree
```

`Aesop.setTree` (definition, [line 108](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L108))

```lean
def setTree : Tree → SearchM Q Unit
```

`Aesop.modifyTree` (definition, [line 111](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L111))

```lean
def modifyTree : (Tree → Tree) → SearchM Q Unit
```

`Aesop.getIteration` (definition, [line 114](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L114))

```lean
def getIteration : SearchM Q Iteration
```

`Aesop.incrementIteration` (definition, [line 117](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L117))

```lean
def incrementIteration : SearchM Q Unit
```

`Aesop.popGoal?` (definition, [line 120](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L120))

```lean
def popGoal? : SearchM Q (Option GoalRef)
```

`Aesop.enqueueGoals` (definition, [line 126](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L126))

```lean
def enqueueGoals (gs : Array GoalRef) : SearchM Q Unit
```

`Aesop.setMaxRuleApplicationDepthReached` (definition, [line 131](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L131))

```lean
def setMaxRuleApplicationDepthReached : SearchM Q Unit
```

`Aesop.wasMaxRuleApplicationDepthReached` (definition, [line 134](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean#L134))

```lean
def wasMaxRuleApplicationDepthReached : SearchM Q Bool
```

## Depends on

- [Class](queue-2/class.md)
- [TreeM](../tree/treem.md)

## Sources

- [Aesop/Search/SearchM.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/SearchM.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Search.SearchM.json)
