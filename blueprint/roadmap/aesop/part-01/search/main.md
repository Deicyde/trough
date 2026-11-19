---
catalog: module
lean: Aesop.nextActiveGoal, Aesop.expandNextGoal, Aesop.checkGoalLimit, Aesop.checkRappLimit, Aesop.checkRootUnprovable, Aesop.getProof?, Aesop.finalizeProof, Aesop.traceScript, Aesop.traceTree, Aesop.finishIfProven, Aesop.treeHasProgress, Aesop.throwAesopEx, Aesop.handleNonfatalError, Aesop.searchLoop, Aesop.search
statement: formalized
proof: formalized
---

# Search/Main

`Aesop.Search.Main`, in [Aesop/Search/Main.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean), by Jannis Limperg.

`Aesop.nextActiveGoal` (definition, [line 30](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L30))

```lean
partial def nextActiveGoal : SearchM Q GoalRef
```

`Aesop.expandNextGoal` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L38))

```lean
def expandNextGoal : SearchM Q Unit
```

`Aesop.checkGoalLimit` (definition, [line 88](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L88))

```lean
def checkGoalLimit : SearchM Q (Option MessageData)
```

`Aesop.checkRappLimit` (definition, [line 95](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L95))

```lean
def checkRappLimit : SearchM Q (Option MessageData)
```

`Aesop.checkRootUnprovable` (definition, [line 102](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L102))

```lean
def checkRootUnprovable : SearchM Q (Option MessageData)
```

`Aesop.getProof?` (definition, [line 113](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L113))

```lean
def getProof? : SearchM Q (Option Expr)
```

`Aesop.finalizeProof` (definition, [line 116](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L116))

```lean
def finalizeProof : SearchM Q Unit
```

`Aesop.traceScript` (definition, [line 128](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L128))

```lean
def traceScript (completeProof : Bool) : SearchM Q Unit
```

`Aesop.traceTree` (definition, [line 143](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L143))

```lean
def traceTree : SearchM Q Unit
```

`Aesop.finishIfProven` (definition, [line 146](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L146))

```lean
def finishIfProven : SearchM Q Bool
```

`Aesop.treeHasProgress` (definition, [line 167](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L167))

> This function detects whether the search has made progress, meaning that the
> remaining goals after safe prefix expansion are different from the initial goal.
> We approximate this by checking whether, after safe prefix expansion, either
> of the following statements is true.
>
> - There is a safe rapp.
> - A subgoal of the preprocessing rule has been modified during normalisation.
>
> This is an approximation because a safe rule could, in principle, leave the
> initial goal unchanged.

```lean
def treeHasProgress : TreeM Bool
```

`Aesop.throwAesopEx` (definition, [line 190](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L190))

```lean
def throwAesopEx (mvarId : MVarId) (remainingSafeGoals : Array MVarId)
    (safePrefixExpansionSuccess : Bool) (msg? : Option MessageData) :
    SearchM Q α
```

`Aesop.handleNonfatalError` (definition, [line 228](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L228))

```lean
def handleNonfatalError (err : MessageData) : SearchM Q (Array MVarId)
```

`Aesop.searchLoop` (definition, [line 250](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L250))

```lean
partial def searchLoop : SearchM Q (Array MVarId)
```

`Aesop.search` (definition, [line 267](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean#L267))

```lean
def search (goal : MVarId) (ruleSet? : Option LocalRuleSet := none)
     (options : Aesop.Options := {}) (simpConfig : Simp.Config := {})
     (simpConfigSyntax? : Option Term := none) (stats : Stats := {}) :
     MetaM (Array MVarId × Stats)
```

## Depends on

- [Frontend/Extension](../frontend/extension.md)
- [Script/Main](../script/main.md)
- [ExpandSafePrefix](expandsafeprefix.md)
- [Expansion](expansion.md)
- [Queue](queue.md)
- [ExtractProof](../tree/extractproof.md)
- [ExtractScript](../tree/extractscript.md)
- [Free](../tree/free.md)
- [Stats](../tree/stats.md)
- [Tree/Tracing](../tree/tracing.md)

## Proof depends on

- [Tree/Check](../tree/check.md)

## Sources

- [Aesop/Search/Main.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Main.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Search.Main.json)
