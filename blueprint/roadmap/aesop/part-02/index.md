---
catalog: module
lean: Aesop.Index, Aesop.Index.trace, Aesop.Index.merge, Aesop.Index.add, Aesop.Index.unindex, Aesop.Index.foldM, Aesop.Index.fold, Aesop.Index.applicableRules
statement: formalized
proof: formalized
---

# Index

`Aesop.Index`, in [Aesop/Index.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean), by Jannis Limperg.

`Aesop.Index` (structure, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean#L23))

```lean
structure Index (α : Type) where
  byTarget : DiscrTree (Rule α)
  byHyp : DiscrTree (Rule α)
  unindexed : PHashSet (Rule α)
  deriving Inhabited
```

`Aesop.Index.trace` (definition, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean#L33))

```lean
def trace [ToString (Rule α)] (ri : Index α) (traceOpt : TraceOption) :
    CoreM Unit
```

`Aesop.Index.merge` (definition, [line 54](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean#L54))

```lean
def merge (ri₁ ri₂ : Index α) : Index α
```

`Aesop.Index.add` (definition, [line 60](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean#L60))

```lean
partial def add (r : Rule α) (imode : IndexingMode) (ri : Index α) :
    Index α
```

`Aesop.Index.unindex` (definition, [line 73](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean#L73))

```lean
def unindex (ri : Index α) (p : Rule α → Bool) : Index α
```

`Aesop.Index.foldM` (definition, [line 84](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean#L84))

```lean
def foldM [Monad m] (ri : Index α) (f : σ → Rule α → m σ) (init : σ) : m σ
```

`Aesop.Index.fold` (definition, [line 93](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean#L93))

```lean
def fold (ri : Index α) (f : σ → Rule α → σ) (init : σ) : σ
```

`Aesop.Index.applicableRules` (definition, [line 138](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean#L138))

```lean
def applicableRules (ri : Index α) (goal : MVarId)
    (patSubstMap : RulePatternSubstMap)
    (additionalRules : Array (IndexMatchResult (Rule α)))
    (include? : Rule α → Bool) :
    MetaM (Array (IndexMatchResult (Rule α)))
```

## Depends on

- [Index/RulePattern](../part-01/index/rulepattern.md)
- [Rule/Basic](../part-01/rule/basic.md)

## Sources

- [Aesop/Index.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.Index.json)
