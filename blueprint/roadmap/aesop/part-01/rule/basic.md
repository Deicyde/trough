---
catalog: module
lean: Aesop.Rule, Aesop.Rule.compareByPriority, Aesop.Rule.compareByName, Aesop.Rule.compareByPriorityThenName, Aesop.Rule.map, Aesop.Rule.mapM
statement: formalized
proof: formalized
---

# Rule/Basic

`Aesop.Rule.Basic`, in [Aesop/Rule/Basic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Basic.lean), by Jannis Limperg.

`Aesop.Rule` (structure, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Basic.lean#L16))

```lean
structure Rule (α : Type) where
  name : RuleName
  indexingMode : IndexingMode
  pattern? : Option RulePattern
  extra : α
  tac : RuleTacDescr
  deriving Inhabited
```

`Aesop.Rule.compareByPriority` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Basic.lean#L35))

```lean
def compareByPriority [Ord α] (r s : Rule α) : Ordering
```

`Aesop.Rule.compareByName` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Basic.lean#L38))

```lean
def compareByName (r s : Rule α) : Ordering
```

`Aesop.Rule.compareByPriorityThenName` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Basic.lean#L41))

```lean
def compareByPriorityThenName [Ord α] (r s : Rule α) : Ordering
```

`Aesop.Rule.map` (definition, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Basic.lean#L45))

```lean
protected def map (f : α → β) (r : Rule α) : Rule β
```

`Aesop.Rule.mapM` (definition, [line 49](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Basic.lean#L49))

```lean
protected def mapM [Monad m] (f : α → m β) (r : Rule α) : m (Rule β)
```

## Depends on

- [Descr](../ruletac/descr.md)

## Sources

- [Aesop/Rule/Basic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Basic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Rule.Basic.json)
