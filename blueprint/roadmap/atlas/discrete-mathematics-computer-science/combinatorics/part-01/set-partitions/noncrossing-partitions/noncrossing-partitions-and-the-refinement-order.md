---
declaration: section
origin: cited
lean: NoncrossingPartition.SetPartition, NoncrossingPartition.HasCrossing, NoncrossingPartition.IsNoncrossing, NoncrossingPartition, NoncrossingPartition.block, NoncrossingPartition.isNoncrossing_of_le_three
statement: formalized
proof: formalized
---

# Noncrossing partitions and the refinement order

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order/index.html).

## Set partition

A set partition of $\{0, \dots, n-1\}$ is a finite collection of nonempty,
pairwise disjoint subsets of $\{0, \dots, n-1\}$, called blocks, whose union is
$\{0, \dots, n-1\}$.

Formalized by `NoncrossingPartition.SetPartition`, an abbreviation declared in [MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order/index.html#set-partition).

## Crossing in a set partition

A set partition $P$ of $\{0, \dots, n-1\}$ has a crossing
if there are $a < b < c < d$ in $\{0, \dots, n-1\}$ such that $a$ and $c$ lie in the same block
of $P$, $b$ and $d$ lie in the same block of $P$, and these two blocks are different.

Formalized by `NoncrossingPartition.HasCrossing`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order/index.html#has-crossing).

## Noncrossing set partition

A set partition of $\{0, \dots, n-1\}$ is noncrossing if it
has no crossing.

Formalized by `NoncrossingPartition.IsNoncrossing`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order/index.html#is-noncrossing).

## Noncrossing partition

A noncrossing partition of $\{0, \dots, n-1\}$ is a set partition
of $\{0, \dots, n-1\}$ that is noncrossing.

Formalized by `NoncrossingPartition`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order/index.html#noncrossing-partition).

## Block of a noncrossing partition

For a noncrossing partition $P$ of
$\{0, \dots, n-1\}$ and a point $a \in \{0, \dots, n-1\}$, the block of $P$ at $a$ is the block
of the underlying set partition that contains $a$.

Formalized by `NoncrossingPartition.block`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order/index.html#block).

## Partitions of at most three points are noncrossing

For every $n \le 3$, every set
partition of $\{0, \dots, n-1\}$ is noncrossing.

Formalized by `NoncrossingPartition.isNoncrossing_of_le_three`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Basic.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order/index.html#is-noncrossing-of-le-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Noncrossing partitions and the refinement order](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/set-partitions/noncrossing-partitions/noncrossing-partitions-and-the-refinement-order)
