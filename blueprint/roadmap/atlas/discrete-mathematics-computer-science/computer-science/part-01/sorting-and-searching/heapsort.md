---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.heapSort, Cslib.Algorithms.Lean.heapSort_multiset, Cslib.Algorithms.Lean.heapSort_perm, Cslib.Algorithms.Lean.heapSort_sorted, Cslib.Algorithms.Lean.heapSort_correct
statement: formalized
proof: formalized
---

# Heapsort

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/heapsort/index.html).

## Heap sort

For a list $xs$ of elements of a linearly ordered type, heap sort inserts the
entries of $xs$ one at a time, from first to last, into the empty binary min-heap, and then
extracts the minimum of the heap as many times as the heap has entries, each time continuing with
the remaining heap. The output is the list of the extracted minima in the order in which they
were extracted.

Formalized by `Cslib.Algorithms.Lean.heapSort`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/Heap.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Sort/Heap.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/heapsort/index.html#heap-sort).

## Heap sort preserves multiplicities

For every list $xs$ of elements of a linearly ordered
type, the output of heap sort on $xs$ and $xs$ itself are equal as multisets: every value occurs
in both lists the same number of times.

Formalized by `Cslib.Algorithms.Lean.heapSort_multiset`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Heap.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Sort/Heap.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/heapsort/index.html#heap-sort-multiset).

## Heap sort permutes its input

For every list $xs$ of elements of a linearly ordered type,
heap sort returns a permutation of $xs$.

Formalized by `Cslib.Algorithms.Lean.heapSort_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Heap.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Sort/Heap.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/heapsort/index.html#heap-sort-perm).

## Heap sort output is sorted

For every list $xs$ of elements of a linearly ordered type,
heap sort returns a list sorted in nondecreasing order.

Formalized by `Cslib.Algorithms.Lean.heapSort_sorted`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Heap.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Sort/Heap.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/heapsort/index.html#heap-sort-sorted).

## Correctness of heap sort

For every list $xs$ of elements of a linearly ordered type, heap
sort returns a list that is sorted in nondecreasing order and is a permutation of $xs$.

Formalized by `Cslib.Algorithms.Lean.heapSort_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Heap.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Sort/Heap.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/heapsort/index.html#heap-sort-correct).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Heapsort](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/heapsort/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/heapsort)
