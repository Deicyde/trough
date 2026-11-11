---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ThreePartition.ThreePartitionInstance, MetaMathlibExt.Complexity.NPComplete.ThreePartition.WellFormed, MetaMathlibExt.Complexity.NPComplete.ThreePartition.ThreePartitionFeasible, MetaMathlibExt.Complexity.NPComplete.ThreePartition.threePartitionDec, MetaMathlibExt.Complexity.NPComplete.ThreePartition.threePartition_npComplete
statement: formalized
---

# 3-partition problem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/3-partition-problem/index.html).

## 3-partition instances

An instance of 3-PARTITION is a pair $(a, B)$ of a finite list $a$
of natural numbers and a natural number $B$, the target sum.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ThreePartition.ThreePartitionInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/3-partition-problem/index.html#three-partition-instance).

## Well-formed 3-partition instances

A 3-partition instance $(a, B)$ is well formed when the
length of the list $a$ is a multiple of $3$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ThreePartition.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/3-partition-problem/index.html#well-formed).

## Feasible 3-partition instances

Let $(a, B)$ be a 3-partition instance with
$a = (a_0, \dots, a_{N-1})$, and let $m = \lfloor N/3 \rfloor$. The instance is feasible when
there is a map $g : \{0, \dots, N-1\} \to \{0, \dots, m-1\}$ such that for every $t < m$ exactly
three indices $j$ satisfy $g(j) = t$, and the sum of $a_j$ over these indices equals $B$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ThreePartition.ThreePartitionFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/3-partition-problem/index.html#three-partition-feasible).

## 3-PARTITION as a decision problem

The decision problem 3-PARTITION accepts a bitstring
$x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a 3-partition instance
$(a, B)$ that is well formed (the length of the list $a$ is a multiple of $3$) and feasible (the
entries of $a$ can be split into triples each summing to $B$). Bitstrings that do not decode to
an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ThreePartition.threePartitionDec`, a definition declared in [WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/3-partition-problem/index.html#three-partition-dec).

## 3-PARTITION is NP-complete

The decision problem 3-PARTITION on bitstrings is in NP, and
every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), 3-PARTITION (strongly NP-complete).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ThreePartition.threePartition_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreePartitionWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/3-partition-problem/index.html#three-partition-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 3-partition problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/3-partition-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/3-partition-problem)
