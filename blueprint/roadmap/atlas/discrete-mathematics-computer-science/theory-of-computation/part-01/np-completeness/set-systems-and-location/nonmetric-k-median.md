---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.KMedian.KMedianInstance, MetaMathlibExt.Complexity.NPComplete.KMedian.WellFormed, MetaMathlibExt.Complexity.NPComplete.KMedian.KMedianFeasible, MetaMathlibExt.Complexity.NPComplete.KMedian.kMedianDec, MetaMathlibExt.Complexity.NPComplete.KMedian.kMedian_npComplete
statement: formalized
---

# Nonmetric k-median

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-median/index.html).

## k-median instances

A k-median instance is a triple $(d, K, B)$ of a cost matrix $d$, given
as a list of rows of natural numbers (one row per client, one entry per location; the rows need
not have equal length), a natural number $K$ bounding the number of open locations, and a
natural-number budget $B$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.KMedian.KMedianInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/KMedianWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KMedianWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-median/index.html#kmedian-instance).

## Well-formed k-median instances

A k-median instance $(d, K, B)$ is well formed when all
rows of its cost matrix $d$ have the same length.

Formalized by `MetaMathlibExt.Complexity.NPComplete.KMedian.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/KMedianWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KMedianWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-median/index.html#well-formed).

## Feasible k-median instances

Let $(d, K, B)$ be a k-median instance whose cost matrix $d$
has rows $d_0, \dots, d_{n-1}$, one per client, and let $m$ be the length of $d_0$, or $m = 0$
when $n = 0$. The instance is feasible when there are a set $S \subseteq \{0, \dots, m-1\}$ of at
most $K$ locations and a choice of $a(c) \in S$ for each client $c < n$ such that
$\sum_{c < n} d_c(a(c)) \le B$, where $d_c(j)$ is the entry of $d_c$ at index $j$ (counting from
$0$), read as $0$ when $d_c$ has fewer than $j + 1$ entries.

Formalized by `MetaMathlibExt.Complexity.NPComplete.KMedian.KMedianFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/KMedianWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KMedianWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-median/index.html#kmedian-feasible).

## The k-MEDIAN decision problem

**The k-MEDIAN decision problem.** k-MEDIAN (generalized, nonmetric) is the decision problem
that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to
a k-median instance $(d, K, B)$ that is well formed and feasible. That is, $d$ has rows
$d_0, \dots, d_{n-1}$ (the clients) of a common length $m$ (the locations), and there are a set
$S \subseteq \{0, \dots, m-1\}$ of at most $K$ locations and a choice of $a(c) \in S$ for each
client $c < n$ with $\sum_{c < n} d_{c, a(c)} \le B$. Bitstrings that do not decode are
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.KMedian.kMedianDec`, a definition declared in [WantedExt/Complexity/NPComplete/KMedianWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KMedianWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-median/index.html#k-median-dec).

## k-MEDIAN (GENERALIZED, NONMETRIC) is NP-complete

The k-MEDIAN decision problem is in NP,
and every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- O. Kariv and S. L. Hakimi, "An algorithmic approach to network location problems. II: The p-medians", SIAM Journal on Applied Mathematics 37 (1979), 539-560.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.KMedian.kMedian_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/KMedianWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KMedianWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-median/index.html#k-median-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nonmetric k-median](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-median/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-median)
