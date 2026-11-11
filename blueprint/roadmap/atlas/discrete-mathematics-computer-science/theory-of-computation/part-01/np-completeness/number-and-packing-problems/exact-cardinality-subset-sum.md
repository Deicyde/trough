---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.CardinalitySubsetSum.CardinalitySubsetSumInstance, MetaMathlibExt.Complexity.NPComplete.CardinalitySubsetSum.CardinalitySubsetSumFeasible, MetaMathlibExt.Complexity.NPComplete.CardinalitySubsetSum.cardinalitySubsetSumDec, MetaMathlibExt.Complexity.NPComplete.CardinalitySubsetSum.cardinalitySubsetSum_npComplete
statement: formalized
---

# Exact-cardinality subset sum

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/exact-cardinality-subset-sum/index.html).

## Exact-cardinality subset-sum instances

An exact-cardinality subset-sum instance is a
triple $(a, K, T)$ consisting of a list $a$ of natural numbers, a natural number $K$ (the
cardinality) and a natural number $T$ (the target).

Formalized by `MetaMathlibExt.Complexity.NPComplete.CardinalitySubsetSum.CardinalitySubsetSumInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/CardinalitySubsetSumWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CardinalitySubsetSumWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/exact-cardinality-subset-sum/index.html#cardinality-subset-sum-instance).

## Feasibility of an exact-cardinality subset-sum instance

An exact-cardinality subset-sum
instance $(a, K, T)$ is feasible when some subsequence of the list $a$ (entries kept in order, not
necessarily contiguous) has exactly $K$ entries and sum $T$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CardinalitySubsetSum.CardinalitySubsetSumFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/CardinalitySubsetSumWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CardinalitySubsetSumWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/exact-cardinality-subset-sum/index.html#cardinality-subset-sum-feasible).

## Exact-cardinality subset sum as a decision problem

The decision problem
EXACT-CARDINALITY SUBSET SUM accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding, to an exact-cardinality subset-sum instance that is feasible; it rejects every
bitstring that does not decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CardinalitySubsetSum.cardinalitySubsetSumDec`, a definition declared in [WantedExt/Complexity/NPComplete/CardinalitySubsetSumWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CardinalitySubsetSumWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/exact-cardinality-subset-sum/index.html#cardinality-subset-sum-dec).

## EXACT-CARDINALITY SUBSET SUM is NP-complete

The decision problem EXACT-CARDINALITY
SUBSET SUM lies in NP, and every decision problem in NP has a polynomial-time many-one reduction
to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), SUBSET SUM; NP-completeness via the zero-padding reduction from ordinary subset sum.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.CardinalitySubsetSum.cardinalitySubsetSum_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/CardinalitySubsetSumWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CardinalitySubsetSumWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/exact-cardinality-subset-sum/index.html#cardinality-subset-sum-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exact-cardinality subset sum](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/exact-cardinality-subset-sum/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/exact-cardinality-subset-sum)
