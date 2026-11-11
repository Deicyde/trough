---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.quickselect, Cslib.Algorithms.Lean.TimeM.quickselect_eq_none_iff, Cslib.Algorithms.Lean.TimeM.partition3_countP_eq_below, Cslib.Algorithms.Lean.TimeM.partition3_countP_eq_block_add_above, Cslib.Algorithms.Lean.TimeM.partition3_count_lt, Cslib.Algorithms.Lean.TimeM.partition3_count_le, Cslib.Algorithms.Lean.TimeM.quickselect_correct, Cslib.Algorithms.Lean.TimeM.quickselect_eq_getElem?_insertionSort
statement: formalized
proof: formalized
---

# Quickselect

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html).

## Quickselect

Deterministic quickselect takes a list $L$ over a linear order and a
zero-based rank $k$ and returns an element or no element, together with its cost, the number
of element comparisons it makes. If $k \ge |L|$, it returns no element at no cost. Otherwise
it runs the following recursion, starting from the list $L$ and the rank $k$. On an empty list
it returns no element. On a list with first entry $p$ and remaining entries $T$, and a rank
$r$, it forms the three-way partition of $T$ around $p$, with blocks $B$, $E$, $A$ of entries
below, equal to and above $p$, at a cost of $|T|$ comparisons. If $r < |B|$, it recurses on
$B$ with rank $r$; if $|B| \le r < |B| + |E| + 1$, it returns $p$; otherwise it recurses on
$A$ with rank $r - (|B| + |E| + 1)$.

The recursion carries a fuel counter that starts at $|L|$ and drops by one per call, and it
returns no element when the fuel is exhausted; since every recursive call is on a strictly
shorter list, the fuel never runs out on a nonempty list.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickselect`, a definition declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#quickselect).

## Quickselect fails exactly out of range

Let $L$ be a list over a linear order and let
$k$ be a natural number. Quickselect on $L$ with zero-based rank $k$ returns no element if and
only if $|L| \le k$.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickselect_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#quickselect-eq-none-iff).

## Counting through the below block

Let $L$ be a list over a linear order, let $p$ be an
element, let $q$ be a Boolean predicate on the elements, and let $B$, $E$, $A$ be the blocks of
entries below, equal to and above $p$ in the three-way partition of $L$ around $p$. If $q$ is
false on every entry of $E$ and on every entry of $A$, then the number of entries of $L$
satisfying $q$ equals the number of entries of $B$ satisfying $q$, both counted with
multiplicity.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_countP_eq_below`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#partition3-count-p-eq-below).

## Counting through the above block

Let $L$ be a list over a linear order, let $p$ be an
element, let $q$ be a Boolean predicate on the elements, and let $B$, $E$, $A$ be the blocks of
entries below, equal to and above $p$ in the three-way partition of $L$ around $p$. If $q$ is
true on every entry of $B$ and on every entry of $E$, then the number of entries of $L$
satisfying $q$ equals $|B| + |E|$ plus the number of entries of $A$ satisfying $q$, all counted
with multiplicity.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_countP_eq_block_add_above`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#partition3-count-p-eq-block-add-above).

## Entries below the pivot

Let $L$ be a list over a linear order, let $p$ be an element,
and let $B$ be the block of entries below $p$ in the three-way partition of $L$ around $p$.
Then the number of entries of $L$ that are strictly less than $p$, counted with multiplicity,
equals $|B|$.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_count_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#partition3-count-lt).

## Entries at most the pivot

Let $L$ be a list over a linear order, let $p$ be an element,
and let $B$ and $E$ be the blocks of entries below and equal to $p$ in the three-way partition
of $L$ around $p$. Then the number of entries of $L$ that are at most $p$, counted with
multiplicity, equals $|B| + |E|$.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_count_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#partition3-count-le).

## Correctness of quickselect

Let $L$ be a list over a linear order and let $k$ be a
natural number. If quickselect on $L$ with zero-based rank $k$ returns an element $x$, then $x$
is an entry of $L$, and, counting entries of $L$ with multiplicity, the number of entries less
than $x$ is at most $k$ and $k$ is less than the number of entries at most $x$.

Thus $x$ occupies zero-based position $k$ in the sorted order of $L$, also when $x$ is repeated.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickselect_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#quickselect-correct).

## Quickselect agrees with sorting

Let $L$ be a list over a linear order, let $S$ be the
insertion sort of $L$ in nondecreasing order, and let $k$ be a natural number. If $k < |L|$,
quickselect on $L$ with zero-based rank $k$ returns the entry of $S$ at zero-based position $k$;
if $k \ge |L|$, it returns no element.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickselect_eq_getElem?_insertionSort`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#quickselect-eq-get-elem-insertion-sort).

## Rank inequalities determine the quickselect value

Let $L$ be a list over a linear
order, let $k$ be a natural number and let $x$ be an element. Counting entries of $L$ with
multiplicity, if the number of entries less than $x$ is at most $k$ and $k$ is less than the
number of entries at most $x$, then quickselect on $L$ with zero-based rank $k$ returns $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickselect_eq_some_of_count_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#quickselect-eq-some-of-count-rank).

## Worst-case comparison bound for quickselect

For every list $L$ over a linear order, of
length $n$, and every natural number $k$, quickselect on $L$ with rank $k$ makes at most
$n(n-1)/2$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.quickselect_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/Quickselect.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/Quickselect.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html#quickselect-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quickselect](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/quickselect/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/quickselect)
