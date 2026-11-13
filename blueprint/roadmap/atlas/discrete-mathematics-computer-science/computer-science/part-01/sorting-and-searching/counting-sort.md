---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.countingSort, Cslib.Algorithms.Lean.TimeM.countingSort_correct, Cslib.Algorithms.Lean.TimeM.countingSort_time
statement: formalized
proof: formalized
---

# Counting sort

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/counting-sort/index.html).

## Counting sort

Let $k$ be a natural number and let $\mathrm{key}$ assign to each record a
key in $\{0, \dots, k-1\}$. Counting sort of an array $A$ of records returns an array together
with a count of charged operations. It starts $k$ counters at zero, counts the records of $A$ with
each key, replaces the counters by cumulative counts so that the counter of key $q$ holds the
number of records with key at most $q$, and then scans $A$ from right to left: for each record it
decrements the counter of the record's key and writes the record at the resulting position of the
output, which starts as a copy of $A$. One operation is charged for each counter initialization,
key evaluation, counter read, counter write and output write.

Formalized by `Cslib.Algorithms.Lean.TimeM.countingSort`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/Counting.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Sort/Counting.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/counting-sort/index.html#counting-sort).

## Correctness of counting sort

Let $k$ be a natural number, let $\mathrm{key}$ assign to
each record a key in $\{0, \dots, k-1\}$, and let $A$ be an array of records. The array that
counting sort returns on $A$ lists its records in nondecreasing order of key, is a permutation of
$A$, and is stable: for every key $q < k$, the records of the output with key $q$, read from left
to right, form the same sequence as the records of $A$ with key $q$.

Formalized by `Cslib.Algorithms.Lean.TimeM.countingSort_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Counting.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Sort/Counting.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/counting-sort/index.html#counting-sort-correct).

## Running time of counting sort

Let $k$ be a natural number, let $\mathrm{key}$ assign to
each record a key in $\{0, \dots, k-1\}$, and let $A$ be an array of $n$ records. Counting sort on
$A$ with this key is charged at most $7n + 3k$ operations, where one operation is charged for each
counter initialization, key evaluation, counter read, counter write and output write.

Formalized by `Cslib.Algorithms.Lean.TimeM.countingSort_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Counting.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Sort/Counting.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/counting-sort/index.html#counting-sort-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting sort](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/counting-sort/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/counting-sort)
