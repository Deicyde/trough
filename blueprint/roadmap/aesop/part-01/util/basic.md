---
catalog: module
lean: Aesop.time, Aesop.time', Aesop.PersistentHashSet.toList, Aesop.PersistentHashSet.toArray, Aesop.PersistentHashSet.toHashSet, Aesop.PersistentHashSet.filter, Aesop.getConclusionDiscrTreeKeys, Aesop.isEmptyTrie, Aesop.filterDiscrTreeM, Aesop.filterDiscrTree, Aesop.SimpTheorems.addSimpEntry, Aesop.SimpTheorems.foldSimpEntriesM, Aesop.SimpTheorems.foldSimpEntries, Aesop.SimpTheorems.simpEntries, Aesop.SimpTheorems.containsDecl, Aesop.forEachExprInLDeclCore, Aesop.forEachExprInLDecl', Aesop.forEachExprInLDecl, Aesop.forEachExprInLCtxCore, Aesop.forEachExprInLCtx', Aesop.forEachExprInLCtx, Aesop.forEachExprInGoalCore, Aesop.forEachExprInGoal', Aesop.forEachExprInGoal, Aesop.setThe, Aesop.runMetaMAsCoreM, Aesop.runTermElabMAsCoreM, Aesop.runTacticMAsMetaM, Aesop.runTacticSyntaxAsMetaM, Aesop.updateSimpEntryPriority, Aesop.hasSorry, Aesop.isAppOfUpToDefeq, Aesop.getAppUpToDefeq, Aesop.partitionGoalsAndMVars, Aesop.runTacticMCapturingPostState, Aesop.runTacticCapturingPostState, Aesop.runTacticSeqCapturingPostState, Aesop.runTacticsCapturingPostState, Aesop.withAllTransparencySeqSyntax, Aesop.withAllTransparencySyntax, Aesop.addTryThisTacticSeqSuggestion, Aesop.elabPattern, Aesop.tacticsToMessageData, Aesop.getUnusedNames, Aesop.Name.ofComponents, Aesop.withExceptionTransform, Aesop.withExceptionPrefix, Aesop.withPPAnalyze, Aesop.runInMetaState, Aesop.lBoolOr, Aesop.compareArrayLex, Aesop.compareArraySizeThenLex, Aesop.isDefEqReducibleRigid, Aesop.isHypRedundantReducibleRigid
statement: formalized
proof: formalized
---

# Util/Basic

`Aesop.Util.Basic`, in [Aesop/Util/Basic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean), by Jannis Limperg, Asta Halkjær From.

`Aesop.time` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L24))

```lean
def time [Monad m] [MonadLiftT BaseIO m] (x : m α) : m (α × Aesop.Nanos)
```

`Aesop.time'` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L31))

```lean
def time' [Monad m] [MonadLiftT BaseIO m] (x : m Unit) : m Aesop.Nanos
```

`Aesop.PersistentHashSet.toList` (definition, [line 43](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L43))

```lean
def toList (s : PersistentHashSet α) : List α
```

`Aesop.PersistentHashSet.toArray` (definition, [line 49](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L49))

```lean
def toArray (s : PersistentHashSet α) : Array α
```

`Aesop.PersistentHashSet.toHashSet` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L52))

```lean
def toHashSet (s : PHashSet α) : Std.HashSet α
```

`Aesop.PersistentHashSet.filter` (definition, [line 55](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L55))

```lean
def filter (p : α → Bool) (s : PHashSet α) : PHashSet α
```

`Aesop.getConclusionDiscrTreeKeys` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L68))

```lean
def getConclusionDiscrTreeKeys (type : Expr) : MetaM (Array Key)
```

`Aesop.isEmptyTrie` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L76))

```lean
def isEmptyTrie (t : Trie α)
```

`Aesop.filterDiscrTreeM` (definition, [line 86](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L86))

> Remove elements for which `p` returns `false` from the given `DiscrTree`.
> The removed elements are monadically folded over using `f` and `init`, so `f`
> is called once for each removed element and the final state of type `σ` is
> returned.

```lean
def filterDiscrTreeM [Monad m] (p : α → m Bool)
    (f : σ → α → m σ) (init : σ) (t : DiscrTree α) :
    m (DiscrTree α × σ)
```

`Aesop.filterDiscrTree` (definition, [line 103](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L103))

> Remove elements for which `p` returns `false` from the given `DiscrTree`.
> The removed elements are folded over using `f` and `init`, so `f` is called
> once for each removed element and the final state of type `σ` is returned.

```lean
def filterDiscrTree (p : α → Bool) (f : σ → α → σ) (init : σ)
    (t : DiscrTree α) : DiscrTree α × σ
```

`Aesop.SimpTheorems.addSimpEntry` (definition, [line 111](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L111))

```lean
def addSimpEntry (s : SimpTheorems) : SimpEntry → SimpTheorems
```

`Aesop.SimpTheorems.foldSimpEntriesM` (definition, [line 118](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L118))

```lean
def foldSimpEntriesM [Monad m] (f : σ → SimpEntry → m σ) (init : σ)
    (thms : SimpTheorems) : m σ
```

`Aesop.SimpTheorems.foldSimpEntries` (definition, [line 133](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L133))

```lean
def foldSimpEntries (f : σ → SimpEntry → σ) (init : σ) (thms : SimpTheorems) :
    σ
```

`Aesop.SimpTheorems.simpEntries` (definition, [line 137](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L137))

```lean
def simpEntries (thms : SimpTheorems) : Array SimpEntry
```

`Aesop.SimpTheorems.containsDecl` (definition, [line 140](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L140))

```lean
def containsDecl (thms : SimpTheorems) (decl : Name) : Bool
```

`Aesop.forEachExprInLDeclCore` (definition, [line 153](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L153))

```lean
def forEachExprInLDeclCore (ldecl : LocalDecl) (g : Expr → m Bool) :
    MonadCacheT Expr Unit m Unit
```

`Aesop.forEachExprInLDecl'` (definition, [line 162](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L162))

```lean
def forEachExprInLDecl' (ldecl : LocalDecl) (g : Expr → m Bool) :
    m Unit
```

`Aesop.forEachExprInLDecl` (definition, [line 167](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L167))

```lean
def forEachExprInLDecl (ldecl : LocalDecl) (g : Expr → m Unit) :
    m Unit
```

`Aesop.forEachExprInLCtxCore` (definition, [line 172](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L172))

```lean
def forEachExprInLCtxCore (lctx : LocalContext) (g : Expr → m Bool) :
    MonadCacheT Expr Unit m Unit
```

`Aesop.forEachExprInLCtx'` (definition, [line 178](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L178))

```lean
def forEachExprInLCtx' (mvarId : MVarId) (g : Expr → m Bool) : m Unit
```

`Aesop.forEachExprInLCtx` (definition, [line 183](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L183))

```lean
def forEachExprInLCtx (mvarId : MVarId) (g : Expr → m Unit) : m Unit
```

`Aesop.forEachExprInGoalCore` (definition, [line 187](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L187))

```lean
def forEachExprInGoalCore (mvarId : MVarId) (g : Expr → m Bool) :
    MonadCacheT Expr Unit m Unit
```

`Aesop.forEachExprInGoal'` (definition, [line 194](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L194))

```lean
def forEachExprInGoal' (mvarId : MVarId) (g : Expr → m Bool) : m Unit
```

`Aesop.forEachExprInGoal` (definition, [line 198](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L198))

```lean
def forEachExprInGoal (mvarId : MVarId) (g : Expr → m Unit) : m Unit
```

`Aesop.setThe` (definition, [line 205](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L205))

```lean
def setThe (σ) {m} [MonadStateOf σ m] (s : σ) : m PUnit
```

`Aesop.runMetaMAsCoreM` (definition, [line 209](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L209))

```lean
def runMetaMAsCoreM (x : MetaM α) : CoreM α
```

`Aesop.runTermElabMAsCoreM` (definition, [line 213](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L213))

```lean
def runTermElabMAsCoreM (x : Elab.TermElabM α) : CoreM α
```

`Aesop.runTacticMAsMetaM` (definition, [line 216](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L216))

```lean
def runTacticMAsMetaM (x : TacticM α) (goals : List MVarId) :
    MetaM (α × List MVarId)
```

`Aesop.runTacticSyntaxAsMetaM` (definition, [line 221](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L221))

```lean
def runTacticSyntaxAsMetaM (stx : Syntax) (goals : List MVarId) :
    MetaM (List MVarId)
```

`Aesop.updateSimpEntryPriority` (definition, [line 225](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L225))

```lean
def updateSimpEntryPriority (priority : Nat) (e : SimpEntry) : SimpEntry
```

`Aesop.hasSorry` (definition, [line 230](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L230))

```lean
partial def hasSorry [Monad m] [MonadMCtx m] (e : Expr) : m Bool
```

`Aesop.isAppOfUpToDefeq` (definition, [line 247](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L247))

```lean
def isAppOfUpToDefeq (f : Expr) (e : Expr) : MetaM Bool
```

`Aesop.getAppUpToDefeq` (definition, [line 262](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L262))

> If the input expression `e` reduces to `f x₁ ... xₙ` via repeated `whnf`, this
> function returns `f` and `[x₁, ⋯, xₙ]`. Otherwise it returns `e` (unchanged, not
> in WHNF!) and `[]`.

```lean
partial def getAppUpToDefeq (e : Expr) : MetaM (Expr × Array Expr)
```

`Aesop.partitionGoalsAndMVars` (definition, [line 277](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L277))

> Partition an array of structures containing `MVarId`s into 'goals' and
> 'proper mvars'. An `MVarId` from the input array `goals` is classified as a
> proper mvar if any of the `MVarId`s depend on it, and as a goal otherwise.
> Additionally, for each goal, we report the set of mvars that the goal depends
> on.

```lean
def partitionGoalsAndMVars (mvarId : α → MVarId) (goals : Array α) :
    MetaM (Array (α × UnorderedArraySet MVarId) × UnorderedArraySet MVarId)
```

`Aesop.runTacticMCapturingPostState` (definition, [line 296](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L296))

```lean
def runTacticMCapturingPostState (t : TacticM Unit) (preState : Meta.SavedState)
    (preGoals : List MVarId) : MetaM (Meta.SavedState × List MVarId)
```

`Aesop.runTacticCapturingPostState` (definition, [line 310](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L310))

```lean
def runTacticCapturingPostState (t : Syntax.Tactic) (preState : Meta.SavedState)
    (preGoals : List MVarId) : MetaM (Meta.SavedState × List MVarId)
```

`Aesop.runTacticSeqCapturingPostState` (definition, [line 314](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L314))

```lean
def runTacticSeqCapturingPostState (t : TSyntax ``Lean.Parser.Tactic.tacticSeq)
    (preState : Meta.SavedState) (preGoals : List MVarId) :
    MetaM (Meta.SavedState × List MVarId)
```

`Aesop.runTacticsCapturingPostState` (definition, [line 319](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L319))

```lean
def runTacticsCapturingPostState (ts : Array Syntax.Tactic)
    (preState : Meta.SavedState) (preGoals : List MVarId) :
    MetaM (Meta.SavedState × List MVarId)
```

`Aesop.withAllTransparencySeqSyntax` (definition, [line 333](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L333))

```lean
def withAllTransparencySeqSyntax (md : TransparencyMode)
    (k : TSyntax ``tacticSeq) : TSyntax ``tacticSeq
```

`Aesop.withAllTransparencySyntax` (definition, [line 339](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L339))

```lean
def withAllTransparencySyntax (md : TransparencyMode) (k : TSyntax `tactic) :
    TSyntax `tactic
```

`Aesop.addTryThisTacticSeqSuggestion` (definition, [line 367](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L367))

> Register a "Try this" suggestion for a tactic sequence.
>
> It works when the tactic to replace appears on its own line:
>
> ```lean
> by
>   aesop?
> ```
>
> It doesn't work (i.e., the suggestion will appear but in the wrong place) when
> the tactic to replace is preceded by other text on the same line:
>
> ```lean
> have x := by aesop?
> ```
>
> The `Try this:` suggestion in the infoview is not correctly formatted, but
> there's nothing we can do about this at the moment.

```lean
def addTryThisTacticSeqSuggestion (ref : Syntax)
    (suggestion : TSyntax ``Lean.Parser.Tactic.tacticSeq)
    (origSpan? : Option Syntax := none) : MetaM Unit
```

`Aesop.elabPattern` (definition, [line 394](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L394))

```lean
def elabPattern (stx : Syntax) : TermElabM Expr
```

`Aesop.tacticsToMessageData` (definition, [line 416](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L416))

```lean
def tacticsToMessageData (ts : Array Syntax.Tactic) : MessageData
```

`Aesop.getUnusedNames` (definition, [line 422](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L422))

> Note: the returned local context contains invalid `LocalDecl`s.

```lean
def getUnusedNames (lctx : LocalContext) (suggestions : Array Name) : Array Name × LocalContext
```

`Aesop.Name.ofComponents` (definition, [line 436](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L436))

```lean
def Name.ofComponents (cs : List Name) : Name
```

`Aesop.withExceptionTransform` (definition, [line 443](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L443))

```lean
def withExceptionTransform [Monad m] [MonadError m]
    (f : MessageData → MessageData) (x : m α) : m α
```

`Aesop.withExceptionPrefix` (definition, [line 453](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L453))

```lean
def withExceptionPrefix [Monad m] [MonadError m] (pre : MessageData) :
    m α → m α
```

`Aesop.withPPAnalyze` (definition, [line 457](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L457))

```lean
def withPPAnalyze [Monad m] [MonadWithOptions m] (x : m α) : m α
```

`Aesop.runInMetaState` (definition, [line 467](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L467))

> A generalized variant of `Meta.SavedState.runMetaM`

```lean
def runInMetaState [Monad m] [MonadLiftT MetaM m] [MonadFinally m]
    (s : Meta.SavedState) (x : m α) : m α
```

`Aesop.lBoolOr` (definition, [line 476](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L476))

```lean
def lBoolOr : (x y : LBool) → LBool
```

`Aesop.compareArrayLex` (definition, [line 483](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L483))

```lean
def compareArrayLex (cmp : α → α → Ordering) (xs ys : Array α) :
    Ordering
```

`Aesop.compareArraySizeThenLex` (definition, [line 498](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L498))

```lean
def compareArraySizeThenLex (cmp : α → α → Ordering) (xs ys : Array α) :
    Ordering
```

`Aesop.isDefEqReducibleRigid` (definition, [line 509](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L509))

```lean
def isDefEqReducibleRigid (s t : Expr) : MetaM Bool
```

`Aesop.isHypRedundantReducibleRigid` (definition, [line 515](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean#L515))

```lean
def isHypRedundantReducibleRigid (type : Expr) : MetaM Bool
```

## Depends on

- [DiscrTreeConfig](../index/discrtreeconfig.md)
- [Nanos](../../part-02/nanos.md)
- [UnorderedArraySet](unorderedarrayset.md)

## Sources

- [Aesop/Util/Basic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Basic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Util.Basic.json)
