---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MultiwayPartition.MultiwayPartitionInstance, MetaMathlibExt.Complexity.NPComplete.MultiwayPartition.MultiwayPartitionFeasible, MetaMathlibExt.Complexity.NPComplete.MultiwayPartition.multiwayPartitionDec, MetaMathlibExt.Complexity.NPComplete.MultiwayPartition.multiwayPartition_npComplete
statement: formalized
---

# Multiway number partitioning

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiway-number-partitioning/index.html).

## Multiway number partition instances

A multiway number partition instance is a pair
$(a, K)$ consisting of a list $a$ of natural numbers and a natural number $K$ (the number of
parts).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultiwayPartition.MultiwayPartitionInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MultiwayPartitionWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayPartitionWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiway-number-partitioning/index.html#multiway-partition-instance).

## Feasible multiway number partition instances

Let $(a, K)$ be a multiway number partition
instance with $a = (a_0, \dots, a_{m-1})$. It is feasible when $K \ge 1$ and there is a map $f$
from $\{0, \dots, m-1\}$ onto $\{0, \dots, K-1\}$ such that the sums
$\sum_{j < m,\, f(j) = p} a_j$ for $p = 0, \dots, K-1$ are all equal. In other words, the entries
of $a$, counted with repetition, can be split into $K$ nonempty parts with equal sums.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultiwayPartition.MultiwayPartitionFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MultiwayPartitionWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayPartitionWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiway-number-partitioning/index.html#multiway-partition-feasible).

## The MULTIWAY NUMBER PARTITION decision problem

MULTIWAY NUMBER PARTITION is the decision
problem on bitstrings that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding, to a multiway number partition instance $(a, K)$ that is feasible. Bitstrings
that do not decode to a multiway number partition instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultiwayPartition.multiwayPartitionDec`, a definition declared in [WantedExt/Complexity/NPComplete/MultiwayPartitionWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayPartitionWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiway-number-partitioning/index.html#multiway-partition-dec).

## MULTIWAY NUMBER PARTITION is NP-complete

Let MULTIWAY NUMBER PARTITION be the decision
problem that accepts exactly the bitstrings decoding to a feasible multiway number partition
instance: a list of natural numbers and a number $K \ge 1$ such that the entries of the list,
counted with repetition, can be split into $K$ nonempty parts with equal sums. Then MULTIWAY
NUMBER PARTITION is in NP, and every decision problem in NP reduces to it by a polynomial-time
many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MULTIWAY NUMBER PARTITION (the `K = 2` slice is PARTITION).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MultiwayPartition.multiwayPartition_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MultiwayPartitionWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayPartitionWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiway-number-partitioning/index.html#multiway-partition-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiway number partitioning](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiway-number-partitioning/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/multiway-number-partitioning)
