---
catalog: module
lean: Batteries.BinaryHeap.WF.Children, Batteries.BinaryHeap.WF.TopDown, Batteries.BinaryHeap.WF
statement: formalized
proof: formalized
---

# WF

`Batteries.Data.BinaryHeap.WF`, in [Batteries/Data/BinaryHeap/WF.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinaryHeap/WF.lean), by Chad Sharp.

`Batteries.BinaryHeap.WF.Children` (definition, [line 18](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinaryHeap/WF.lean#L18))

> The primary local correctness property for the heap. A node should be >= both its children
> (if it has them).

```lean
def WF.Children [Ord α] (a : Vector α sz) (i : Fin sz) : Prop
```

`Batteries.BinaryHeap.WF.TopDown` (definition, [line 26](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinaryHeap/WF.lean#L26))

> The vector underlying a `BinaryHeap` is well-formed iff every node is ≥ any children it has

```lean
def WF.TopDown [Ord α] (v : Vector α sz) : Prop
```

`Batteries.BinaryHeap.WF` (definition, [line 31](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinaryHeap/WF.lean#L31))

> The well-formedness property of a binary heap

```lean
def WF [Ord α] (heap : BinaryHeap α) : Prop
```

## Depends on

- [BinaryHeap/Basic](basic.md)

## Sources

- [Batteries/Data/BinaryHeap/WF.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/BinaryHeap/WF.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.BinaryHeap.WF.json)
