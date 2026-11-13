---
catalog: module
lean: Cslib.Turing.StackTape, Cslib.Turing.StackTape.nil, Cslib.Turing.StackTape.empty_eq_nil, Cslib.Turing.StackTape.nil_toList, Cslib.Turing.StackTape.cons, Cslib.Turing.StackTape.cons_none_nil_toList, Cslib.Turing.StackTape.cons_some_toList, Cslib.Turing.StackTape.tail, Cslib.Turing.StackTape.head, Cslib.Turing.StackTape.eq_iff, Cslib.Turing.StackTape.head_cons, Cslib.Turing.StackTape.tail_cons, Cslib.Turing.StackTape.cons_head_tail, Cslib.Turing.StackTape.mapSome, Cslib.Turing.StackTape.length, Cslib.Turing.StackTape.length_tail_le, Cslib.Turing.StackTape.length_cons_none, Cslib.Turing.StackTape.length_cons_some, Cslib.Turing.StackTape.length_cons_le, Cslib.Turing.StackTape.length_mapSome, Cslib.Turing.StackTape.length_nil
statement: formalized
proof: formalized
---

# StackTape: Infinite, eventually-`none` lists of `Option`s

`Cslib.Foundations.Data.StackTape`, in [Cslib/Foundations/Data/StackTape.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean), by Bolton Bailey.

> This file defines `StackTape`, a stack-like data structure of `Option` values,
> where the tape is considered to be infinite and eventually all `none`s.
> This is useful as a data structure with a simple API for manipulation by Turing machines.
>
> ## Design
>
> `StackTape` is represented as a list of `Option` values where the list cannot end with `none`.
> The end of the list is then treated as the start of an infinite sequence of `none` values
> by the low-level API.
> This design makes it convenient to express the length of the tape in terms of the list length.
>
> An alternative design would be to represent the tape as a `Stream' (Option Symbol)`,
> with additional fields tracking the length and the fact that the stream eventually becomes `none`.
> This design might complicate reasoning about the length of the tape, but could make other operations
> more straightforward.
>
> …

`Cslib.Turing.StackTape` (structure, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L49))

> An infinite tape representation using a list of `Option` values,
> where the list is eventually `none`.
>
> Represented as a `List (Option Symbol)` that does not end with `none`.

```lean
structure StackTape (Symbol : Type*) where
  /-- The underlying list representation -/
  toList : List (Option Symbol)
  /--
  The list can be empty (i.e. `none`),
  but if it is not empty, the last element is not (`some`) `none`
  -/
  toList_getLast?_ne_some_none : toList.getLast? ≠ some none
```

`Cslib.Turing.StackTape.nil` (definition, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L65))

> The empty `StackTape`

```lean
def nil : StackTape Symbol
```

`Cslib.Turing.StackTape.empty_eq_nil` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L74))

```lean
lemma empty_eq_nil : (∅ : StackTape Symbol) = nil
```

`Cslib.Turing.StackTape.nil_toList` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L77))

```lean
lemma nil_toList : (nil : StackTape Symbol).toList = []
```

`Cslib.Turing.StackTape.cons` (definition, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L80))

> Prepend an `Option` to the `StackTape`

```lean
def cons (x : Option Symbol) (xs : StackTape Symbol) : StackTape Symbol
```

`Cslib.Turing.StackTape.cons_none_nil_toList` (lemma, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L87))

```lean
lemma cons_none_nil_toList : (cons none (nil : StackTape Symbol)).toList = []
```

`Cslib.Turing.StackTape.cons_some_toList` (lemma, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L91))

```lean
lemma cons_some_toList (a : Symbol) (l : StackTape Symbol) :
    (cons (some a) l).toList = some a :: l.toList
```

`Cslib.Turing.StackTape.tail` (definition, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L96))

> Remove the first element of the `StackTape`, returning the rest

```lean
def tail (l : StackTape Symbol) : StackTape Symbol
```

`Cslib.Turing.StackTape.head` (definition, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L103))

> Get the first element of the `StackTape`.

```lean
def head (l : StackTape Symbol) : Option Symbol
```

`Cslib.Turing.StackTape.eq_iff` (lemma, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L108))

```lean
lemma eq_iff (l1 l2 : StackTape Symbol) :
    l1 = l2 ↔ l1.head = l2.head ∧ l1.tail = l2.tail
```

`Cslib.Turing.StackTape.head_cons` (lemma, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L118))

```lean
lemma head_cons (o : Option Symbol) (l : StackTape Symbol) : (cons o l).head = o
```

`Cslib.Turing.StackTape.tail_cons` (lemma, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L126))

```lean
lemma tail_cons (o : Option Symbol) (l : StackTape Symbol) : (cons o l).tail = l
```

`Cslib.Turing.StackTape.cons_head_tail` (lemma, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L135))

```lean
lemma cons_head_tail (l : StackTape Symbol) :
    cons (l.head) (l.tail) = l
```

`Cslib.Turing.StackTape.mapSome` (definition, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L142))

> Create a `StackTape` from a list by mapping all elements to `some`

```lean
def mapSome (l : List Symbol) : StackTape Symbol
```

`Cslib.Turing.StackTape.length` (definition, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L148))

> The length of the `StackTape` is the number of elements up to the last non-`none` element

```lean
def length (l : StackTape Symbol) : ℕ
```

`Cslib.Turing.StackTape.length_tail_le` (lemma, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L150))

```lean
lemma length_tail_le (l : StackTape Symbol) : l.tail.length ≤ l.length
```

`Cslib.Turing.StackTape.length_cons_none` (lemma, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L156))

```lean
lemma length_cons_none (l : StackTape Symbol) :
    (cons none l).length = l.length + if l.length = 0 then 0 else 1
```

`Cslib.Turing.StackTape.length_cons_some` (lemma, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L161))

```lean
lemma length_cons_some (a : Symbol) (l : StackTape Symbol) :
    (cons (some a) l).length = l.length + 1
```

`Cslib.Turing.StackTape.length_cons_le` (lemma, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L165))

```lean
lemma length_cons_le (o : Option Symbol) (l : StackTape Symbol) :
    (cons o l).length ≤ l.length + 1
```

`Cslib.Turing.StackTape.length_mapSome` (lemma, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L170))

```lean
lemma length_mapSome (l : List Symbol) : (mapSome l).length = l.length
```

`Cslib.Turing.StackTape.length_nil` (lemma, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean#L173))

```lean
lemma length_nil : (nil : StackTape Symbol).length = 0
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/StackTape.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/StackTape.lean)
