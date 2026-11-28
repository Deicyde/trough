---
catalog: module
lean: Array.equalSet_eq_true, Array.idxOf?_toList, Array.toList_erase, Array.size_eraseIdxIfInBounds, Array.toList_drop, Array.extract_empty_of_start_eq_stop, Array.extract_append_of_stop_le_size_left, Array.extract_append_of_size_left_le_start, Array.extract_eq_of_size_le_stop, Array.toList_swapIfInBounds
statement: formalized
proof: formalized
---

# Array/Lemmas

`Batteries.Data.Array.Lemmas`, in [Batteries/Data/Array/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean), by Mario Carneiro, Gabriel Ebner.

> ### equalSet

`Array.equalSet_eq_true` (theorem, [line 19](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L19))

```lean
theorem equalSet_eq_true [BEq α] [LawfulBEq α] (xs ys : Array α) :
    xs.equalSet ys = true ↔ ∀ a, a ∈ xs ↔ a ∈ ys
```

> ### idxOf?

`Array.idxOf?_toList` (theorem, [line 27](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L27))

```lean
theorem idxOf?_toList [BEq α] {a : α} {l : Array α} :
    l.toList.idxOf? a = l.idxOf? a
```

> ### erase

`Array.toList_erase` (theorem, [line 34](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L34))

```lean
theorem toList_erase [BEq α] (l : Array α) (a : α) :
    (l.erase a).toList = l.toList.erase a
```

`Array.size_eraseIdxIfInBounds` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L39))

```lean
theorem size_eraseIdxIfInBounds (a : Array α) (i : Nat) :
    (a.eraseIdxIfInBounds i).size = if i < a.size then a.size-1 else a.size
```

`Array.toList_drop` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L43))

```lean
theorem toList_drop (as: Array α) (n : Nat) :
    (as.drop n).toList = as.toList.drop n
```

> ### set

> ### map

> ### mem

> ### insertAt

> ### extract

`Array.extract_empty_of_start_eq_stop` (theorem, [line 57](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L57))

```lean
theorem extract_empty_of_start_eq_stop {a : Array α} :
    a.extract i i = #[]
```

`Array.extract_append_of_stop_le_size_left` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L60))

```lean
theorem extract_append_of_stop_le_size_left {a b : Array α} (h : j ≤ a.size) :
    (a ++ b).extract i j = a.extract i j
```

`Array.extract_append_of_size_left_le_start` (theorem, [line 63](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L63))

```lean
theorem extract_append_of_size_left_le_start {a b : Array α} (h : a.size ≤ i) :
    (a ++ b).extract i j = b.extract (i - a.size) (j - a.size)
```

`Array.extract_eq_of_size_le_stop` (theorem, [line 67](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L67))

```lean
theorem extract_eq_of_size_le_stop {a : Array α} (h : a.size ≤ j) :
    a.extract i j = a.extract i
```

> ### swapIfInBounds

`Array.toList_swapIfInBounds` (theorem, [line 71](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean#L71))

```lean
theorem toList_swapIfInBounds {a : Array α} :
    (a.swapIfInBounds i j).toList = a.toList.swap i j
```

## Depends on

- [Array/Basic](basic.md)
- [List/Basic](../list/part-01/basic.md)

## Proof depends on

- [List/Lemmas](../list/part-01/lemmas.md)

## Sources

- [Batteries/Data/Array/Lemmas.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Array.Lemmas.json)
