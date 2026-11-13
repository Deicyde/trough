---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PeriodicSubgroupsInProductSetKourovka16Problem38Wanted.subgroupInPeriodicProductIsPeriodic, MathlibExt.GroupTheory.PeriodicSubgroupsInProductSetKourovka16Problem38Wanted.subgroupInPeriodicProductIsPeriodic_holds
statement: formalized
---

# Products of periodic subgroups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-periodic-subgroups/index.html).

## Kourovka Problem 16.38 (subgroups inside a product of periodic subgroups)

The statement,
posed by F. de Giovanni, that for every soluble group $G$ and all subgroups $A$ and $B$ of $G$ in
which every element has finite order, every subgroup $H$ of $G$ contained in the set $AB$ of all
products $ab$ with $a \in A$ and $b \in B$ has every element of finite order.

Formalized by `MathlibExt.GroupTheory.PeriodicSubgroupsInProductSetKourovka16Problem38Wanted.subgroupInPeriodicProductIsPeriodic`, a definition declared in [WantedExt/GroupTheory/PeriodicSubgroupsInProductSetKourovka16Problem38Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PeriodicSubgroupsInProductSetKourovka16Problem38Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-periodic-subgroups/index.html#subgroup-in-periodic-product-is-periodic).

## Subgroups inside a product of two periodic subgroups of a soluble group are periodic

Let $G$
be a soluble group and let $A$ and $B$ be subgroups of $G$ in which every element has finite order.
Then every subgroup $H$ of $G$ contained in the set $AB$ of all products $ab$ with $a \in A$ and
$b \in B$ is periodic: every element of $H$ has finite order. This answers Kourovka Problem 16.38
(F. de Giovanni) in the affirmative; the proof is due to Kinyon and Urban (Proposition 3.8).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.38 (F. de Giovanni); resolution: M. Kinyon and J. Urban (with Codex gpt-6-astra), Results on problems from the Kourovka Notebook, preprint, version 4 (19 September 2026), Proposition 3.8 (if G is soluble and A, B ≤ G are periodic, every subgroup contained in the set AB is periodic); the Kourovka Notebook (21st issue) marks 16.38 solved (Yes, AI solution confirmed by B. Amberg), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.PeriodicSubgroupsInProductSetKourovka16Problem38Wanted.subgroupInPeriodicProductIsPeriodic_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PeriodicSubgroupsInProductSetKourovka16Problem38Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PeriodicSubgroupsInProductSetKourovka16Problem38Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-periodic-subgroups/index.html#subgroup-in-periodic-product-is-periodic-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Products of periodic subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-periodic-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/products-of-periodic-subgroups)
