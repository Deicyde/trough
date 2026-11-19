---
catalog: module
lean: Aesop.RuleResult, Aesop.RuleResult.toEmoji, Aesop.RuleResult.isSuccessful, Aesop.SafeRuleResult, Aesop.SafeRuleResult.toEmoji, Aesop.SafeRuleResult.isSuccessfulOrPostponed, Aesop.runRegularRuleTac, Aesop.addRapps, Aesop.withRuleTraceNode, Aesop.runRegularRuleCore, Aesop.runSafeRule, Aesop.runUnsafeRule, Aesop.SafeRulesResult, Aesop.SafeRulesResult.toEmoji, Aesop.runFirstSafeRule, Aesop.applyPostponedSafeRule, Aesop.runFirstUnsafeRule, Aesop.expandGoal
statement: formalized
proof: formalized
---

# Expansion

`Aesop.Search.Expansion`, in [Aesop/Search/Expansion.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean), by Jannis Limperg.

`Aesop.RuleResult` (inductive type, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L25))

```lean
inductive RuleResult
  | proved (newRapps : Array RappRef)
  | succeeded (newRapps : Array RappRef)
  | failed
```

`Aesop.RuleResult.toEmoji` (definition, [line 32](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L32))

```lean
def toEmoji : RuleResult → String
```

`Aesop.RuleResult.isSuccessful` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L37))

```lean
def isSuccessful
```

`Aesop.SafeRuleResult` (inductive type, [line 43](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L43))

```lean
inductive SafeRuleResult
  | regular (result : RuleResult)
  | postponed (result : PostponedSafeRule)
```

`Aesop.SafeRuleResult.toEmoji` (definition, [line 49](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L49))

```lean
def toEmoji : SafeRuleResult → String
```

`Aesop.SafeRuleResult.isSuccessfulOrPostponed` (definition, [line 53](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L53))

```lean
def isSuccessfulOrPostponed
```

`Aesop.runRegularRuleTac` (definition, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L59))

```lean
def runRegularRuleTac (goal : Goal) (tac : RuleTac) (ruleName : RuleName)
    (indexMatchLocations : Array IndexMatchLocation)
    (patternSubsts? : Option (Array Substitution))
    (options : Options') : BaseM (Except Exception RuleTacOutput)
```

`Aesop.addRapps` (definition, [line 72](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L72))

```lean
def addRapps (parentRef : GoalRef) (rule : RegularRule)
    (rapps : Array RuleApplication) : SearchM Q RuleResult
```

`Aesop.withRuleTraceNode` (definition, [line 110](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L110))

```lean
def withRuleTraceNode (ruleName : RuleName)
    (toEmoji : α → String) (suffix : String) (k : SearchM Q α) : SearchM Q α
```

`Aesop.runRegularRuleCore` (definition, [line 118](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L118))

```lean
def runRegularRuleCore (parentRef : GoalRef) (rule : RegularRule)
    (indexMatchLocations : Array IndexMatchLocation)
    (patternSubsts? : Option (Array Substitution)) :
    SearchM Q (Option RuleTacOutput)
```

`Aesop.runSafeRule` (definition, [line 136](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L136))

```lean
def runSafeRule (parentRef : GoalRef) (matchResult : IndexMatchResult SafeRule) :
    SearchM Q SafeRuleResult
```

`Aesop.runUnsafeRule` (definition, [line 160](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L160))

```lean
def runUnsafeRule (parentRef : GoalRef)
    (matchResult : IndexMatchResult UnsafeRule) : SearchM Q RuleResult
```

`Aesop.SafeRulesResult` (inductive type, [line 171](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L171))

```lean
inductive SafeRulesResult
  | proved (newRapps : Array RappRef)
  | succeeded (newRapps : Array RappRef)
  | failed (postponed : Array PostponedSafeRule)
  | skipped
```

`Aesop.SafeRulesResult.toEmoji` (definition, [line 177](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L177))

```lean
def SafeRulesResult.toEmoji : SafeRulesResult → String
```

`Aesop.runFirstSafeRule` (definition, [line 183](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L183))

```lean
def runFirstSafeRule (gref : GoalRef) : SearchM Q SafeRulesResult
```

`Aesop.applyPostponedSafeRule` (definition, [line 202](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L202))

```lean
def applyPostponedSafeRule (r : PostponedSafeRule) (parentRef : GoalRef) :
    SearchM Q RuleResult
```

`Aesop.runFirstUnsafeRule` (definition, [line 207](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L207))

```lean
partial def runFirstUnsafeRule (postponedSafeRules : Array PostponedSafeRule)
    (parentRef : GoalRef) : SearchM Q RuleResult
```

`Aesop.expandGoal` (definition, [line 232](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean#L232))

```lean
def expandGoal (gref : GoalRef) : SearchM Q RuleResult
```

## Depends on

- [UpdateGoal](../forward/state-2/updategoal.md)
- [Norm](expansion-2/norm.md)
- [AddRapp](../tree/addrapp.md)

## Sources

- [Aesop/Search/Expansion.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Search.Expansion.json)
