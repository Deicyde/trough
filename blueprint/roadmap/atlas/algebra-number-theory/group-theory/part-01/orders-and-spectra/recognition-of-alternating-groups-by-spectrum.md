---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.elementOrders, MathlibExt.GroupTheory.AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.alternatingGroupRecognizableBySpectrum, MathlibExt.GroupTheory.AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.alternatingGroupRecognizableBySpectrum_holds, MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.spectrum, MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.IsCompositionSeries, MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.IsNonabelianFactor, MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.alternatingSpectrumOneNonabelianFactor, MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.alternatingSpectrumOneNonabelianFactor_holds
statement: formalized
---

# Recognition of alternating groups by spectrum

10 results, 7 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html).

## Spectrum of a group

The spectrum $\pi_e(G)$ of a group $G$ is the set of orders of the
elements of $G$, where an element of infinite order is assigned order $0$.

Formalized by `MathlibExt.GroupTheory.AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.elementOrders`, a definition declared in [WantedExt/GroupTheory/AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#element-orders).

## Kourovka Problem 16.107 on recognition of alternating groups by spectrum

This proposition
asserts that there is a natural number $N$ such that for every $n \ge N$, every finite group $G$
with the same spectrum (set of element orders) as the alternating group $A_n$ is isomorphic to
$A_n$.

Formalized by `MathlibExt.GroupTheory.AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.alternatingGroupRecognizableBySpectrum`, a definition declared in [WantedExt/GroupTheory/AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#alternating-group-recognizable-by-spectr).

## Large alternating groups are recognizable by spectrum

There is a natural number $N$ such that
for every $n \ge N$, every finite group $G$ whose set of element orders equals that of the
alternating group $A_n$ is isomorphic to $A_n$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.107 (W. J. Shi); resolution: I. B. Gorshkov, Recognizability of alternating groups by spectrum, Algebra and Logic 52 (2013), no. 1, 41-45, arXiv:1302.4825, abstract (the simple alternating groups Aₙ are recognizable by spectrum for n ≠ 6, 10); Kourovka Archive, Problem 16.107 (answer: Yes, it is), https://arxiv.org/abs/1302.4825.

Stated but not proved: `MathlibExt.GroupTheory.AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.alternatingGroupRecognizableBySpectrum_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlternatingGroupSpectrumRecognitionKourovka16Problem107Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#alternating-group-recognizable-by-spectr-2).

## Spectrum of a group

The spectrum $\omega(G)$ of a group $G$ is the set of natural numbers
that are orders of elements of $G$, where an element of infinite order is assigned order $0$.

Formalized by `MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.spectrum`, a definition declared in [WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#spectrum).

## Finite composition series

Let $G$ be a group and $m$ a natural number. A sequence
$s_0, s_1, \dots, s_m$ of subgroups of $G$ is a composition series of length $m$ if $s_0$ is the
trivial subgroup, $s_m = G$, and for each $i < m$ the subgroup $s_i$ is a normal subgroup of
$s_{i+1}$ and the quotient $s_{i+1}/s_i$ is a simple group.

Formalized by `MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.IsCompositionSeries`, a definition declared in [WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#is-composition-series).

## Non-abelian factor of a chain of subgroups

Let $G$ be a group, let $s_0, s_1, \dots, s_m$
be subgroups of $G$, and let $i < m$. The $i$-th factor of the chain is non-abelian if
$s_i \cap s_{i+1}$ is a normal subgroup of $s_{i+1}$ and the quotient group
$s_{i+1}/(s_i \cap s_{i+1})$ is non-abelian, that is, it has elements $x, y$ with $xy \ne yx$.
When $s_i \le s_{i+1}$, this quotient is $s_{i+1}/s_i$.

Formalized by `MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.IsNonabelianFactor`, a definition declared in [WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#is-nonabelian-factor).

## Kourovka Problem 16.27 (statement)

The statement that for every natural number $n$ and
every finite group $G$ whose spectrum, the set of orders of its elements, equals the spectrum of
the alternating group $A_n$, every composition series of $G$ has at most one non-abelian factor.

The problem was posed by A. V. Vasil'ev and V. D. Mazurov.

Formalized by `MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.alternatingSpectrumOneNonabelianFactor`, a definition declared in [WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#alternating-spectrum-one-nonabelian-fact).

## Groups isospectral to an alternating group (Kourovka Problem 16.27)

Let $n$ be a natural
number and let $G$ be a finite group whose spectrum, the set of orders of its elements, equals the
spectrum of the alternating group $A_n$. Then every composition series of $G$ has at most one
non-abelian factor.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.27 (A. V. Vasil'ev and V. D. Mazurov); resolution: I. B. Gorshkov, Algebra and Logic 52 (2013), no. 1, 41-45, Kourovka Archive, Problem 16.27 (Yes, it is).

Stated but not proved: `MathlibExt.GroupTheory.AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.alternatingSpectrumOneNonabelianFactor_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlternatingSpectrumCompositionFactorsKourovka16Problem27Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#alternating-spectrum-one-nonabelian-fact-2).

## Kourovka Problem 19.80 ($OC_7$-groups)

The proposition, asked by W. J. Shi, that every
$OC_7$-group, that is, every group whose set of element orders is exactly $\{1, 2, \dots, 7\}$
(such a group is periodic), is isomorphic to the alternating group $A_7$.

Formalized by `MathlibExt.GroupTheory.ElementOrdersOneToSevenAlternatingKourovka19Problem80Wanted.ocSevenGroupIsAlternating`, a definition declared in [WantedExt/GroupTheory/ElementOrdersOneToSevenAlternatingKourovka19Problem80Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrdersOneToSevenAlternatingKourovka19Problem80Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#oc-seven-group-is-alternating).

## Groups with element orders $1$ to $7$ are isomorphic to $A_7$

Every group, finite or
infinite, whose set of element orders is exactly $\{1, 2, \dots, 7\}$ is isomorphic to the
alternating group $A_7$. This answers Kourovka Problem 19.80 positively (Mamontov and Jabara).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.80 (W. J. Shi); resolution: A. S. Mamontov and E. Jabara, Recognizing A₇ by its set of element orders, Siberian Math. J. 62 (2021), no. 1, 93-104, doi:10.1134/S0037446621010109, Kourovka Archive, Problem 19.80: Yes, it is true, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.ElementOrdersOneToSevenAlternatingKourovka19Problem80Wanted.ocSevenGroupIsAlternating_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ElementOrdersOneToSevenAlternatingKourovka19Problem80Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ElementOrdersOneToSevenAlternatingKourovka19Problem80Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html#oc-seven-group-is-alternating-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Recognition of alternating groups by spectrum](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orders-and-spectra/recognition-of-alternating-groups-by-spectrum)
