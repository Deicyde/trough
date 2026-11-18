---
catalog: module
lean: Array.merge, Array.mergeDedupWith, Array.mergeDedup, Array.mergeUnsortedDedup, Array.mergeAdjacentDups, Array.dedupSorted, Array.sortDedup
statement: formalized
proof: formalized
---

# Merge

`Batteries.Data.Array.Merge`, in [Batteries/Data/Array/Merge.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean), by Jannis Limperg.

`Array.merge` (definition, [line 16](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean#L16))

> `O(|xs| + |ys|)`. Merge arrays `xs` and `ys`. If the arrays are sorted according to `lt`, then the
> result is sorted as well. If two (or more) elements are equal according to `lt`, they are preserved.

```lean
def merge (lt : α → α → Bool) (xs ys : Array α) : Array α
```

`Array.mergeDedupWith` (definition, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean#L39))

> `O(|xs| + |ys|)`. Merge arrays `xs` and `ys`, which must be sorted according to `compare` and must
> not contain duplicates. Equal elements are merged using `merge`. If `merge` respects the order
> (i.e. for all `x`, `y`, `y'`, `z`, if `x < y < z` and `x < y' < z` then `x < merge y y' < z`)
> then the resulting array is again sorted.

```lean
def mergeDedupWith [ord : Ord α] (xs ys : Array α) (merge : α → α → α) : Array α
```

`Array.mergeDedup` (definition, [line 61](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean#L61))

> `O(|xs| + |ys|)`. Merge arrays `xs` and `ys`, which must be sorted according to `compare` and must
> not contain duplicates. If an element appears in both `xs` and `ys`, only one copy is kept.

```lean
def mergeDedup [ord : Ord α] (xs ys : Array α) : Array α
```

`Array.mergeUnsortedDedup` (definition, [line 70](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean#L70))

> `O(|xs| * |ys|)`. Merge `xs` and `ys`, which do not need to be sorted. Elements which occur in
> both `xs` and `ys` are only added once. If `xs` and `ys` do not contain duplicates, then neither
> does the result.

```lean
def mergeUnsortedDedup [eq : BEq α] (xs ys : Array α) : Array α
```

`Array.mergeAdjacentDups` (definition, [line 87](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean#L87))

> `O(|xs|)`. Replace each run `[x₁, ⋯, xₙ]` of equal elements in `xs` with
> `f ⋯ (f (f x₁ x₂) x₃) ⋯ xₙ`.

```lean
def mergeAdjacentDups [eq : BEq α] (f : α → α → α) (xs : Array α) : Array α
```

`Array.dedupSorted` (definition, [line 103](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean#L103))

> `O(|xs|)`. Deduplicate a sorted array. The array must be sorted with to an order which agrees with
> `==`, i.e. whenever `x == y` then `compare x y == .eq`.

```lean
def dedupSorted [eq : BEq α] (xs : Array α) : Array α
```

`Array.sortDedup` (definition, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean#L107))

> `O(|xs| log |xs|)`. Sort and deduplicate an array.

```lean
def sortDedup [ord : Ord α] (xs : Array α) : Array α
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Array/Merge.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Merge.lean)
