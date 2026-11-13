---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.CountablyManyRightOrdersKourovka16Problem51Wanted.rightOrders, MathlibExt.GroupTheory.CountablyManyRightOrdersKourovka16Problem51Wanted.existsCountablyInfinitelyRightOrderable, MathlibExt.GroupTheory.CountablyManyRightOrdersKourovka16Problem51Wanted.existsCountablyInfinitelyRightOrderable_refuted
statement: formalized
---

# Spaces of right orders

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/spaces-of-right-orders/index.html).

## Right orders of a group (Kourovka 16.51)

The right orders of a group $G$ are the linear
orders $\le$ on $G$ that are invariant under right multiplication: $a \le b$ implies $ac \le bc$ for
all $a, b, c \in G$.

Formalized by `MathlibExt.GroupTheory.CountablyManyRightOrdersKourovka16Problem51Wanted.rightOrders`, a definition declared in [WantedExt/GroupTheory/CountablyManyRightOrdersKourovka16Problem51Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CountablyManyRightOrdersKourovka16Problem51Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/spaces-of-right-orders/index.html#right-orders).

## Groups with countably infinitely many right orders (Kourovka 16.51)

The statement that
some group has a countably infinite set of right orders.

Formalized by `MathlibExt.GroupTheory.CountablyManyRightOrdersKourovka16Problem51Wanted.existsCountablyInfinitelyRightOrderable`, a definition declared in [WantedExt/GroupTheory/CountablyManyRightOrdersKourovka16Problem51Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CountablyManyRightOrdersKourovka16Problem51Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/spaces-of-right-orders/index.html#exists-countably-infinitely-right-ordera).

## No group has countably infinitely many right orders

For every group $G$, the set of right
orders on $G$ (linear orders $\le$ on $G$ such that $a \le b$ implies $ac \le bc$ for all
$a, b, c \in G$) is either finite or uncountable. That is, Kourovka Problem 16.51 has a negative
answer.

Linnell proves this for left orders, which correspond to right orders through
$a \le' b \iff b^{-1} \le a^{-1}$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.51 (V. M. Kopytov, N. Ya. Medvedev); resolution: P. A. Linnell, Bull. London Math. Soc. 43 (2011), 200-202; A. Clay, preprint, arXiv:0909.0273 (2009); A. Navas and C. Rivas, Algebr. Geom. Topol. 9 (2009), 2079-2100, Linnell, Theorem 1.3 (no group can be left-ordered in a countably infinite number of ways), based on A. V. Zenkov (1997, locally indicable groups); Clay, Corollary 3.10 (the set of left orderings of any group is finite or uncountable); the Kourovka Notebook (21st issue) marks 16.51 solved (No, there are no such groups), https://arxiv.org/abs/0909.0273.

Stated but not proved: `MathlibExt.GroupTheory.CountablyManyRightOrdersKourovka16Problem51Wanted.existsCountablyInfinitelyRightOrderable_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/CountablyManyRightOrdersKourovka16Problem51Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CountablyManyRightOrdersKourovka16Problem51Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/spaces-of-right-orders/index.html#exists-countably-infinitely-right-ordera-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spaces of right orders](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/spaces-of-right-orders/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orderable-groups/spaces-of-right-orders)
