---
catalog: module
lean: Aesop.RulePatternSubstMap, Aesop.RulePatternSubstMap.insertArray, Aesop.RulePatternSubstMap.ofArray, Aesop.RulePatternSubstMap.toFlatArray, Aesop.RulePatternIndex.Entry, Aesop.RulePatternIndex, Aesop.RulePatternIndex.add, Aesop.RulePatternIndex.merge, Aesop.RulePatternIndex.getSingle, Aesop.RulePatternIndex.getCore, Aesop.RulePatternIndex.get, Aesop.RulePatternIndex.getInLocalDeclCore, Aesop.RulePatternIndex.getInLocalDecl, Aesop.RulePatternIndex.getInGoal
statement: formalized
proof: formalized
---

# Index/RulePattern

`Aesop.Index.RulePattern`, in [Aesop/Index/RulePattern.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean), by Jannis Limperg.

`Aesop.RulePatternSubstMap` (abbreviation, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L22))

> A map from rule names to rule pattern substitutions. When run on a goal,
> the rule pattern index returns such a map.

```lean
abbrev RulePatternSubstMap
```

`Aesop.RulePatternSubstMap.insertArray` (definition, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L28))

> Insert an array of rule pattern substitutions into a rule pattern
> substitution map.

```lean
def insertArray (xs : Array (RuleName × Substitution))
    (m : RulePatternSubstMap) : RulePatternSubstMap
```

`Aesop.RulePatternSubstMap.ofArray` (definition, [line 36](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L36))

> Build a rule pattern substitution map from an array of substitutions.

```lean
def ofArray (xs : Array (RuleName × Substitution)) : RulePatternSubstMap
```

`Aesop.RulePatternSubstMap.toFlatArray` (definition, [line 40](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L40))

> Convert a rule pattern substitution map to a flat array of substitutions.

```lean
def toFlatArray (m : RulePatternSubstMap) : Array (RuleName × Substitution)
```

`Aesop.RulePatternIndex.Entry` (structure, [line 49](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L49))

> An entry of the rule pattern index.

```lean
structure RulePatternIndex.Entry where
  /-- The name of the rule to which the pattern belongs. -/
  name : RuleName
  /-- The rule's pattern. We assume that there is at most one pattern per
  rule. -/
  pattern : RulePattern
  deriving Inhabited
```

`Aesop.RulePatternIndex` (structure, [line 63](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L63))

> A rule pattern index. Maps expressions `e` to rule patterns that likely
> unify with `e`.

```lean
structure RulePatternIndex where
  /-- The index. -/
  tree : DiscrTree RulePatternIndex.Entry
  /-- `true` iff the index contains no patterns. -/
  isEmpty : Bool
  deriving Inhabited
```

`Aesop.RulePatternIndex.add` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L76))

> Add a rule pattern to the index.

```lean
def add (name : RuleName) (pattern : RulePattern) (idx : RulePatternIndex) :
    RulePatternIndex
```

`Aesop.RulePatternIndex.merge` (definition, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L82))

> Merge two rule pattern indices. Patterns that appear in both indices appear
> twice in the result.

```lean
def merge (idx₁ idx₂ : RulePatternIndex) : RulePatternIndex
```

`Aesop.RulePatternIndex.getSingle` (definition, [line 93](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L93))

> Get rule pattern substitutions for the patterns that match `e`.

```lean
def getSingle (e : Expr) (idx : RulePatternIndex) :
    BaseM (Array (RuleName × Substitution))
```

`Aesop.RulePatternIndex.getCore` (definition, [line 106](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L106))

> Get all substitutions of the rule patterns that match a subexpression of
> `e`. Subexpressions containing bound variables are not considered. The returned
> array may contain duplicates.

```lean
def getCore (e : Expr) (idx : RulePatternIndex) :
    BaseM (Array (RuleName × Substitution))
```

`Aesop.RulePatternIndex.get` (definition, [line 128](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L128))

```lean
def get (e : Expr) (idx : RulePatternIndex) : BaseM RulePatternSubstMap
```

`Aesop.RulePatternIndex.getInLocalDeclCore` (definition, [line 134](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L134))

> Get all substitutions of the rule patterns that match a subexpression of
> the given local declaration. Subexpressions containing bound variables are not
> considered.

```lean
def getInLocalDeclCore (acc : RulePatternSubstMap) (ldecl : LocalDecl)
    (idx : RulePatternIndex) : BaseM RulePatternSubstMap
```

`Aesop.RulePatternIndex.getInLocalDecl` (definition, [line 146](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L146))

```lean
def getInLocalDecl (ldecl : LocalDecl) (idx : RulePatternIndex) :
    BaseM RulePatternSubstMap
```

`Aesop.RulePatternIndex.getInGoal` (definition, [line 153](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean#L153))

> Get all substitutions of the rule patterns that match a subexpression of
> a hypothesis or the target. Subexpressions containing bound variables are not
> considered.

```lean
def getInGoal (goal : MVarId) (idx : RulePatternIndex) :
    BaseM RulePatternSubstMap
```

## Depends on

- [Aesop/RulePattern](../../part-02/rulepattern.md)
- [OrderedHashSet](../util/orderedhashset.md)

## Sources

- [Aesop/Index/RulePattern.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/RulePattern.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Index.RulePattern.json)
