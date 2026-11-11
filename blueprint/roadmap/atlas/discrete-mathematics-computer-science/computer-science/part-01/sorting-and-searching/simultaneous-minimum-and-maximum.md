---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.minMax, Cslib.Algorithms.Lean.TimeM.minMax_ret, Cslib.Algorithms.Lean.TimeM.minMax_eq_none_iff, Cslib.Algorithms.Lean.TimeM.minMax_eq_some_iff, Cslib.Algorithms.Lean.TimeM.minMax_nil, Cslib.Algorithms.Lean.TimeM.minMax_singleton, Cslib.Algorithms.Lean.TimeM.minMax_time_odd, Cslib.Algorithms.Lean.TimeM.minMax_time_even
statement: formalized
proof: formalized
---

# Simultaneous minimum and maximum

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html).

## Simultaneous minimum and maximum

Given a list $xs$ over a linearly ordered type, the
paired algorithm returns no result when $xs$ is empty and otherwise returns a pair (a candidate
minimum and a candidate maximum), counting one unit of time for each comparison of elements. On a
one-element list $[a]$ it returns $(a, a)$ without a comparison. On a longer list of odd length
both candidates start at the first element without a comparison; on a list of even length they
start at the smaller and the larger of the first two elements, found with one comparison. The
remaining elements are then taken in consecutive pairs: one comparison orders the pair, its smaller
member replaces the candidate minimum if it is strictly smaller (one comparison), and its larger
member replaces the candidate maximum if it is strictly larger (one comparison).

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax`, a definition declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max).

## Correctness of the simultaneous minimum and maximum algorithm

For every list $xs$ over a
linearly ordered type, the simultaneous minimum and maximum algorithm returns no result on $xs$
when $xs$ is empty, and returns the pair $(\min xs, \max xs)$ of the least and greatest elements
of $xs$ otherwise.

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max-ret).

## The min–max algorithm returns no result exactly on the empty list

For every list $xs$
over a linearly ordered type, the simultaneous minimum and maximum algorithm returns no result on
$xs$ if and only if $xs$ is empty.

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max-eq-none-iff).

## Characterization of the min–max output

For every list $xs$ over a linearly ordered type
and all elements $lo$ and $hi$ of that type, the simultaneous minimum and maximum algorithm returns
the pair $(lo, hi)$ on $xs$ if and only if $lo$ and $hi$ both belong to $xs$, $lo \le x$ for every
$x$ in $xs$, and $x \le hi$ for every $x$ in $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max-eq-some-iff).

## The min–max algorithm on the empty list

On the empty list, the simultaneous minimum and
maximum algorithm returns no result and makes no comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max-nil).

## The min–max algorithm on a one-element list

For every element $a$ of a linearly ordered
type, on the list $[a]$ the simultaneous minimum and maximum algorithm returns the pair $(a, a)$
and makes no comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max-singleton).

## Comparisons of the min–max algorithm on odd-length lists

For every natural number $k$ and
every list of length $2k + 1$ over a linearly ordered type, the simultaneous minimum and maximum
algorithm makes exactly $3k$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax_time_odd`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max-time-odd).

## Comparisons of the min–max algorithm on even-length lists

For every natural number
$k \ge 1$ and every list of length $2k$ over a linearly ordered type, the simultaneous minimum and
maximum algorithm makes exactly $3k - 2$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax_time_even`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max-time-even).

## Comparison count of the simultaneous minimum and maximum algorithm

For every list of
length $n$ over a linearly ordered type, the simultaneous minimum and maximum algorithm makes no
comparisons when $n = 0$ and exactly $\lceil 3n/2 \rceil - 2$ comparisons when $n \ge 1$.

This counts element-order decisions, not full RAM instructions or comparator bit complexity.

Formalized by `Cslib.Algorithms.Lean.TimeM.minMax_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MinMax.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Selection/MinMax.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html#min-max-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simultaneous minimum and maximum](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/simultaneous-minimum-and-maximum)
