---
catalog: module
lean: Aesop.ForwardIndex, Aesop.ForwardIndex.trace, Aesop.ForwardIndex.merge, Aesop.ForwardIndex.insert, Aesop.ForwardIndex.get, Aesop.ForwardIndex.getRuleWithName?, Aesop.ForwardIndex.getConstRuleMatches
statement: formalized
proof: formalized
---

# Index/Forward

`Aesop.Index.Forward`, in [Aesop/Index/Forward.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean), by Xavier Généreux, Jannis Limperg.

`Aesop.ForwardIndex` (structure, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean#L20))

> Index for forward rules.

```lean
structure ForwardIndex where
  /-- Maps expressions `T` to all tuples `(r, i)` where `r : ForwardRule`,
  `i : PremiseIndex` and the `i`-th argument of the type of `r.expr` (counting
  from zero) likely unifies with `T`. -/
  tree : DiscrTree (ForwardRule × PremiseIndex)
  /-- Indexes the forward rules contained in `tree` by name. -/
  nameToRule : PHashMap RuleName ForwardRule
  /-- Constant forward rules, i.e. forward rules that have no premises and no
  rule pattern. -/
  constRules : PHashSet ForwardRule
  deriving Inhabited
```

`Aesop.ForwardIndex.trace` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean#L38))

> Trace the rules contained in `idx` if `traceOpt` is enabled.

```lean
protected def trace (traceOpt : TraceOption) (idx : ForwardIndex) : CoreM Unit
```

`Aesop.ForwardIndex.merge` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean#L48))

> Merge two indices.

```lean
def merge (idx₁ idx₂ : ForwardIndex) : ForwardIndex
```

`Aesop.ForwardIndex.insert` (definition, [line 54](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean#L54))

> Insert a forward rule into the `ForwardIndex`.

```lean
def insert (r : ForwardRule) (idx : ForwardIndex) : ForwardIndex
```

`Aesop.ForwardIndex.get` (definition, [line 74](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean#L74))

> Get the forward rules whose maximal premises likely unify with `e`.
> Each returned pair `(r, i)` contains a rule `r` and the index `i` of the premise
> of `r` that likely unifies with `e`.

```lean
def get (idx : ForwardIndex) (e : Expr) :
    MetaM (Array (ForwardRule × PremiseIndex))
```

`Aesop.ForwardIndex.getRuleWithName?` (definition, [line 79](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean#L79))

> Get the forward rule with the given rule name.

```lean
def getRuleWithName? (n : RuleName) (idx : ForwardIndex) : Option ForwardRule
```

`Aesop.ForwardIndex.getConstRuleMatches` (definition, [line 85](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean#L85))

> Get forward rule matches for the constant forward rules (i.e., those with no
> premises and no rule pattern). Accordingly, the returned matches contain no
> hypotheses.

```lean
def getConstRuleMatches (idx : ForwardIndex) : Array ForwardRuleMatch
```

## Depends on

- [Types](../forward/match-2/types.md)

## Sources

- [Aesop/Index/Forward.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Forward.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Index.Forward.json)
