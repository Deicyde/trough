---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.elementOrders, MathlibExt.GroupTheory.SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.IsSubgroupOrNormalSectionOf, MathlibExt.GroupTheory.SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.sameSpectrumIncomparableGroups, MathlibExt.GroupTheory.SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.sameSpectrumIncomparableGroups_holds
statement: formalized
---

# Finite groups with the same spectrum

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/finite-groups-with-the-same-spectrum/index.html).

## Element-order spectrum of a group

The spectrum $\pi_e(G)$ of a group $G$ is the set of
orders of the elements of $G$, where an element of infinite order counts as having order $0$.

Formalized by `MathlibExt.GroupTheory.SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.elementOrders`, a definition declared in [WantedExt/GroupTheory/SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/finite-groups-with-the-same-spectrum/index.html#element-orders).

## Subgroup or quotient of a normal subgroup

For groups $A$ and $B$, the statement that $A$
is isomorphic to a subgroup of $B$ or to a quotient of a normal subgroup of $B$: there is an
injective homomorphism $A \to B$, or there are a normal subgroup $N$ of $B$ and a surjective
homomorphism $N \to A$.

Formalized by `MathlibExt.GroupTheory.SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.IsSubgroupOrNormalSectionOf`, a definition declared in [WantedExt/GroupTheory/SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/finite-groups-with-the-same-spectrum/index.html#is-subgroup-or-normal-section-of).

## Finite groups with equal spectra, neither a subgroup or normal-subgroup quotient of the other (problem)

**Finite groups with equal spectra, neither a subgroup or normal-subgroup quotient of the
other (problem).** The statement that there exist finite groups $G_1$ and $G_2$ with the same
spectrum $\pi_e(G_1) = \pi_e(G_2)$ (the set of orders of elements), such that every finite group
with spectrum $\pi_e(G_1)$ has order at most some fixed bound $B$, and such that neither of $G_1$,
$G_2$ is isomorphic to a subgroup or to a quotient of a normal subgroup of the other.

This is Kourovka Notebook Problem 16.106 (W. J. Shi), which asks for $h(\pi_e(G_1)) < \infty$,
where $h(\Gamma)$ is the number of finite groups with spectrum $\Gamma$ up to isomorphism; the
bound on orders is equivalent, since there are finitely many groups of each order.

Formalized by `MathlibExt.GroupTheory.SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.sameSpectrumIncomparableGroups`, a definition declared in [WantedExt/GroupTheory/SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/finite-groups-with-the-same-spectrum/index.html#same-spectrum-incomparable-groups).

## Finite groups with equal spectra, neither a subgroup or normal-subgroup quotient of the other (Kourovka 16.106)

**Finite groups with equal spectra, neither a subgroup or normal-subgroup quotient of the other
(Kourovka 16.106).** There exist finite groups $G_1$ and $G_2$ such that:

- $G_1$ and $G_2$ have the same spectrum, where the spectrum $\pi_e(G)$ of a group $G$ is the set
  of orders of its elements;
- there is a bound $B$ such that every finite group $G$ with $\pi_e(G) = \pi_e(G_1)$ has order at
  most $B$;
- $G_1$ is not isomorphic to a subgroup of $G_2$ or to a quotient of a normal subgroup of $G_2$,
  and $G_2$ is not isomorphic to a subgroup of $G_1$ or to a quotient of a normal subgroup of $G_1$.

The bound on orders says that only finitely many finite groups have spectrum $\pi_e(G_1)$, up to
isomorphism. The Kourovka Archive gives the example $G_1 = L_{15}(2^{60}).3$ and
$G_2 = L_{15}(2^{60}).5$ (Grechkoseeva).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.106 (W. J. Shi); resolution: M. A. Grechkoseeva, Algebra and Logic 47 (2008), no. 4, 229-241, Kourovka Archive, Problem 16.106 (answer: Yes, there do, for example G₁ = L₁₅(2⁶⁰).3 and G₂ = L₁₅(2⁶⁰).5).

Stated but not proved: `MathlibExt.GroupTheory.SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.sameSpectrumIncomparableGroups_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SameSpectrumIncomparableGroupsKourovka16Problem106Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/finite-groups-with-the-same-spectrum/index.html#same-spectrum-incomparable-groups-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite groups with the same spectrum](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/finite-groups-with-the-same-spectrum/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orders-and-spectra/finite-groups-with-the-same-spectrum)
