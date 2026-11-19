---
catalog: module
lean: Batteries.BinomialHeap.Imp.Heap.findMin_val, Batteries.BinomialHeap.Imp.Heap.deleteMin_fst, Batteries.BinomialHeap.Imp.HeapNode.WF.realSize_eq, Batteries.BinomialHeap.Imp.Heap.WF.size_eq
statement: formalized
proof: formalized
---

# BinomialHeap/Lemmas

`Batteries.Data.BinomialHeap.Lemmas`, in [Batteries/Data/BinomialHeap/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinomialHeap/Lemmas.lean), by Mario Carneiro.

`Batteries.BinomialHeap.Imp.Heap.findMin_val` (theorem, [line 15](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinomialHeap/Lemmas.lean#L15))

```lean
theorem Heap.findMin_val : ((s : Heap α).findMin le k res).val = s.headD le res.val
```

`Batteries.BinomialHeap.Imp.Heap.deleteMin_fst` (theorem, [line 20](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinomialHeap/Lemmas.lean#L20))

```lean
theorem Heap.deleteMin_fst : ((s : Heap α).deleteMin le).map (·.1) = s.head? le
```

`Batteries.BinomialHeap.Imp.HeapNode.WF.realSize_eq` (theorem, [line 25](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinomialHeap/Lemmas.lean#L25))

```lean
theorem HeapNode.WF.realSize_eq :
    ∀ {n} {s : HeapNode α}, s.WF le a n → s.realSize + 1 = 2 ^ n
```

`Batteries.BinomialHeap.Imp.Heap.WF.size_eq` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinomialHeap/Lemmas.lean#L32))

```lean
theorem Heap.WF.size_eq :
    ∀ {s : Heap α}, s.WF le n → s.size = s.realSize
```

## Depends on

- [BinomialHeap/Basic](basic.md)

## Sources

- [Batteries/Data/BinomialHeap/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BinomialHeap/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.BinomialHeap.Lemmas.json)
