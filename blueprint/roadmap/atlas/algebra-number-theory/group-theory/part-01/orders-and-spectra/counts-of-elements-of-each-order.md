---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ElementOrderCountPrimePowerKourovka18Problem112Wanted.elementOrderCountPrimePowerOrders, MathlibExt.GroupTheory.ElementOrderCountPrimePowerKourovka18Problem112Wanted.elementOrderCountPrimePowerOrders_holds
statement: formalized
---

# Counts of elements of each order

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/counts-of-elements-of-each-order/index.html).

## Shi's question on element-order counts (Kourovka 18.112)

The proposition that if a
finite group $G$ has the property that, for every divisor $d > 1$ of $|G|$ and every subgroup $H$
of $G$ whose order is coprime to $d$, $|H|$ divides the number of elements of $G$ of order $d$,
then every non-identity element of $G$ has prime-power order.

Formalized by `MathlibExt.GroupTheory.ElementOrderCountPrimePowerKourovka18Problem112Wanted.elementOrderCountPrimePowerOrders`, a definition declared in [WantedExt/GroupTheory/ElementOrderCountPrimePowerKourovka18Problem112Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ElementOrderCountPrimePowerKourovka18Problem112Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/counts-of-elements-of-each-order/index.html#element-order-count-prime-power-orders).

## Counting elements of each order forces prime-power orders

Let $G$ be a finite group such
that for every divisor $d > 1$ of $|G|$ and every subgroup $H$ of $G$ whose order is coprime to
$d$, the order $|H|$ divides the number of elements of $G$ of order $d$. Then every non-identity
element of $G$ has prime-power order.

Buturlakin, Shen and Shi proved this in 2017, answering Kourovka Problem 18.112 (W. J. Shi); the
Kourovka Archive answers 18.112 "Yes, it is true".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.112 (W. J. Shi); resolution: A. A. Buturlakin, R. Shen and W. Shi, Siberian Math. J. 58 (2017), 405-407, Kourovka Archive, Problem 18.112 (Yes, it is true).

Stated but not proved: `MathlibExt.GroupTheory.ElementOrderCountPrimePowerKourovka18Problem112Wanted.elementOrderCountPrimePowerOrders_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ElementOrderCountPrimePowerKourovka18Problem112Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ElementOrderCountPrimePowerKourovka18Problem112Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/counts-of-elements-of-each-order/index.html#element-order-count-prime-power-orders-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counts of elements of each order](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/counts-of-elements-of-each-order/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra/counts-of-elements-of-each-order)
