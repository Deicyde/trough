---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.quickSort, Cslib.Algorithms.Lean.TimeM.quickSort_correct, Cslib.Algorithms.Lean.TimeM.quickSort_time, Cslib.Algorithms.Lean.TimeM.betweenCount, Cslib.Algorithms.Lean.TimeM.quickSort_expectedTime_uniformPermutation, Cslib.Algorithms.Lean.TimeM.quickSort_expectedTime_uniformPermutation_toReal
statement: formalized
proof: formalized
---

# Quicksort

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quicksort/index.html).

## Quicksort

Deterministic quicksort on lists over a linear order, using the first entry as
pivot and counting comparisons. The empty list is returned unchanged at no cost. On a list with
first entry $p$ and tail $t$, the algorithm stably splits $t$ into the entries less than $p$, equal
to $p$ and greater than $p$, using one comparison per entry of $t$; it then recursively sorts the
lesser and greater parts and returns the sorted lesser part, followed by $p$, the entries equal to
$p$ in their original order, and the sorted greater part. The cost is the total number of
comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickSort`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/Quick.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Quick.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quicksort/index.html#quick-sort).

## Correctness of quicksort

For every list $\ell$ over a linear order, the output of
quicksort on $\ell$ is sorted in nondecreasing order and is a permutation of $\ell$; in
particular every value occurs in the output exactly as often as in $\ell$.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickSort_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Quick.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Quick.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quicksort/index.html#quick-sort-correct).

## Worst-case comparison bound for quicksort

For every list of length $n$ over a linear
order, quicksort performs at most $n(n-1)/2$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickSort_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Quick.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Quick.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quicksort/index.html#quick-sort-time).

## Number of list entries strictly between two values

For a list $\ell$ over a linear order
and elements $a$ and $b$, this is the number of entries $x$ of $\ell$, counted with multiplicity,
such that $a < x < b$.

Formalized by `Cslib.Algorithms.Lean.TimeM.betweenCount`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/QuickExpected.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/QuickExpected.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quicksort/index.html#between-count).

## Expected comparisons of quicksort on a random permutation

Let $\ell$ be a list without
repeated entries over a linear order. The expected number of comparisons made by quicksort on the
list obtained by rearranging the entries of $\ell$ by a uniformly random permutation of their
positions, computed in the extended nonnegative reals $[0, \infty]$, equals

$$\sum_{a < b} \frac{2}{d(a, b) + 2},$$

where the sum runs over pairs of entries $a < b$ of $\ell$ and $d(a, b)$ is the number of entries
of $\ell$ strictly between $a$ and $b$ (CLRS Section 7.4).

Formalized by `Cslib.Algorithms.Lean.TimeM.quickSort_expectedTime_uniformPermutation`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/QuickExpected.lean, line 813](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/QuickExpected.lean#L813). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quicksort/index.html#quick-sort-expected-time-uniform-permuta).

## Expected comparisons of quicksort on a random permutation, as a real number

Let $\ell$
be a list without repeated entries over a linear order. Take the expected number of comparisons
made by quicksort on the list obtained by rearranging the entries of $\ell$ by a uniformly random
permutation of their positions, which is an element of $[0, \infty]$, and convert it to a real
number. The result equals the real sum

$$\sum_{a < b} \frac{2}{d(a, b) + 2},$$

where the sum runs over pairs of entries $a < b$ of $\ell$ and $d(a, b)$ is the number of entries
of $\ell$ strictly between $a$ and $b$.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickSort_expectedTime_uniformPermutation_toReal`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/QuickExpected.lean, line 855](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/QuickExpected.lean#L855). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quicksort/index.html#quick-sort-expected-time-uniform-permuta-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quicksort](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quicksort/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/quicksort)
