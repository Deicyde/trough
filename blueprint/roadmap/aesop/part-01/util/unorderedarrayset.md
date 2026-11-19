---
catalog: module
lean: Aesop.UnorderedArraySet, Aesop.UnorderedArraySet.empty, Aesop.UnorderedArraySet.singleton, Aesop.UnorderedArraySet.insert, Aesop.UnorderedArraySet.ofDeduplicatedArray, Aesop.UnorderedArraySet.ofSortedArray, Aesop.UnorderedArraySet.ofArray, Aesop.UnorderedArraySet.ofArraySlow, Aesop.UnorderedArraySet.ofHashSet, Aesop.UnorderedArraySet.ofPersistentHashSet, Aesop.UnorderedArraySet.toArray, Aesop.UnorderedArraySet.erase, Aesop.UnorderedArraySet.filterM, Aesop.UnorderedArraySet.filter, Aesop.UnorderedArraySet.merge, Aesop.UnorderedArraySet.contains, Aesop.UnorderedArraySet.foldM, Aesop.UnorderedArraySet.fold, Aesop.UnorderedArraySet.partition, Aesop.UnorderedArraySet.size, Aesop.UnorderedArraySet.isEmpty, Aesop.UnorderedArraySet.anyM, Aesop.UnorderedArraySet.any, Aesop.UnorderedArraySet.allM, Aesop.UnorderedArraySet.all
statement: formalized
proof: formalized
---

# UnorderedArraySet

`Aesop.Util.UnorderedArraySet`, in [Aesop/Util/UnorderedArraySet.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean), by Jannis Limperg.

`Aesop.UnorderedArraySet` (structure, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L17))

```lean
structure UnorderedArraySet (α) [BEq α] where
  private mk ::
  private rep : Array α
  deriving Inhabited
```

`Aesop.UnorderedArraySet.empty` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L27))

> O(1)

```lean
protected def empty : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.singleton` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L34))

> O(1)

```lean
protected def singleton (a : α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.insert` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L38))

> O(n)

```lean
def insert (x : α) : UnorderedArraySet α → UnorderedArraySet α
```

`Aesop.UnorderedArraySet.ofDeduplicatedArray` (definition, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L42))

> Precondition: `xs` contains no duplicates.

```lean
protected def ofDeduplicatedArray (xs : Array α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.ofSortedArray` (definition, [line 46](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L46))

> Precondition: `xs` is sorted.

```lean
protected def ofSortedArray (xs : Array α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.ofArray` (definition, [line 51](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L51))

> O(n*log(n))

```lean
protected def ofArray [ord : Ord α] (xs : Array α) :
    UnorderedArraySet α
```

`Aesop.UnorderedArraySet.ofArraySlow` (definition, [line 56](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L56))

> O(n^2)

```lean
protected def ofArraySlow (xs : Array α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.ofHashSet` (definition, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L59))

```lean
protected def ofHashSet [Hashable α] (xs : Std.HashSet α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.ofPersistentHashSet` (definition, [line 62](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L62))

```lean
protected def ofPersistentHashSet [Hashable α] (xs : PersistentHashSet α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.toArray` (definition, [line 65](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L65))

```lean
protected def toArray (s : UnorderedArraySet α) : Array α
```

`Aesop.UnorderedArraySet.erase` (definition, [line 69](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L69))

> O(n)

```lean
def erase (x : α) (s : UnorderedArraySet α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.filterM` (definition, [line 73](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L73))

> O(n)

```lean
def filterM [Monad m] (p : α → m Bool) (s : UnorderedArraySet α) :
    m (UnorderedArraySet α)
```

`Aesop.UnorderedArraySet.filter` (definition, [line 78](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L78))

> O(n)

```lean
def filter (p : α → Bool) (s : UnorderedArraySet α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.merge` (definition, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L82))

> O(n*m)

```lean
def merge (s t : UnorderedArraySet α) : UnorderedArraySet α
```

`Aesop.UnorderedArraySet.contains` (definition, [line 89](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L89))

> O(n)

```lean
def contains (x : α) (s : UnorderedArraySet α) : Bool
```

`Aesop.UnorderedArraySet.foldM` (definition, [line 93](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L93))

> O(n)

```lean
def foldM [Monad m] (f : σ → α → m σ) (init : σ) (s : UnorderedArraySet α) :
    m σ
```

`Aesop.UnorderedArraySet.fold` (definition, [line 101](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L101))

> O(n)

```lean
def fold (f : σ → α → σ) (init : σ) (s : UnorderedArraySet α) : σ
```

`Aesop.UnorderedArraySet.partition` (definition, [line 104](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L104))

```lean
def partition (f : α → Bool) (s : UnorderedArraySet α) :
    (UnorderedArraySet α × UnorderedArraySet α)
```

`Aesop.UnorderedArraySet.size` (definition, [line 110](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L110))

> O(1)

```lean
def size (s : UnorderedArraySet α) : Nat
```

`Aesop.UnorderedArraySet.isEmpty` (definition, [line 114](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L114))

> O(1)

```lean
def isEmpty (s : UnorderedArraySet α) : Bool
```

`Aesop.UnorderedArraySet.anyM` (definition, [line 118](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L118))

> O(n)

```lean
def anyM [Monad m] (p : α → m Bool) (s : UnorderedArraySet α) (start := 0)
    (stop := s.size) : m Bool
```

`Aesop.UnorderedArraySet.any` (definition, [line 123](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L123))

> O(n)

```lean
def any (p : α → Bool) (s : UnorderedArraySet α) (start := 0) (stop := s.size) :
    Bool
```

`Aesop.UnorderedArraySet.allM` (definition, [line 128](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L128))

> O(n)

```lean
def allM [Monad m] (p : α → m Bool) (s : UnorderedArraySet α) (start := 0)
    (stop := s.size) : m Bool
```

`Aesop.UnorderedArraySet.all` (definition, [line 133](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean#L133))

> O(n)

```lean
def all (p : α → Bool) (s : UnorderedArraySet α) (start := 0) (stop := s.size) :
    Bool
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Util/UnorderedArraySet.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnorderedArraySet.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Util.UnorderedArraySet.json)
