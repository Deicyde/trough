---
catalog: module
lean: Aesop.NormM.Context, Aesop.NormM.State, Aesop.NormM, Aesop.getForwardState, Aesop.getResetForwardState, Aesop.modifyForwardState, Aesop.updateForwardState, Aesop.eraseForwardRuleMatch, Aesop.applyDiffToForwardState, Aesop.NormRuleResult, Aesop.NormRuleResult.newGoal?, Aesop.NormRuleResult.steps?, Aesop.optNormRuleResultEmoji, Aesop.withNormTraceNode, Aesop.runNormRuleTac, Aesop.runNormRule, Aesop.runFirstNormRule, Aesop.mkNormSimpScriptStep, Aesop.normSimpCore, Aesop.checkSimp, Aesop.normSimp, Aesop.normUnfoldCore, Aesop.normUnfold, Aesop.NormSeqResult, Aesop.NormRuleResult.toNormSeqResult, Aesop.optNormRuleResultToNormSeqResult, Aesop.NormStep, Aesop.runNormSteps, Aesop.NormStep.runPreSimpRules, Aesop.NormStep.runPostSimpRules, Aesop.NormStep.unfold, Aesop.NormStep.simp, Aesop.normalizeGoalMVar, Aesop.normalizeGoalIfNecessary
statement: formalized
proof: formalized
---

# Norm

`Aesop.Search.Expansion.Norm`, in [Aesop/Search/Expansion/Norm.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean), by Jannis Limperg.

`Aesop.NormM.Context` (structure, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L27))

```lean
structure Context where
  options : Options'
  ruleSet : LocalRuleSet
  normSimpContext : NormSimpContext
```

`Aesop.NormM.State` (structure, [line 32](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L32))

```lean
structure State where
  forwardState : ForwardState
  forwardRuleMatches : ForwardRuleMatches
  deriving Inhabited
```

`Aesop.NormM` (abbreviation, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L39))

```lean
abbrev NormM
```

`Aesop.getForwardState` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L41))

```lean
def getForwardState : NormM ForwardState
```

`Aesop.getResetForwardState` (definition, [line 44](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L44))

```lean
def getResetForwardState : NormM ForwardState
```

`Aesop.modifyForwardState` (definition, [line 47](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L47))

```lean
def modifyForwardState (fs : ForwardState) (newMatches : Array ForwardRuleMatch)
    (erasedHyps : Std.HashSet FVarId) : NormM Unit
```

`Aesop.updateForwardState` (definition, [line 56](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L56))

```lean
def updateForwardState (goal : MVarId) : NormM Unit
```

`Aesop.eraseForwardRuleMatch` (definition, [line 61](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L61))

```lean
def eraseForwardRuleMatch (m : ForwardRuleMatch) : NormM Unit
```

`Aesop.applyDiffToForwardState` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L64))

```lean
def applyDiffToForwardState (diff : GoalDiff) : NormM Unit
```

`Aesop.NormRuleResult` (inductive type, [line 69](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L69))

```lean
inductive NormRuleResult
  | succeeded (goal : MVarId) (steps? : Option (Array Script.LazyStep))
  | proved (steps? : Option (Array Script.LazyStep))
```

`Aesop.NormRuleResult.newGoal?` (definition, [line 75](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L75))

```lean
def newGoal? : NormRuleResult → Option MVarId
```

`Aesop.NormRuleResult.steps?` (definition, [line 79](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L79))

```lean
def steps? : NormRuleResult → Option (Array Script.LazyStep)
```

`Aesop.optNormRuleResultEmoji` (definition, [line 84](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L84))

```lean
def optNormRuleResultEmoji : Option NormRuleResult → String
```

`Aesop.withNormTraceNode` (definition, [line 90](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L90))

```lean
def withNormTraceNode (ruleName : DisplayRuleName)
    (k : NormM (Option NormRuleResult)) : NormM (Option NormRuleResult)
```

`Aesop.runNormRuleTac` (definition, [line 105](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L105))

> On success, returns the rule tactic's result, the new forward state and the
> new forward rule matches. If `rule` corresponds to some forward rule matches,
> returns the matches as well.

```lean
def runNormRuleTac (rule : NormRule) (input : RuleTacInput) (fs : ForwardState)
    (rs : LocalRuleSet) :
    NormM $
      Option (NormRuleResult × ForwardState × Std.HashSet FVarId) ×
      Array ForwardRuleMatch
```

`Aesop.runNormRule` (definition, [line 138](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L138))

```lean
def runNormRule (goal : MVarId) (mvars : UnorderedArraySet MVarId)
    (rule : IndexMatchResult NormRule) : NormM (Option NormRuleResult)
```

`Aesop.runFirstNormRule` (definition, [line 158](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L158))

```lean
def runFirstNormRule (goal : MVarId) (mvars : UnorderedArraySet MVarId)
    (rules : Array (IndexMatchResult NormRule)) :
    NormM (Option (DisplayRuleName × NormRuleResult))
```

`Aesop.mkNormSimpScriptStep` (definition, [line 167](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L167))

```lean
def mkNormSimpScriptStep
    (preGoal : MVarId) (postGoal? : Option MVarId)
    (preState postState : Meta.SavedState) (usedTheorems : Simp.UsedSimps) :
    NormM Script.LazyStep
```

`Aesop.normSimpCore` (definition, [line 190](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L190))

```lean
def normSimpCore (goal : MVarId) (goalMVars : Std.HashSet MVarId) :
    NormM (Option NormRuleResult)
```

`Aesop.checkSimp` (definition, [line 249](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L249))

```lean
def checkSimp (name : String) (mayCloseGoal : Bool) (goal : MVarId)
    (x : NormM (Option NormRuleResult)) : NormM (Option NormRuleResult)
```

`Aesop.normSimp` (definition, [line 271](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L271))

```lean
def normSimp (goal : MVarId) (goalMVars : Std.HashSet MVarId) :
    NormM (Option NormRuleResult)
```

`Aesop.normUnfoldCore` (definition, [line 281](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L281))

```lean
def normUnfoldCore (goal : MVarId) : NormM (Option NormRuleResult)
```

`Aesop.normUnfold` (definition, [line 292](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L292))

```lean
def normUnfold (goal : MVarId) : NormM (Option NormRuleResult)
```

`Aesop.NormSeqResult` (inductive type, [line 301](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L301))

```lean
inductive NormSeqResult where
  | proved (script : Array (DisplayRuleName × Option (Array Script.LazyStep)))
  | changed (goal : MVarId)
      (script : Array (DisplayRuleName × Option (Array Script.LazyStep)))
  | unchanged
```

`Aesop.NormRuleResult.toNormSeqResult` (definition, [line 307](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L307))

```lean
def NormRuleResult.toNormSeqResult (ruleName : DisplayRuleName) :
    NormRuleResult → NormSeqResult
```

`Aesop.optNormRuleResultToNormSeqResult` (definition, [line 312](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L312))

```lean
def optNormRuleResultToNormSeqResult :
    Option (DisplayRuleName × NormRuleResult) → NormSeqResult
```

`Aesop.NormStep` (abbreviation, [line 317](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L317))

```lean
abbrev NormStep
```

`Aesop.runNormSteps` (definition, [line 321](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L321))

```lean
def runNormSteps (goal : MVarId) (steps : Array NormStep)
    (stepsNe : 0 < steps.size) : NormM NormSeqResult
```

`Aesop.NormStep.runPreSimpRules` (definition, [line 364](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L364))

```lean
def runPreSimpRules (mvars : UnorderedArraySet MVarId) : NormStep
```

`Aesop.NormStep.runPostSimpRules` (definition, [line 369](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L369))

```lean
def runPostSimpRules (mvars : UnorderedArraySet MVarId) : NormStep
```

`Aesop.NormStep.unfold` (definition, [line 374](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L374))

```lean
def unfold : NormStep
```

`Aesop.NormStep.simp` (definition, [line 382](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L382))

```lean
def simp (mvars : Std.HashSet MVarId) : NormStep
```

`Aesop.normalizeGoalMVar` (definition, [line 392](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L392))

```lean
partial def normalizeGoalMVar (goal : MVarId)
    (mvars : UnorderedArraySet MVarId) : NormM NormSeqResult
```

`Aesop.normalizeGoalIfNecessary` (definition, [line 405](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean#L405))

```lean
def normalizeGoalIfNecessary (gref : GoalRef) [Aesop.Queue Q] :
    SearchM Q Bool
```

## Depends on

- [ApplyGoalDiff](../../forward/state-2/applygoaldiff.md)
- [RuleTac](../../../part-02/ruletac.md)
- [Expansion/Basic](basic.md)
- [Simp](simp.md)
- [RuleSelection](../ruleselection.md)
- [Tree/State](../../tree/state.md)

## Sources

- [Aesop/Search/Expansion/Norm.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Norm.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Search.Expansion.Norm.json)
