---
catalog: module
lean: Lean.PersistentHashMap.ofList, Lean.PersistentHashMap.ofListWith, Lean.PersistentHashMap.ofArray, Lean.PersistentHashMap.ofArrayWith, Lean.PersistentHashMap.mergeWithM, Lean.PersistentHashMap.mergeWith
statement: formalized
proof: formalized
---

# PersistentHashMap

`Batteries.Lean.PersistentHashMap`, in [Batteries/Lean/PersistentHashMap.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/PersistentHashMap.lean), by Jannis Limperg.

`Lean.PersistentHashMap.ofList` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/PersistentHashMap.lean#L20))

> Builds a `PersistentHashMap` from a list of key-value pairs. Values of
> duplicated keys are replaced by their respective last occurrences.

```lean
def ofList (xs : List (α × β)) : PersistentHashMap α β
```

`Lean.PersistentHashMap.ofListWith` (definition, [line 27](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/PersistentHashMap.lean#L27))

> Variant of `ofList` which accepts a function that combines values of duplicated
> keys.

```lean
def ofListWith (xs : List (α × β)) (f : α → β → β → β) :
    PersistentHashMap α β
```

`Lean.PersistentHashMap.ofArray` (definition, [line 38](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/PersistentHashMap.lean#L38))

> Builds a `PersistentHashMap` from an array of key-value pairs. Values of
> duplicated keys are replaced by their respective last occurrences.

```lean
def ofArray (xs : Array (α × β)) : PersistentHashMap α β
```

`Lean.PersistentHashMap.ofArrayWith` (definition, [line 45](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/PersistentHashMap.lean#L45))

> Variant of `ofArray` which accepts a function that combines values of duplicated
> keys.

```lean
def ofArrayWith (xs : Array (α × β)) (f : α → β → β → β) :
    PersistentHashMap α β
```

`Lean.PersistentHashMap.mergeWithM` (definition, [line 57](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/PersistentHashMap.lean#L57))

> Merge two `PersistentHashMap`s. The values of keys which appear in both maps are
> combined using the monadic function `f`.

```lean
def mergeWithM [Monad m] (self other : PersistentHashMap α β)
    (f : α → β → β → m β) : m (PersistentHashMap α β)
```

`Lean.PersistentHashMap.mergeWith` (definition, [line 69](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/PersistentHashMap.lean#L69))

> Merge two `PersistentHashMap`s. The values of keys which appear in both maps are
> combined using `f`.

```lean
def mergeWith (self other : PersistentHashMap α β) (f : α → β → β → β) :
    PersistentHashMap α β
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/PersistentHashMap.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/PersistentHashMap.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.PersistentHashMap.json)
