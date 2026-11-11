---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PSLExtensionNewElementOrderKourovka14Problem60Wanted.PSL, MathlibExt.GroupTheory.PSLExtensionNewElementOrderKourovka14Problem60Wanted.extensionOfPSLHasNewElementOrder, MathlibExt.GroupTheory.PSLExtensionNewElementOrderKourovka14Problem60Wanted.extensionOfPSLHasNewElementOrder_holds
statement: formalized
---

# Element orders of extensions of projective linear groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/element-orders-of-extensions-of-projective-linea/index.html).

## Projective special linear group

For a natural number $n$ and a field $F$,
$\mathrm{PSL}_n(F)$ is the quotient $\mathrm{SL}_n(F)/Z(\mathrm{SL}_n(F))$ of the special linear
group $\mathrm{SL}_n(F)$ of $n \times n$ matrices over $F$ with determinant $1$ by its centre.

Formalized by `MathlibExt.GroupTheory.PSLExtensionNewElementOrderKourovka14Problem60Wanted.PSL`, an abbreviation declared in [WantedExt/GroupTheory/PSLExtensionNewElementOrderKourovka14Problem60Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PSLExtensionNewElementOrderKourovka14Problem60Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/element-orders-of-extensions-of-projective-linea/index.html#psl).

## Kourovka 14.60: new element orders in extensions of projective special linear groups

The proposition that for every $n \ge 3$, every prime $p$ and every $k \ge 1$, with $q = p^k$ and
$\mathbb{F}_q$ the field with $q$ elements, the following holds: whenever $H$ is a nontrivial normal
subgroup of a finite group $G$ and $G/H$ is isomorphic to the projective special linear group
$\mathrm{PSL}_n(\mathbb{F}_q)$, some element of $G$ has an order that is not the order of any
element of $G/H$.

Formalized by `MathlibExt.GroupTheory.PSLExtensionNewElementOrderKourovka14Problem60Wanted.extensionOfPSLHasNewElementOrder`, a definition declared in [WantedExt/GroupTheory/PSLExtensionNewElementOrderKourovka14Problem60Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PSLExtensionNewElementOrderKourovka14Problem60Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/element-orders-of-extensions-of-projective-linea/index.html#extension-of-pslhas-new-element-order).

## Extensions of PSL have a new element order

Resolved true: the Kourovka Archive answers 14.60 "Yes, it is true": Zavarnitsine proved it for `n ≠
4` and Grechkoseeva and Skresanov for `n = 4` (the editors note that an earlier claim of failure for
`n = 4` was erroneous). Source: E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group
Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems,
Problem 14.60 (V. D. Mazurov); resolution: A. V. Zavarnitsine, Siberian Math. J. 49 (2008), 246-256
(n ≠ 4); M. A. Grechkoseeva and S. V. Skresanov, Siberian Electron. Math. Rep. 17 (2020), 585-589 (n
= 4), Kourovka Archive, Problem 14.60 (answer: Yes, it is true; the editors note that an earlier
claim of failure for n = 4 was erroneous).

Stated but not proved: `MathlibExt.GroupTheory.PSLExtensionNewElementOrderKourovka14Problem60Wanted.extensionOfPSLHasNewElementOrder_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PSLExtensionNewElementOrderKourovka14Problem60Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PSLExtensionNewElementOrderKourovka14Problem60Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/element-orders-of-extensions-of-projective-linea/index.html#extension-of-pslhas-new-element-order-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Element orders of extensions of projective linear groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/element-orders-of-extensions-of-projective-linea/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra/element-orders-of-extensions-of-projective-linea)
