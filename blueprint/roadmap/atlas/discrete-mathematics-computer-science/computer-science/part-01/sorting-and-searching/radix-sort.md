---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.radixSort, Cslib.Algorithms.Lean.TimeM.radixSort_correct, Cslib.Algorithms.Lean.TimeM.radixSort_time
statement: formalized
proof: formalized
---

# Radix sort

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/radix-sort/index.html).

## Radix sort

Let $b \ge 2$ and let every record carry a key that is a vector of $d$ digits
in $\{0, \dots, b-1\}$, most significant digit first, at positions $0, \dots, d-1$. Radix sort
runs $d$ passes of stable counting sort on the array, the pass for position $i$ sorting by the
digit of the key at position $i$, for $i = d-1, d-2, \dots, 0$, that is, from the least to the most
significant digit. Its cost is the total cost of the $d$ counting-sort passes.

Formalized by `Cslib.Algorithms.Lean.TimeM.radixSort`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/Radix.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Radix.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/radix-sort/index.html#radix-sort).

## Correctness of radix sort

Let $b \ge 2$ and let every record carry a key that is a vector
$(k_0, \dots, k_{d-1})$ of $d$ digits in $\{0, \dots, b-1\}$, most significant digit first. For
every input array, the output of radix sort is a permutation of the input, is in nondecreasing
lexicographic order of keys, and is in nondecreasing order of the numbers
$\sum_{i < d} k_i b^{d-1-i}$ whose base-$b$ digits are the keys. Moreover it is stable: for every
key vector $v$, the records with key $v$ appear in the output in the same order as in the input.

Formalized by `Cslib.Algorithms.Lean.TimeM.radixSort_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Radix.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Radix.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/radix-sort/index.html#radix-sort-correct).

## Cost bound for radix sort

Let $b \ge 2$ and let every record carry a key that is a vector
of $d$ digits in $\{0, \dots, b-1\}$. On an array of $n$ records, radix sort uses at most
$d(7n + 3b)$ charged operations, where each counting-sort pass charges one unit for every counter
initialization, key evaluation, counter read, counter write and output write.

Formalized by `Cslib.Algorithms.Lean.TimeM.radixSort_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Radix.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Radix.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/radix-sort/index.html#radix-sort-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Radix sort](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/radix-sort/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/radix-sort)
