---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.HasSubsetFactorization, MathlibExt.GroupTheory.SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.subsetFactorizationCounterexampleEveryLength, MathlibExt.GroupTheory.SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.subsetFactorizationCounterexampleEveryLength_holds
statement: formalized
---

# Factorizations of groups into subsets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/factorizations-of-groups-into-subsets/index.html).

## Factorization of a group into subsets of given sizes

Let $G$ be a group, $k$ a natural
number and $a_0, \dots, a_{k-1}$ natural numbers. The group $G$ has a subset factorization of
type $(a_0, \dots, a_{k-1})$ when there are finite subsets $A_0, \dots, A_{k-1}$ of $G$ with
$|A_i| = a_i$ for every $i$ such that $G = A_0 A_1 \cdots A_{k-1}$, that is, every $g \in G$ can be
written as $g = x_0 x_1 \cdots x_{k-1}$ with $x_i \in A_i$ for every $i$.

Formalized by `MathlibExt.GroupTheory.SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.HasSubsetFactorization`, a definition declared in [WantedExt/GroupTheory/SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/factorizations-of-groups-into-subsets/index.html#has-subset-factorization).

## Kourovka Problem 19.35: counterexamples to subset factorization of every length

The
statement that for every natural number $k \ge 3$ there are a finite group $G$ and natural numbers
$a_0, \dots, a_{k-1}$, each at least $2$, with $a_0 a_1 \cdots a_{k-1} = |G|$, such that $G$ has
no subset factorization of type $(a_0, \dots, a_{k-1})$: there are no subsets
$A_0, \dots, A_{k-1}$ of $G$ with $|A_i| = a_i$ for every $i$ and $G = A_0 A_1 \cdots A_{k-1}$.

Formalized by `MathlibExt.GroupTheory.SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.subsetFactorizationCounterexampleEveryLength`, a definition declared in [WantedExt/GroupTheory/SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/factorizations-of-groups-into-subsets/index.html#subset-factorization-counterexample-ever).

## Finite groups without subset factorizations exist for every length

For every natural number
$k \ge 3$ there are a finite group $G$ and natural numbers $a_0, \dots, a_{k-1}$, each at least
$2$, with $a_0 a_1 \cdots a_{k-1} = |G|$, such that there are no subsets $A_0, \dots, A_{k-1}$ of
$G$ with $|A_i| = a_i$ for every $i$ and $G = A_0 A_1 \cdots A_{k-1}$, that is, with every element
of $G$ a product $x_0 x_1 \cdots x_{k-1}$ where $x_i \in A_i$ for every $i$.

In McCulloch's Theorem 2.3, $G$ is a Frobenius group of order $2^{k-1}(2^{k-1} - 1)$ and the
factors are $(2, \dots, 2, 2^{k-1} - 1, 2)$; the case $k = 3$ is Bergman's example in the
alternating group $A_4$. This answers Kourovka Problem 19.35 (M. H. Hooshmand) in the negative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.35 (M. H. Hooshmand); resolution: R. McCulloch, Some answers regarding factorizations of finite groups, arXiv:2607.20569 (2026); counterexamples first given by M. Kabenyuk, Factorizations of finite groups, arXiv:2102.08605, Kourovka Archive, Problem 19.35: No (Bergman's A4 example for k = 3); counterexamples for all k ≥ 3 are constructed in (McCulloch); paper, Theorem 2.3: the Frobenius group of order 2^(k-1)(2^(k-1) - 1) has no k-fold factorization for (2, …, 2, 2^(k-1) - 1, 2), https://arxiv.org/abs/2607.20569.

Stated but not proved: `MathlibExt.GroupTheory.SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.subsetFactorizationCounterexampleEveryLength_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SubsetFactorizationCounterexamplesKourovka19Problem35Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/factorizations-of-groups-into-subsets/index.html#subset-factorization-counterexample-ever-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Factorizations of groups into subsets](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/factorizations-of-groups-into-subsets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/combinatorics-in-groups/factorizations-of-groups-into-subsets)
