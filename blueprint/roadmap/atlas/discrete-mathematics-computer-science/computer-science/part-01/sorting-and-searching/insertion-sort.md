---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.compareLE, Cslib.Algorithms.Lean.TimeM.insertionSortInsert, Cslib.Algorithms.Lean.TimeM.insertionSort, Cslib.Algorithms.Lean.TimeM.ret_insertionSortInsert, Cslib.Algorithms.Lean.TimeM.ret_insertionSort, Cslib.Algorithms.Lean.TimeM.insertionSort_eq_insertionSortM, Cslib.Algorithms.Lean.TimeM.insertionSort_sorted, Cslib.Algorithms.Lean.TimeM.insertionSort_perm
statement: formalized
proof: formalized
---

# Insertion sort

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html).

## Charged comparison

For elements $x$ and $y$ of a linearly ordered type, this
computation returns the truth value of $x \le y$ and charges one unit of time.

Formalized by `Cslib.Algorithms.Lean.TimeM.compareLE`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#compare-le).

## Costed insertion into a list

Let $a$ be an element of a linearly ordered type. Inserting
$a$ into the empty list returns $[a]$ at no cost. Inserting $a$ into a list with head $b$ and
tail $l$ first charges one unit for comparing $a \le b$; if $a \le b$ it returns $a$ followed by
$b$ and $l$, and otherwise it inserts $a$ into $l$, adding that cost, and returns $b$ followed by
the result.

Formalized by `Cslib.Algorithms.Lean.TimeM.insertionSortInsert`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#insertion-sort-insert).

## Insertion sort with comparison cost

On a list over a linearly ordered type, insertion
sort returns the empty list at no cost when the input is empty. On a list with head $a$ and
tail $l$, it sorts $l$ and then inserts $a$ into the result by costed insertion; its cost is the
cost of sorting $l$ plus the cost of that insertion. Exactly one unit is charged for each order
comparison.

Formalized by `Cslib.Algorithms.Lean.TimeM.insertionSort`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#insertion-sort).

## Costed insertion returns the ordered insertion

For an element $a$ and a list $l$ over a
linearly ordered type, the list returned by costed insertion of $a$ into $l$ is the ordered
insertion of $a$ into $l$ with respect to $\le$: $a$ is placed immediately before the first
element $b$ of $l$ with $a \le b$, or at the end of $l$ if there is no such element.

Formalized by `Cslib.Algorithms.Lean.TimeM.ret_insertionSortInsert`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#ret-insertion-sort-insert).

## Cost-annotated insertion sort returns the standard insertion sort

For every list $xs$
over a linearly ordered type, the list returned by insertion sort with comparison costs equals the
standard insertion sort of $xs$ with respect to $\le$, which inserts the head into the sorted
tail.

Formalized by `Cslib.Algorithms.Lean.TimeM.ret_insertionSort`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#ret-insertion-sort).

## Agreement with CSLib's monadic insertion sort

For a list $l$ over a linearly ordered
type in the lowest universe, the costed insertion sort of $l$ equals CSLib's generic monadic
insertion sort run in the time-counting monad with the charged comparison: the returned lists
agree and the numbers of charged comparisons agree.

Formalized by `Cslib.Algorithms.Lean.TimeM.insertionSort_eq_insertionSortM`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#insertion-sort-eq-insertion-sort-m).

## Insertion sort returns a sorted list

For every list $l$ over a linearly ordered type,
the list returned by insertion sort on $l$ is nondecreasing.

Formalized by `Cslib.Algorithms.Lean.TimeM.insertionSort_sorted`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#insertion-sort-sorted).

## Insertion sort permutes its input

For every list $l$ over a linearly ordered type, the
list returned by insertion sort is a permutation of $l$; in particular every element occurs in
it exactly as often as in $l$.

Formalized by `Cslib.Algorithms.Lean.TimeM.insertionSort_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#insertion-sort-perm).

## Correctness of insertion sort

For every list $l$ over a linearly ordered type, the list
returned by insertion sort is nondecreasing and is a permutation of $l$.

Formalized by `Cslib.Algorithms.Lean.TimeM.insertionSort_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#insertion-sort-correct).

## Cost of a single insertion

For an element $a$ and a list $l$ over a linearly ordered
type, costed insertion of $a$ into $l$ charges at most $n$ comparisons, where $n$ is the length
of $l$.

Formalized by `Cslib.Algorithms.Lean.TimeM.insertionSortInsert_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#insertion-sort-insert-time-le).

## Comparison bound for insertion sort

On a list of length $n$ over a linearly ordered
type, insertion sort charges at most $n(n-1)/2$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.insertionSort_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/InsertionCost.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html#insertion-sort-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Insertion sort](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/insertion-sort/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/insertion-sort)
