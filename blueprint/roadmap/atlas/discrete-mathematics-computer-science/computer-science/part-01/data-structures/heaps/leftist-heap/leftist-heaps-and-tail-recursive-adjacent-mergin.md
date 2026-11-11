---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.LHeap, Cslib.Algorithms.Lean.LHeap.size, Cslib.Algorithms.Lean.LHeap.rank, Cslib.Algorithms.Lean.LHeap.mset_tree, Cslib.Algorithms.Lean.LHeap.all_le, Cslib.Algorithms.Lean.LHeap.heap, Cslib.Algorithms.Lean.LHeap.ltree, Cslib.Algorithms.Lean.LHeap.make
statement: formalized
proof: formalized
---

# Leftist heaps and tail-recursive adjacent merging

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html).

## Leftist Heap datatype (concrete)

## Leftist heap

Leftist heap: Empty or Node rank value left right

Formalized by `Cslib.Algorithms.Lean.LHeap`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#lheap).

## Number of nodes of a leftist heap

Size (number of nodes)

Formalized by `Cslib.Algorithms.Lean.LHeap.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#size).

## Rank of a leftist heap

Rank (right spine length, or stored rank)

Formalized by `Cslib.Algorithms.Lean.LHeap.rank`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#rank).

## Multiset of elements of a leftist heap

Multiset of elements

Formalized by `Cslib.Algorithms.Lean.LHeap.mset_tree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#mset-tree).

## Lower bound on all elements of a heap

All elements in heap are ≥ x (for heap ordering)

Formalized by `Cslib.Algorithms.Lean.LHeap.all_le`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#all-le).

## Min-heap property

Min-heap property: root ≤ all in subtrees

Formalized by `Cslib.Algorithms.Lean.LHeap.heap`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#heap).

## Leftist invariant with correct stored ranks

Leftist invariant: stored rank is correct and left rank ≥ right rank
   For every node `N storedRank x l r`, require:
   - `storedRank = rank r + 1`;
   - `rank l ≥ rank r`;
   - `ltree l`;
   - `ltree r`.

Formalized by `Cslib.Algorithms.Lean.LHeap.ltree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#ltree).

## Node constructor restoring the leftist property

Helper to restore leftist property.
   Constructs a node whose stored rank is exactly one plus the rank
   of its resulting right subtree (b.rank + 1 or a.rank + 1 after swap).

Formalized by `Cslib.Algorithms.Lean.LHeap.make`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#make).

## Fuel-based auxiliary merge of leftist heaps

Auxiliary fuel-based merge to avoid termination proof complexity.
   When reconstructing an existing node during recursion, preserves its
   original stored rank (does not replace it with 0).

Formalized by `Cslib.Algorithms.Lean.LHeap.mergeAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#merge-aux).

## Merge of leftist heaps

Leftist merge (public API)

Formalized by `Cslib.Algorithms.Lean.LHeap.merge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#merge).

## Fuel-based auxiliary cost of merging

Auxiliary fuel-based cost of merge.
   Complexity model faithful to textbook convention: only calls/steps of `merge`
   are counted. Reversal of accumulator in `merge_adj2` and other auxiliary
   operations are not counted.

Formalized by `Cslib.Algorithms.Lean.LHeap.T_mergeAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#t-merge-aux).

## Cost of merging leftist heaps

Cost of merge: number of merge steps (only merge calls counted)

Formalized by `Cslib.Algorithms.Lean.LHeap.T_merge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#t-merge).

## Non-tail-recursive adjacent merging of heaps

Non-tail-recursive merge_adj

Formalized by `Cslib.Algorithms.Lean.LHeap.merge_adj`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#merge-adj).

## Tail-recursive adjacent merging with an accumulator

Tail-recursive merge_adj2 with accumulator, no use of List.append.
   Genuinely tail-recursive: uses an accumulator and reverse at base case.
   Does not use List.append (avoids append operator).
   Complexity model: only merge steps counted, so `T_merge_adj2 acc ts = T_merge_adj ts`
   should hold; accumulator reversal overhead is intentionally excluded
   per textbook convention that only merge calls are counted.

Formalized by `Cslib.Algorithms.Lean.LHeap.merge_adj2`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#merge-adj2).

## Cost of non-tail-recursive adjacent merging

Cost of merge_adj: only merge steps counted per textbook

Formalized by `Cslib.Algorithms.Lean.LHeap.T_merge_adj`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#t-merge-adj).

## Cost of tail-recursive adjacent merging

Cost of merge_adj2 (accumulator version): only merge steps counted.
   Follows textbook convention that only calls/steps of `merge` are counted,
   so accumulator handling does not contribute to cost. Hence the required
   comparison `T_merge_adj2 acc ts = T_merge_adj ts` remains valid.

Formalized by `Cslib.Algorithms.Lean.LHeap.T_merge_adj2`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#t-merge-adj2).

## Fuel-based merging of all heaps with tail-recursive passes

merge_all2 uses merge_adj2 (tail-recursive variant)

Formalized by `Cslib.Algorithms.Lean.LHeap.merge_all2Aux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#merge-all2-aux).

## Singleton leftist heap

Singleton heap: stored rank 1 = rank E + 1, leftist

Formalized by `Cslib.Algorithms.Lean.LHeap.singleton`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#singleton).

## Leftist heap from a list by tail-recursive merging

lheap_list2: convert list to leftist heap via merge_all2 (tail-recursive adj).
   Uses merge_all2 which itself uses merge_adj2.

Formalized by `Cslib.Algorithms.Lean.LHeap.lheap_list2`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#lheap-list2).

## Combined multiset of a list of heaps

Combined multiset of every heap in a list, including duplicates.

Formalized by `Cslib.Algorithms.Lean.LHeap.sumMSet`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#sum-mset).

## Min-heap ordering of every heap in a list

Every heap in the list satisfies the min-heap ordering predicate.

Formalized by `Cslib.Algorithms.Lean.LHeap.HeapList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#heap-list).

## Leftist invariant for every heap in a list

Every heap in the list has correct stored ranks and is leftist.

Formalized by `Cslib.Algorithms.Lean.LHeap.LTreeList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#ltree-list).

## Correctness and cost equivalence of tail-recursive heap construction

Graded theorem: correctness of lheap_list2 and complexity equivalence.
   Complexity model faithful to textbook: only merge calls counted.

Formalized by `Cslib.Algorithms.Lean.fdsa_chap15_ex04`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 1027](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L1027). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#fdsa-chap15-ex04).

## List-to-heap construction preserves the multiset

List construction preserves the entire input multiset, including duplicates.

Formalized by `Cslib.Algorithms.Lean.LHeap.mset_lheap_list2`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 1054](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L1054). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#mset-lheap-list2).

## List-to-heap construction gives a min-heap

List construction satisfies min-heap ordering.

Formalized by `Cslib.Algorithms.Lean.LHeap.heap_lheap_list2`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 1059](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L1059). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#heap-lheap-list2).

## List-to-heap construction gives a leftist tree

List construction satisfies both stored-rank correctness and leftist balance.

Formalized by `Cslib.Algorithms.Lean.LHeap.ltree_lheap_list2`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 1063](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L1063). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#ltree-lheap-list2).

## Per-input correctness of list-to-heap construction

A reusable per-input form of the three construction-correctness conjuncts.

Formalized by `Cslib.Algorithms.Lean.LHeap.lheap_list2_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 1067](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L1067). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#lheap-list2-correct).

## Accumulator characterization of tail-recursive adjacent merging

The accumulator is a reversed prefix; newly merged pairs follow it in
input order. This additional output characterization is not required by the
original exercise. Append appears only in the specification, not the algorithm.

Formalized by `Cslib.Algorithms.Lean.LHeap.merge_adj2_eq_reverse_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean, line 1075](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LeftistHeap.lean#L1075). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html#merge-adj2-eq-reverse-append).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Leftist heaps and tail-recursive adjacent merging](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/heaps/leftist-heap/leftist-heaps-and-tail-recursive-adjacent-mergin)
