---
catalog: module
lean: Aesop.NormRuleInfo, Aesop.NormRule, Aesop.defaultNormPenalty, Aesop.defaultSimpRulePriority, Aesop.Safety, Aesop.SafeRuleInfo, Aesop.SafeRule, Aesop.defaultSafePenalty, Aesop.UnsafeRuleInfo, Aesop.UnsafeRule, Aesop.defaultSuccessProbability, Aesop.RegularRule, Aesop.RegularRule.successProbability, Aesop.RegularRule.isSafe, Aesop.RegularRule.isUnsafe, Aesop.RegularRule.withRule, Aesop.RegularRule.name, Aesop.RegularRule.indexingMode, Aesop.RegularRule.tac, Aesop.NormSimpRule, Aesop.LocalNormSimpRule, Aesop.LocalNormSimpRule.name, Aesop.UnfoldRule, Aesop.UnfoldRule.name
statement: formalized
proof: formalized
---

# Rule

`Aesop.Rule`, in [Aesop/Rule.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean), by Jannis Limperg, Asta Halkjær From.

> ### Normalisation Rules

`Aesop.NormRuleInfo` (structure, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L19))

```lean
structure NormRuleInfo where
  penalty : Int
  deriving Inhabited
```

`Aesop.NormRule` (abbreviation, [line 32](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L32))

```lean
abbrev NormRule
```

`Aesop.defaultNormPenalty` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L37))

```lean
def defaultNormPenalty : Int
```

`Aesop.defaultSimpRulePriority` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L39))

```lean
def defaultSimpRulePriority : Int
```

> ### Safe and Almost Safe Rules

`Aesop.Safety` (inductive type, [line 44](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L44))

```lean
inductive Safety
  | safe
  | almostSafe
  deriving Inhabited
```

`Aesop.SafeRuleInfo` (structure, [line 58](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L58))

```lean
structure SafeRuleInfo where
  penalty : Int
  safety : Safety
  deriving Inhabited
```

`Aesop.SafeRule` (abbreviation, [line 72](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L72))

```lean
abbrev SafeRule
```

`Aesop.defaultSafePenalty` (definition, [line 77](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L77))

```lean
def defaultSafePenalty : Int
```

> ### Unsafe Rules

`Aesop.UnsafeRuleInfo` (structure, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L82))

```lean
structure UnsafeRuleInfo where
  successProbability : Percent
  deriving Inhabited
```

`Aesop.UnsafeRule` (abbreviation, [line 97](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L97))

```lean
abbrev UnsafeRule
```

`Aesop.defaultSuccessProbability` (definition, [line 102](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L102))

```lean
def defaultSuccessProbability : Percent
```

> ### Regular Rules

`Aesop.RegularRule` (inductive type, [line 107](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L107))

```lean
inductive RegularRule
  | safe (r : SafeRule)
  | «unsafe» (r : UnsafeRule)
  deriving Inhabited, BEq
```

`Aesop.RegularRule.successProbability` (definition, [line 119](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L119))

```lean
def successProbability : RegularRule → Percent
```

`Aesop.RegularRule.isSafe` (definition, [line 123](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L123))

```lean
def isSafe : RegularRule → Bool
```

`Aesop.RegularRule.isUnsafe` (definition, [line 127](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L127))

```lean
def isUnsafe : RegularRule → Bool
```

`Aesop.RegularRule.withRule` (definition, [line 132](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L132))

```lean
def withRule (f : ∀ {α}, Rule α → β) : RegularRule → β
```

`Aesop.RegularRule.name` (definition, [line 136](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L136))

```lean
def name (r : RegularRule) : RuleName
```

`Aesop.RegularRule.indexingMode` (definition, [line 139](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L139))

```lean
def indexingMode (r : RegularRule) : IndexingMode
```

`Aesop.RegularRule.tac` (definition, [line 142](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L142))

```lean
def tac (r : RegularRule) : RuleTacDescr
```

> ### Normalisation Simp Rules

`Aesop.NormSimpRule` (structure, [line 155](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L155))

> A global rule for the norm simplifier. Each `SimpEntry` represents a member
> of the simp set, e.g. a declaration whose type is an equality or a smart
> unfolding theorem for a declaration.

```lean
structure NormSimpRule where
  name : RuleName
  entries : Array SimpEntry
  deriving Inhabited
```

`Aesop.LocalNormSimpRule` (structure, [line 174](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L174))

> A local rule for the norm simplifier.

```lean
structure LocalNormSimpRule where
  id : Name
  simpTheorem : Term
  deriving Inhabited
```

`Aesop.LocalNormSimpRule.name` (definition, [line 187](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L187))

```lean
def name (r : LocalNormSimpRule) : RuleName
```

`Aesop.UnfoldRule` (structure, [line 193](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L193))

```lean
structure UnfoldRule where
  decl : Name
  unfoldThm? : Option Name
  deriving Inhabited
```

`Aesop.UnfoldRule.name` (definition, [line 206](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean#L206))

```lean
def name (r : UnfoldRule) : RuleName
```

## Depends on

- [Rule/Basic](../part-01/rule/basic.md)

## Sources

- [Aesop/Rule.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.Rule.json)
