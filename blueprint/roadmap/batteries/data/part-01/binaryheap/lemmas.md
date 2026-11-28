---
catalog: module
lean: Batteries.BinaryHeap.popMax_perm, Batteries.BinaryHeap.toSortedArray_perm, Batteries.BinaryHeap.size_empty, Batteries.BinaryHeap.size_singleton, Batteries.BinaryHeap.empty_wf, Batteries.BinaryHeap.singleton_wf, Batteries.BinaryHeap.max_empty, Batteries.BinaryHeap.max_singleton, Batteries.BinaryHeap.mkHeap_wf, Batteries.BinaryHeap.mkHeap_perm, Batteries.BinaryHeap.extractMax_fst, Batteries.BinaryHeap.extractMax_snd, Batteries.BinaryHeap.size_decreaseKey, Batteries.BinaryHeap.size_increaseKey, Batteries.BinaryHeap.insert_wf, Batteries.BinaryHeap.mem_empty, Batteries.BinaryHeap.mem_singleton, Batteries.BinaryHeap.mem_insert, Batteries.BinaryHeap.mem_iff_get, Batteries.BinaryHeap.max_ge_all, Batteries.BinaryHeap.popMax_wf, Batteries.BinaryHeap.replaceMax_wf, Batteries.BinaryHeap.insertExtractMax_wf, Batteries.BinaryHeap.size_insertExtractMax, Batteries.BinaryHeap.insertExtractMax_fst_of_empty, Batteries.BinaryHeap.insertExtractMax_fst_of_lt, Batteries.BinaryHeap.insertExtractMax_fst_of_not_lt, Batteries.BinaryHeap.insertExtractMax_empty, Batteries.BinaryHeap.replaceMax_empty, Batteries.BinaryHeap.size_replaceMax_of_empty, Batteries.BinaryHeap.size_replaceMax_of_nonempty, Batteries.BinaryHeap.replaceMax_fst, Batteries.BinaryHeap.popMax_empty, Batteries.BinaryHeap.extractMax_empty, Batteries.BinaryHeap.mem_of_mem_popMax, Batteries.BinaryHeap.decreaseKey_wf, Batteries.BinaryHeap.increaseKey_wf, Batteries.BinaryHeap.toSortedArray_sorted, Batteries.BinaryHeap.size_toSortedArray, Batteries.BinaryHeap.mem_toSortedArray, Array.toBinaryHeap_wf, Vector.toBinaryHeap_wf, Array.size_toBinaryHeap, Batteries.Vector.size_toBinaryHeap, Array.mem_toBinaryHeap, Batteries.Vector.mem_toBinaryHeap, Array.heapSort_perm, Array.size_heapSort, Array.heapSort_sorted
statement: formalized
proof: formalized
---

# BinaryHeap/Lemmas

`Batteries.Data.BinaryHeap.Lemmas`, in [Batteries/Data/BinaryHeap/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean), by Chad Sharp.

> ### heapifyDown related lemmas

> ### heapifyUp related lemmas

> Other permutation related lemmas

`Batteries.BinaryHeap.popMax_perm` (theorem, [line 265](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L265))

> popMax returns a permutation: the original is a perm of max :: popMax

```lean
public theorem popMax_perm [Ord α] {heap : BinaryHeap α} (h : 0 < heap.size) :
    (heap.arr[0] :: heap.popMax.arr.toList).Perm heap.arr.toList
```

`Batteries.BinaryHeap.toSortedArray_perm` (theorem, [line 302](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L302))

> `toSortedArray` produces a permutation of the heap.

```lean
public theorem toSortedArray_perm [Ord α] (heap : BinaryHeap α) :
    heap.toSortedArray.Perm heap.arr
```

`Batteries.BinaryHeap.size_empty` (theorem, [line 335](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L335))

```lean
theorem size_empty [Ord α] : (@empty α).size = 0
```

`Batteries.BinaryHeap.size_singleton` (theorem, [line 339](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L339))

```lean
theorem size_singleton [Ord α] {x : α} : (singleton x).size = 1
```

`Batteries.BinaryHeap.empty_wf` (theorem, [line 343](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L343))

```lean
theorem empty_wf [Ord α] : WF (empty : BinaryHeap α)
```

`Batteries.BinaryHeap.singleton_wf` (theorem, [line 348](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L348))

```lean
theorem singleton_wf [Ord α] {x : α} : WF (singleton x)
```

`Batteries.BinaryHeap.max_empty` (theorem, [line 353](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L353))

```lean
theorem max_empty [Ord α] : (empty : BinaryHeap α).max = none
```

`Batteries.BinaryHeap.max_singleton` (theorem, [line 357](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L357))

```lean
theorem max_singleton [Ord α] {x : α} : (singleton x).max = some x
```

`Batteries.BinaryHeap.mkHeap_wf` (theorem, [line 362](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L362))

> Constructing a heap from a vector produces a well-formed heap.

```lean
theorem mkHeap_wf [Ord α] [Std.TransOrd α] {a : Vector α sz} :
    WF.TopDown (mkHeap a)
```

`Batteries.BinaryHeap.mkHeap_perm` (theorem, [line 367](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L367))

```lean
theorem mkHeap_perm [Ord α] {a : Vector α sz} : (mkHeap a).toArray.Perm a.toArray
```

`Batteries.BinaryHeap.extractMax_fst` (theorem, [line 371](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L371))

```lean
theorem extractMax_fst [Ord α] (heap : BinaryHeap α) :
    heap.extractMax.1 = heap.max
```

`Batteries.BinaryHeap.extractMax_snd` (theorem, [line 375](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L375))

```lean
theorem extractMax_snd [Ord α] (heap : BinaryHeap α) :
    heap.extractMax.2 = heap.popMax
```

`Batteries.BinaryHeap.size_decreaseKey` (theorem, [line 379](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L379))

```lean
theorem size_decreaseKey [Ord α] (heap : BinaryHeap α) (i : Fin heap.size) (x : α) :
    (heap.decreaseKey i x).size = heap.size
```

`Batteries.BinaryHeap.size_increaseKey` (theorem, [line 384](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L384))

```lean
theorem size_increaseKey [Ord α] (heap : BinaryHeap α) (i : Fin heap.size) (x : α) :
    (heap.increaseKey i x).size = heap.size
```

`Batteries.BinaryHeap.insert_wf` (theorem, [line 389](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L389))

```lean
theorem insert_wf [Ord α] [Std.TransOrd α] {heap : BinaryHeap α} (h_wf : heap.WF) :
    (heap.insert x).WF
```

`Batteries.BinaryHeap.mem_empty` (theorem, [line 399](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L399))

```lean
theorem mem_empty [Ord α] {x : α} : ¬x ∈ empty
```

`Batteries.BinaryHeap.mem_singleton` (theorem, [line 403](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L403))

```lean
theorem mem_singleton [Ord α] {x : α} : x ∈ singleton y ↔ x = y
```

`Batteries.BinaryHeap.mem_insert` (theorem, [line 407](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L407))

```lean
theorem mem_insert [Ord α] {heap : BinaryHeap α} :
    y ∈ heap.insert x ↔ y ∈ heap ∨ y = x
```

`Batteries.BinaryHeap.mem_iff_get` (theorem, [line 411](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L411))

```lean
theorem mem_iff_get [Ord α] {heap : BinaryHeap α} :
    a ∈ heap ↔ ∃ i : Fin heap.size, heap.get i = a
```

`Batteries.BinaryHeap.max_ge_all` (theorem, [line 417](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L417))

```lean
theorem max_ge_all [Ord α] [Std.TransOrd α]
    {heap : BinaryHeap α} (hwf : WF heap) (h_in: y ∈ heap) (h_ne : heap.size > 0) :
    compare (heap.max.get <| by simp_all [max,size]) y |>.isGE
```

`Batteries.BinaryHeap.popMax_wf` (theorem, [line 427](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L427))

> Removing the maximum element from a well-formed heap preserves well-formedness.

```lean
theorem popMax_wf [Ord α] [Std.TransOrd α] {heap : BinaryHeap α} (h_wf : WF heap) :
    WF (heap.popMax)
```

`Batteries.BinaryHeap.replaceMax_wf` (theorem, [line 438](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L438))

> Replacing the maximum element in a well-formed heap preserves well-formedness.

```lean
theorem replaceMax_wf [Ord α] [Std.TransOrd α] {heap : BinaryHeap α} (h_wf : WF heap) :
    WF (heap.replaceMax x).2
```

`Batteries.BinaryHeap.insertExtractMax_wf` (theorem, [line 446](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L446))

```lean
theorem insertExtractMax_wf [Ord α] [Std.TransOrd α] {heap : BinaryHeap α} (h_wf : WF heap) :
    WF (heap.insertExtractMax x).2
```

`Batteries.BinaryHeap.size_insertExtractMax` (theorem, [line 456](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L456))

```lean
theorem size_insertExtractMax [Ord α] (heap : BinaryHeap α) (x : α) :
    (heap.insertExtractMax x).2.size = heap.size
```

`Batteries.BinaryHeap.insertExtractMax_fst_of_empty` (theorem, [line 461](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L461))

```lean
theorem insertExtractMax_fst_of_empty [Ord α] {heap : BinaryHeap α} (h : heap.size = 0) (x : α) :
    (heap.insertExtractMax x).1 = x
```

`Batteries.BinaryHeap.insertExtractMax_fst_of_lt` (theorem, [line 465](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L465))

```lean
theorem insertExtractMax_fst_of_lt [Ord α] {heap : BinaryHeap α}
    (hmax : heap.max = some m) (h_lt : (compare x m).isLT) :
    (heap.insertExtractMax x).1 = m
```

`Batteries.BinaryHeap.insertExtractMax_fst_of_not_lt` (theorem, [line 470](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L470))

```lean
theorem insertExtractMax_fst_of_not_lt [Ord α] {heap : BinaryHeap α}
    (hmax : heap.max = some m) (h_nlt : ¬(compare x m).isLT) :
    (heap.insertExtractMax x).1 = x
```

`Batteries.BinaryHeap.insertExtractMax_empty` (theorem, [line 476](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L476))

```lean
theorem insertExtractMax_empty [Ord α] (x : α) : empty.insertExtractMax x = (x, empty)
```

`Batteries.BinaryHeap.replaceMax_empty` (theorem, [line 480](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L480))

```lean
theorem replaceMax_empty [Ord α] (x : α) : empty.replaceMax x = (none, singleton x)
```

`Batteries.BinaryHeap.size_replaceMax_of_empty` (theorem, [line 484](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L484))

```lean
theorem size_replaceMax_of_empty [Ord α] {heap : BinaryHeap α} (h : heap.size = 0) (x : α) :
    (heap.replaceMax x).2.size = 1
```

`Batteries.BinaryHeap.size_replaceMax_of_nonempty` (theorem, [line 489](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L489))

```lean
theorem size_replaceMax_of_nonempty [Ord α] {heap : BinaryHeap α} (h : heap.size ≠ 0) (x : α) :
    (heap.replaceMax x).2.size = heap.size
```

`Batteries.BinaryHeap.replaceMax_fst` (theorem, [line 495](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L495))

```lean
theorem replaceMax_fst [Ord α] (heap : BinaryHeap α) (x : α) :
    (heap.replaceMax x).1 = heap.max
```

`Batteries.BinaryHeap.popMax_empty` (theorem, [line 500](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L500))

```lean
theorem popMax_empty [Ord α] : (empty : BinaryHeap α).popMax = empty
```

`Batteries.BinaryHeap.extractMax_empty` (theorem, [line 504](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L504))

```lean
theorem extractMax_empty [Ord α] : (empty : BinaryHeap α).extractMax = (none, empty)
```

`Batteries.BinaryHeap.mem_of_mem_popMax` (theorem, [line 508](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L508))

> Elements in popMax were in the original heap

```lean
theorem mem_of_mem_popMax [Ord α] {heap : BinaryHeap α} (h : x ∈ heap.popMax) :
    x ∈ heap
```

`Batteries.BinaryHeap.decreaseKey_wf` (theorem, [line 518](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L518))

> Decreasing a key value in a well-formed heap and reheapifying downward preserves
> well-formedness.

```lean
theorem decreaseKey_wf [Ord α] [Std.TransOrd α] {heap : BinaryHeap α}
    {i : Fin heap.size} (hwf : WF heap) (h_ge : compare (heap.get i) x |>.isGE) :
    WF (heap.decreaseKey i x)
```

`Batteries.BinaryHeap.increaseKey_wf` (theorem, [line 534](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L534))

> Increasing a key value in a well-formed heap and reheapifying upward preserves well-formedness.

```lean
theorem increaseKey_wf [Ord α] [Std.TransOrd α] {heap : BinaryHeap α}
    {i : Fin heap.size} (h_wf : WF heap) (h_ge : compare x (heap.get i) |>.isGE) :
    WF (heap.increaseKey i x)
```

`Batteries.BinaryHeap.toSortedArray_sorted` (theorem, [line 561](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L561))

> toSortedArray produces a sorted array if the heap is well-formed

```lean
theorem toSortedArray_sorted [Ord α] [Std.TransOrd α] {heap : BinaryHeap α} (hwf : WF heap) :
    heap.toSortedArray.toList.Pairwise (compare · · |>.isGE)
```

`Batteries.BinaryHeap.size_toSortedArray` (theorem, [line 566](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L566))

```lean
theorem size_toSortedArray [Ord α] {heap : BinaryHeap α} : heap.toSortedArray.size = heap.size
```

`Batteries.BinaryHeap.mem_toSortedArray` (theorem, [line 570](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L570))

```lean
theorem mem_toSortedArray [Ord α] {heap : BinaryHeap α} {x : α} :
    x ∈ heap.toSortedArray ↔ x ∈ heap
```

`Array.toBinaryHeap_wf` (theorem, [line 582](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L582))

> Converting an array to a binary heap produces a well-formed heap.

```lean
theorem Array.toBinaryHeap_wf [Ord α] [Std.TransOrd α] {a : Array α} : WF (a.toBinaryHeap)
```

`Vector.toBinaryHeap_wf` (theorem, [line 587](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L587))

> Converting a vector to a binary heap produces a well-formed heap.

```lean
theorem Vector.toBinaryHeap_wf [Ord α] [Std.TransOrd α] {a : Vector α sz} :
    WF a.toBinaryHeap
```

`Array.size_toBinaryHeap` (theorem, [line 592](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L592))

```lean
theorem Array.size_toBinaryHeap [Ord α] {a : Array α} : a.toBinaryHeap.size = a.size
```

`Batteries.Vector.size_toBinaryHeap` (theorem, [line 596](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L596))

```lean
theorem Batteries.Vector.size_toBinaryHeap [Ord α] {a : Vector α sz} :
    a.toBinaryHeap.size = sz
```

`Array.mem_toBinaryHeap` (theorem, [line 601](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L601))

```lean
theorem Array.mem_toBinaryHeap [Ord α] {a : Array α} : x ∈ a.toBinaryHeap ↔ x ∈ a
```

`Batteries.Vector.mem_toBinaryHeap` (theorem, [line 605](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L605))

```lean
theorem Batteries.Vector.mem_toBinaryHeap [Ord α] {a : Vector α sz} {x : α} :
    x ∈ a.toBinaryHeap ↔ x ∈ a
```

`Array.heapSort_perm` (theorem, [line 610](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L610))

```lean
theorem Array.heapSort_perm [instOrd : Ord α] {a : Array α} : a.heapSort.Perm a
```

`Array.size_heapSort` (theorem, [line 616](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L616))

```lean
theorem Array.size_heapSort [Ord α] {a : Array α} : a.heapSort.size = a.size
```

`Array.heapSort_sorted` (theorem, [line 620](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean#L620))

> `heapSort` produces a sorted array.

```lean
theorem Array.heapSort_sorted [instOrd : Ord α] [Std.TransOrd α] {a : Array α} :
    a.heapSort.toList.Pairwise (compare · · |>.isLE)
```

## Depends on

- [WF](wf.md)

## Proof depends on

- [Vector/Lemmas](../../part-02/vector/lemmas.md)

## Sources

- [Batteries/Data/BinaryHeap/Lemmas.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/BinaryHeap/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.BinaryHeap.Lemmas.json)
