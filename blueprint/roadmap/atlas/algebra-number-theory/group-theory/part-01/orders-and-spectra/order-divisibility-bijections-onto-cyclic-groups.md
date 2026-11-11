---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OrderDivisibilityBijectionCyclicKourovka18Problem1Wanted.orderDivisibilityBijectionToCyclic, MathlibExt.GroupTheory.OrderDivisibilityBijectionCyclicKourovka18Problem1Wanted.orderDivisibilityBijectionToCyclic_holds
statement: formalized
---

# Order-divisibility bijections onto cyclic groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/order-divisibility-bijections-onto-cyclic-groups/index.html).

## Kourovka Problem 18.1 (statement)

The statement that for every finite group $G$, of order
$n$ say, there is a bijection $f$ from $G$ onto the cyclic group $\mathbb{Z}/n\mathbb{Z}$ such that
for every $x \in G$ the order of $x$ divides the additive order of $f(x)$.

Formalized by `MathlibExt.GroupTheory.OrderDivisibilityBijectionCyclicKourovka18Problem1Wanted.orderDivisibilityBijectionToCyclic`, a definition declared in [WantedExt/GroupTheory/OrderDivisibilityBijectionCyclicKourovka18Problem1Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OrderDivisibilityBijectionCyclicKourovka18Problem1Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/order-divisibility-bijections-onto-cyclic-groups/index.html#order-divisibility-bijection-to-cyclic).

## Amiri's theorem (Kourovka Problem 18.1)

For every finite group $G$, of order $n$ say, there is
a bijection $f$ from $G$ onto the cyclic group $\mathbb{Z}/n\mathbb{Z}$ such that for every
$x \in G$ the order of $x$ divides the additive order of $f(x)$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.1 (I. M. Isaacs); resolution: M. Amiri, J. Pure Appl. Algebra 228 (2024), no. 7, 107632 (preprint arXiv:2002.11455), abstract (for any finite group G of order n there is a bijection f from G onto C_n with o(x) | o(f(x)) for all x); the Kourovka Notebook (21st issue) marks 18.1 solved (Yes, it does), https://arxiv.org/abs/2002.11455.

Stated but not proved: `MathlibExt.GroupTheory.OrderDivisibilityBijectionCyclicKourovka18Problem1Wanted.orderDivisibilityBijectionToCyclic_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OrderDivisibilityBijectionCyclicKourovka18Problem1Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OrderDivisibilityBijectionCyclicKourovka18Problem1Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/order-divisibility-bijections-onto-cyclic-groups/index.html#order-divisibility-bijection-to-cyclic-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Order-divisibility bijections onto cyclic groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/order-divisibility-bijections-onto-cyclic-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra/order-divisibility-bijections-onto-cyclic-groups)
