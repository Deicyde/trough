---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ComplementedSubgroupLatticeNormalKourovka11Problem128Wanted.normalSubgroupOfKGroupIsKGroup, MathlibExt.GroupTheory.ComplementedSubgroupLatticeNormalKourovka11Problem128Wanted.normalSubgroupOfKGroupIsKGroup_refuted
statement: formalized
---

# Groups with complemented subgroup lattices

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/groups-with-complemented-subgroup-lattices/index.html).

## Kourovka Problem 11.128 on normal subgroups of $K$-groups

Call a group $G$ a $K$-group
when its subgroup lattice is complemented: every subgroup $A$ of $G$ has a subgroup $B$ with
$A \cap B = 1$ and $\langle A, B \rangle = G$. This is the assertion (M. Emaldi) that every normal
subgroup of a $K$-group, viewed as a group in its own right, is again a $K$-group.

Formalized by `MathlibExt.GroupTheory.ComplementedSubgroupLatticeNormalKourovka11Problem128Wanted.normalSubgroupOfKGroupIsKGroup`, a definition declared in [WantedExt/GroupTheory/ComplementedSubgroupLatticeNormalKourovka11Problem128Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ComplementedSubgroupLatticeNormalKourovka11Problem128Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/groups-with-complemented-subgroup-lattices/index.html#normal-subgroup-of-kgroup-is-kgroup).

## Normal subgroups of $K$-groups need not be $K$-groups

There is a group $G$ whose subgroup
lattice is complemented (a $K$-group) with a normal subgroup $N$ whose own subgroup lattice is not
complemented; so Kourovka Problem 11.128 has a negative answer.

The Kourovka Archive answers 11.128 "No, it is not" (Obraztsov).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.128 (M. Emaldi); resolution: V. N. Obraztsov, J. Austral. Math. Soc. (Ser. A) 61, no. 2 (1996), 267-288, Kourovka Archive, Problem 11.128: "No, it is not", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.ComplementedSubgroupLatticeNormalKourovka11Problem128Wanted.normalSubgroupOfKGroupIsKGroup_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ComplementedSubgroupLatticeNormalKourovka11Problem128Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ComplementedSubgroupLatticeNormalKourovka11Problem128Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/groups-with-complemented-subgroup-lattices/index.html#normal-subgroup-of-kgroup-is-kgroup-refu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Groups with complemented subgroup lattices](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/groups-with-complemented-subgroup-lattices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/subgroup-embedding/groups-with-complemented-subgroup-lattices)
