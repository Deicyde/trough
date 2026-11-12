---
catalog: module
lean: List.mergeM, List.nil_mergeM, List.mergeM_right, List.cons_mergeM_cons, List.mergeM_pure, List.idRun_mergeM, Cslib.IsMonadHom.map_listMergeM, List.mergeSortM, List.mergeSortM_nil, List.mergeSortM_singleton, List.mergeSortM_pure, List.idRun_mergeSortM, Cslib.IsMonadHom.map_listMergeSortM
statement: formalized
proof: formalized
---

# A Monadic version of the builtin `List.mergeSort`

`Cslib.Algorithms.Lean.Sort.Merge`, in [Cslib/Algorithms/Lean/Sort/Merge.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean), by Kim Morrison, Eric Wieser.

> This can be instantiated with `Id` to recover the original, or with `TimeM` or `FreeM` for
> algorithmic analysis.

`List.mergeM` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L27))

> A monadic version of `List.merge`

```lean
def mergeM (xs ys : List α) (le : α → α → m Bool) : m (List α)
```

`List.nil_mergeM` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L38))

```lean
theorem nil_mergeM (ys : List α) (le : α → α → m Bool) : mergeM [] ys le = pure ys
```

`List.mergeM_right` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L41))

```lean
theorem mergeM_right (xs : List α) (le : α → α → m Bool) : mergeM xs [] le = pure xs
```

`List.cons_mergeM_cons` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L45))

```lean
theorem cons_mergeM_cons (x y : α) (xs ys : List α) (le : α → α → m Bool) :
mergeM (x :: xs) (y :: ys) le = do
if ← le x y then
return x :: (← mergeM xs (y :: ys) le)
else
return y :: (← mergeM (x :: xs) ys le)
```

`List.mergeM_pure` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L54))

```lean
theorem mergeM_pure [LawfulMonad m] (xs ys : List α) (le : α → α → Bool) :
    mergeM xs ys (fun x y => (pure (le x y) : m Bool)) = pure (merge xs ys le)
```

`List.idRun_mergeM` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L59))

```lean
theorem idRun_mergeM (xs ys : List α) (le : α → α → Id Bool) :
    Id.run (mergeM xs ys le) = merge xs ys (fun x y => Id.run <| le x y)
```

`Cslib.IsMonadHom.map_listMergeM` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L64))

```lean
theorem _root_.Cslib.IsMonadHom.map_listMergeM {f : {β : Type} → m β → n β}
    (hf : IsMonadHom m n f) (xs ys : List α) (le : α → α → m Bool) :
    f (mergeM xs ys le) = mergeM xs ys (fun x y => f (le x y))
```

`List.mergeSortM` (definition, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L72))

> A monadic version of `List.mergeSortM`

```lean
def mergeSortM (xs : List α) (le : α → α → m Bool) : m (List α)
```

`List.mergeSortM_nil` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L81))

```lean
theorem mergeSortM_nil (le : α → α → m Bool) : mergeSortM [] le = pure []
```

`List.mergeSortM_singleton` (theorem, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L83))

```lean
theorem mergeSortM_singleton (a : α) (le : α → α → m Bool) :
mergeSortM [a] le = pure [a]
```

`List.mergeSortM_pure` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L88))

```lean
theorem mergeSortM_pure [LawfulMonad m] (xs : List α) (le : α → α → Bool) :
    mergeSortM xs (fun x y => (pure (le x y) : m Bool)) = pure (mergeSort xs le)
```

`List.idRun_mergeSortM` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L98))

```lean
theorem idRun_mergeSortM (xs : List α) (le : α → α → Id Bool) :
    Id.run (mergeSortM xs le) = mergeSort xs (fun x y => Id.run <| le x y)
```

`Cslib.IsMonadHom.map_listMergeSortM` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean#L103))

```lean
theorem _root_.Cslib.IsMonadHom.map_listMergeSortM {f : {β : Type} → m β → n β}
    (hf : IsMonadHom m n f) (xs : List α) (le : α → α → m Bool) :
    f (mergeSortM xs le) = mergeSortM xs (fun x y => f (le x y))
```

## Depends on

- [(unbundled) morphisms of monads](../../../foundations/control/monad/ismonadhom.md)

## Sources

- [Cslib/Algorithms/Lean/Sort/Merge.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Sort/Merge.lean)
