---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PartitionMeetingInfiniteCosetsKourovka16Problem43Wanted.threePartitionMeetsInfiniteCosets, MathlibExt.GroupTheory.PartitionMeetingInfiniteCosetsKourovka16Problem43Wanted.threePartitionMeetsInfiniteCosets_holds
statement: formalized
---

# Partitions meeting every infinite coset

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/partitions-meeting-every-infinite-coset/index.html).

## Kourovka 16.43: partitioning $\bigoplus_{\omega_1} \mathbb{Z}/3\mathbb{Z}$ into three parts meeting every infinite coset

**Kourovka 16.43: partitioning $\bigoplus_{\omega_1} \mathbb{Z}/3\mathbb{Z}$ into three parts
meeting every infinite coset.** The proposition that for every set $I$ of cardinality $\aleph_1$,
the group $A = \bigoplus_{i \in I} \mathbb{Z}/3\mathbb{Z}$ of finitely supported functions from $I$
to $\mathbb{Z}/3\mathbb{Z}$ can be partitioned into three subsets $A_0, A_1, A_2$ such that for
every infinite subgroup $H$ of $A$ and every $x \in A$, the coset $x + H$ meets each $A_i$.

Formalized by `MathlibExt.GroupTheory.PartitionMeetingInfiniteCosetsKourovka16Problem43Wanted.threePartitionMeetsInfiniteCosets`, a definition declared in [WantedExt/GroupTheory/PartitionMeetingInfiniteCosetsKourovka16Problem43Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PartitionMeetingInfiniteCosetsKourovka16Problem43Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/partitions-meeting-every-infinite-coset/index.html#three-partition-meets-infinite-cosets).

## A partition of $\bigoplus_{\omega_1} \mathbb{Z}/3\mathbb{Z}$ into three parts meeting every infinite coset

**A partition of $\bigoplus_{\omega_1} \mathbb{Z}/3\mathbb{Z}$ into three parts meeting every
infinite coset.** Let $I$ be a set of cardinality $\aleph_1$ and let $A = \bigoplus_{i \in I}
\mathbb{Z}/3\mathbb{Z}$ be the group of finitely supported functions from $I$ to
$\mathbb{Z}/3\mathbb{Z}$. Then $A$ can be partitioned into three subsets $A_0, A_1, A_2$ such that
for every infinite subgroup $H$ of $A$ and every $x \in A$, the coset $x + H$ meets each $A_i$.

The Kourovka Archive records more: every infinite abelian group with finitely many involutions can
be partitioned into infinitely many subsets such that every coset modulo an infinite subgroup meets
each subset of the partition.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.43 (E. G. Zelenyuk); resolution: Y. Zelenyuk, J. Combin. Theory Ser. A 115 (2008), 331-339, Kourovka Archive, Problem 16.43 (Yes; moreover every infinite abelian group with finitely many involutions can be partitioned into infinitely many subsets such that every coset modulo an infinite subgroup meets each subset).

Stated but not proved: `MathlibExt.GroupTheory.PartitionMeetingInfiniteCosetsKourovka16Problem43Wanted.threePartitionMeetsInfiniteCosets_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PartitionMeetingInfiniteCosetsKourovka16Problem43Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PartitionMeetingInfiniteCosetsKourovka16Problem43Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/partitions-meeting-every-infinite-coset/index.html#three-partition-meets-infinite-cosets-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partitions meeting every infinite coset](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/partitions-meeting-every-infinite-coset/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/combinatorics-in-groups/partitions-meeting-every-infinite-coset)
