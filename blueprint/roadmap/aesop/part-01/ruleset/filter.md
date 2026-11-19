---
catalog: module
lean: Aesop.RuleFilter, Aesop.RuleFilter.matchesPhase, Aesop.RuleFilter.matchesBuilder, Aesop.RuleFilter.«matches», Aesop.RuleFilter.matchesSimpTheorem?, Aesop.RuleFilter.matchesLocalNormSimpRule?, Aesop.RuleSetNameFilter, Aesop.RuleSetNameFilter.all, Aesop.RuleSetNameFilter.matchesAll, Aesop.RuleSetNameFilter.«matches», Aesop.RuleSetNameFilter.matchedRuleSetNames
statement: formalized
proof: formalized
---

# Filter

`Aesop.RuleSet.Filter`, in [Aesop/RuleSet/Filter.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean), by Jannis Limperg.

`Aesop.RuleFilter` (structure, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L17))

```lean
structure RuleFilter where
  name : Name
  scope : ScopeName
  /--
  `#[]` means 'match any builder'
  -/
  builders : Array BuilderName
  /--
  `#[]` means 'match any phase'
  -/
  phases : Array PhaseName
```

`Aesop.RuleFilter.matchesPhase` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L31))

```lean
def matchesPhase (f : RuleFilter) (p : PhaseName) : Bool
```

`Aesop.RuleFilter.matchesBuilder` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L34))

```lean
def matchesBuilder (f : RuleFilter) (b : BuilderName) : Bool
```

`Aesop.RuleFilter.«matches»` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L37))

```lean
def «matches» (f : RuleFilter) (n : RuleName) : Bool
```

`Aesop.RuleFilter.matchesSimpTheorem?` (definition, [line 43](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L43))

```lean
def matchesSimpTheorem? (f : RuleFilter) : Option Name
```

`Aesop.RuleFilter.matchesLocalNormSimpRule?` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L52))

> Returns the identifier of the local norm simp rule matched by `f`, if any.

```lean
def matchesLocalNormSimpRule? (f : RuleFilter) : Option Name
```

`Aesop.RuleSetNameFilter` (structure, [line 60](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L60))

```lean
structure RuleSetNameFilter where
  ns : Array RuleSetName -- #[] means 'match any rule set'
```

`Aesop.RuleSetNameFilter.all` (definition, [line 65](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L65))

```lean
protected def all : RuleSetNameFilter
```

`Aesop.RuleSetNameFilter.matchesAll` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L68))

```lean
def matchesAll (f : RuleSetNameFilter) : Bool
```

`Aesop.RuleSetNameFilter.«matches»` (definition, [line 71](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L71))

```lean
def «matches» (f : RuleSetNameFilter) (n : RuleSetName) : Bool
```

`Aesop.RuleSetNameFilter.matchedRuleSetNames` (definition, [line 74](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean#L74))

```lean
def matchedRuleSetNames (f : RuleSetNameFilter) : Option (Array RuleSetName)
```

## Depends on

- [Rule/Name](../rule/name.md)
- [RuleSet/Name](name.md)

## Sources

- [Aesop/RuleSet/Filter.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Filter.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleSet.Filter.json)
