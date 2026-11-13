---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ElementOrderSetRealizationsKourovka12Problem84Wanted.elementOrders, MathlibExt.GroupTheory.ElementOrderSetRealizationsKourovka12Problem84Wanted.twoRealizationsImplyInfinitelyMany, MathlibExt.GroupTheory.ElementOrderSetRealizationsKourovka12Problem84Wanted.twoRealizationsImplyInfinitelyMany_refuted, MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.elementOrders, MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.AtMostIsoClasses, MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.InfinitelyManyIsoClasses, MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.spectrumGroupCountBoundedOrInfinite, MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.spectrumGroupCountBoundedOrInfinite_refuted
statement: formalized
---

# Number of groups with a given spectrum

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html).

## The spectrum of a group (Kourovka 12.84)

The spectrum of a group $G$ is the set
$\{\operatorname{ord}(g) : g \in G\}$ of the orders of its elements, where an element of infinite
order is counted as having order $0$.

Formalized by `MathlibExt.GroupTheory.ElementOrderSetRealizationsKourovka12Problem84Wanted.elementOrders`, a definition declared in [WantedExt/GroupTheory/ElementOrderSetRealizationsKourovka12Problem84Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrderSetRealizationsKourovka12Problem84Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html#element-orders).

## Syskin's question on groups with a given spectrum (Kourovka 12.84)

The proposition that
for every set $\Omega$ of natural numbers, if two non-isomorphic finite groups both have set of
element orders $\Omega$, then for every natural number $k$ there are $k$ pairwise non-isomorphic
finite groups whose set of element orders is $\Omega$; that is, infinitely many.

Formalized by `MathlibExt.GroupTheory.ElementOrderSetRealizationsKourovka12Problem84Wanted.twoRealizationsImplyInfinitelyMany`, a definition declared in [WantedExt/GroupTheory/ElementOrderSetRealizationsKourovka12Problem84Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrderSetRealizationsKourovka12Problem84Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html#two-realizations-imply-infinitely-many).

## Two isospectral finite groups do not force infinitely many

There are a set $\Omega$ of
natural numbers and a natural number $k$ such that two non-isomorphic finite groups have set of
element orders $\Omega$, but there are no $k$ pairwise non-isomorphic finite groups whose set of
element orders is $\Omega$.

For example, by Theorem 2.1(iii) of the survey of Grechkoseeva, Mazurov, Shi, Vasil'ev and Yang,
the finite groups with the set of element orders of $S_6(2)$ are exactly $S_6(2)$ and
$O_8^+(2)$, which have different orders. The Kourovka Archive answers 12.84 "No, it is not"
(V. D. Mazurov, 1994).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.84 (well-known problem; S. A. Syskin); resolution: V. D. Mazurov, Algebra and Logic 33 (1994), no. 1, 49-55; M. A. Grechkoseeva, V. D. Mazurov, W. Shi, A. V. Vasil'ev and N. Yang, Finite groups isospectral to simple groups, arXiv:2111.15198, Kourovka Archive, Problem 12.84: No, it is not; Grechkoseeva et al., Theorem 2.1(iii): a finite group has the spectrum of S_6(2) if and only if it is S_6(2) or O_8^+(2), https://arxiv.org/abs/2111.15198.

Stated but not proved: `MathlibExt.GroupTheory.ElementOrderSetRealizationsKourovka12Problem84Wanted.twoRealizationsImplyInfinitelyMany_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ElementOrderSetRealizationsKourovka12Problem84Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrderSetRealizationsKourovka12Problem84Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html#two-realizations-imply-infinitely-many-r).

## Spectrum of a group (Kourovka 13.63)

For a group $G$, the spectrum $\pi_e(G)$ is the set
of orders of elements of $G$, where an element of infinite order counts as having order $0$.

Formalized by `MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.elementOrders`, a definition declared in [WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html#element-orders-2).

## At most $k$ isomorphism types with spectrum $\Gamma$

For a set $\Gamma$ of natural numbers
and a natural number $k$, this property holds when, for any finite groups $G_0, \dots, G_k$ (not
necessarily distinct) whose spectra $\pi_e(G_i)$ (the sets of orders of elements of $G_i$) all
equal $\Gamma$, there are indices $i \ne j$ with $G_i \cong G_j$.

This expresses $h(\Gamma) \le k$, where $h(\Gamma)$ is the number of isomorphism classes of finite
groups with spectrum $\Gamma$, without counting isomorphism classes directly.

Formalized by `MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.AtMostIsoClasses`, a definition declared in [WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html#at-most-iso-classes).

## Infinitely many isomorphism types with spectrum $\Gamma$

For a set $\Gamma$ of natural
numbers, this property holds when, for every natural number $n$, there are $n$ pairwise
non-isomorphic finite groups $G_0, \dots, G_{n-1}$ whose spectra $\pi_e(G_i)$ (the sets of orders
of elements of $G_i$) all equal $\Gamma$.

This expresses $h(\Gamma) = \infty$, where $h(\Gamma)$ is the number of isomorphism classes of
finite groups with spectrum $\Gamma$.

Formalized by `MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.InfinitelyManyIsoClasses`, a definition declared in [WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html#infinitely-many-iso-classes).

## Kourovka Problem 13.63 (bounded or infinite number of groups per spectrum)

The proposition,
asked about by W. J. Shi, that there is a natural number $k$ such that for every set $\Gamma$ of
natural numbers, either $h(\Gamma) \le k$ or $h(\Gamma) = \infty$, where $h(\Gamma)$ is the number
of isomorphism classes of finite groups $G$ whose spectrum $\pi_e(G)$ (set of element orders) is
$\Gamma$. Here $h(\Gamma) \le k$ means that among any $k + 1$ finite groups with spectrum $\Gamma$
two are isomorphic, and $h(\Gamma) = \infty$ means that for every $n$ there are $n$ pairwise
non-isomorphic finite groups with spectrum $\Gamma$.

Formalized by `MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.spectrumGroupCountBoundedOrInfinite`, a definition declared in [WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html#spectrum-group-count-bounded-or-infinite).

## No uniform bound on the number of groups with a given spectrum

For a set $\Gamma$ of natural
numbers, let $h(\Gamma)$ be the number of isomorphism classes of finite groups $G$ whose spectrum
$\pi_e(G)$ (set of element orders) is $\Gamma$; $h(\Gamma) \le k$ means that among any $k + 1$
finite groups with spectrum $\Gamma$ two are isomorphic, and $h(\Gamma) = \infty$ means that for
every $n$ there are $n$ pairwise non-isomorphic finite groups with spectrum $\Gamma$. Kourovka
Problem 13.63 has a negative answer: there is no natural number $k$ such that for every set
$\Gamma$ of natural numbers, either $h(\Gamma) \le k$ or $h(\Gamma) = \infty$.

Zavarnitsine proves $h(\pi_e(L_3(7^{3^r}))) = r + 1$ for every $r \ge 0$, where $L_3(q)$ is the
projective special linear group $\mathrm{PSL}_3(q)$, so $h$ takes every positive finite value and
no $k$ works.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.63 (W. J. Shi); resolution: A. V. Zavarnitsine, J. Group Theory 7 (2004), no. 1, 81-97, h(π_e(L_3(7^(3^r)))) = r + 1 for every r ≥ 0; Kourovka Archive, Problem 13.63 (answer: No, there is no such number).

Stated but not proved: `MathlibExt.GroupTheory.ElementOrderSpectrumCountKourovka13Problem63Wanted.spectrumGroupCountBoundedOrInfinite_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrderSpectrumCountKourovka13Problem63Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html#spectrum-group-count-bounded-or-infinite-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Number of groups with a given spectrum](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orders-and-spectra/number-of-groups-with-a-given-spectrum)
