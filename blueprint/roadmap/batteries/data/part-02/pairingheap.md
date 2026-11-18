---
catalog: module
lean: Batteries.PairingHeapImp.Heap, Batteries.PairingHeapImp.Heap.size, Batteries.PairingHeapImp.Heap.singleton, Batteries.PairingHeapImp.Heap.isEmpty, Batteries.PairingHeapImp.Heap.merge, Batteries.PairingHeapImp.Heap.combine, Batteries.PairingHeapImp.Heap.headD, Batteries.PairingHeapImp.Heap.head?, Batteries.PairingHeapImp.Heap.deleteMin, Batteries.PairingHeapImp.Heap.tail?, Batteries.PairingHeapImp.Heap.tail, Batteries.PairingHeapImp.Heap.NoSibling, Batteries.PairingHeapImp.Heap.noSibling_merge, Batteries.PairingHeapImp.Heap.noSibling_combine, Batteries.PairingHeapImp.Heap.noSibling_deleteMin, Batteries.PairingHeapImp.Heap.noSibling_tail?, Batteries.PairingHeapImp.Heap.noSibling_tail, Batteries.PairingHeapImp.Heap.size_merge_node, Batteries.PairingHeapImp.Heap.size_merge, Batteries.PairingHeapImp.Heap.size_combine, Batteries.PairingHeapImp.Heap.size_deleteMin, Batteries.PairingHeapImp.Heap.size_tail?, Batteries.PairingHeapImp.Heap.size_tail, Batteries.PairingHeapImp.Heap.size_deleteMin_lt, Batteries.PairingHeapImp.Heap.size_tail?_lt, Batteries.PairingHeapImp.Heap.foldM, Batteries.PairingHeapImp.Heap.fold, Batteries.PairingHeapImp.Heap.toArray, Batteries.PairingHeapImp.Heap.toList, Batteries.PairingHeapImp.Heap.foldTreeM, Batteries.PairingHeapImp.Heap.foldTree, Batteries.PairingHeapImp.Heap.toListUnordered, Batteries.PairingHeapImp.Heap.toArrayUnordered, Batteries.PairingHeapImp.Heap.NodeWF, Batteries.PairingHeapImp.Heap.WF, Batteries.PairingHeapImp.Heap.WF.singleton, Batteries.PairingHeapImp.Heap.WF.merge_node, Batteries.PairingHeapImp.Heap.WF.merge, Batteries.PairingHeapImp.Heap.WF.combine, Batteries.PairingHeapImp.Heap.WF.deleteMin, Batteries.PairingHeapImp.Heap.WF.tail?, Batteries.PairingHeapImp.Heap.WF.tail, Batteries.PairingHeapImp.Heap.deleteMin_fst, Batteries.PairingHeap, Batteries.mkPairingHeap, Batteries.PairingHeap.empty, Batteries.PairingHeap.isEmpty, Batteries.PairingHeap.size, Batteries.PairingHeap.singleton, Batteries.PairingHeap.merge, Batteries.PairingHeap.insert, Batteries.PairingHeap.ofList, Batteries.PairingHeap.ofArray, Batteries.PairingHeap.deleteMin, Batteries.PairingHeap.head?, Batteries.PairingHeap.head!, Batteries.PairingHeap.headI, Batteries.PairingHeap.tail?, Batteries.PairingHeap.tail, Batteries.PairingHeap.toList, Batteries.PairingHeap.toArray, Batteries.PairingHeap.toListUnordered, Batteries.PairingHeap.toArrayUnordered
statement: formalized
proof: formalized
---

# PairingHeap

`Batteries.Data.PairingHeap`, in [Batteries/Data/PairingHeap.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean), by Yuyang Zhao.

`Batteries.PairingHeapImp.Heap` (inductive type, [line 24](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L24))

> A `Heap` is the nodes of the pairing heap.
> Each node have two pointers: `child` going to the first child of this node,
> and `sibling` goes to the next sibling of this tree.
> So it actually encodes a forest where each node has children
> `node.child`, `node.child.sibling`, `node.child.sibling.sibling`, etc.
>
> Each edge in this forest denotes a `le a b` relation that has been checked, so
> the root is smaller than everything else under it.

```lean
inductive Heap (α : Type u) where
  /-- An empty forest, which has depth `0`. -/
  | nil : Heap α
  /-- A forest consists of a root `a`, a forest `child` elements greater than `a`,
  and another forest `sibling`. -/
  | node (a : α) (child sibling : Heap α) : Heap α
  deriving Repr
```

`Batteries.PairingHeapImp.Heap.size` (definition, [line 33](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L33))

> `O(n)`. The number of elements in the heap.

```lean
def Heap.size : Heap α → Nat
```

`Batteries.PairingHeapImp.Heap.singleton` (definition, [line 38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L38))

> A node containing a single element `a`.

```lean
def Heap.singleton (a : α) : Heap α
```

`Batteries.PairingHeapImp.Heap.isEmpty` (definition, [line 41](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L41))

> `O(1)`. Is the heap empty?

```lean
def Heap.isEmpty : Heap α → Bool
```

`Batteries.PairingHeapImp.Heap.merge` (definition, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L46))

> `O(1)`. Merge two heaps. Ignore siblings.

```lean
def Heap.merge (le : α → α → Bool) : Heap α → Heap α → Heap α
```

`Batteries.PairingHeapImp.Heap.combine` (definition, [line 54](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L54))

> Auxiliary for `Heap.deleteMin`: merge the forest in pairs.

```lean
def Heap.combine (le : α → α → Bool) : Heap α → Heap α
```

`Batteries.PairingHeapImp.Heap.headD` (definition, [line 59](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L59))

> `O(1)`. Get the smallest element in the heap, including the passed in value `a`.

```lean
def Heap.headD (a : α) : Heap α → α
```

`Batteries.PairingHeapImp.Heap.head?` (definition, [line 64](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L64))

> `O(1)`. Get the smallest element in the heap, if it has an element.

```lean
def Heap.head? : Heap α → Option α
```

`Batteries.PairingHeapImp.Heap.deleteMin` (definition, [line 69](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L69))

> Amortized `O(log n)`. Find and remove the the minimum element from the heap.

```lean
def Heap.deleteMin (le : α → α → Bool) : Heap α → Option (α × Heap α)
```

`Batteries.PairingHeapImp.Heap.tail?` (definition, [line 74](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L74))

> Amortized `O(log n)`. Get the tail of the pairing heap after removing the minimum element.

```lean
def Heap.tail? (le : α → α → Bool) (h : Heap α) : Option (Heap α)
```

`Batteries.PairingHeapImp.Heap.tail` (definition, [line 78](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L78))

> Amortized `O(log n)`. Remove the minimum element of the heap.

```lean
def Heap.tail (le : α → α → Bool) (h : Heap α) : Heap α
```

`Batteries.PairingHeapImp.Heap.NoSibling` (inductive type, [line 82](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L82))

> A predicate says there is no more than one tree.

```lean
inductive Heap.NoSibling : Heap α → Prop
  /-- An empty heap is no more than one tree. -/
  | nil : NoSibling .nil
  /-- Or there is exactly one tree. -/
  | node (a c) : NoSibling (.node a c .nil)
```

`Batteries.PairingHeapImp.Heap.noSibling_merge` (theorem, [line 94](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L94))

```lean
theorem Heap.noSibling_merge (le) (s₁ s₂ : Heap α) :
    (s₁.merge le s₂).NoSibling
```

`Batteries.PairingHeapImp.Heap.noSibling_combine` (theorem, [line 99](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L99))

```lean
theorem Heap.noSibling_combine (le) (s : Heap α) :
    (s.combine le).NoSibling
```

`Batteries.PairingHeapImp.Heap.noSibling_deleteMin` (theorem, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L107))

```lean
theorem Heap.noSibling_deleteMin {s : Heap α} (eq : s.deleteMin le = some (a, s')) :
    s'.NoSibling
```

`Batteries.PairingHeapImp.Heap.noSibling_tail?` (theorem, [line 111](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L111))

```lean
theorem Heap.noSibling_tail? {s : Heap α} : s.tail? le = some s' →
    s'.NoSibling
```

`Batteries.PairingHeapImp.Heap.noSibling_tail` (theorem, [line 117](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L117))

```lean
theorem Heap.noSibling_tail (le) (s : Heap α) : (s.tail le).NoSibling
```

`Batteries.PairingHeapImp.Heap.size_merge_node` (theorem, [line 123](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L123))

```lean
theorem Heap.size_merge_node (le) (a₁ : α) (c₁ s₁ : Heap α) (a₂ : α) (c₂ s₂ : Heap α) :
    (merge le (.node a₁ c₁ s₁) (.node a₂ c₂ s₂)).size = c₁.size + c₂.size + 2
```

`Batteries.PairingHeapImp.Heap.size_merge` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L127))

```lean
theorem Heap.size_merge (le) {s₁ s₂ : Heap α} (h₁ : s₁.NoSibling) (h₂ : s₂.NoSibling) :
    (merge le s₁ s₂).size = s₁.size + s₂.size
```

`Batteries.PairingHeapImp.Heap.size_combine` (theorem, [line 133](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L133))

```lean
theorem Heap.size_combine (le) (s : Heap α) :
    (s.combine le).size = s.size
```

`Batteries.PairingHeapImp.Heap.size_deleteMin` (theorem, [line 142](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L142))

```lean
theorem Heap.size_deleteMin {s : Heap α} (h : s.NoSibling) (eq : s.deleteMin le = some (a, s')) :
    s.size = s'.size + 1
```

`Batteries.PairingHeapImp.Heap.size_tail?` (theorem, [line 146](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L146))

```lean
theorem Heap.size_tail? {s : Heap α} (h : s.NoSibling) : s.tail? le = some s' →
    s.size = s'.size + 1
```

`Batteries.PairingHeapImp.Heap.size_tail` (theorem, [line 152](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L152))

```lean
theorem Heap.size_tail (le) {s : Heap α} (h : s.NoSibling) : (s.tail le).size = s.size - 1
```

`Batteries.PairingHeapImp.Heap.size_deleteMin_lt` (theorem, [line 158](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L158))

```lean
theorem Heap.size_deleteMin_lt {s : Heap α} (eq : s.deleteMin le = some (a, s')) :
    s'.size < s.size
```

`Batteries.PairingHeapImp.Heap.size_tail?_lt` (theorem, [line 162](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L162))

```lean
theorem Heap.size_tail?_lt {s : Heap α} : s.tail? le = some s' →
    s'.size < s.size
```

`Batteries.PairingHeapImp.Heap.foldM` (definition, [line 172](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L172))

> `O(n log n)`. Monadic fold over the elements of a heap in increasing order,
> by repeatedly pulling the minimum element out of the heap.

```lean
def Heap.foldM [Monad m] (le : α → α → Bool) (s : Heap α)
    (init : β) (f : β → α → m β) : m β
```

`Batteries.PairingHeapImp.Heap.fold` (definition, [line 185](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L185))

> `O(n log n)`. Fold over the elements of a heap in increasing order,
> by repeatedly pulling the minimum element out of the heap.

```lean
def Heap.fold (le : α → α → Bool) (s : Heap α) (init : β) (f : β → α → β) : β
```

`Batteries.PairingHeapImp.Heap.toArray` (definition, [line 189](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L189))

> `O(n log n)`. Convert the heap to an array in increasing order.

```lean
def Heap.toArray (le : α → α → Bool) (s : Heap α) : Array α
```

`Batteries.PairingHeapImp.Heap.toList` (definition, [line 192](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L192))

> `O(n log n)`. Convert the heap to a list in increasing order.

```lean
def Heap.toList (le : α → α → Bool) (s : Heap α) : List α
```

`Batteries.PairingHeapImp.Heap.foldTreeM` (definition, [line 195](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L195))

> `O(n)`. Fold a monadic function over the tree structure to accumulate a value.

```lean
def Heap.foldTreeM [Monad m] (nil : β) (join : α → β → β → m β) : Heap α → m β
```

`Batteries.PairingHeapImp.Heap.foldTree` (definition, [line 200](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L200))

> `O(n)`. Fold a function over the tree structure to accumulate a value.

```lean
def Heap.foldTree (nil : β) (join : α → β → β → β) (s : Heap α) : β
```

`Batteries.PairingHeapImp.Heap.toListUnordered` (definition, [line 204](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L204))

> `O(n)`. Convert the heap to a list in arbitrary order.

```lean
def Heap.toListUnordered (s : Heap α) : List α
```

`Batteries.PairingHeapImp.Heap.toArrayUnordered` (definition, [line 208](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L208))

> `O(n)`. Convert the heap to an array in arbitrary order.

```lean
def Heap.toArrayUnordered (s : Heap α) : Array α
```

`Batteries.PairingHeapImp.Heap.NodeWF` (definition, [line 217](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L217))

> The well formedness predicate for a heap node.
> It asserts that:
> * If `a` is added at the top to make the forest into a tree, the resulting tree
>   is a `le`-min-heap (if `le` is well-behaved)

```lean
def Heap.NodeWF (le : α → α → Bool) (a : α) : Heap α → Prop
```

`Batteries.PairingHeapImp.Heap.WF` (inductive type, [line 227](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L227))

> The well formedness predicate for a pairing heap.
> It asserts that:
> * There is no more than one tree.
> * It is a `le`-min-heap (if `le` is well-behaved)

```lean
inductive Heap.WF (le : α → α → Bool) : Heap α → Prop
  /-- It is an empty heap. -/
  | nil : WF le .nil
  /-- There is exactly one tree and it is a `le`-min-heap. -/
  | node (h : c.NodeWF le a) : WF le (.node a c .nil)
```

`Batteries.PairingHeapImp.Heap.WF.singleton` (theorem, [line 233](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L233))

```lean
theorem Heap.WF.singleton : (Heap.singleton a).WF le
```

`Batteries.PairingHeapImp.Heap.WF.merge_node` (theorem, [line 235](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L235))

```lean
theorem Heap.WF.merge_node (h₁ : NodeWF le a₁ c₁) (h₂ : NodeWF le a₂ c₂) :
    (merge le (.node a₁ c₁ s₁) (.node a₂ c₂ s₂)).WF le
```

`Batteries.PairingHeapImp.Heap.WF.merge` (theorem, [line 242](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L242))

```lean
theorem Heap.WF.merge (h₁ : s₁.WF le) (h₂ : s₂.WF le) :
    (merge le s₁ s₂).WF le
```

`Batteries.PairingHeapImp.Heap.WF.combine` (theorem, [line 250](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L250))

```lean
theorem Heap.WF.combine (h : s.NodeWF le a) : (combine le s).WF le
```

`Batteries.PairingHeapImp.Heap.WF.deleteMin` (theorem, [line 256](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L256))

```lean
theorem Heap.WF.deleteMin {s : Heap α} (h : s.WF le)
    (eq : s.deleteMin le = some (a, s')) : s'.WF le
```

`Batteries.PairingHeapImp.Heap.WF.tail?` (theorem, [line 260](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L260))

```lean
theorem Heap.WF.tail? (hwf : (s : Heap α).WF le) : s.tail? le = some tl →
  tl.WF le
```

`Batteries.PairingHeapImp.Heap.WF.tail` (theorem, [line 266](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L266))

```lean
theorem Heap.WF.tail (hwf : (s : Heap α).WF le) : (s.tail le).WF le
```

`Batteries.PairingHeapImp.Heap.deleteMin_fst` (theorem, [line 272](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L272))

```lean
theorem Heap.deleteMin_fst : ((s : Heap α).deleteMin le).map (·.1) = s.head?
```

`Batteries.PairingHeap` (definition, [line 298](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L298))

> A [pairing heap](https://en.wikipedia.org/wiki/Pairing_heap) is a data structure which supports
> the following primary operations:
>
> * `insert : α → PairingHeap α → PairingHeap α`: add an element to the heap
> * `deleteMin : PairingHeap α → Option (α × PairingHeap α)`:
>   remove the minimum element from the heap
> * `merge : PairingHeap α → PairingHeap α → PairingHeap α`: combine two heaps
>
> The first two operations are known as a "priority queue", so this could be called
> a "mergeable priority queue". The standard choice for a priority queue is a binary heap,
> which supports `insert` and `deleteMin` in `O(log n)`, but `merge` is `O(n)`.
> With a `PairingHeap`, `insert` and `merge` are `O(1)`, `deleteMin` is amortized `O(log n)`.
>
> Note that `deleteMin` may be `O(n)` in a single operation. So if you need an efficient
> persistent priority queue, you should use other data structures with better worst-case time.

```lean
def PairingHeap (α : Type u) (le : α → α → Bool)
```

`Batteries.mkPairingHeap` (definition, [line 302](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L302))

> `O(1)`. Make a new empty pairing heap.

```lean
def mkPairingHeap (α : Type u) (le : α → α → Bool) : PairingHeap α le
```

`Batteries.PairingHeap.empty` (definition, [line 309](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L309))

> `O(1)`. Make a new empty pairing heap.

```lean
def empty : PairingHeap α le
```

`Batteries.PairingHeap.isEmpty` (definition, [line 314](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L314))

> `O(1)`. Is the heap empty?

```lean
def isEmpty (b : PairingHeap α le) : Bool
```

`Batteries.PairingHeap.size` (definition, [line 317](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L317))

> `O(n)`. The number of elements in the heap.

```lean
def size (b : PairingHeap α le) : Nat
```

`Batteries.PairingHeap.singleton` (definition, [line 320](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L320))

> `O(1)`. Make a new heap containing `a`.

```lean
def singleton (a : α) : PairingHeap α le
```

`Batteries.PairingHeap.merge` (definition, [line 324](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L324))

> `O(1)`. Merge the contents of two heaps.

```lean
def merge : PairingHeap α le → PairingHeap α le → PairingHeap α le
```

`Batteries.PairingHeap.insert` (definition, [line 328](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L328))

> `O(1)`. Add element `a` to the given heap `h`.

```lean
def insert (a : α) (h : PairingHeap α le) : PairingHeap α le
```

`Batteries.PairingHeap.ofList` (definition, [line 332](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L332))

> `O(n log n)`. Construct a heap from a list by inserting all the elements.

```lean
def ofList (le : α → α → Bool) (as : List α) : PairingHeap α le
```

`Batteries.PairingHeap.ofArray` (definition, [line 336](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L336))

> `O(n log n)`. Construct a heap from a list by inserting all the elements.

```lean
def ofArray (le : α → α → Bool) (as : Array α) : PairingHeap α le
```

`Batteries.PairingHeap.deleteMin` (definition, [line 340](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L340))

> Amortized `O(log n)`. Remove and return the minimum element from the heap.

```lean
def deleteMin (b : PairingHeap α le) : Option (α × PairingHeap α le)
```

`Batteries.PairingHeap.head?` (definition, [line 346](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L346))

> `O(1)`. Returns the smallest element in the heap, or `none` if the heap is empty.

```lean
def head? (b : PairingHeap α le) : Option α
```

`Batteries.PairingHeap.head!` (definition, [line 349](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L349))

> `O(1)`. Returns the smallest element in the heap, or panics if the heap is empty.

```lean
def head! [Inhabited α] (b : PairingHeap α le) : α
```

`Batteries.PairingHeap.headI` (definition, [line 352](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L352))

> `O(1)`. Returns the smallest element in the heap, or `default` if the heap is empty.

```lean
def headI [Inhabited α] (b : PairingHeap α le) : α
```

`Batteries.PairingHeap.tail?` (definition, [line 357](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L357))

> Amortized `O(log n)`. Removes the smallest element from the heap, or `none` if the heap is empty.

```lean
def tail? (b : PairingHeap α le) : Option (PairingHeap α le)
```

`Batteries.PairingHeap.tail` (definition, [line 363](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L363))

> Amortized `O(log n)`. Removes the smallest element from the heap, if possible.

```lean
def tail (b : PairingHeap α le) : PairingHeap α le
```

`Batteries.PairingHeap.toList` (definition, [line 366](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L366))

> `O(n log n)`. Convert the heap to a list in increasing order.

```lean
def toList (b : PairingHeap α le) : List α
```

`Batteries.PairingHeap.toArray` (definition, [line 369](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L369))

> `O(n log n)`. Convert the heap to an array in increasing order.

```lean
def toArray (b : PairingHeap α le) : Array α
```

`Batteries.PairingHeap.toListUnordered` (definition, [line 372](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L372))

> `O(n)`. Convert the heap to a list in arbitrary order.

```lean
def toListUnordered (b : PairingHeap α le) : List α
```

`Batteries.PairingHeap.toArrayUnordered` (definition, [line 375](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean#L375))

> `O(n)`. Convert the heap to an array in arbitrary order.

```lean
def toArrayUnordered (b : PairingHeap α le) : Array α
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [Order](../../classes/order.md)

## Sources

- [Batteries/Data/PairingHeap.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/PairingHeap.lean)
