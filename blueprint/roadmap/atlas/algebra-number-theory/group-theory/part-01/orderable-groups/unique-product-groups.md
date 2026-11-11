---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.UniqueProductNotLeftOrderableKourovka15Problem49Wanted.IsLeftOrderable, MathlibExt.GroupTheory.UniqueProductNotLeftOrderableKourovka15Problem49Wanted.uniqueProductGroupNotLeftOrderable, MathlibExt.GroupTheory.UniqueProductNotLeftOrderableKourovka15Problem49Wanted.uniqueProductGroupNotLeftOrderable_holds
statement: formalized
---

# Unique product groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/unique-product-groups/index.html).

## Left-orderable groups

A group $G$ is left-orderable if it admits a linear order $\le$ such
that $a \le b$ implies $ca \le cb$ for all $a, b, c \in G$.

Formalized by `MathlibExt.GroupTheory.UniqueProductNotLeftOrderableKourovka15Problem49Wanted.IsLeftOrderable`, a definition declared in [WantedExt/GroupTheory/UniqueProductNotLeftOrderableKourovka15Problem49Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UniqueProductNotLeftOrderableKourovka15Problem49Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/unique-product-groups/index.html#is-left-orderable).

## Kourovka Problem 15.49 (unique product groups and left orders)

The statement, asked by
P. Linnell, that there exists a group $G$ with unique products that is not left-orderable. Here $G$
has unique products if for all finite nonempty subsets $X, Y \subseteq G$ there are $x_0 \in X$ and
$y_0 \in Y$ such that $(x_0, y_0)$ is the only pair $(x, y) \in X \times Y$ with $xy = x_0 y_0$.

Formalized by `MathlibExt.GroupTheory.UniqueProductNotLeftOrderableKourovka15Problem49Wanted.uniqueProductGroupNotLeftOrderable`, a definition declared in [WantedExt/GroupTheory/UniqueProductNotLeftOrderableKourovka15Problem49Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UniqueProductNotLeftOrderableKourovka15Problem49Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/unique-product-groups/index.html#unique-product-group-not-left-orderable).

## A unique product group need not be left-orderable

There exists a group $G$ that has unique
products but is not left-orderable: for all finite nonempty subsets $X, Y \subseteq G$ there are
$x_0 \in X$ and $y_0 \in Y$ such that $(x_0, y_0)$ is the only pair $(x, y) \in X \times Y$ with
$xy = x_0 y_0$, and yet $G$ admits no linear order invariant under left multiplication.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.49 (P. Linnell); resolution: N. Dunfield, Appendix B in S. Kionke and J. Raimbault, On geometric aspects of diffuse groups, Doc. Math. 21 (2016), 873-915, arXiv:1411.6449, Section 2.2 and the appendix (diffuse groups have unique products, by Bowditch's observation; the appendix gives a compact hyperbolic 3-manifold group that is diffuse but not left-orderable); Kourovka Archive, Problem 15.49 (answer: Yes, there does), https://arxiv.org/abs/1411.6449.

Stated but not proved: `MathlibExt.GroupTheory.UniqueProductNotLeftOrderableKourovka15Problem49Wanted.uniqueProductGroupNotLeftOrderable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/UniqueProductNotLeftOrderableKourovka15Problem49Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UniqueProductNotLeftOrderableKourovka15Problem49Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/unique-product-groups/index.html#unique-product-group-not-left-orderable-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unique product groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/unique-product-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orderable-groups/unique-product-groups)
