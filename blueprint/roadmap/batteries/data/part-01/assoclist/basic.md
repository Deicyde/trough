---
catalog: module
lean: Batteries.AssocList, Batteries.AssocList.toList, Batteries.AssocList.isEmpty, Batteries.AssocList.length, Batteries.AssocList.foldlM, Batteries.AssocList.foldl, Batteries.AssocList.foldlM_eq, Batteries.AssocList.foldl_eq, Batteries.AssocList.toListTR, Batteries.AssocList.toList_eq_toListTR, Batteries.AssocList.forM, Batteries.AssocList.mapKey, Batteries.AssocList.mapVal, Batteries.AssocList.filterMapVal, Batteries.AssocList.findEntryP?, Batteries.AssocList.findEntry?, Batteries.AssocList.find?, Batteries.AssocList.any, Batteries.AssocList.all, Batteries.AssocList.All, Batteries.AssocList.contains, Batteries.AssocList.replace, Batteries.AssocList.eraseP, Batteries.AssocList.erase, Batteries.AssocList.modify, Batteries.AssocList.forIn, Batteries.AssocList.pop?, List.toAssocList, Batteries.AssocList.beq
statement: formalized
proof: formalized
---

# Association lists

`Batteries.Data.AssocList.Basic`, in [Batteries/Data/AssocList/Basic.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean), by Leonardo de Moura, Mario Carneiro.

> `AssocList α β` is a `List (α × β)` with the pair structure flattened into the list constructor.
> This file defines the type and its operations; the lemmas relating those operations to the
> corresponding `List` operations along `AssocList.toList` are in `Batteries.Data.AssocList.Lemmas`.

`Batteries.AssocList` (inductive type, [line 26](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L26))

> `AssocList α β` is "the same as" `List (α × β)`, but flattening the structure
> leads to one fewer pointer indirection (in the current code generator).
> It is mainly intended as a component of `HashMap`, but it can also be used as a plain
> key-value map.

```lean
inductive AssocList (α : Type u) (β : Type v) where
  /-- An empty list -/
  | nil
  /-- Add a `key, value` pair to the list -/
  | cons (key : α) (value : β) (tail : AssocList α β)
  deriving Inhabited
```

`Batteries.AssocList.toList` (definition, [line 40](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L40))

> `O(n)`. Convert an `AssocList α β` into the equivalent `List (α × β)`.
> This is used to give specifications for all the `AssocList` functions
> in terms of corresponding list functions.

```lean
def toList : AssocList α β → List (α × β)
```

`Batteries.AssocList.isEmpty` (definition, [line 47](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L47))

> `O(1)`. Is the list empty?

```lean
def isEmpty : AssocList α β → Bool
```

`Batteries.AssocList.length` (definition, [line 52](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L52))

> The number of entries in an `AssocList`.

```lean
def length (L : AssocList α β) : Nat
```

`Batteries.AssocList.foldlM` (definition, [line 58](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L58))

> `O(n)`. Fold a monadic function over the list, from head to tail.

```lean
def foldlM [Monad m] (f : δ → α → β → m δ) : (init : δ) → AssocList α β → m δ
```

`Batteries.AssocList.foldl` (definition, [line 63](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L63))

> `O(n)`. Fold a function over the list, from head to tail.

```lean
def foldl (f : δ → α → β → δ) (init : δ) (as : AssocList α β) : δ
```

`Batteries.AssocList.foldlM_eq` (theorem, [line 66](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L66))

```lean
theorem foldlM_eq [Monad m] (f : δ → α → β → m δ) (init l) :
    foldlM f init l = l.toList.foldlM (fun d (a, b) => f d a b) init
```

`Batteries.AssocList.foldl_eq` (theorem, [line 70](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L70))

```lean
theorem foldl_eq (f : δ → α → β → δ) (init l) :
    foldl f init l = l.toList.foldl (fun d (a, b) => f d a b) init
```

`Batteries.AssocList.toListTR` (definition, [line 75](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L75))

> Optimized version of `toList`.

```lean
def toListTR (as : AssocList α β) : List (α × β)
```

`Batteries.AssocList.toList_eq_toListTR` (theorem, [line 78](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L78))

```lean
theorem toList_eq_toListTR : @toList = @toListTR
```

`Batteries.AssocList.forM` (definition, [line 82](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L82))

> `O(n)`. Run monadic function `f` on all elements in the list, from head to tail.

```lean
def forM [Monad m] (f : α → β → m PUnit) : AssocList α β → m PUnit
```

`Batteries.AssocList.mapKey` (definition, [line 87](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L87))

> `O(n)`. Map a function `f` over the keys of the list.

```lean
def mapKey (f : α → δ) : AssocList α β → AssocList δ β
```

`Batteries.AssocList.mapVal` (definition, [line 92](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L92))

> `O(n)`. Map a function `f` over the values of the list.

```lean
def mapVal (f : α → β → δ) : AssocList α β → AssocList α δ
```

`Batteries.AssocList.filterMapVal` (definition, [line 97](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L97))

> `O(n)`. Map a function `f` over the values of the list, dropping `none`.

```lean
def filterMapVal (f : α → β → Option δ) : AssocList α β → AssocList α δ
```

`Batteries.AssocList.findEntryP?` (definition, [line 104](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L104))

> `O(n)`. Returns the first entry in the list whose entry satisfies `p`.

```lean
def findEntryP? (p : α → β → Bool) : AssocList α β → Option (α × β)
```

`Batteries.AssocList.findEntry?` (definition, [line 109](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L109))

> `O(n)`. Returns the first entry in the list whose key is equal to `a`.

```lean
def findEntry? [BEq α] (a : α) (l : AssocList α β) : Option (α × β)
```

`Batteries.AssocList.find?` (definition, [line 113](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L113))

> `O(n)`. Returns the first value in the list whose key is equal to `a`.

```lean
def find? [BEq α] (a : α) : AssocList α β → Option β
```

`Batteries.AssocList.any` (definition, [line 120](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L120))

> `O(n)`. Returns true if any entry in the list satisfies `p`.

```lean
def any (p : α → β → Bool) : AssocList α β → Bool
```

`Batteries.AssocList.all` (definition, [line 125](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L125))

> `O(n)`. Returns true if every entry in the list satisfies `p`.

```lean
def all (p : α → β → Bool) : AssocList α β → Bool
```

`Batteries.AssocList.All` (definition, [line 130](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L130))

> Returns true if every entry in the list satisfies `p`.

```lean
def All (p : α → β → Prop) (l : AssocList α β) : Prop
```

`Batteries.AssocList.contains` (definition, [line 134](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L134))

> `O(n)`. Returns true if there is an element in the list whose key is equal to `a`.

```lean
def contains [BEq α] (a : α) (l : AssocList α β) : Bool
```

`Batteries.AssocList.replace` (definition, [line 140](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L140))

> `O(n)`. Replace the first entry in the list
> with key equal to `a` to have key `a` and value `b`.

```lean
def replace [BEq α] (a : α) (b : β) : AssocList α β → AssocList α β
```

`Batteries.AssocList.eraseP` (definition, [line 147](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L147))

> `O(n)`. Remove the first entry in the list with key equal to `a`.

```lean
def eraseP (p : α → β → Bool) : AssocList α β → AssocList α β
```

`Batteries.AssocList.erase` (definition, [line 152](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L152))

> `O(n)`. Remove the first entry in the list with key equal to `a`.

```lean
def erase [BEq α] (a : α) (l : AssocList α β) : AssocList α β
```

`Batteries.AssocList.modify` (definition, [line 159](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L159))

> `O(n)`. Replace the first entry `a', b` in the list
> with key equal to `a` to have key `a` and value `f a' b`.

```lean
def modify [BEq α] (a : α) (f : α → β → β) : AssocList α β → AssocList α β
```

`Batteries.AssocList.forIn` (definition, [line 166](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L166))

> The implementation of `ForIn`, which enables `for (k, v) in aList do ...` notation.

```lean
protected def forIn [Monad m]
    (as : AssocList α β) (init : δ) (f : (α × β) → δ → m (ForInStep δ)) : m δ
```

`Batteries.AssocList.pop?` (definition, [line 179](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L179))

> Split the list into head and tail, if possible.

```lean
def pop? : AssocList α β → Option ((α × β) × AssocList α β)
```

`List.toAssocList` (definition, [line 187](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L187))

> Converts a list into an `AssocList`. This is the inverse function to `AssocList.toList`.

```lean
def _root_.List.toAssocList : List (α × β) → AssocList α β
```

`Batteries.AssocList.beq` (definition, [line 192](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean#L192))

> Implementation of `==` on `AssocList`.

```lean
protected def beq [BEq α] [BEq β] : AssocList α β → AssocList α β → Bool
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/AssocList/Basic.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/AssocList/Basic.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.AssocList.Basic.json)
