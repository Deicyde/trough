---
catalog: module
lean: Batteries.BinomialHeap.Imp.HeapNode, Batteries.BinomialHeap.Imp.HeapNode.realSize, Batteries.BinomialHeap.Imp.HeapNode.singleton, Batteries.BinomialHeap.Imp.HeapNode.rank, Batteries.BinomialHeap.Imp.HeapNode.rankTR, Batteries.BinomialHeap.Imp.HeapNode.rankTR_eq, Batteries.BinomialHeap.Imp.Heap, Batteries.BinomialHeap.Imp.Heap.realSize, Batteries.BinomialHeap.Imp.Heap.size, Batteries.BinomialHeap.Imp.Heap.isEmpty, Batteries.BinomialHeap.Imp.Heap.singleton, Batteries.BinomialHeap.Imp.Heap.rankGT, Batteries.BinomialHeap.Imp.Heap.length, Batteries.BinomialHeap.Imp.combine, Batteries.BinomialHeap.Imp.Heap.merge, Batteries.BinomialHeap.Imp.HeapNode.toHeap, Batteries.BinomialHeap.Imp.Heap.headD, Batteries.BinomialHeap.Imp.Heap.head?, Batteries.BinomialHeap.Imp.FindMin, Batteries.BinomialHeap.Imp.Heap.findMin, Batteries.BinomialHeap.Imp.Heap.deleteMin, Batteries.BinomialHeap.Imp.Heap.tail?, Batteries.BinomialHeap.Imp.Heap.tail, Batteries.BinomialHeap.Imp.Heap.realSize_merge, Batteries.BinomialHeap.Imp.HeapNode.realSize_toHeap, Batteries.BinomialHeap.Imp.Heap.realSize_deleteMin, Batteries.BinomialHeap.Imp.Heap.realSize_tail?, Batteries.BinomialHeap.Imp.Heap.realSize_tail, Batteries.BinomialHeap.Imp.Heap.foldM, Batteries.BinomialHeap.Imp.Heap.fold, Batteries.BinomialHeap.Imp.Heap.toArray, Batteries.BinomialHeap.Imp.Heap.toList, Batteries.BinomialHeap.Imp.HeapNode.foldTreeM, Batteries.BinomialHeap.Imp.Heap.foldTreeM, Batteries.BinomialHeap.Imp.Heap.foldTree, Batteries.BinomialHeap.Imp.Heap.toListUnordered, Batteries.BinomialHeap.Imp.Heap.toArrayUnordered, Batteries.BinomialHeap.Imp.HeapNode.WF, Batteries.BinomialHeap.Imp.Heap.WF, Batteries.BinomialHeap.Imp.Heap.WF.nil, Batteries.BinomialHeap.Imp.Heap.WF.singleton, Batteries.BinomialHeap.Imp.Heap.WF.of_rankGT, Batteries.BinomialHeap.Imp.Heap.WF.of_le, Batteries.BinomialHeap.Imp.Heap.rankGT.of_le, Batteries.BinomialHeap.Imp.Heap.WF.rankGT, Batteries.BinomialHeap.Imp.Heap.WF.merge', Batteries.BinomialHeap.Imp.Heap.WF.merge, Batteries.BinomialHeap.Imp.HeapNode.WF.rank_eq, Batteries.BinomialHeap.Imp.HeapNode.WF.toHeap, Batteries.BinomialHeap.Imp.FindMin.WF, Batteries.BinomialHeap.Imp.Heap.WF.findMin, Batteries.BinomialHeap.Imp.Heap.WF.deleteMin, Batteries.BinomialHeap.Imp.Heap.WF.tail?, Batteries.BinomialHeap.Imp.Heap.WF.tail, Batteries.BinomialHeap, Batteries.mkBinomialHeap, Batteries.BinomialHeap.empty, Batteries.BinomialHeap.isEmpty, Batteries.BinomialHeap.size, Batteries.BinomialHeap.singleton, Batteries.BinomialHeap.merge, Batteries.BinomialHeap.insert, Batteries.BinomialHeap.ofList, Batteries.BinomialHeap.ofArray, Batteries.BinomialHeap.deleteMin, Batteries.BinomialHeap.forIn, Batteries.BinomialHeap.head?, Batteries.BinomialHeap.head!, Batteries.BinomialHeap.headI, Batteries.BinomialHeap.tail?, Batteries.BinomialHeap.tail, Batteries.BinomialHeap.foldM, Batteries.BinomialHeap.fold, Batteries.BinomialHeap.toList, Batteries.BinomialHeap.toArray, Batteries.BinomialHeap.toListUnordered, Batteries.BinomialHeap.toArrayUnordered
statement: formalized
proof: formalized
---

# BinomialHeap/Basic

`Batteries.Data.BinomialHeap.Basic`, in [Batteries/Data/BinomialHeap/Basic.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean), by Leonardo de Moura, Jannis Limperg, Mario Carneiro.

`Batteries.BinomialHeap.Imp.HeapNode` (inductive type, [line 28](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L28))

> A `HeapNode` is one of the internal nodes of the binomial heap.
> It is always a perfect binary tree, with the depth of the tree stored in the `Heap`.
> However the interpretation of the two pointers is different: we view the `child`
> as going to the first child of this node, and `sibling` goes to the next sibling
> of this tree. So it actually encodes a forest where each node has children
> `node.child`, `node.child.sibling`, `node.child.sibling.sibling`, etc.
>
> Each edge in this forest denotes a `le a b` relation that has been checked, so
> the root is smaller than everything else under it.

```lean
inductive HeapNode (α : Type u) where
  /-- An empty forest, which has depth `0`. -/
  | nil : HeapNode α
  /-- A forest of rank `r + 1` consists of a root `a`,
  a forest `child` of rank `r` elements greater than `a`,
  and another forest `sibling` of rank `r`. -/
  | node (a : α) (child sibling : HeapNode α) : HeapNode α
  deriving Repr
```

`Batteries.BinomialHeap.Imp.HeapNode.realSize` (definition, [line 42](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L42))

> The "real size" of the node, counting up how many values of type `α` are stored.
> This is `O(n)` and is intended mainly for specification purposes.
> For a well formed `HeapNode` the size is always `2^n - 1` where `n` is the depth.

```lean
def HeapNode.realSize : HeapNode α → Nat
```

`Batteries.BinomialHeap.Imp.HeapNode.singleton` (definition, [line 47](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L47))

> A node containing a single element `a`.

```lean
def HeapNode.singleton (a : α) : HeapNode α
```

`Batteries.BinomialHeap.Imp.HeapNode.rank` (definition, [line 53](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L53))

> `O(log n)`. The rank, or the number of trees in the forest.
> It is also the depth of the forest.

```lean
def HeapNode.rank : HeapNode α → Nat
```

`Batteries.BinomialHeap.Imp.HeapNode.rankTR` (definition, [line 58](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L58))

> Tail-recursive version of `HeapNode.rank`.

```lean
def HeapNode.rankTR (s : HeapNode α) : Nat
```

`Batteries.BinomialHeap.Imp.HeapNode.rankTR_eq` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L64))

```lean
theorem HeapNode.rankTR_eq : @rankTR = @rank
```

`Batteries.BinomialHeap.Imp.Heap` (inductive type, [line 75](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L75))

> A `Heap` is the top level structure in a binomial heap.
> It consists of a forest of `HeapNode`s with strictly increasing ranks.

```lean
inductive Heap (α : Type u) where
  /-- An empty heap. -/
  | nil : Heap α
  /-- A cons node contains a tree of root `val`, children `node` and rank `rank`,
  and then `next` which is the rest of the forest. -/
  | cons (rank : Nat) (val : α) (node : HeapNode α) (next : Heap α) : Heap α
  deriving Repr
```

`Batteries.BinomialHeap.Imp.Heap.realSize` (definition, [line 88](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L88))

> `O(n)`. The "real size" of the heap, counting up how many values of type `α` are stored.
> This is intended mainly for specification purposes.
> Prefer `Heap.size`, which is the same for well formed heaps.

```lean
def Heap.realSize : Heap α → Nat
```

`Batteries.BinomialHeap.Imp.Heap.size` (definition, [line 93](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L93))

> `O(log n)`. The number of elements in the heap.

```lean
def Heap.size : Heap α → Nat
```

`Batteries.BinomialHeap.Imp.Heap.isEmpty` (definition, [line 98](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L98))

> `O(1)`. Is the heap empty?

```lean
def Heap.isEmpty : Heap α → Bool
```

`Batteries.BinomialHeap.Imp.Heap.singleton` (definition, [line 103](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L103))

> `O(1)`. The heap containing a single value `a`.

```lean
def Heap.singleton (a : α) : Heap α
```

`Batteries.BinomialHeap.Imp.Heap.rankGT` (definition, [line 106](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L106))

> `O(1)`. Auxiliary for `Heap.merge`: Is the minimum rank in `Heap` strictly larger than `n`?

```lean
def Heap.rankGT : Heap α → Nat → Prop
```

`Batteries.BinomialHeap.Imp.Heap.length` (definition, [line 116](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L116))

> `O(log n)`. The number of trees in the forest.

```lean
def Heap.length : Heap α → Nat
```

`Batteries.BinomialHeap.Imp.combine` (definition, [line 124](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L124))

> `O(1)`. Auxiliary for `Heap.merge`: combines two heap nodes of the same rank
> into one with the next larger rank.

```lean
def combine (le : α → α → Bool) (a₁ a₂ : α) (n₁ n₂ : HeapNode α) : α × HeapNode α
```

`Batteries.BinomialHeap.Imp.Heap.merge` (definition, [line 131](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L131))

> Merge two forests of binomial trees. The forests are assumed to be ordered
> by rank and `merge` maintains this invariant.

```lean
def Heap.merge (le : α → α → Bool) : Heap α → Heap α → Heap α
```

`Batteries.BinomialHeap.Imp.HeapNode.toHeap` (definition, [line 152](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L152))

> `O(log n)`. Convert a `HeapNode` to a `Heap` by reversing the order of the nodes
> along the `sibling` spine.

```lean
def HeapNode.toHeap (s : HeapNode α) : Heap α
```

`Batteries.BinomialHeap.Imp.Heap.headD` (definition, [line 159](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L159))

> `O(log n)`. Get the smallest element in the heap, including the passed in value `a`.

```lean
def Heap.headD (le : α → α → Bool) (a : α) : Heap α → α
```

`Batteries.BinomialHeap.Imp.Heap.head?` (definition, [line 164](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L164))

> `O(log n)`. Get the smallest element in the heap, if it has an element.

```lean
def Heap.head? (le : α → α → Bool) : Heap α → Option α
```

`Batteries.BinomialHeap.Imp.FindMin` (structure, [line 172](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L172))

> The return type of `FindMin`, which encodes various quantities needed to
> reconstruct the tree in `deleteMin`.

```lean
structure FindMin (α) where
  /-- The list of elements prior to the minimum element, encoded as a "difference list". -/
  before : Heap α → Heap α := id
  /-- The minimum element. -/
  val : α
  /-- The children of the minimum element. -/
  node : HeapNode α
  /-- The forest after the minimum element. -/
  next : Heap α
```

`Batteries.BinomialHeap.Imp.Heap.findMin` (definition, [line 186](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L186))

> `O(log n)`. Find the minimum element, and return a data structure `FindMin` with information
> needed to reconstruct the rest of the binomial heap.

```lean
def Heap.findMin (le : α → α → Bool) (k : Heap α → Heap α) :
    Heap α → FindMin α → FindMin α
```

`Batteries.BinomialHeap.Imp.Heap.deleteMin` (definition, [line 196](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L196))

> `O(log n)`. Find and remove the the minimum element from the binomial heap.

```lean
def Heap.deleteMin (le : α → α → Bool) : Heap α → Option (α × Heap α)
```

`Batteries.BinomialHeap.Imp.Heap.tail?` (definition, [line 203](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L203))

> `O(log n)`. Get the tail of the binomial heap after removing the minimum element.

```lean
def Heap.tail? (le : α → α → Bool) (h : Heap α) : Option (Heap α)
```

`Batteries.BinomialHeap.Imp.Heap.tail` (definition, [line 207](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L207))

> `O(log n)`. Remove the minimum element of the heap.

```lean
def Heap.tail (le : α → α → Bool) (h : Heap α) : Heap α
```

`Batteries.BinomialHeap.Imp.Heap.realSize_merge` (theorem, [line 209](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L209))

```lean
theorem Heap.realSize_merge (le) (s₁ s₂ : Heap α) :
    (s₁.merge le s₂).realSize = s₁.realSize + s₂.realSize
```

`Batteries.BinomialHeap.Imp.HeapNode.realSize_toHeap` (theorem, [line 246](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L246))

```lean
theorem HeapNode.realSize_toHeap (s : HeapNode α) : s.toHeap.realSize = s.realSize
```

`Batteries.BinomialHeap.Imp.Heap.realSize_deleteMin` (theorem, [line 251](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L251))

```lean
theorem Heap.realSize_deleteMin {s : Heap α} (eq : s.deleteMin le = some (a, s')) :
    s.realSize = s'.realSize + 1
```

`Batteries.BinomialHeap.Imp.Heap.realSize_tail?` (theorem, [line 263](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L263))

```lean
theorem Heap.realSize_tail? {s : Heap α} : s.tail? le = some s' →
    s.realSize = s'.realSize + 1
```

`Batteries.BinomialHeap.Imp.Heap.realSize_tail` (theorem, [line 269](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L269))

```lean
theorem Heap.realSize_tail (le) (s : Heap α) : (s.tail le).realSize = s.realSize - 1
```

`Batteries.BinomialHeap.Imp.Heap.foldM` (definition, [line 279](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L279))

> `O(n log n)`. Monadic fold over the elements of a heap in increasing order,
> by repeatedly pulling the minimum element out of the heap.

```lean
def Heap.foldM [Monad m] (le : α → α → Bool) (s : Heap α)
    (init : β) (f : β → α → m β) : m β
```

`Batteries.BinomialHeap.Imp.Heap.fold` (definition, [line 292](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L292))

> `O(n log n)`. Fold over the elements of a heap in increasing order,
> by repeatedly pulling the minimum element out of the heap.

```lean
def Heap.fold (le : α → α → Bool) (s : Heap α) (init : β) (f : β → α → β) : β
```

`Batteries.BinomialHeap.Imp.Heap.toArray` (definition, [line 296](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L296))

> `O(n log n)`. Convert the heap to an array in increasing order.

```lean
def Heap.toArray (le : α → α → Bool) (s : Heap α) : Array α
```

`Batteries.BinomialHeap.Imp.Heap.toList` (definition, [line 299](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L299))

> `O(n log n)`. Convert the heap to a list in increasing order.

```lean
def Heap.toList (le : α → α → Bool) (s : Heap α) : List α
```

`Batteries.BinomialHeap.Imp.HeapNode.foldTreeM` (definition, [line 305](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L305))

> `O(n)`. Fold a monadic function over the tree structure to accumulate a value.

```lean
def HeapNode.foldTreeM : HeapNode α → m β
```

`Batteries.BinomialHeap.Imp.Heap.foldTreeM` (definition, [line 310](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L310))

> `O(n)`. Fold a monadic function over the tree structure to accumulate a value.

```lean
def Heap.foldTreeM : Heap α → m β
```

`Batteries.BinomialHeap.Imp.Heap.foldTree` (definition, [line 317](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L317))

> `O(n)`. Fold a function over the tree structure to accumulate a value.

```lean
def Heap.foldTree (nil : β) (join : α → β → β → β) (s : Heap α) : β
```

`Batteries.BinomialHeap.Imp.Heap.toListUnordered` (definition, [line 321](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L321))

> `O(n)`. Convert the heap to a list in arbitrary order.

```lean
def Heap.toListUnordered (s : Heap α) : List α
```

`Batteries.BinomialHeap.Imp.Heap.toArrayUnordered` (definition, [line 325](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L325))

> `O(n)`. Convert the heap to an array in arbitrary order.

```lean
def Heap.toArrayUnordered (s : Heap α) : Array α
```

`Batteries.BinomialHeap.Imp.HeapNode.WF` (definition, [line 336](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L336))

> The well formedness predicate for a heap node.
> It asserts that:
> * If `a` is added at the top to make the forest into a tree, the resulting tree
>   is a `le`-min-heap (if `le` is well-behaved)
> * When interpreting `child` and `sibling` as left and right children of a binary tree,
>   it is a perfect binary tree with depth `r`

```lean
def HeapNode.WF (le : α → α → Bool) (a : α) : HeapNode α → Nat → Prop
```

`Batteries.BinomialHeap.Imp.Heap.WF` (definition, [line 346](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L346))

> The well formedness predicate for a binomial heap.
> It asserts that:
> * It consists of a list of well formed trees with the specified ranks
> * The ranks are in strictly increasing order, and all are at least `n`

```lean
def Heap.WF (le : α → α → Bool) (n : Nat) : Heap α → Prop
```

`Batteries.BinomialHeap.Imp.Heap.WF.nil` (theorem, [line 350](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L350))

```lean
theorem Heap.WF.nil : Heap.nil.WF le n
```

`Batteries.BinomialHeap.Imp.Heap.WF.singleton` (theorem, [line 352](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L352))

```lean
theorem Heap.WF.singleton : (Heap.singleton a).WF le 0
```

`Batteries.BinomialHeap.Imp.Heap.WF.of_rankGT` (theorem, [line 354](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L354))

```lean
theorem Heap.WF.of_rankGT (hlt : s.rankGT n) (h : Heap.WF le n' s) : s.WF le (n+1)
```

`Batteries.BinomialHeap.Imp.Heap.WF.of_le` (theorem, [line 359](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L359))

```lean
theorem Heap.WF.of_le (hle : n ≤ n') (h : Heap.WF le n' s) : s.WF le n
```

`Batteries.BinomialHeap.Imp.Heap.rankGT.of_le` (theorem, [line 364](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L364))

```lean
theorem Heap.rankGT.of_le (h : Heap.rankGT s n) (h' : n' ≤ n) : s.rankGT n'
```

`Batteries.BinomialHeap.Imp.Heap.WF.rankGT` (theorem, [line 369](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L369))

```lean
theorem Heap.WF.rankGT (h : Heap.WF lt (n+1) s) : s.rankGT n
```

`Batteries.BinomialHeap.Imp.Heap.WF.merge'` (theorem, [line 374](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L374))

```lean
theorem Heap.WF.merge' (h₁ : s₁.WF le n) (h₂ : s₂.WF le n) :
    (merge le s₁ s₂).WF le n ∧ ((s₁.rankGT n ↔ s₂.rankGT n) → (merge le s₁ s₂).rankGT n)
```

`Batteries.BinomialHeap.Imp.Heap.WF.merge` (theorem, [line 410](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L410))

```lean
theorem Heap.WF.merge (h₁ : s₁.WF le n) (h₂ : s₂.WF le n) : (merge le s₁ s₂).WF le n
```

`Batteries.BinomialHeap.Imp.HeapNode.WF.rank_eq` (theorem, [line 413](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L413))

```lean
theorem HeapNode.WF.rank_eq : ∀ {n} {s : HeapNode α}, s.WF le a n → s.rank = n
```

`Batteries.BinomialHeap.Imp.HeapNode.WF.toHeap` (theorem, [line 417](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L417))

```lean
theorem HeapNode.WF.toHeap {s : HeapNode α} (h : s.WF le a n) : s.toHeap.WF le 0
```

`Batteries.BinomialHeap.Imp.FindMin.WF` (structure, [line 430](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L430))

> The well formedness predicate for a `FindMin` value.
> This is not actually a predicate, as it contains an additional data value
> `rank` corresponding to the rank of the returned node, which is omitted from `findMin`.

```lean
structure FindMin.WF (le : α → α → Bool) (res : FindMin α) where
  /-- The rank of the minimum element -/
  rank : Nat
  /-- `before` is a difference list which can be appended to a binomial heap
  with ranks at least `rank` to produce another well formed heap. -/
  before : ∀ {s}, s.WF le rank → (res.before s).WF le 0
  /-- `node` is a well formed forest of rank `rank` with `val` at the root. -/
  node : res.node.WF le res.val rank
  /-- `next` is a binomial heap with ranks above `rank + 1`. -/
  next : res.next.WF le (rank + 1)
```

`Batteries.BinomialHeap.Imp.Heap.WF.findMin` (definition, [line 442](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L442))

> The conditions under which `findMin` is well-formed.

```lean
def Heap.WF.findMin {s : Heap α} (h : s.WF le n) (hr : res.WF le)
    (hk : ∀ {s}, s.WF le n → (k s).WF le 0) : ((s : Heap α).findMin le k res).WF le
```

`Batteries.BinomialHeap.Imp.Heap.WF.deleteMin` (theorem, [line 453](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L453))

```lean
theorem Heap.WF.deleteMin {s : Heap α}
    (h : s.WF le n) (eq : s.deleteMin le = some (a, s')) : s'.WF le 0
```

`Batteries.BinomialHeap.Imp.Heap.WF.tail?` (theorem, [line 465](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L465))

```lean
theorem Heap.WF.tail? (hwf : (s : Heap α).WF le n) : s.tail? le = some tl → tl.WF le 0
```

`Batteries.BinomialHeap.Imp.Heap.WF.tail` (theorem, [line 470](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L470))

```lean
theorem Heap.WF.tail (hwf : (s : Heap α).WF le n) : (s.tail le).WF le 0
```

`Batteries.BinomialHeap` (definition, [line 495](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L495))

> A [binomial heap](https://en.wikipedia.org/wiki/Binomial_heap) is a data structure which supports
> the following primary operations:
>
> * `insert : α → BinomialHeap α → BinomialHeap α`: add an element to the heap
> * `deleteMin : BinomialHeap α → Option (α × BinomialHeap α)`:
>   remove the minimum element from the heap
> * `merge : BinomialHeap α → BinomialHeap α → BinomialHeap α`: combine two heaps
>
> The first two operations are known as a "priority queue", so this could be called
> a "mergeable priority queue". The standard choice for a priority queue is a binary heap,
> which supports `insert` and `deleteMin` in `O(log n)`, but `merge` is `O(n)`.
> With a `BinomialHeap`, all three operations are `O(log n)`.

```lean
def BinomialHeap (α : Type u) (le : α → α → Bool)
```

`Batteries.mkBinomialHeap` (definition, [line 499](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L499))

> `O(1)`. Make a new empty binomial heap.

```lean
def mkBinomialHeap (α : Type u) (le : α → α → Bool) : BinomialHeap α le
```

`Batteries.BinomialHeap.empty` (definition, [line 506](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L506))

> `O(1)`. Make a new empty binomial heap.

```lean
def empty : BinomialHeap α le
```

`Batteries.BinomialHeap.isEmpty` (definition, [line 512](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L512))

> `O(1)`. Is the heap empty?

```lean
def isEmpty (b : BinomialHeap α le) : Bool
```

`Batteries.BinomialHeap.size` (definition, [line 515](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L515))

> `O(log n)`. The number of elements in the heap.

```lean
def size (b : BinomialHeap α le) : Nat
```

`Batteries.BinomialHeap.singleton` (definition, [line 518](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L518))

> `O(1)`. Make a new heap containing `a`.

```lean
def singleton (a : α) : BinomialHeap α le
```

`Batteries.BinomialHeap.merge` (definition, [line 521](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L521))

> `O(log n)`. Merge the contents of two heaps.

```lean
def merge : BinomialHeap α le → BinomialHeap α le → BinomialHeap α le
```

`Batteries.BinomialHeap.insert` (definition, [line 525](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L525))

> `O(log n)`. Add element `a` to the given heap `h`.

```lean
def insert (a : α) (h : BinomialHeap α le) : BinomialHeap α le
```

`Batteries.BinomialHeap.ofList` (definition, [line 528](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L528))

> `O(n log n)`. Construct a heap from a list by inserting all the elements.

```lean
def ofList (le : α → α → Bool) (as : List α) : BinomialHeap α le
```

`Batteries.BinomialHeap.ofArray` (definition, [line 531](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L531))

> `O(n log n)`. Construct a heap from a list by inserting all the elements.

```lean
def ofArray (le : α → α → Bool) (as : Array α) : BinomialHeap α le
```

`Batteries.BinomialHeap.deleteMin` (definition, [line 534](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L534))

> `O(log n)`. Remove and return the minimum element from the heap.

```lean
def deleteMin (b : BinomialHeap α le) : Option (α × BinomialHeap α le)
```

`Batteries.BinomialHeap.forIn` (definition, [line 545](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L545))

> `O(n log n)`. Implementation of `for x in (b : BinomialHeap α le) ...` notation,
> which iterates over the elements in the heap in increasing order.

```lean
protected def forIn [Monad m] (b : BinomialHeap α le) (x : β) (f : α → β → m (ForInStep β)) : m β
```

`Batteries.BinomialHeap.head?` (definition, [line 551](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L551))

> `O(log n)`. Returns the smallest element in the heap, or `none` if the heap is empty.

```lean
def head? (b : BinomialHeap α le) : Option α
```

`Batteries.BinomialHeap.head!` (definition, [line 554](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L554))

> `O(log n)`. Returns the smallest element in the heap, or panics if the heap is empty.

```lean
def head! [Inhabited α] (b : BinomialHeap α le) : α
```

`Batteries.BinomialHeap.headI` (definition, [line 557](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L557))

> `O(log n)`. Returns the smallest element in the heap, or `default` if the heap is empty.

```lean
def headI [Inhabited α] (b : BinomialHeap α le) : α
```

`Batteries.BinomialHeap.tail?` (definition, [line 560](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L560))

> `O(log n)`. Removes the smallest element from the heap, or `none` if the heap is empty.

```lean
def tail? (b : BinomialHeap α le) : Option (BinomialHeap α le)
```

`Batteries.BinomialHeap.tail` (definition, [line 566](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L566))

> `O(log n)`. Removes the smallest element from the heap, if possible.

```lean
def tail (b : BinomialHeap α le) : BinomialHeap α le
```

`Batteries.BinomialHeap.foldM` (definition, [line 572](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L572))

> `O(n log n)`. Monadic fold over the elements of a heap in increasing order,
> by repeatedly pulling the minimum element out of the heap.

```lean
def foldM [Monad m] (b : BinomialHeap α le) (init : β) (f : β → α → m β) : m β
```

`Batteries.BinomialHeap.fold` (definition, [line 579](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L579))

> `O(n log n)`. Fold over the elements of a heap in increasing order,
> by repeatedly pulling the minimum element out of the heap.

```lean
def fold (b : BinomialHeap α le) (init : β) (f : β → α → β) : β
```

`Batteries.BinomialHeap.toList` (definition, [line 582](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L582))

> `O(n log n)`. Convert the heap to a list in increasing order.

```lean
def toList (b : BinomialHeap α le) : List α
```

`Batteries.BinomialHeap.toArray` (definition, [line 585](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L585))

> `O(n log n)`. Convert the heap to an array in increasing order.

```lean
def toArray (b : BinomialHeap α le) : Array α
```

`Batteries.BinomialHeap.toListUnordered` (definition, [line 588](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L588))

> `O(n)`. Convert the heap to a list in arbitrary order.

```lean
def toListUnordered (b : BinomialHeap α le) : List α
```

`Batteries.BinomialHeap.toArrayUnordered` (definition, [line 591](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean#L591))

> `O(n)`. Convert the heap to an array in arbitrary order.

```lean
def toArrayUnordered (b : BinomialHeap α le) : Array α
```

## Depends on

- [Additional definitions on `ForInStep`](../../../control/forinstep/basic.md)

## Proof depends on

- [Order](../../../classes/order.md)

## Sources

- [Batteries/Data/BinomialHeap/Basic.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinomialHeap/Basic.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.BinomialHeap.Basic.json)
