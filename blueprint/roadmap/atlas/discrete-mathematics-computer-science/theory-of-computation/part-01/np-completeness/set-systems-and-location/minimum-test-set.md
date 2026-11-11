---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.MinimumTestSetInstance, MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.WellFormed, MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.MinimumTestSetFeasible, MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.minimumTestSetDec, MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.minimumTestSet_npComplete
statement: formalized
---

# Minimum test set

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/minimum-test-set/index.html).

## Minimum test set instance

An instance of MINIMUM TEST SET is a triple $(n, C, K)$ of a
natural number $n$ (the number of elements), a finite list $C$ of finite lists of natural numbers
(the tests) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.MinimumTestSetInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/minimum-test-set/index.html#minimum-test-set-instance).

## Well-formed minimum test set instance

An instance $(n, C, K)$ of MINIMUM TEST SET is well
formed when every test in the list $C$ is a list of numbers below $n$ without repeated entries,
so that each test lists a subset of $\{0, \dots, n-1\}$, each element once.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/minimum-test-set/index.html#well-formed).

## Feasible minimum test set instance

An instance $(n, C, K)$ of MINIMUM TEST SET is feasible
when some sublist $T$ of $C$ (obtained by deleting entries of $C$) has length at most $K$ and
distinguishes every pair: for all distinct $a, b < n$ some test in $T$ contains exactly one of
$a$ and $b$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.MinimumTestSetFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/minimum-test-set/index.html#minimum-test-set-feasible).

## The MINIMUM TEST SET decision problem

It accepts a bitstring $x$ exactly when $x$ decodes,
under the canonical bitstring encoding, to a triple $(n, C, K)$ of a natural number $n$, a list
$C$ of lists of natural numbers (the tests) and a natural number $K$ with the following
properties: every test is a list of numbers below $n$ without repeated entries, and some sublist
$T$ of $C$, obtained by deleting entries of $C$, has length at most $K$ and distinguishes every
pair, that is, for all distinct $a, b < n$ some test in $T$ contains exactly one of $a$ and $b$.
Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.minimumTestSetDec`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/minimum-test-set/index.html#minimum-test-set-dec).

## MINIMUM TEST SET is NP-complete

The MINIMUM TEST SET decision problem lies in NP, and
every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MINIMUM TEST COLLECTION; A. De Bonis, L. Gargano, and U. Vaccaro, "Generalized framework for test set problems" (1997).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MinimumTestSet.minimumTestSet_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumTestSetWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/minimum-test-set/index.html#minimum-test-set-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum test set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/minimum-test-set/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/minimum-test-set)
