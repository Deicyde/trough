---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NonconjugateMaximalSubgroupProductsKourovka10Problem34Wanted.nonsolubleProductOfNonconjugateMaximals, MathlibExt.GroupTheory.NonconjugateMaximalSubgroupProductsKourovka10Problem34Wanted.nonsolubleProductOfNonconjugateMaximals_refuted
statement: formalized
---

# Products of maximal subgroups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/products-of-maximal-subgroups/index.html).

## Non-soluble products of non-conjugate maximal subgroups (Kourovka 10.34, Monakhov)

The
statement that there is a finite group $G$ that is not soluble such that $G = MN$ for every two
maximal subgroups $M$ and $N$ of $G$ that are not conjugate in $G$. Here $MN$ is the set of
products $mn$ with $m \in M$ and $n \in N$.

Formalized by `MathlibExt.GroupTheory.NonconjugateMaximalSubgroupProductsKourovka10Problem34Wanted.nonsolubleProductOfNonconjugateMaximals`, a definition declared in [WantedExt/GroupTheory/NonconjugateMaximalSubgroupProductsKourovka10Problem34Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NonconjugateMaximalSubgroupProductsKourovka10Problem34Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/products-of-maximal-subgroups/index.html#nonsoluble-product-of-nonconjugate-maxim).

## Finite groups that are the product of every two non-conjugate maximal subgroups are soluble

There is no finite group $G$ that is not soluble such that $G = MN$ for every two maximal
subgroups $M$ and $N$ of $G$ that are not conjugate in $G$; here $MN$ is the set of products $mn$
with $m \in M$ and $n \in N$. This answers Kourovka Problem 10.34 in the negative.

Sater (arXiv:2608.02970) and Li and Yang (arXiv:2608.19478) prove that a finite group with this
property is soluble (the almost simple case is due to Tikhonenko and Tyutyanov, 2010). The
Kourovka Notebook (21st issue) marks 10.34 solved, "No, there are no such groups".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 10.34 (V. S. Monakhov); resolution: R. Sater, Finite groups that are the product of every pair of non-conjugate maximal subgroups are soluble, arXiv:2608.02970 (2026); J. Li and Y. Yang, Products of nonconjugate maximal subgroups, arXiv:2608.19478 (2026), main theorems: a finite group with MN = G for all non-conjugate maximal subgroups M, N is soluble; the Kourovka Notebook (21st issue) marks 10.34 solved, https://arxiv.org/abs/2608.19478.

Stated but not proved: `MathlibExt.GroupTheory.NonconjugateMaximalSubgroupProductsKourovka10Problem34Wanted.nonsolubleProductOfNonconjugateMaximals_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/NonconjugateMaximalSubgroupProductsKourovka10Problem34Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NonconjugateMaximalSubgroupProductsKourovka10Problem34Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/products-of-maximal-subgroups/index.html#nonsoluble-product-of-nonconjugate-maxim-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Products of maximal subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/products-of-maximal-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/products-of-maximal-subgroups)
