---
catalog: module
lean: Batteries.AssocList.headKey?, Batteries.AssocList.headKey?_nil, Batteries.AssocList.headKey?_cons, Batteries.AssocList.headKey?_eq_head?, Batteries.AssocList.LTHeadKey, Batteries.AssocList.ltHeadKey_nil, Batteries.AssocList.ltHeadKey_cons, Batteries.AssocList.ltHeadKey_iff, Batteries.AssocList.KeysOrdered, Batteries.AssocList.keysOrdered_cons_nil, Batteries.AssocList.keysOrdered_iff_pairwise, Batteries.AssocList.KeysOrdered.tail, Batteries.AssocList.KeysOrdered.lt_of_mem, Batteries.AssocList.KeysOrdered.ltHeadKey, Batteries.AssocList.ltHeadKey_of_cons, Batteries.AssocList.ltHeadKey_of_le, Batteries.AssocList.LEHeadKey, Batteries.AssocList.leHeadKey_cons_cons, Batteries.AssocList.leHeadKey_iff, Batteries.AssocList.ltHeadKey_of_leHeadKey, Batteries.AssocList.leHeadKey_cons, Batteries.AssocList.KeysOrdered.cons, Batteries.AssocList.find?_eq_none_of_ltHeadKey, Batteries.AssocList.orderedInsert, Batteries.AssocList.orderedInsert_nil, Batteries.AssocList.orderedInsert_cons, Batteries.AssocList.headKey?_orderedInsert, Batteries.AssocList.headKey?_orderedInsert_or, Batteries.AssocList.KeysOrdered.orderedInsert_aux, Batteries.AssocList.KeysOrdered.orderedInsert, Batteries.AssocList.toList_orderedInsert, Batteries.AssocList.leHeadKey_filterMapVal, Batteries.AssocList.KeysOrdered.filterMapVal, Batteries.AssocList.orderedMerge, Batteries.AssocList.ltHeadKey_orderedMerge, Batteries.AssocList.KeysOrdered.orderedMerge, Batteries.AssocList.orderedFind?, Batteries.AssocList.orderedFind?_nil, Batteries.AssocList.orderedFind?_eq_find?, Batteries.AssocList.orderedFind?_eq, Batteries.AssocList.orderedFind?_eq_none_of_ltHeadKey, Batteries.AssocList.orderedFind?_cons, Batteries.AssocList.orderedFind?_cons_self, Batteries.AssocList.orderedFind?_orderedInsert, Batteries.AssocList.orderedFind?_orderedInsert_self, Batteries.AssocList.ext_orderedFind?, Batteries.AssocList.orderedFind?_filterMapVal, Batteries.AssocList.filterMapVal_filterMapVal, Batteries.OrderedAssocList, Batteries.OrderedAssocList.nil, Batteries.OrderedAssocList.toAssocList_nil, Batteries.OrderedAssocList.length, Batteries.OrderedAssocList.length_nil, Batteries.OrderedAssocList.length_mk_cons, Batteries.OrderedAssocList.head?, Batteries.OrderedAssocList.head?_eq_head?, Batteries.OrderedAssocList.tail, Batteries.OrderedAssocList.toAssocList_tail_mk_nil, Batteries.OrderedAssocList.toAssocList_tail_mk_cons, Batteries.OrderedAssocList.length_tail, Batteries.OrderedAssocList.find?, Batteries.OrderedAssocList.contains, Batteries.OrderedAssocList.getElem?_nil, Batteries.OrderedAssocList.getElem?_mk_nil, Batteries.OrderedAssocList.contains_eq_isSome_getElem?, Batteries.OrderedAssocList.headKey?, Batteries.OrderedAssocList.headKey?_nil, Batteries.OrderedAssocList.headKey?_mk_cons, Batteries.OrderedAssocList.LTHeadKey, Batteries.OrderedAssocList.ltHeadKey_tail, Batteries.OrderedAssocList.getElem?_eq_none_of_ltHeadKey, Batteries.OrderedAssocList.getElem?_mk_cons, Batteries.OrderedAssocList.getElem?_mk_cons_self, Batteries.OrderedAssocList.ext_toAssocList, Batteries.OrderedAssocList.ext, Batteries.OrderedAssocList.contains_nil, Batteries.OrderedAssocList.contains_mk_cons_self, Batteries.OrderedAssocList.cons, Batteries.OrderedAssocList.toAssocList_cons, Batteries.OrderedAssocList.getElem?_cons, Batteries.OrderedAssocList.headKey?_cons, Batteries.OrderedAssocList.insert, Batteries.OrderedAssocList.toAssocList_insert, Batteries.OrderedAssocList.insert_mk_nil, Batteries.OrderedAssocList.insert_mk_cons, Batteries.OrderedAssocList.length_insert_ne_zero, Batteries.OrderedAssocList.getElem?_insert, Batteries.OrderedAssocList.getElem?_insert_self, Batteries.OrderedAssocList.contains_insert, Batteries.OrderedAssocList.contains_insert_self, Batteries.OrderedAssocList.filterMapVal, Batteries.OrderedAssocList.toAssocList_filterMapVal, Batteries.OrderedAssocList.getElem?_filterMapVal, Batteries.OrderedAssocList.filterMapVal_filterMapVal, Batteries.OrderedAssocList.merge, Batteries.OrderedAssocList.toAssocList_merge, Batteries.OrderedAssocList.merge_nil_nil, Batteries.OrderedAssocList.merge_mk_nil_mk_cons, Batteries.OrderedAssocList.merge_mk_cons_mk_nil, Batteries.OrderedAssocList.getElem?_merge, Batteries.OrderedAssocList.merge_comm, Batteries.OrderedAssocList.merge_assoc, Batteries.OrderedAssocList.add, Batteries.OrderedAssocList.getElem?_add, Batteries.OrderedAssocList.mul, Batteries.OrderedAssocList.getElem?_mul
statement: formalized
proof: formalized
---

# Ordered association lists

`Batteries.Data.OrderedAssocList`, in [Batteries/Data/OrderedAssocList.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean), by Kim Morrison.

> `OrderedAssocList` is a wrapper around `AssocList`,
> with the additional invariant that the keys are in strictly increasing order.
>
> As a consequence, an `OrderedAssocList` is determined by the lookup function `l[x]?`, that is
> `(∀ a, l₁[a]? = l₂[a]?) → l₁ = l₂`
> and this makes proving identities between operations much easier than with `AssocList`.
>
> As the operations on `OrderedAssocList` are defined in terms of `AssocList`,
> they evaluate in the kernel, but inherit the `O(n)` time complexity
> (i.e. are not suitable for large data). Their advantage relative to an ordered map is the
> simple extensionality property above.
>
> We will later add another wrapper requiring that a "default" value does not appear,
> so e.g. finitely supported functions can be uniquely represented.
>
> The main operations defined are:
> * `l[x]?`, which linearly searches the list, stopping if the keys get too large.
> * `insert`, which inserts a new key-value pair, maintaining the order invariant.
> * `filterMapVal f`, for `f : α → β → Option γ`, which applies a function to values,
>   dropping some values.
> * `merge f` for `f : α → Option β → Option γ → Option δ` which merges two lists,
>   dropping some values. It runs in time `O(l₁.length + l₂.length)`.

> We first define some predicates and operations in the `AssocList` namespace.
>
> * `KeysOrdered cmp l` asserts that the keys of an `l : AssocList` are strictly increasing
>   with respect to a comparator `cmp`.
> * `LTHeadKey cmp a l` asserts that `a` is less than (according to `cmp`) the first key of `l`,
>   or that `l` is empty.

`Batteries.AssocList.headKey?` (definition, [line 56](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L56))

> The head key of an `AssocList`, or `none` if the list is empty.

```lean
def headKey? (l : AssocList α β) : Option α
```

`Batteries.AssocList.headKey?_nil` (theorem, [line 61](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L61))

```lean
theorem headKey?_nil : headKey? (.nil : AssocList α β) = none
```

`Batteries.AssocList.headKey?_cons` (theorem, [line 62](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L62))

```lean
theorem headKey?_cons : headKey? (.cons a b t) = some a
```

`Batteries.AssocList.headKey?_eq_head?` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L64))

```lean
theorem headKey?_eq_head? (l : AssocList α β) : l.headKey? = l.toList.head?.map Prod.fst
```

`Batteries.AssocList.LTHeadKey` (abbreviation, [line 70](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L70))

> The condition that an element is less than the first key of an `AssocList`, or that list is empty.

```lean
abbrev LTHeadKey (cmp : α → α → Ordering) (a : α) (t : AssocList α β) : Prop
```

`Batteries.AssocList.ltHeadKey_nil` (theorem, [line 73](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L73))

```lean
theorem ltHeadKey_nil {cmp : α → α → Ordering} :
    LTHeadKey cmp a (.nil : AssocList α β) = True
```

`Batteries.AssocList.ltHeadKey_cons` (theorem, [line 75](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L75))

```lean
theorem ltHeadKey_cons : LTHeadKey cmp a (.cons x y t) = (cmp a x = .lt)
```

`Batteries.AssocList.ltHeadKey_iff` (theorem, [line 77](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L77))

```lean
theorem ltHeadKey_iff {l : AssocList α β} :
    LTHeadKey cmp a l ↔ ∀ p ∈ l.toList.head?, cmp a p.1 = .lt
```

`Batteries.AssocList.KeysOrdered` (definition, [line 85](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L85))

> The predicate that the keys of an `AssocList` are
> in strictly increasing order according to the comparator `cmp`.

```lean
def KeysOrdered (cmp : α → α → Ordering) : AssocList α β → Prop
```

`Batteries.AssocList.keysOrdered_cons_nil` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L89))

```lean
theorem keysOrdered_cons_nil : KeysOrdered cmp (.cons a b nil)
```

`Batteries.AssocList.keysOrdered_iff_pairwise` (theorem, [line 91](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L91))

```lean
theorem keysOrdered_iff_pairwise {α : Type u} {β : Type v} {cmp : α → α → Ordering}
    [TransCmp cmp] {l : AssocList α β} :
    KeysOrdered cmp l ↔ l.toList.Pairwise (fun p q : α × β => cmp p.1 q.1 = .lt)
```

`Batteries.AssocList.KeysOrdered.tail` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L106))

```lean
theorem KeysOrdered.tail (h : KeysOrdered cmp (.cons a b t)) : KeysOrdered cmp t
```

`Batteries.AssocList.KeysOrdered.lt_of_mem` (theorem, [line 108](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L108))

```lean
theorem KeysOrdered.lt_of_mem {α : Type u} {β : Type v} {cmp : α → α → Ordering} [TransCmp cmp]
    {x : α} {y : β} {t : AssocList α β} (h : KeysOrdered cmp (cons x y t))
    {p : α × β} (hp : p ∈ t.toList) : cmp x p.1 = .lt
```

`Batteries.AssocList.KeysOrdered.ltHeadKey` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L115))

```lean
theorem KeysOrdered.ltHeadKey (w : KeysOrdered cmp (cons a b t)) : LTHeadKey cmp a t
```

`Batteries.AssocList.ltHeadKey_of_cons` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L118))

```lean
theorem ltHeadKey_of_cons [TransCmp cmp] (w : LTHeadKey cmp a (cons x y t))
    (h : KeysOrdered cmp (cons x y t)) :
    LTHeadKey cmp a t
```

`Batteries.AssocList.ltHeadKey_of_le` (theorem, [line 128](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L128))

```lean
theorem ltHeadKey_of_le [TransCmp cmp] (h : cmp x a ≠ .gt) (w : LTHeadKey cmp a t) :
    LTHeadKey cmp x t
```

`Batteries.AssocList.LEHeadKey` (abbreviation, [line 140](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L140))

> A relation on two `AssocList`s, asserting that the head key of the first list is at most
> the head key of the second list, or that the second list is empty.

```lean
abbrev LEHeadKey
    (cmp : α → α → Ordering) (s : AssocList α β) (t : AssocList α γ) : Prop
```

`Batteries.AssocList.leHeadKey_cons_cons` (theorem, [line 147](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L147))

```lean
theorem leHeadKey_cons_cons :
    LEHeadKey cmp (cons a b t) (cons x y s) = (cmp a x ≠ .gt)
```

`Batteries.AssocList.leHeadKey_iff` (theorem, [line 150](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L150))

```lean
theorem leHeadKey_iff {s : AssocList α β} {t : AssocList α γ} :
    LEHeadKey cmp s t ↔ ∀ q ∈ t.toList.head?, ∃ p ∈ s.toList.head?, cmp p.1 q.1 ≠ .gt
```

`Batteries.AssocList.ltHeadKey_of_leHeadKey` (theorem, [line 154](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L154))

```lean
theorem ltHeadKey_of_leHeadKey [TransCmp cmp]
    (w : LTHeadKey cmp a s) (h : LEHeadKey cmp s t) :
    LTHeadKey cmp a t
```

`Batteries.AssocList.leHeadKey_cons` (theorem, [line 165](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L165))

```lean
theorem leHeadKey_cons [TransCmp cmp]
    (h : KeysOrdered cmp (cons x y t)) (w : LEHeadKey cmp t s) :
    LEHeadKey cmp (cons x y t) s
```

`Batteries.AssocList.KeysOrdered.cons` (theorem, [line 179](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L179))

```lean
theorem KeysOrdered.cons {cmp : α → α → Ordering}
    (w : LTHeadKey cmp a t) (h : KeysOrdered cmp t) :
    KeysOrdered cmp (.cons a b t)
```

`Batteries.AssocList.find?_eq_none_of_ltHeadKey` (theorem, [line 183](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L183))

```lean
theorem find?_eq_none_of_ltHeadKey {cmp : α → α → Ordering} [TransCmp cmp] [BEq α] [LawfulBEq α]
    (w : LTHeadKey cmp a l) (h : KeysOrdered cmp l) :
    l.find? a = none
```

> # Ordered-respecting operations on `AssocList`
>
> We now define `orderedInsert`, and `orderedMerge`,
> which will later be wrapped as `OrderedAssocList.insert` and `OrderedAssocList.merge`.
>
> We prove that with `KeysOrdered` input these functions produce `KeysOrdered` outputs.
> We prove the same about `AssocList.filterMapVal`.

`Batteries.AssocList.orderedInsert` (definition, [line 213](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L213))

> Insert a key-value pair into an `AssocList`,
> in such a way that if the original list has keys in increasing order,
> so does the result.
> (Otherwise, it is inserted before the first key the new key is smaller than,
> or replaces the first key the new key is equal to.)
>
> We later wrap this as `OrderedAssocList.insert`.

```lean
def orderedInsert (cmp : α → α → Ordering) (l : AssocList α β) (a : α) (b : β) : AssocList α β
```

`Batteries.AssocList.orderedInsert_nil` (theorem, [line 221](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L221))

```lean
theorem orderedInsert_nil : (nil : AssocList α β).orderedInsert cmp a b = .cons a b nil
```

`Batteries.AssocList.orderedInsert_cons` (theorem, [line 224](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L224))

```lean
theorem orderedInsert_cons :
    orderedInsert cmp (.cons x y t) a b = match _w : cmp a x with
    | .lt => .cons a b (.cons x y t)
    | .eq => .cons a b t
    | .gt => .cons x y (orderedInsert cmp t a b)
```

`Batteries.AssocList.headKey?_orderedInsert` (theorem, [line 230](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L230))

```lean
theorem headKey?_orderedInsert {l : AssocList α β} :
    headKey? (orderedInsert cmp l a b) =
      match headKey? l with
        | none => some a
        | some x => match cmp a x with | .lt | .eq => some a | .gt => some x
```

`Batteries.AssocList.headKey?_orderedInsert_or` (theorem, [line 239](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L239))

```lean
theorem headKey?_orderedInsert_or (cmp) (l : AssocList α β) (a) (b) :
    headKey? (orderedInsert cmp l a b) = some a ∨
      headKey? (orderedInsert cmp l a b) = headKey? l
```

`Batteries.AssocList.KeysOrdered.orderedInsert_aux` (theorem, [line 248](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L248))

```lean
theorem KeysOrdered.orderedInsert_aux [LawfulEqCmp cmp] [OrientedCmp cmp] {x y t}
    (h : KeysOrdered cmp (AssocList.cons x y t)) (w : cmp a x = Ordering.gt) :
    KeysOrdered cmp (AssocList.cons x y (AssocList.orderedInsert cmp t a b))
```

`Batteries.AssocList.KeysOrdered.orderedInsert` (theorem, [line 261](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L261))

```lean
theorem KeysOrdered.orderedInsert [LawfulEqCmp cmp] [OrientedCmp cmp] (h : KeysOrdered cmp l) :
    KeysOrdered cmp (AssocList.orderedInsert cmp l a b)
```

`Batteries.AssocList.toList_orderedInsert` (theorem, [line 275](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L275))

```lean
theorem toList_orderedInsert {α : Type u} {β : Type v} {cmp : α → α → Ordering}
    [LawfulEqCmp cmp] [TransCmp cmp] {l : AssocList α β} (h : KeysOrdered cmp l) (a : α) (b : β) :
    (orderedInsert cmp l a b).toList =
      l.toList.filter (fun p => cmp a p.1 == .gt) ++
        (a, b) :: l.toList.filter (fun p => cmp a p.1 == .lt)
```

`Batteries.AssocList.leHeadKey_filterMapVal` (theorem, [line 303](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L303))

```lean
theorem leHeadKey_filterMapVal [TransCmp cmp] (h : KeysOrdered cmp l) :
    LEHeadKey cmp l (l.filterMapVal f)
```

`Batteries.AssocList.KeysOrdered.filterMapVal` (theorem, [line 314](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L314))

```lean
theorem KeysOrdered.filterMapVal [TransCmp cmp] (h : KeysOrdered cmp l) :
    KeysOrdered cmp (l.filterMapVal f)
```

`Batteries.AssocList.orderedMerge` (definition, [line 339](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L339))

> Merge two `AssocList`s,
> at each stage taking the first key-value pair from whichever list has a smaller first key.
> If both inputs have keys in strictly increasing order, so does the result.
> (We later wrap this as `OrderedAssocList.merge`.)
>
> We combine values using a function `f : α → Option β → Option γ → Option δ` which we call as
> `f a (some b) none` when encountering a key present only in the first list (with value `b`),
> `f a none (some g)` when encountering a key present only in the second list (with value `g`), and
> `f a (some b) (some g)` when encountering a key present in both lists.
> (Note the value of `f a none none` is never used.)

```lean
def orderedMerge (cmp : α → α → Ordering) (f : α → Option β → Option γ → Option δ) :
    AssocList α β → AssocList α γ → AssocList α δ
```

`Batteries.AssocList.ltHeadKey_orderedMerge` (theorem, [line 356](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L356))

```lean
theorem ltHeadKey_orderedMerge [TransCmp cmp]
    (h₁ : LTHeadKey cmp a l₁) (h₂ : LTHeadKey cmp a l₂)
    (w₁ : KeysOrdered cmp l₁) (w₂ : KeysOrdered cmp l₂) :
    LTHeadKey cmp a (orderedMerge cmp f l₁ l₂)
```

`Batteries.AssocList.KeysOrdered.orderedMerge` (theorem, [line 388](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L388))

```lean
theorem KeysOrdered.orderedMerge [LawfulEqCmp cmp] [TransCmp cmp]
    (h₁ : KeysOrdered cmp l₁) (h₂ : KeysOrdered cmp l₂) :
    KeysOrdered cmp (AssocList.orderedMerge cmp f l₁ l₂)
```

`Batteries.AssocList.orderedFind?` (definition, [line 430](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L430))

> Find the value associated to a key by traversing left to right,
> short-circuiting once we are considering larger keys.

```lean
def orderedFind? (cmp : α → α → Ordering) (l : AssocList α β) (x : α) : Option β
```

`Batteries.AssocList.orderedFind?_nil` (theorem, [line 438](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L438))

```lean
theorem orderedFind?_nil {cmp : α → α → Ordering} :
    orderedFind? cmp (nil : AssocList α β) x = none
```

`Batteries.AssocList.orderedFind?_eq_find?` (theorem, [line 441](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L441))

```lean
theorem orderedFind?_eq_find?
    {cmp : α → α → Ordering} [LawfulEqCmp cmp] [TransCmp cmp] [BEq α] [LawfulBEq α]
    (l : AssocList α β) (h : l.KeysOrdered cmp) (x : α) : l.orderedFind? cmp x = l.find? x
```

`Batteries.AssocList.orderedFind?_eq` (theorem, [line 460](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L460))

```lean
theorem orderedFind?_eq
    {cmp : α → α → Ordering} [LawfulEqCmp cmp] [TransCmp cmp] [BEq α] [LawfulBEq α]
    (l : AssocList α β) (h : l.KeysOrdered cmp) (x : α) :
    l.orderedFind? cmp x = (l.toList.find? (·.1 == x)).map (·.2)
```

`Batteries.AssocList.orderedFind?_eq_none_of_ltHeadKey` (theorem, [line 466](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L466))

```lean
theorem orderedFind?_eq_none_of_ltHeadKey (l : AssocList α β) (w : LTHeadKey cmp x l) :
    orderedFind? cmp l x = none
```

`Batteries.AssocList.orderedFind?_cons` (theorem, [line 476](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L476))

```lean
theorem orderedFind?_cons [TransCmp cmp]
    (h : (AssocList.cons a b t).KeysOrdered cmp) :
    orderedFind? cmp (.cons a b t) x = if cmp x a = .eq then some b else orderedFind? cmp t x
```

`Batteries.AssocList.orderedFind?_cons_self` (theorem, [line 493](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L493))

```lean
theorem orderedFind?_cons_self [OrientedCmp cmp] :
    orderedFind? cmp (.cons a b t) a = some b
```

`Batteries.AssocList.orderedFind?_orderedInsert` (theorem, [line 497](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L497))

```lean
theorem orderedFind?_orderedInsert {cmp : α → α → Ordering} [LawfulEqCmp cmp] [TransCmp cmp]
    (l : AssocList α β) (h : KeysOrdered cmp l) (a : α) (b : β) :
    (orderedInsert cmp l a b).orderedFind? cmp x =
      if cmp x a = .eq then some b else l.orderedFind? cmp x
```

`Batteries.AssocList.orderedFind?_orderedInsert_self` (theorem, [line 521](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L521))

```lean
theorem orderedFind?_orderedInsert_self {cmp : α → α → Ordering} [LawfulEqCmp cmp] [TransCmp cmp]
    (l : AssocList α β) (h : KeysOrdered cmp l)  (a : α) (b : β) :
    (orderedInsert cmp l a b).orderedFind? cmp a = some b
```

`Batteries.AssocList.ext_orderedFind?` (theorem, [line 530](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L530))

> If two `AssocList`s have ordered keys
> we can check whether they are equal by checking if their `orderedFind?` functions are equal.

```lean
theorem ext_orderedFind?
    (cmp : α → α → Ordering) [LawfulEqCmp cmp] [TransCmp cmp]
    {l₁ l₂ : AssocList α β} (h₁ : l₁.KeysOrdered cmp) (h₂ : l₂.KeysOrdered cmp)
    (w : ∀ a, l₁.orderedFind? cmp a = l₂.orderedFind? cmp a) : l₁ = l₂
```

`Batteries.AssocList.orderedFind?_filterMapVal` (theorem, [line 577](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L577))

```lean
theorem orderedFind?_filterMapVal {cmp : α → α → Ordering} [LawfulEqCmp cmp] [TransCmp cmp]
    {l : AssocList α β} (h : KeysOrdered cmp l) :
    (filterMapVal f l).orderedFind? cmp a = (l.orderedFind? cmp a).bind (fun b => f a b)
```

`Batteries.AssocList.filterMapVal_filterMapVal` (theorem, [line 604](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L604))

```lean
theorem filterMapVal_filterMapVal {cmp : α → α → Ordering} [LawfulEqCmp cmp] [TransCmp cmp]
    {f : α → γ → Option δ} {g : α → β → Option γ}
    {l : AssocList α β} (h : KeysOrdered cmp l) :
    filterMapVal f (filterMapVal g l) =
      filterMapVal (fun a b => (g a b).bind (fun c => f a c)) l
```

`Batteries.OrderedAssocList` (structure, [line 629](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L629))

> An `OrderedAssocList` is an `AssocList` with the additional invariant that
> the keys are in strictly increasing order according to some specified comparator function.

```lean
structure OrderedAssocList {α : Type u} (cmp : α → α → Ordering) (β : Type v) where
  /-- The underlying `AssocList` of an `OrderedAssocList`. -/
  toAssocList : AssocList α β
  /-- The invariant that the keys are in strictly increasing order according to `cmp`. -/
  keysOrdered : toAssocList.KeysOrdered cmp
```

`Batteries.OrderedAssocList.nil` (definition, [line 640](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L640))

> The empty `OrderedAssocList`.

```lean
def nil : OrderedAssocList cmp β
```

`Batteries.OrderedAssocList.toAssocList_nil` (theorem, [line 642](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L642))

```lean
theorem toAssocList_nil : (nil : OrderedAssocList cmp β).toAssocList = .nil
```

`Batteries.OrderedAssocList.length` (definition, [line 645](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L645))

> The length of an `OrderedAssocList`.

```lean
def length (l : OrderedAssocList cmp β) : Nat
```

`Batteries.OrderedAssocList.length_nil` (theorem, [line 647](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L647))

```lean
theorem length_nil : length (nil : OrderedAssocList cmp β) = 0
```

`Batteries.OrderedAssocList.length_mk_cons` (theorem, [line 648](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L648))

```lean
theorem length_mk_cons : length ⟨.cons a b t, h⟩ = length ⟨t, h.tail⟩ + 1
```

`Batteries.OrderedAssocList.head?` (definition, [line 652](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L652))

> The first key-value pair in an `OrderedAssocList`.

```lean
def head? (l : OrderedAssocList cmp β) : Option (α × β)
```

`Batteries.OrderedAssocList.head?_eq_head?` (theorem, [line 657](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L657))

```lean
theorem head?_eq_head? (l : OrderedAssocList cmp β) : l.head? = l.toAssocList.toList.head?
```

`Batteries.OrderedAssocList.tail` (definition, [line 663](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L663))

> The tail of an `OrderedAssocList`.

```lean
def tail (l : OrderedAssocList cmp β) : OrderedAssocList cmp β
```

`Batteries.OrderedAssocList.toAssocList_tail_mk_nil` (theorem, [line 668](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L668))

```lean
theorem toAssocList_tail_mk_nil {h} :
    (tail (⟨.nil, h⟩ : OrderedAssocList cmp β)).toAssocList = .nil
```

`Batteries.OrderedAssocList.toAssocList_tail_mk_cons` (theorem, [line 670](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L670))

```lean
theorem toAssocList_tail_mk_cons {h} :
    (tail (⟨.cons a b t, h⟩ : OrderedAssocList cmp β)).toAssocList = t
```

`Batteries.OrderedAssocList.length_tail` (theorem, [line 673](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L673))

```lean
theorem length_tail : length (tail l) = length l - 1
```

`Batteries.OrderedAssocList.find?` (definition, [line 684](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L684))

> Find the value associated to a key by traversing left to right,
> short-circuiting once we are considering larger keys.
>
> This is the internal implementation of  `l[x]?`, which should be preferred.

```lean
def find? (l : OrderedAssocList cmp β) (x : α) : Option β
```

`Batteries.OrderedAssocList.contains` (definition, [line 688](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L688))

> Check if an `OrderedAssocList` contains a specific key.

```lean
def contains (l : OrderedAssocList cmp β) (x : α) : Bool
```

`Batteries.OrderedAssocList.getElem?_nil` (theorem, [line 694](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L694))

```lean
theorem getElem?_nil {x : α} : (nil : OrderedAssocList cmp β)[x]? = none
```

`Batteries.OrderedAssocList.getElem?_mk_nil` (theorem, [line 695](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L695))

```lean
theorem getElem?_mk_nil {x : α} : (⟨.nil, h⟩ : OrderedAssocList cmp β)[x]? = none
```

`Batteries.OrderedAssocList.contains_eq_isSome_getElem?` (theorem, [line 697](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L697))

```lean
theorem contains_eq_isSome_getElem? {l : OrderedAssocList cmp β} :
    l.contains a = l[a]?.isSome
```

`Batteries.OrderedAssocList.headKey?` (definition, [line 701](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L701))

> The first key in an `OrderedAssocList`, or `none` if the list is empty.

```lean
def headKey? (l : OrderedAssocList cmp β) : Option α
```

`Batteries.OrderedAssocList.headKey?_nil` (theorem, [line 703](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L703))

```lean
theorem headKey?_nil : headKey? (nil : OrderedAssocList cmp β) = none
```

`Batteries.OrderedAssocList.headKey?_mk_cons` (theorem, [line 704](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L704))

```lean
theorem headKey?_mk_cons : headKey? ⟨.cons a b t, h⟩ = some a
```

`Batteries.OrderedAssocList.LTHeadKey` (definition, [line 707](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L707))

> Either `a` is less than the first key of `l`, or `l` is empty.

```lean
def LTHeadKey (a : α) (l : OrderedAssocList cmp β) : Prop
```

`Batteries.OrderedAssocList.ltHeadKey_tail` (theorem, [line 711](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L711))

> The head key of a tail is either `none`, or greater than the original head key.

```lean
theorem ltHeadKey_tail (h : AssocList.KeysOrdered cmp (.cons a b t)) :
    LTHeadKey a ⟨t, h.tail⟩
```

`Batteries.OrderedAssocList.getElem?_eq_none_of_ltHeadKey` (theorem, [line 714](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L714))

```lean
theorem getElem?_eq_none_of_ltHeadKey (l : OrderedAssocList cmp β) (w : LTHeadKey x l) :
    l[x]? = none
```

`Batteries.OrderedAssocList.getElem?_mk_cons` (theorem, [line 718](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L718))

```lean
theorem getElem?_mk_cons [TransCmp cmp]
    {h : (AssocList.cons a b t).KeysOrdered cmp} :
    (⟨.cons a b t, h⟩ : OrderedAssocList _ _)[x]? =
      if cmp x a = .eq then some b else (⟨t, h.tail⟩ : OrderedAssocList _ _)[x]?
```

`Batteries.OrderedAssocList.getElem?_mk_cons_self` (theorem, [line 732](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L732))

```lean
theorem getElem?_mk_cons_self [OrientedCmp cmp]
    {h : (AssocList.cons a b t).KeysOrdered cmp} :
    (⟨.cons a b t, h⟩ : OrderedAssocList _ _)[a]? = some b
```

`Batteries.OrderedAssocList.ext_toAssocList` (theorem, [line 737](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L737))

```lean
theorem ext_toAssocList {l₁ l₂ : OrderedAssocList cmp β}
    (w : l₁.toAssocList = l₂.toAssocList) : l₁ = l₂
```

`Batteries.OrderedAssocList.ext` (theorem, [line 741](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L741))

```lean
theorem ext [LawfulEqCmp cmp] [TransCmp cmp] {l₁ l₂ : OrderedAssocList cmp β}
    (w : ∀ a : α, l₁[a]? = l₂[a]?) : l₁ = l₂
```

`Batteries.OrderedAssocList.contains_nil` (theorem, [line 748](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L748))

```lean
theorem contains_nil : contains (nil : OrderedAssocList cmp β) x = false
```

`Batteries.OrderedAssocList.contains_mk_cons_self` (theorem, [line 749](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L749))

```lean
theorem contains_mk_cons_self [OrientedCmp cmp]
    {h : (AssocList.cons a b t).KeysOrdered cmp} :
    contains ⟨.cons a b t, h⟩ a = true
```

`Batteries.OrderedAssocList.cons` (definition, [line 759](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L759))

> Prepend a key-value pair,
> requiring a proof that the key is smaller than the existing smallest key.

```lean
def cons (a : α) (b : β) (l : OrderedAssocList cmp β) (w : LTHeadKey a l) :
    OrderedAssocList cmp β
```

`Batteries.OrderedAssocList.toAssocList_cons` (theorem, [line 765](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L765))

```lean
theorem toAssocList_cons : (cons a b l w).toAssocList = .cons a b l.toAssocList
```

`Batteries.OrderedAssocList.getElem?_cons` (theorem, [line 771](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L771))

```lean
theorem getElem?_cons [TransCmp cmp] {l : OrderedAssocList cmp β} {w} :
    (cons a b l w)[x]? = if cmp x a = .eq then some b else l[x]?
```

`Batteries.OrderedAssocList.headKey?_cons` (theorem, [line 776](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L776))

```lean
theorem headKey?_cons : headKey? (cons a b l w) = some a
```

`Batteries.OrderedAssocList.insert` (definition, [line 792](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L792))

> Insert a key-value pair into an `OrderedAssocList`.
> This replaces the current value if the key is already present,
> and otherwise inserts it before the first key which is greater than the inserted key.

```lean
def insert (l : OrderedAssocList cmp β) (a : α) (b : β) : OrderedAssocList cmp β
```

`Batteries.OrderedAssocList.toAssocList_insert` (theorem, [line 795](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L795))

```lean
theorem toAssocList_insert (l : OrderedAssocList cmp β) (a : α) (b : β) :
    (insert l a b).toAssocList = l.toAssocList.orderedInsert cmp a b
```

`Batteries.OrderedAssocList.insert_mk_nil` (theorem, [line 798](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L798))

```lean
theorem insert_mk_nil :
    insert (⟨.nil, h⟩ : OrderedAssocList cmp β) a b =
      ⟨.cons a b .nil, AssocList.keysOrdered_cons_nil⟩
```

`Batteries.OrderedAssocList.insert_mk_cons` (theorem, [line 802](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L802))

```lean
theorem insert_mk_cons :
    insert (⟨.cons x y t, h⟩ : OrderedAssocList cmp β) a b = match w : cmp a x with
    | .lt => ⟨.cons a b (.cons x y t), ⟨w, h⟩⟩
    | .eq => ⟨.cons a b t, by
        cases (LawfulEqCmp.eq_of_compare w); exact h⟩
    | .gt => ⟨.cons x y (t.orderedInsert cmp a b),
        h.orderedInsert_aux w⟩
```

`Batteries.OrderedAssocList.length_insert_ne_zero` (theorem, [line 813](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L813))

```lean
theorem length_insert_ne_zero {l : OrderedAssocList cmp β} : (insert l a b).length ≠ 0
```

`Batteries.OrderedAssocList.getElem?_insert` (theorem, [line 824](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L824))

```lean
theorem getElem?_insert (l : OrderedAssocList cmp β) (a : α) (b : β) :
    (insert l a b)[x]? = if cmp x a = .eq then some b else l[x]?
```

`Batteries.OrderedAssocList.getElem?_insert_self` (theorem, [line 828](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L828))

```lean
theorem getElem?_insert_self (l : OrderedAssocList cmp β) (a : α) (b : β) :
    (insert l a b)[a]? = some b
```

`Batteries.OrderedAssocList.contains_insert` (theorem, [line 832](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L832))

```lean
theorem contains_insert (l : OrderedAssocList cmp β) (a : α) (b : β) :
    (l.insert a b).contains x = ((cmp x a = .eq) || l.contains x)
```

`Batteries.OrderedAssocList.contains_insert_self` (theorem, [line 840](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L840))

```lean
theorem contains_insert_self (l : OrderedAssocList cmp β) (a : α) (b : β) :
    (l.insert a b).contains a = true
```

`Batteries.OrderedAssocList.filterMapVal` (definition, [line 854](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L854))

> Apply a function to each key-value pair,
> either replacing the value or dropping it if the function returns `none`.

```lean
def filterMapVal (f : α → β → Option δ) (l : OrderedAssocList cmp β) :
    OrderedAssocList cmp δ
```

`Batteries.OrderedAssocList.toAssocList_filterMapVal` (theorem, [line 858](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L858))

```lean
theorem toAssocList_filterMapVal (f : α → β → Option δ) (l : OrderedAssocList cmp β) :
    (filterMapVal f l).toAssocList = l.toAssocList.filterMapVal f
```

`Batteries.OrderedAssocList.getElem?_filterMapVal` (theorem, [line 862](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L862))

```lean
theorem getElem?_filterMapVal [LawfulEqCmp cmp] (l : OrderedAssocList cmp β) :
    (filterMapVal f l)[a]? = l[a]?.bind (fun b => f a b)
```

`Batteries.OrderedAssocList.filterMapVal_filterMapVal` (theorem, [line 866](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L866))

```lean
theorem filterMapVal_filterMapVal [LawfulEqCmp cmp]
    {f : α → γ → Option δ} {g : α → β → Option γ}
    {l : OrderedAssocList cmp β} :
    filterMapVal f (filterMapVal g l) =
      filterMapVal (fun a b => (g a b).bind (fun c => f a c)) l
```

`Batteries.OrderedAssocList.merge` (definition, [line 884](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L884))

> Merge two `OrderedAssocList`s using a function `α → Option β → Option γ → Option δ`,
> dropping values where the function returns `none`.

```lean
def merge (f : α → Option β → Option γ → Option δ)
    (l₁ : OrderedAssocList cmp β) (l₂ : OrderedAssocList cmp γ) : OrderedAssocList cmp δ
```

`Batteries.OrderedAssocList.toAssocList_merge` (theorem, [line 889](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L889))

```lean
theorem toAssocList_merge {l₁ : OrderedAssocList cmp β} :
    (merge f l₁ l₂).toAssocList = AssocList.orderedMerge cmp f l₁.toAssocList l₂.toAssocList
```

`Batteries.OrderedAssocList.merge_nil_nil` (theorem, [line 893](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L893))

```lean
theorem merge_nil_nil {f : α → Option β → Option γ → Option δ} :
    merge f (nil : OrderedAssocList cmp β) nil = nil
```

`Batteries.OrderedAssocList.merge_mk_nil_mk_cons` (theorem, [line 898](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L898))

```lean
theorem merge_mk_nil_mk_cons {f : α → Option β → Option γ → Option δ} :
    merge f (⟨.nil, h⟩ : OrderedAssocList cmp β) ⟨.cons x' y' t', h'⟩ =
      filterMapVal (fun a g => f a none (some g)) ⟨.cons x' y' t', h'⟩
```

`Batteries.OrderedAssocList.merge_mk_cons_mk_nil` (theorem, [line 904](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L904))

```lean
theorem merge_mk_cons_mk_nil {f : α → Option β → Option γ → Option δ} :
    merge f ⟨.cons x y t, h⟩ (⟨.nil, h'⟩ : OrderedAssocList cmp γ) =
      filterMapVal (fun a b => f a (some b) none) ⟨.cons x y t, h⟩
```

`Batteries.OrderedAssocList.getElem?_merge` (theorem, [line 955](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L955))

```lean
theorem getElem?_merge {f : α → Option β → Option γ → Option δ}
    (hf : f a none none = none) {l₁ : OrderedAssocList cmp β} {l₂} :
    (merge f l₁ l₂)[a]? = f a l₁[a]? l₂[a]?
```

`Batteries.OrderedAssocList.merge_comm` (theorem, [line 1024](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L1024))

```lean
theorem merge_comm
    (f : α → Option β → Option γ → Option δ) (g : α → Option γ → Option β → Option δ)
    (hg : ∀ a, g a none none = none)
    (w : ∀ a x y, f a x y = g a y x)
    (l₁ : OrderedAssocList cmp β) (l₂) : merge f l₁ l₂ = merge g l₂ l₁
```

`Batteries.OrderedAssocList.merge_assoc` (theorem, [line 1032](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L1032))

```lean
theorem merge_assoc
    (f₁ : α → Option β₁ → Option β₂ → Option γ₁) (f₂ : α → Option γ₁ → Option β₃ → Option ε)
    (g₁ : α → Option β₂ → Option β₃ → Option γ₂) (g₂ : α → Option β₁ → Option γ₂ → Option ε)
    (hf₁ : ∀ a, f₁ a none none = none) (hf₂ : ∀ a, f₂ a none none = none)
    (hg₁ : ∀ a, g₁ a none none = none) (hg₂ : ∀ a, g₂ a none none = none)
    (w : ∀ a x y z, f₂ a (f₁ a x y) z = g₂ a x (g₁ a y z))
    (l₁ : OrderedAssocList cmp β₁) (l₂) (l₃) :
    merge f₂ (merge f₁ l₁ l₂) l₃ = merge g₂ l₁ (merge g₁ l₂ l₃)
```

`Batteries.OrderedAssocList.add` (definition, [line 1047](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L1047))

> Add two `OrderedAssocList`s, taking the value from one list if the other value is missing.
> (That is, treating missing values as `0`.)

```lean
def add [Add β] (l₁ : OrderedAssocList cmp β) (l₂ : OrderedAssocList cmp β) :
    OrderedAssocList cmp β
```

`Batteries.OrderedAssocList.getElem?_add` (theorem, [line 1061](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L1061))

```lean
theorem getElem?_add [Add β] {l₁ : OrderedAssocList cmp β} {a : α} :
    (add l₁ l₂)[a]? =
      match l₁[a]?, l₂[a]? with
      | some x, some y => some (x + y)
      | some x, none => some x
      | none, some y => some y
      | none, none => none
```

`Batteries.OrderedAssocList.mul` (definition, [line 1076](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L1076))

> Multiply two `OrderedAssocList`s,
> dropping any values where the corresponding value in the other list is missing.
> (That is, treating missing values as `0`.)

```lean
def mul [Mul β] (l₁ : OrderedAssocList cmp β) (l₂ : OrderedAssocList cmp β) :
    OrderedAssocList cmp β
```

`Batteries.OrderedAssocList.getElem?_mul` (theorem, [line 1087](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean#L1087))

```lean
theorem getElem?_mul [Mul β] {l₁ : OrderedAssocList cmp β} {a : α} :
    (mul l₁ l₂)[a]? =
      match l₁[a]?, l₂[a]? with
      | some x, some y => some (x * y)
      | some _, none => none
      | none, some _ => none
      | none, none => none
```

## Depends on

- [Association lists](assoclist/basic.md)

## Proof depends on

- [Order](../../classes/order.md)
- [Lemmas about association lists](assoclist/lemmas.md)

## Sources

- [Batteries/Data/OrderedAssocList.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/OrderedAssocList.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Data.OrderedAssocList.json)
