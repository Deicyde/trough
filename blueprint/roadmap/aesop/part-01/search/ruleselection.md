---
catalog: module
lean: Aesop.selectNormRules, Aesop.preprocessRule, Aesop.selectSafeRules, Aesop.selectUnsafeRules
statement: formalized
proof: formalized
---

# RuleSelection

`Aesop.Search.RuleSelection`, in [Aesop/Search/RuleSelection.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/RuleSelection.lean), by Jannis Limperg.

`Aesop.selectNormRules` (definition, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/RuleSelection.lean#L19))

```lean
def selectNormRules (rs : LocalRuleSet) (fms : ForwardRuleMatches)
    (goal : MVarId) : BaseM (Array (IndexMatchResult NormRule))
```

`Aesop.preprocessRule` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/RuleSelection.lean#L23))

```lean
def preprocessRule : SafeRule
```

`Aesop.selectSafeRules` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/RuleSelection.lean#L35))

```lean
def selectSafeRules (g : Goal) :
    SearchM Q (Array (IndexMatchResult SafeRule))
```

`Aesop.selectUnsafeRules` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/RuleSelection.lean#L48))

```lean
def selectUnsafeRules (postponedSafeRules : Array PostponedSafeRule)
    (gref : GoalRef) : SearchM Q UnsafeQueue
```

## Depends on

- [SearchM](searchm.md)
- [RunMetaM](../tree/runmetam.md)

## Sources

- [Aesop/Search/RuleSelection.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/RuleSelection.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Search.RuleSelection.json)
