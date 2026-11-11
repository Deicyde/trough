---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.extractMin, Cslib.Algorithms.Lean.TimeM.selectionSort, Cslib.Algorithms.Lean.TimeM.extractMin_time, Cslib.Algorithms.Lean.TimeM.extractMin_correct, Cslib.Algorithms.Lean.TimeM.selectionSort_correct, Cslib.Algorithms.Lean.TimeM.selectionSort_time
statement: formalized
proof: formalized
---

# Selection sort

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/selection-sort/index.html).

## Minimum extraction

Given an initial candidate $c$ in a linearly ordered type and a list
$L$, minimum extraction returns a pair $(m, r)$ together with a cost. If $L$ is empty, it returns
$c$ with the empty list at cost $0$. If $L$ has head $x$ and tail $L'$, it compares $x$ with $c$
at cost one: if $x < c$, it extracts from $L'$ with candidate $x$, obtaining $(m, r)$, and returns
$m$ with the list $c$ followed by $r$; otherwise it extracts from $L'$ with candidate $c$,
obtaining $(m, r)$, and returns $m$ with the list $x$ followed by $r$. The total cost is one plus
the cost of the recursive extraction.

Formalized by `Cslib.Algorithms.Lean.TimeM.extractMin`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/Selection.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Selection.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/selection-sort/index.html#extract-min).

## Selection sort

Selection sort of a list $L$ over a linearly ordered type is defined
recursively. If $L$ is empty, the result is the empty list at cost $0$. If $L$ has head $x$ and
tail $L'$, minimum extraction from $L'$ with initial candidate $x$ yields a minimum $m$ and the
list $r$ of remaining elements, and the result is $m$ followed by the selection sort of $r$. The
cost is the sum of the costs of all these minimum extractions.

Formalized by `Cslib.Algorithms.Lean.TimeM.selectionSort`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/Selection.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Selection.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/selection-sort/index.html#selection-sort).

## Cost of minimum extraction

For every element $c$ of a linearly ordered type and every
list $L$ over it, minimum extraction from $L$ with initial candidate $c$ has cost exactly $|L|$,
the length of $L$; that is, it performs exactly $|L|$ order comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.extractMin_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Selection.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Selection.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/selection-sort/index.html#extract-min-time).

## Correctness of minimum extraction

Let $c$ be an element of a linearly ordered type and
$L$ a list over it, and let $(m, r)$ be the pair returned by minimum extraction from $L$ with
initial candidate $c$. Then the list $m$ followed by $r$ is a permutation of the list $c$ followed
by $L$, $m \le c$, and $m \le x$ for every element $x$ of $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.extractMin_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Selection.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Selection.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/selection-sort/index.html#extract-min-correct).

## Correctness of selection sort

For every list $L$ over a linearly ordered type, the list
returned by selection sort on $L$ is sorted in nondecreasing order (each entry is $\le$ every
later entry) and is a permutation of $L$, so it preserves duplicate multiplicities.

Formalized by `Cslib.Algorithms.Lean.TimeM.selectionSort_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Selection.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Selection.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/selection-sort/index.html#selection-sort-correct).

## Comparison count of selection sort

For every list of length $n$ over a linearly ordered
type, selection sort has cost exactly $n(n-1)/2$ in the model that charges one unit per order
comparison; that is, it performs exactly $n(n-1)/2$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.selectionSort_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Selection.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Selection.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/selection-sort/index.html#selection-sort-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Selection sort](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/selection-sort/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/selection-sort)
