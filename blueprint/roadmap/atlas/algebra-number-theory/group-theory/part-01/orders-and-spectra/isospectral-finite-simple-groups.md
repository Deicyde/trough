---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.spectrum, MathlibExt.GroupTheory.ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.threeIsospectralSimpleGroups, MathlibExt.GroupTheory.ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.threeIsospectralSimpleGroups_refuted
statement: formalized
---

# Isospectral finite simple groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/isospectral-finite-simple-groups/index.html).

## Spectrum of a group

The spectrum $\omega(G)$ of a group $G$ is the set of orders of its
elements, where an element of infinite order is counted as having order $0$.

Formalized by `MathlibExt.GroupTheory.ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.spectrum`, a definition declared in [WantedExt/GroupTheory/ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/isospectral-finite-simple-groups/index.html#spectrum).

## Three isospectral finite simple groups

Kourovka 16.25 (A. V. Vasil'ev): there are three pairwise non-isomorphic finite non-abelian
simple groups with the same spectrum.

Formalized by `MathlibExt.GroupTheory.ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.threeIsospectralSimpleGroups`, a definition declared in [WantedExt/GroupTheory/ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/isospectral-finite-simple-groups/index.html#three-isospectral-simple-groups).

## No three non-isomorphic finite non-abelian simple groups are isospectral

There do not exist
three pairwise non-isomorphic finite non-abelian simple groups $G_1, G_2, G_3$ with
$\omega(G_1) = \omega(G_2) = \omega(G_3)$, where the spectrum $\omega(G)$ of a group $G$ is the
set of orders of its elements.

This answers Kourovka Problem 16.25 (A. V. Vasil'ev) in the negative; the Kourovka Archive cites
Buturlakin (2010).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.25 (A. V. Vasil'ev); resolution: A. A. Buturlakin, Sib. Èlektron. Mat. Izv. 7 (2010), 111-114, Kourovka Archive, Problem 16.25 (No).

Stated but not proved: `MathlibExt.GroupTheory.ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.threeIsospectralSimpleGroups_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ThreeIsospectralSimpleGroupsKourovka16Problem25Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/isospectral-finite-simple-groups/index.html#three-isospectral-simple-groups-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Isospectral finite simple groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/isospectral-finite-simple-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra/isospectral-finite-simple-groups)
