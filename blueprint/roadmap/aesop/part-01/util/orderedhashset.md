---
catalog: module
lean: Aesop.OrderedHashSet, Aesop.OrderedHashSet.emptyWithCapacity, Aesop.OrderedHashSet.insert, Aesop.OrderedHashSet.insertMany, Aesop.OrderedHashSet.ofArray, Aesop.OrderedHashSet.contains, Aesop.OrderedHashSet.foldlM, Aesop.OrderedHashSet.foldl, Aesop.OrderedHashSet.foldrM, Aesop.OrderedHashSet.foldr
statement: formalized
proof: formalized
---

# OrderedHashSet

`Aesop.Util.OrderedHashSet`, in [Aesop/Util/OrderedHashSet.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean).

`Aesop.OrderedHashSet` (structure, [line 12](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L12))

> A hash set that preserves the order of insertions.

```lean
structure OrderedHashSet (α) [BEq α] [Hashable α] where
  toArray : Array α
  toHashSet : HashSet α
  deriving Inhabited
```

`Aesop.OrderedHashSet.emptyWithCapacity` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L24))

```lean
def emptyWithCapacity (n : Nat) : OrderedHashSet α
```

`Aesop.OrderedHashSet.insert` (definition, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L28))

```lean
def insert (x : α) (s : OrderedHashSet α) : OrderedHashSet α
```

`Aesop.OrderedHashSet.insertMany` (definition, [line 36](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L36))

```lean
def insertMany [ForIn Id ρ α] (xs : ρ) (s : OrderedHashSet α) :
    OrderedHashSet α
```

`Aesop.OrderedHashSet.ofArray` (definition, [line 43](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L43))

```lean
def ofArray (xs : Array α) : OrderedHashSet α
```

`Aesop.OrderedHashSet.contains` (definition, [line 46](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L46))

```lean
def contains (x : α) (s : OrderedHashSet α) : Bool
```

`Aesop.OrderedHashSet.foldlM` (definition, [line 56](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L56))

```lean
def foldlM [Monad m] (f : β → α → m β) (init : β)
    (s : OrderedHashSet α) : m β
```

`Aesop.OrderedHashSet.foldl` (definition, [line 60](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L60))

```lean
def foldl (f : β → α → β) (init : β) (s : OrderedHashSet α) : β
```

`Aesop.OrderedHashSet.foldrM` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L64))

```lean
def foldrM [Monad m] (f : α → β → m β) (init : β)
    (s : OrderedHashSet α) : m β
```

`Aesop.OrderedHashSet.foldr` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean#L68))

```lean
def foldr (f : α → β → β) (init : β) (s : OrderedHashSet α) : β
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Util/OrderedHashSet.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/OrderedHashSet.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Util.OrderedHashSet.json)
