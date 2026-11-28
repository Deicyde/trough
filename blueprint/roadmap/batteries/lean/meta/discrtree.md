---
catalog: module
lean: Lean.Meta.DiscrTree.Key.cmp, Lean.Meta.DiscrTree.Trie.mergePreservingDuplicates, Lean.Meta.DiscrTree.mergePreservingDuplicates
statement: formalized
proof: formalized
---

# DiscrTree

`Batteries.Lean.Meta.DiscrTree`, in [Batteries/Lean/Meta/DiscrTree.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/DiscrTree.lean), by Jannis Limperg, Kim Morrison.

`Lean.Meta.DiscrTree.Key.cmp` (definition, [line 23](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/DiscrTree.lean#L23))

> Compare two `Key`s. The ordering is total but otherwise arbitrary. (It uses
> `Name.quickCmp` internally.)

```lean
protected def cmp : Key → Key → Ordering
```

`Lean.Meta.DiscrTree.Trie.mergePreservingDuplicates` (definition, [line 41](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/DiscrTree.lean#L41))

> Merge two `Trie`s. Duplicate values are preserved.

```lean
partial def mergePreservingDuplicates (t₁ t₂ : Trie α) : Trie α
```

`Lean.Meta.DiscrTree.mergePreservingDuplicates` (definition, [line 59](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/DiscrTree.lean#L59))

> Merge two `DiscrTree`s. Duplicate values are preserved.

```lean
def mergePreservingDuplicates (t u : DiscrTree α) : DiscrTree α
```

## Depends on

- [PersistentHashMap](../persistenthashmap.md)

## Proof depends on

- [Merge](../../data/part-01/array/merge.md)

## Sources

- [Batteries/Lean/Meta/DiscrTree.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/DiscrTree.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.Meta.DiscrTree.json)
