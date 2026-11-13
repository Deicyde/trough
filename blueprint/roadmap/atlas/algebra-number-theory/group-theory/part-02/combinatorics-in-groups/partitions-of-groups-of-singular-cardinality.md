---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SingularCardinalityPartitionKourovka13Problem45Wanted.singularCardinalityPartition, MathlibExt.GroupTheory.SingularCardinalityPartitionKourovka13Problem45Wanted.singularCardinalityPartition_refuted
statement: formalized
---

# Partitions of groups of singular cardinality

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/partitions-of-groups-of-singular-cardinality/index.html).

## Partitions of groups of singular cardinality (Kourovka 13.45)

The statement that every
infinite group $G$ whose cardinality $\mathfrak{m} = |G|$ is singular (not regular) can be split
into two disjoint sets $A_1$ and $A_2$ with $A_1 \cup A_2 = G$ such that $A_1 F \ne G$ and
$A_2 F \ne G$ for every subset $F \subseteq G$ with $|F| < \mathfrak{m}$, where
$A F = \{a f : a \in A, f \in F\}$.

Formalized by `MathlibExt.GroupTheory.SingularCardinalityPartitionKourovka13Problem45Wanted.singularCardinalityPartition`, a definition declared in [WantedExt/GroupTheory/SingularCardinalityPartitionKourovka13Problem45Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SingularCardinalityPartitionKourovka13Problem45Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/partitions-of-groups-of-singular-cardinality/index.html#singular-cardinality-partition).

## Some group of singular cardinality has no such partition

There is an infinite group $G$
whose cardinality $\mathfrak{m} = |G|$ is singular (not regular) such that for all disjoint sets
$A_1$ and $A_2$ with $A_1 \cup A_2 = G$ there is a subset $F \subseteq G$ with
$|F| < \mathfrak{m}$ and $A_1 F = G$ or $A_2 F = G$, where $A F = \{a f : a \in A, f \in F\}$.
That is, the statement of Kourovka Problem 13.45 fails.

Protasov and Slobodianiuk show that the answer depends on the algebraic structure of $G$: such a
partition exists for every free group, but not for abelian groups of singular cardinality. The
Kourovka Archive answers 13.45 "No, not always".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.45 (I. V. Protasov); resolution: I. Protasov and S. Slobodianiuk, A note on partitions of groups, Quest. Answers Gen. Topology 33 (2015), no. 2, 61-70, arXiv:1408.5607, abstract and Theorem 2(iii): the statement fails for abelian groups of singular cardinality (it holds for free groups); Kourovka Archive, Problem 13.45, https://arxiv.org/abs/1408.5607.

Stated but not proved: `MathlibExt.GroupTheory.SingularCardinalityPartitionKourovka13Problem45Wanted.singularCardinalityPartition_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SingularCardinalityPartitionKourovka13Problem45Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SingularCardinalityPartitionKourovka13Problem45Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/partitions-of-groups-of-singular-cardinality/index.html#singular-cardinality-partition-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partitions of groups of singular cardinality](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/partitions-of-groups-of-singular-cardinality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/combinatorics-in-groups/partitions-of-groups-of-singular-cardinality)
