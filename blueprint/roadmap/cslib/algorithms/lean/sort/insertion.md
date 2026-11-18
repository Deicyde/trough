---
catalog: module
lean: List.orderedInsertM, List.orderedInsertM_nil, List.orderedInsertM_cons, List.orderedInsertM_pure, List.idRun_orderedInsertM, Cslib.IsMonadHom.map_orderedInsertM, List.insertionSortM, List.insertionSortM_nil, List.insertionSortM_cons, List.insertionSortM_pure, List.idRun_insertionSortM, Cslib.IsMonadHom.map_listInsertionSortM
statement: formalized
proof: formalized
---

# A Monadic version of Mathlib's `List.insertionSort`

`Cslib.Algorithms.Lean.Sort.Insertion`, in [Cslib/Algorithms/Lean/Sort/Insertion.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean), by Jeremy Avigad, Eric Wieser.

> This can be instantiated with `Id` to recover the original, or with `TimeM` or `FreeM` for
> algorithmic analysis.

`List.orderedInsertM` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L27))

> A monadic version of `List.orderedInsert`.

```lean
def orderedInsertM (a : α) : List α → m (List α)
```

`List.orderedInsertM_nil` (theorem, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L31))

```lean
theorem orderedInsertM_nil (a : α) : orderedInsertM r a [] = pure [a]
```

`List.orderedInsertM_cons` (theorem, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L33))

```lean
theorem orderedInsertM_cons (a b : α) (l : List α) :
    orderedInsertM r a (b :: l) = do
      if ← r a b then return a :: b :: l else return b :: (← orderedInsertM r a l)
```

`List.orderedInsertM_pure` (theorem, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L39))

```lean
theorem orderedInsertM_pure [LawfulMonad m] (r : α → α → Bool) (a : α) (xs : List α) :
    orderedInsertM (fun x y => (pure (r x y) : m Bool)) a xs =
      pure (orderedInsert (r · ·) a xs)
```

`List.idRun_orderedInsertM` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L45))

```lean
theorem idRun_orderedInsertM (r : α → α → Id Bool) (a : α) (xs : List α) :
    Id.run (orderedInsertM r a xs) = orderedInsert (fun x y => Id.run <| r x y) a xs
```

`Cslib.IsMonadHom.map_orderedInsertM` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L50))

```lean
theorem _root_.Cslib.IsMonadHom.map_orderedInsertM {f : {β : Type} → m β → n β}
    (hf : IsMonadHom m n f) (r : α → α → m Bool) (a : α) (xs : List α) :
    f (orderedInsertM r a xs) = orderedInsertM (fun x y => f (r x y)) a xs
```

`List.insertionSortM` (definition, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L56))

> A monadic version of `List.insertionSort`.

```lean
def insertionSortM : List α → m (List α)
```

`List.insertionSortM_nil` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L60))

```lean
theorem insertionSortM_nil : insertionSortM r [] = pure []
```

`List.insertionSortM_cons` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L62))

```lean
theorem insertionSortM_cons (b : α) (l : List α) :
    insertionSortM r (b :: l) = (do orderedInsertM r b (← insertionSortM r l))
```

`List.insertionSortM_pure` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L67))

```lean
theorem insertionSortM_pure [LawfulMonad m] (xs : List α) (r : α → α → Bool) :
    insertionSortM (fun x y => (pure (r x y) : m Bool)) xs = pure (insertionSort (r · ·) xs)
```

`List.idRun_insertionSortM` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L72))

```lean
theorem idRun_insertionSortM (xs : List α) (r : α → α → Id Bool) :
    Id.run (insertionSortM r xs) = insertionSort (fun x y => Id.run <| r x y) xs
```

`Cslib.IsMonadHom.map_listInsertionSortM` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean#L77))

```lean
theorem _root_.Cslib.IsMonadHom.map_listInsertionSortM {f : {β : Type} → m β → n β}
    (hf : IsMonadHom m n f) (r : α → α → m Bool) (xs : List α) :
    f (insertionSortM r xs) = insertionSortM (fun x y => f (r x y)) xs
```

## Depends on

- [(unbundled) morphisms of monads](../../../foundations/control/monad/ismonadhom.md)

## Sources

- [Cslib/Algorithms/Lean/Sort/Insertion.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Insertion.lean)
