---
catalog: module
lean: Batteries.BinaryHeap, Batteries.BinaryHeap.maxChild, Batteries.BinaryHeap.maxChild_gt, Batteries.BinaryHeap.heapifyDown, Batteries.BinaryHeap.mkHeap, Batteries.BinaryHeap.heapifyUp, Batteries.BinaryHeap.empty, Batteries.BinaryHeap.mem_def, Batteries.BinaryHeap.singleton, Batteries.BinaryHeap.size, Batteries.BinaryHeap.vector, Batteries.BinaryHeap.toArray_vector, Batteries.BinaryHeap.mem_vector, Batteries.BinaryHeap.get, Batteries.BinaryHeap.insert, Batteries.BinaryHeap.size_insert, Batteries.BinaryHeap.max, Batteries.BinaryHeap.popMax, Batteries.BinaryHeap.size_popMax, Batteries.BinaryHeap.extractMax, Batteries.BinaryHeap.max_eq_none_iff, Batteries.BinaryHeap.size_pos_of_max, Batteries.BinaryHeap.insertExtractMax, Batteries.BinaryHeap.replaceMax, Batteries.BinaryHeap.decreaseKey, Batteries.BinaryHeap.increaseKey, Batteries.BinaryHeap.toSortedArray, Vector.toBinaryHeap, Array.toBinaryHeap, Array.heapSort
statement: formalized
proof: formalized
---

# BinaryHeap/Basic

`Batteries.Data.BinaryHeap.Basic`, in [Batteries/Data/BinaryHeap/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean), by Mario Carneiro, François G. Dorais, Chad Sharp.

`Batteries.BinaryHeap` (structure, [line 13](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L13))

> A max-heap data structure.

```lean
structure BinaryHeap (α : Type w) [Ord α] where
  /-- `O(1)`. Get data array for a `BinaryHeap`. -/
  arr : Array α
```

`Batteries.BinaryHeap.maxChild` (definition, [line 21](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L21))

> Given a node, return the index of its larger child, if it exists

```lean
def maxChild [Ord α] (a : Vector α sz) (i : Fin sz) : Option (Fin sz)
```

`Batteries.BinaryHeap.maxChild_gt` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L35))

> maxChild returns an index greater than i.

```lean
theorem maxChild_gt [Ord α] {a : Vector α sz} {i : Fin sz} {j : Fin sz}
    (h : maxChild a i = some j) : i < j
```

`Batteries.BinaryHeap.heapifyDown` (definition, [line 42](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L42))

> Core operation for binary heaps, expressed directly on arrays.
> Given an array which is a max-heap, push item `i` down to restore the max-heap property.

```lean
def heapifyDown [Ord α] (a : Vector α sz) (i : Fin sz) :
    Vector α sz
```

`Batteries.BinaryHeap.mkHeap` (definition, [line 56](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L56))

> Core operation for binary heaps, expressed directly on arrays.
> Construct a heap from an unsorted array, by heapifying all the elements.

```lean
def mkHeap [Ord α] (a : Vector α sz) : Vector α sz
```

`Batteries.BinaryHeap.heapifyUp` (definition, [line 70](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L70))

> Core operation for binary heaps, expressed directly on arrays.
> Given an array which is a max-heap, push item `i` up to restore the max-heap property.

```lean
def heapifyUp [Ord α] (a : Vector α sz) (i : Fin sz) :
    Vector α sz
```

`Batteries.BinaryHeap.empty` (definition, [line 82](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L82))

> `O(1)`. Build a new empty heap.

```lean
def empty [Ord α] : BinaryHeap α
```

`Batteries.BinaryHeap.mem_def` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L89))

```lean
theorem mem_def [Ord α] {x : α} {h : BinaryHeap α} : x ∈ h ↔ x ∈ h.arr
```

`Batteries.BinaryHeap.singleton` (definition, [line 93](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L93))

> `O(1)`. Build a one-element heap.

```lean
def singleton [Ord α] (x : α) : BinaryHeap α
```

`Batteries.BinaryHeap.size` (definition, [line 97](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L97))

> `O(1)`. Get the number of elements in a `BinaryHeap`.

```lean
def size [Ord α] (heap : BinaryHeap α) : Nat
```

`Batteries.BinaryHeap.vector` (definition, [line 101](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L101))

> `O(1)`. Get data vector of a `BinaryHeap`.

```lean
def vector [Ord α] (heap : BinaryHeap α) : Vector α heap.size
```

`Batteries.BinaryHeap.toArray_vector` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L103))

```lean
theorem toArray_vector [Ord α] (heap : BinaryHeap α) : heap.vector.toArray = heap.arr
```

`Batteries.BinaryHeap.mem_vector` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L106))

```lean
theorem mem_vector [Ord α] {heap : BinaryHeap α} : x ∈ heap.vector ↔ x ∈ heap.arr
```

`Batteries.BinaryHeap.get` (definition, [line 111](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L111))

> `O(1)`. Get an element in the heap by index.

```lean
def get [Ord α] (heap : BinaryHeap α) (i : Fin heap.size) : α
```

`Batteries.BinaryHeap.insert` (definition, [line 115](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L115))

> `O(log n)`. Insert an element into a `BinaryHeap`, preserving the max-heap property.

```lean
def insert [Ord α] (heap : BinaryHeap α) (x : α) : BinaryHeap α
```

`Batteries.BinaryHeap.size_insert` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L118))

```lean
theorem size_insert [Ord α] (heap : BinaryHeap α) (x : α) :
    (heap.insert x).size = heap.size + 1
```

`Batteries.BinaryHeap.max` (definition, [line 124](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L124))

> `O(1)`. Get the maximum element in a `BinaryHeap`.

```lean
def max [Ord α] (heap : BinaryHeap α) : Option α
```

`Batteries.BinaryHeap.popMax` (definition, [line 129](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L129))

> `O(log n)`. Remove the maximum element from a `BinaryHeap`.
> Call `max` first to actually retrieve the maximum element.

```lean
def popMax [Ord α] (heap : BinaryHeap α) : BinaryHeap α
```

`Batteries.BinaryHeap.size_popMax` (theorem, [line 139](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L139))

```lean
theorem size_popMax [Ord α] (heap : BinaryHeap α) :
    heap.popMax.size = heap.size - 1
```

`Batteries.BinaryHeap.extractMax` (definition, [line 148](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L148))

> `O(log n)`. Return and remove the maximum element from a `BinaryHeap`.

```lean
def extractMax [Ord α] (heap : BinaryHeap α) : Option α × BinaryHeap α
```

`Batteries.BinaryHeap.max_eq_none_iff` (theorem, [line 152](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L152))

```lean
theorem max_eq_none_iff [Ord α] {heap : BinaryHeap α} :
    heap.max = none ↔ heap.size = 0
```

`Batteries.BinaryHeap.size_pos_of_max` (theorem, [line 156](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L156))

```lean
theorem size_pos_of_max [Ord α] {heap : BinaryHeap α} (h : heap.max = some x) :
    0 < heap.size
```

`Batteries.BinaryHeap.insertExtractMax` (definition, [line 165](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L165))

> `O(log n)`. Equivalent to `extractMax (heap.insert x)`, except that extraction cannot fail.

```lean
def insertExtractMax [Ord α] (heap : BinaryHeap α) (x : α) : α × BinaryHeap α
```

`Batteries.BinaryHeap.replaceMax` (definition, [line 176](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L176))

> `O(log n)`. Equivalent to `(heap.max, heap.popMax.insert x)`.

```lean
def replaceMax [Ord α] (heap : BinaryHeap α) (x : α) : Option α × BinaryHeap α
```

`Batteries.BinaryHeap.decreaseKey` (definition, [line 185](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L185))

> `O(log n)`. Replace the value at index `i` by `x`. Assumes that `x ≤ heap.get i`.

```lean
def decreaseKey [Ord α] (heap : BinaryHeap α) (i : Fin heap.size) (x : α) : BinaryHeap α
```

`Batteries.BinaryHeap.increaseKey` (definition, [line 190](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L190))

> `O(log n)`. Replace the value at index `i` by `x`. Assumes that `heap.get i ≤ x`.

```lean
def increaseKey [Ord α] (heap : BinaryHeap α) (i : Fin heap.size) (x : α) : BinaryHeap α
```

`Batteries.BinaryHeap.toSortedArray` (definition, [line 195](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L195))

> `O(n log n)`. Return the contents of `heap` as an array sorted in descending order.

```lean
def toSortedArray [Ord α] (heap : BinaryHeap α) : Array α
```

`Vector.toBinaryHeap` (definition, [line 212](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L212))

> `O(n)`. Convert an unsorted vector to a `BinaryHeap`.

```lean
def Vector.toBinaryHeap [Ord α] (v : Vector α n) : Batteries.BinaryHeap α
```

`Array.toBinaryHeap` (definition, [line 218](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L218))

> `O(n)`. Convert an unsorted array to a `BinaryHeap`.

```lean
def Array.toBinaryHeap [Ord α] (a : Array α) : Batteries.BinaryHeap α
```

`Array.heapSort` (definition, [line 223](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean#L223))

> `O(n log n)`. Sort an array using a `BinaryHeap`.

```lean
def Array.heapSort [instOrd : Ord α] (a : Array α) : Array α
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/BinaryHeap/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinaryHeap/Basic.lean)
