---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AbsolutelyDensePartitionKourovka13Problem47Wanted.countableAbsolutelyDensePartition, MathlibExt.GroupTheory.AbsolutelyDensePartitionKourovka13Problem47Wanted.countableAbsolutelyDensePartition_holds, MathlibExt.GroupTheory.DensePartitionExpansiveSequenceKourovka15Problem80Wanted.IsExpansiveSequence, MathlibExt.GroupTheory.DensePartitionExpansiveSequenceKourovka15Problem80Wanted.countableDensePartitionHasExpansiveSequence, MathlibExt.GroupTheory.DensePartitionExpansiveSequenceKourovka15Problem80Wanted.countableDensePartitionHasExpansiveSequence_refuted
statement: formalized
---

# Dense partitions of groups

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/dense-partitions-of-groups/index.html).

## Protasov's question on absolutely dense partitions (Kourovka 13.47)

The proposition that
every countable abelian group $G$ with only finitely many elements of order $2$ can be partitioned
into two disjoint sets $A_1$ and $A_2$ with $A_1 \cup A_2 = G$ such that $A_1$ and $A_2$ are both
dense in every non-discrete Hausdorff group topology on $G$.

Formalized by `MathlibExt.GroupTheory.AbsolutelyDensePartitionKourovka13Problem47Wanted.countableAbsolutelyDensePartition`, a definition declared in [WantedExt/GroupTheory/AbsolutelyDensePartitionKourovka13Problem47Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AbsolutelyDensePartitionKourovka13Problem47Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/dense-partitions-of-groups/index.html#countable-absolutely-dense-partition).

## Kourovka Problem 13.47 has a positive answer

Every countable abelian group $G$ with only
finitely many elements of order $2$ can be partitioned into two disjoint sets $A_1$ and $A_2$ with
$A_1 \cup A_2 = G$ such that $A_1$ and $A_2$ are both dense in every non-discrete Hausdorff group
topology on $G$.

The Kourovka Archive answers 13.47 "Yes, it can", citing Zelenyuk.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.47 (I. V. Protasov); resolution: E. G. Zelenyuk, Ukrain. Math. J. 51 (1999), no. 1, 44-50, Kourovka Archive, Problem 13.47 (answer: Yes, it can).

Stated but not proved: `MathlibExt.GroupTheory.AbsolutelyDensePartitionKourovka13Problem47Wanted.countableAbsolutelyDensePartition_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AbsolutelyDensePartitionKourovka13Problem47Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AbsolutelyDensePartitionKourovka13Problem47Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/dense-partitions-of-groups/index.html#countable-absolutely-dense-partition-hol).

## Expansive sequence

In a topological space $G$, a sequence $(F_n)_{n \in \mathbb{N}}$ of
finite subsets of $G$ is expansive if the sets $F_n$ are pairwise disjoint and for every nonempty
open set $U \subseteq G$ there is $m \in \mathbb{N}$ such that $F_n$ meets $U$ for all $n > m$.

Formalized by `MathlibExt.GroupTheory.DensePartitionExpansiveSequenceKourovka15Problem80Wanted.IsExpansiveSequence`, a definition declared in [WantedExt/GroupTheory/DensePartitionExpansiveSequenceKourovka15Problem80Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DensePartitionExpansiveSequenceKourovka15Problem80Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/dense-partitions-of-groups/index.html#is-expansive-sequence).

## Kourovka Problem 15.80: dense partitions and expansive sequences

Every topological group
$G$ admitting a sequence $(P_i)_{i \in \mathbb{N}}$ of pairwise disjoint dense subsets with union
$G$ has an expansive sequence.

Formalized by `MathlibExt.GroupTheory.DensePartitionExpansiveSequenceKourovka15Problem80Wanted.countableDensePartitionHasExpansiveSequence`, a definition declared in [WantedExt/GroupTheory/DensePartitionExpansiveSequenceKourovka15Problem80Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DensePartitionExpansiveSequenceKourovka15Problem80Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/dense-partitions-of-groups/index.html#countable-dense-partition-has-expansive).

## Kourovka Problem 15.80 has a negative answer

It is not true that every topological group $G$
admitting a sequence $(P_i)_{i \in \mathbb{N}}$ of pairwise disjoint dense subsets with union $G$
has an expansive sequence, that is, a sequence $(F_n)_{n \in \mathbb{N}}$ of pairwise disjoint
finite subsets of $G$ such that every nonempty open set $U \subseteq G$ meets $F_n$ for all $n$
larger than some $m$.

S. Corson's counterexample: $\prod_{\mathbb{N}} \mathbb{R}$ with the box topology has no countable
dense subset, hence no expansive sequence (the union of one is countable and dense), but its base
of $2^{\aleph_0}$ open sets of size $2^{\aleph_0}$ lets a transfinite induction partition it into
countably many dense subsets.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 15.80 (I. V. Protasov); resolution: S. Corson, letter of 19 May 2025, as recorded in the Kourovka Notebook (21st issue), Problem 15.80, G = ∏_ℕ ℝ with the box topology: not separable, hence without expansive sequences, but partitionable into countably many dense subsets by transfinite induction; the Kourovka Notebook (21st issue) marks 15.80 solved (answer: Not necessarily), https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.DensePartitionExpansiveSequenceKourovka15Problem80Wanted.countableDensePartitionHasExpansiveSequence_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DensePartitionExpansiveSequenceKourovka15Problem80Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DensePartitionExpansiveSequenceKourovka15Problem80Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/dense-partitions-of-groups/index.html#countable-dense-partition-has-expansive-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dense partitions of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/dense-partitions-of-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/combinatorics-in-groups/dense-partitions-of-groups)
