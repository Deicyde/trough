---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AbelianLocallyQuaternionProductKourovka18Problem95Wanted.IsLocallyQuaternion, MathlibExt.GroupTheory.AbelianLocallyQuaternionProductKourovka18Problem95Wanted.abelianLocallyQuaternionProductSoluble, MathlibExt.GroupTheory.AbelianLocallyQuaternionProductKourovka18Problem95Wanted.abelianLocallyQuaternionProductSoluble_holds
statement: formalized
---

# Products of abelian and locally quaternion groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-abelian-and-locally-quaternion-group/index.html).

## Locally quaternion subgroup

A subgroup $B$ of a group $G$ is locally quaternion if there
is a strictly increasing sequence $C_0 < C_1 < C_2 < \cdots$ of subgroups of $G$, each isomorphic
to a generalized quaternion group $Q_{2^{k+2}}$ of order $2^{k+2}$ for some $k \ge 1$, whose
supremum (for a chain, the union) is $B$. In particular $B$ is infinite.

Formalized by `MathlibExt.GroupTheory.AbelianLocallyQuaternionProductKourovka18Problem95Wanted.IsLocallyQuaternion`, a definition declared in [WantedExt/GroupTheory/AbelianLocallyQuaternionProductKourovka18Problem95Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AbelianLocallyQuaternionProductKourovka18Problem95Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-abelian-and-locally-quaternion-group/index.html#is-locally-quaternion).

## Kourovka Problem 18.95 (Sozutov)

The proposition that every group $G$ with subgroups $A$
and $B$ such that $A$ is abelian, $B$ is locally quaternion, and $G = AB$ (every element of $G$ is a
product $ab$ with $a \in A$ and $b \in B$) is soluble.

Formalized by `MathlibExt.GroupTheory.AbelianLocallyQuaternionProductKourovka18Problem95Wanted.abelianLocallyQuaternionProductSoluble`, a definition declared in [WantedExt/GroupTheory/AbelianLocallyQuaternionProductKourovka18Problem95Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AbelianLocallyQuaternionProductKourovka18Problem95Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-abelian-and-locally-quaternion-group/index.html#abelian-locally-quaternion-product-solub).

## Products of abelian and locally quaternion groups are soluble

Let $G$ be a group with
subgroups $A$ and $B$ such that $A$ is abelian, $B$ is locally quaternion, and $G = AB$, that is,
every element of $G$ is a product $ab$ with $a \in A$ and $b \in B$. Then $G$ is soluble.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.95 (A. I. Sozutov); resolution: B. Amberg and Ya. Sysak, On products of groups with abelian subgroups of small index, J. Group Theory 20 (2017), no. 6, 1061-1072, Kourovka Archive, Problem 18.95: Yes, it is; Corollary 1.2 (arXiv:1611.10093): if a group G = AB is the product of an abelian subgroup A and a locally quaternion subgroup B, then G is soluble (Theorem 1.1: derived length at most 3), https://arxiv.org/abs/1611.10093.

Stated but not proved: `MathlibExt.GroupTheory.AbelianLocallyQuaternionProductKourovka18Problem95Wanted.abelianLocallyQuaternionProductSoluble_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AbelianLocallyQuaternionProductKourovka18Problem95Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AbelianLocallyQuaternionProductKourovka18Problem95Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-abelian-and-locally-quaternion-group/index.html#abelian-locally-quaternion-product-solub-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Products of abelian and locally quaternion groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-abelian-and-locally-quaternion-group/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-abelian-and-locally-quaternion-group)
