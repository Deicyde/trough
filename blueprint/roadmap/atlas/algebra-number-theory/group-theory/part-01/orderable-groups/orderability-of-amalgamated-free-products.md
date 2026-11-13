---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.IsRightOrderable, MathlibExt.GroupTheory.AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.amalgamOfOrderedGroupsRightOrderable, MathlibExt.GroupTheory.AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.amalgamOfOrderedGroupsRightOrderable_holds
statement: formalized
---

# Orderability of amalgamated free products

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-amalgamated-free-products/index.html).

## Right-orderable group

A group $G$ is right-orderable if it admits a linear order $\le$
that is invariant under right multiplication: $a \le b$ implies $ac \le bc$ for all
$a, b, c \in G$.

Formalized by `MathlibExt.GroupTheory.AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.IsRightOrderable`, a definition declared in [WantedExt/GroupTheory/AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-amalgamated-free-products/index.html#is-right-orderable).

## Kourovka Problem 15.34 (statement)

The statement that for every family $(G_i)_{i \in I}$
of groups, each with a linear order invariant under multiplication on both sides, every group $H$
with such a linear order, and all strictly increasing group homomorphisms
$\varphi_i \colon H \to G_i$, the free product of the $G_i$ with $H$ amalgamated along the maps
$\varphi_i$ is right-orderable.

The problem was posed by V. V. Bludov.

Formalized by `MathlibExt.GroupTheory.AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.amalgamOfOrderedGroupsRightOrderable`, a definition declared in [WantedExt/GroupTheory/AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-amalgamated-free-products/index.html#amalgam-of-ordered-groups-right-orderabl).

## Bludov–Glass theorem (Kourovka Problem 15.34)

Let $(G_i)_{i \in I}$ be a family of groups,
each with a linear order invariant under multiplication on both sides ($a \le b$ implies
$ca \le cb$ and $ac \le bc$), let $H$ be a group with such a linear order, and for each $i$ let
$\varphi_i \colon H \to G_i$ be a strictly increasing group homomorphism. Then the free product of
the $G_i$ with $H$ amalgamated along the maps $\varphi_i$ is right-orderable: it admits a linear
order such that $a \le b$ implies $ac \le bc$ for all $a, b, c$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.34 (V. V. Bludov); resolution: V. V. Bludov and A. M. W. Glass, On free products of right ordered groups with amalgamated subgroups, Math. Proc. Cambridge Philos. Soc. 146 (2009), 591-601, main theorem (the free product of ordered groups G₁, G₂ with subgroups amalgamated via an order-preserving isomorphism is right orderable; extended to arbitrary families); Kourovka Archive, Problem 15.34 (answer: Yes, it is).

Stated but not proved: `MathlibExt.GroupTheory.AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.amalgamOfOrderedGroupsRightOrderable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AmalgamatedOrderedGroupsRightOrderableKourovka15Problem34Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-amalgamated-free-products/index.html#amalgam-of-ordered-groups-right-orderabl-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orderability of amalgamated free products](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-amalgamated-free-products/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orderable-groups/orderability-of-amalgamated-free-products)
