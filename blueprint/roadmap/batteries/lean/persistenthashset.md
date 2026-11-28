---
catalog: module
lean: Lean.PersistentHashSet.anyM, Lean.PersistentHashSet.any, Lean.PersistentHashSet.allM, Lean.PersistentHashSet.all, Lean.PersistentHashSet.insertMany, Lean.PersistentHashSet.ofArray, Lean.PersistentHashSet.ofList, Lean.PersistentHashSet.merge
statement: formalized
proof: formalized
---

# PersistentHashSet

`Batteries.Lean.PersistentHashSet`, in [Batteries/Lean/PersistentHashSet.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean), by Jannis Limperg.

`Lean.PersistentHashSet.anyM` (definition, [line 29](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean#L29))

> Returns `true` if `f` returns `true` for any element of the set.

```lean
def anyM [Monad m] (s : PersistentHashSet α) (f : α → m Bool) : m Bool
```

`Lean.PersistentHashSet.any` (definition, [line 39](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean#L39))

> Returns `true` if `f` returns `true` for any element of the set.

```lean
def any (s : PersistentHashSet α) (f : α → Bool) : Bool
```

`Lean.PersistentHashSet.allM` (definition, [line 46](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean#L46))

> Returns `true` if `f` returns `true` for all elements of the set.

```lean
def allM [Monad m] (s : PersistentHashSet α) (f : α → m Bool) : m Bool
```

`Lean.PersistentHashSet.all` (definition, [line 56](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean#L56))

> Returns `true` if `f` returns `true` for all elements of the set.

```lean
def all (s : PersistentHashSet α) (f : α → Bool) : Bool
```

`Lean.PersistentHashSet.insertMany` (definition, [line 65](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean#L65))

> Insert all elements from a collection into a `PersistentHashSet`.

```lean
def insertMany [ForIn Id ρ α] (s : PersistentHashSet α) (as : ρ) :
    PersistentHashSet α
```

`Lean.PersistentHashSet.ofArray` (definition, [line 76](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean#L76))

> Obtain a `PersistentHashSet` from an array.

```lean
protected def ofArray [BEq α] [Hashable α] (as : Array α) : PersistentHashSet α
```

`Lean.PersistentHashSet.ofList` (definition, [line 83](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean#L83))

> Obtain a `PersistentHashSet` from a list.

```lean
protected def ofList [BEq α] [Hashable α] (as : List α) : PersistentHashSet α
```

`Lean.PersistentHashSet.merge` (definition, [line 90](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean#L90))

> Merge two `PersistentHashSet`s.

```lean
def merge (s t : PersistentHashSet α) : PersistentHashSet α
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/PersistentHashSet.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/PersistentHashSet.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.PersistentHashSet.json)
