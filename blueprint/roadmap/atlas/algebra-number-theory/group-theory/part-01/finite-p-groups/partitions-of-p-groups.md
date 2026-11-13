---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PGroupPartitionAbelianComponentKourovka15Problem26Wanted.IsGroupPartition, MathlibExt.GroupTheory.PGroupPartitionAbelianComponentKourovka15Problem26Wanted.pGroupPartitionHasAbelianComponent, MathlibExt.GroupTheory.PGroupPartitionAbelianComponentKourovka15Problem26Wanted.pGroupPartitionHasAbelianComponent_holds
statement: formalized
---

# Partitions of p-groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/partitions-of-p-groups/index.html).

## Partition of a group

Let $G$ be a group. A set $C$ of subgroups of $G$ is a partition of
$G$ when every member of $C$ is a proper subgroup of $G$, every element of $G$ lies in some member
of $C$, and any two distinct members of $C$ intersect in the trivial subgroup. The members of $C$
are called its components.

Formalized by `MathlibExt.GroupTheory.PGroupPartitionAbelianComponentKourovka15Problem26Wanted.IsGroupPartition`, a definition declared in [WantedExt/GroupTheory/PGroupPartitionAbelianComponentKourovka15Problem26Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PGroupPartitionAbelianComponentKourovka15Problem26Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/partitions-of-p-groups/index.html#is-group-partition).

## Berkovich's question on abelian components of partitions

The statement that for every prime
$p$, every finite $p$-group $G$ and every partition $C$ of $G$ (a set of proper subgroups of $G$
whose union is $G$ and any two distinct members of which intersect in the trivial subgroup), some
member $H$ of $C$ is abelian, that is, $xy = yx$ for all $x, y \in H$.

This is Kourovka Notebook Problem 15.26 (Ya. G. Berkovich).

Formalized by `MathlibExt.GroupTheory.PGroupPartitionAbelianComponentKourovka15Problem26Wanted.pGroupPartitionHasAbelianComponent`, a definition declared in [WantedExt/GroupTheory/PGroupPartitionAbelianComponentKourovka15Problem26Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PGroupPartitionAbelianComponentKourovka15Problem26Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/partitions-of-p-groups/index.html#p-group-partition-has-abelian-component).

## Every partition of a finite $p$-group has an abelian component

For every prime $p$, every
finite $p$-group $G$ and every partition $C$ of $G$ (a set of proper subgroups of $G$ whose union is
$G$ and any two distinct members of which intersect in the trivial subgroup), some member $H$ of $C$
is abelian, that is, $xy = yx$ for all $x, y \in H$.

Resolved true: by Theorem B of Cat's preprint, every partition of a finite $p$-group into nontrivial
components has an abelian component (for non-abelian $G$ an elementary abelian one meeting the
Frattini subgroup $\Phi(G)$ of $G$ trivially); the Kourovka Notebook (21st issue) marks 15.26
solved, "Yes, it is true" (AI solution confirmed by E. I. Khukhro). Components are not required to
be nontrivial here: a trivial component is abelian, and removing it leaves a partition.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 15.26 (Ya. G. Berkovich); resolution: G. Cat, A Frattini-free component in every partition, and Kourovka 15.26, preprint (2026), AI-generated solution confirmed by E. I. Khukhro, Theorem B (a partition of a finite p-group into nontrivial components has an abelian component), derived from Theorem A; the Kourovka Notebook (21st issue) marks 15.26 solved, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/08/kourovka_15-26-ai.pdf.

Stated but not proved: `MathlibExt.GroupTheory.PGroupPartitionAbelianComponentKourovka15Problem26Wanted.pGroupPartitionHasAbelianComponent_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PGroupPartitionAbelianComponentKourovka15Problem26Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PGroupPartitionAbelianComponentKourovka15Problem26Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/partitions-of-p-groups/index.html#p-group-partition-has-abelian-component-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partitions of p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/partitions-of-p-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/finite-p-groups/partitions-of-p-groups)
