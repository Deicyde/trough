---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OrderSpectrumSimpleGroupKourovka12Problem39Wanted.elementOrders, MathlibExt.GroupTheory.OrderSpectrumSimpleGroupKourovka12Problem39Wanted.simpleGroupRecognizedByOrderAndSpectrum, MathlibExt.GroupTheory.OrderSpectrumSimpleGroupKourovka12Problem39Wanted.simpleGroupRecognizedByOrderAndSpectrum_holds
statement: formalized
---

# Recognition by order and spectrum

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-by-order-and-spectrum/index.html).

## Set of element orders (Kourovka 12.39)

For a group $G$, the set of natural numbers that
occur as the order of some element of $G$, where an element of infinite order is counted as
having order $0$.

Formalized by `MathlibExt.GroupTheory.OrderSpectrumSimpleGroupKourovka12Problem39Wanted.elementOrders`, a definition declared in [WantedExt/GroupTheory/OrderSpectrumSimpleGroupKourovka12Problem39Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OrderSpectrumSimpleGroupKourovka12Problem39Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-by-order-and-spectrum/index.html#element-orders).

## Shi's conjecture on recognition by order and element orders (Kourovka 12.39)

The
statement that for every finite group $G$ and every finite simple group $S$, if $G$ and $S$ have
the same order and the same set of element orders, then $G$ is isomorphic to $S$.

Formalized by `MathlibExt.GroupTheory.OrderSpectrumSimpleGroupKourovka12Problem39Wanted.simpleGroupRecognizedByOrderAndSpectrum`, a definition declared in [WantedExt/GroupTheory/OrderSpectrumSimpleGroupKourovka12Problem39Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OrderSpectrumSimpleGroupKourovka12Problem39Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-by-order-and-spectrum/index.html#simple-group-recognized-by-order-and-spe).

## Finite simple groups are recognized by order and element orders

For every finite group $G$
and every finite simple group $S$, if $G$ and $S$ have the same order and the same set of element
orders, then $G$ is isomorphic to $S$. That is, Shi's conjecture (Kourovka Problem 12.39) holds.

Here a simple group may be cyclic of prime order. The Kourovka Archive records the answer "Yes,
they must", proved by Xu and Shi and by Vasil'ev, Grechkoseeva and Mazurov.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.39 (W. J. Shi; A. S. Kondratiev); resolution: M. C. Xu and W. J. Shi, Algebra Colloq. 10 (2003), 427-443; A. V. Vasil'ev, M. A. Grechkoseeva and V. D. Mazurov, Algebra Logic 48 (2009), 385-409, Kourovka Archive, Problem 12.39: Yes, they must.

Stated but not proved: `MathlibExt.GroupTheory.OrderSpectrumSimpleGroupKourovka12Problem39Wanted.simpleGroupRecognizedByOrderAndSpectrum_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OrderSpectrumSimpleGroupKourovka12Problem39Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OrderSpectrumSimpleGroupKourovka12Problem39Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-by-order-and-spectrum/index.html#simple-group-recognized-by-order-and-spe-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Recognition by order and spectrum](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-by-order-and-spectrum/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra/recognition-by-order-and-spectrum)
