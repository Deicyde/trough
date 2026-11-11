---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AutomorphismGroupProperSubgroupKourovka15Problem27Wanted.autIsoAutOfProperSubgroup, MathlibExt.GroupTheory.AutomorphismGroupProperSubgroupKourovka15Problem27Wanted.autIsoAutOfProperSubgroup_holds
statement: formalized
---

# Automorphism groups of p-groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/automorphism-groups-of-p-groups/index.html).

## Berkovich's problem on automorphism groups of p-groups (Kourovka 15.27)

The statement that
for some prime $p$ there are a finite $p$-group $G$ of order greater than $2$ and a proper subgroup
$H < G$ whose automorphism groups are isomorphic, $\mathrm{Aut}(G) \cong \mathrm{Aut}(H)$.

Formalized by `MathlibExt.GroupTheory.AutomorphismGroupProperSubgroupKourovka15Problem27Wanted.autIsoAutOfProperSubgroup`, a definition declared in [WantedExt/GroupTheory/AutomorphismGroupProperSubgroupKourovka15Problem27Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutomorphismGroupProperSubgroupKourovka15Problem27Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/automorphism-groups-of-p-groups/index.html#aut-iso-aut-of-proper-subgroup).

## A p-group and a proper subgroup with isomorphic automorphism groups (Kourovka 15.27)

For some
prime $p$ there are a finite $p$-group $G$ of order greater than $2$ and a proper subgroup $H < G$
with $\mathrm{Aut}(G) \cong \mathrm{Aut}(H)$ as groups.

T. Li's example is a $2$-group $G$ of order $32$ with a subgroup $H$ of order $16$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.27 (Ya. G. Berkovich); resolution: T. Li, Arch. Math. 92 (2009), 287-290, Kourovka Archive, Problem 15.27 (answer: Yes, it is possible, for |G| = 2|H| = 32).

Stated but not proved: `MathlibExt.GroupTheory.AutomorphismGroupProperSubgroupKourovka15Problem27Wanted.autIsoAutOfProperSubgroup_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AutomorphismGroupProperSubgroupKourovka15Problem27Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutomorphismGroupProperSubgroupKourovka15Problem27Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/automorphism-groups-of-p-groups/index.html#aut-iso-aut-of-proper-subgroup-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Automorphism groups of p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/automorphism-groups-of-p-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/automorphisms/automorphism-groups/automorphism-groups-of-p-groups)
