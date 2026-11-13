---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.augmentationIdeal, MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.MemDimensionSubgroup, MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.dimensionQuotientCentral, MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.dimensionQuotientExponentTwo, MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.dimensionQuotientCentral_refuted, MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.dimensionQuotientExponentTwo_refuted
statement: formalized
---

# Dimension subgroups

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/dimension-subgroups/index.html).

## Augmentation ideal of the integral group ring

For a group $G$, the augmentation ideal
$\Delta(G)$ of the integral group ring $\mathbb{Z}G$ is the $\mathbb{Z}$-submodule spanned by the
elements $g - 1$ for $g \in G$. It is the kernel of the augmentation map
$\mathbb{Z}G \to \mathbb{Z}$, $\sum_g a_g g \mapsto \sum_g a_g$.

Formalized by `MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.augmentationIdeal`, a definition declared in [WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/dimension-subgroups/index.html#augmentation-ideal).

## Dimension subgroups

Let $\Delta(G)$ be the augmentation ideal of the integral group ring
$\mathbb{Z}G$ of a group $G$, and for $n \in \mathbb{N}$ let $\Delta(G)^n$ be its $n$-th power, the
$\mathbb{Z}$-span of all products of $n$ elements of $\Delta(G)$. An element $g \in G$ lies in the
$n$-th dimension subgroup $D_n(G) = G \cap (1 + \Delta(G)^n)$ when $g - 1 \in \Delta(G)^n$.

Formalized by `MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.MemDimensionSubgroup`, a definition declared in [WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/dimension-subgroups/index.html#mem-dimension-subgroup).

## Gupta–Kuz'min centrality question (Kourovka 12.22(a))

The statement that for every group
$G$, every $n \ge 1$, every element $x$ of the $n$-th dimension subgroup $D_n(G)$ and every
$g \in G$, the commutator $x g x^{-1} g^{-1}$ lies in $\gamma_n(G)$, the $n$-th term of the lower
central series of $G$, indexed so that $\gamma_1(G) = G$ and
$\gamma_{k+1}(G) = [\gamma_k(G), G]$. Equivalently, the image of $D_n(G)$ in $G/\gamma_n(G)$ is
central.

Formalized by `MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.dimensionQuotientCentral`, a definition declared in [WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/dimension-subgroups/index.html#dimension-quotient-central).

## Gupta–Kuz'min exponent question (Kourovka 12.22(b))

The statement that for every group
$G$, every $n \ge 1$ and every element $x$ of the $n$-th dimension subgroup $D_n(G)$, the square
$x^2$ lies in $\gamma_n(G)$, the $n$-th term of the lower central series of $G$, indexed so that
$\gamma_1(G) = G$ and $\gamma_{k+1}(G) = [\gamma_k(G), G]$. Equivalently, the image of $D_n(G)$ in
$G/\gamma_n(G)$ has exponent dividing $2$.

Formalized by `MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.dimensionQuotientExponentTwo`, a definition declared in [WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/dimension-subgroups/index.html#dimension-quotient-exponent-two).

## Dimension quotients need not be central

There exist a group $G$, an integer $n \ge 1$, an
element $x$ of the $n$-th dimension subgroup $D_n(G)$ and an element $g \in G$ such that the
commutator $x g x^{-1} g^{-1}$ does not lie in $\gamma_n(G)$, the $n$-th term of the lower central
series of $G$ (indexed so that $\gamma_1(G) = G$). That is, the answer to Kourovka Problem 12.22(a)
is negative: the image of $D_n(G)$ in $G/\gamma_n(G)$ need not be central.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.22 (N. D. Gupta, Yu. V. Kuz'min); resolution: N. D. Gupta and Yu. V. Kuz'min, J. Pure Appl. Algebra 104, no. 1 (1995), 191-197 (part a); L. Bartholdi and R. Mikhailov, J. Topology 16, no. 2 (2023), 822-853 (part b), Kourovka Archive, Problem 12.22: "a) No, not always; moreover, `D_n(G)/γ_n(G)` need not be contained in any term of the upper central series of `G/γ_n(G)` with fixed number" and "b) No, not always", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.dimensionQuotientCentral_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/dimension-subgroups/index.html#dimension-quotient-central-refuted).

## Dimension quotients need not have exponent dividing 2

There exist a group $G$, an integer
$n \ge 1$ and an element $x$ of the $n$-th dimension subgroup $D_n(G)$ such that $x^2$ does not lie
in $\gamma_n(G)$, the $n$-th term of the lower central series of $G$ (indexed so that
$\gamma_1(G) = G$). That is, the answer to Kourovka Problem 12.22(b) is negative: the image of
$D_n(G)$ in $G/\gamma_n(G)$ need not have exponent dividing $2$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.22 (N. D. Gupta, Yu. V. Kuz'min); resolution: N. D. Gupta and Yu. V. Kuz'min, J. Pure Appl. Algebra 104, no. 1 (1995), 191-197 (part a); L. Bartholdi and R. Mikhailov, J. Topology 16, no. 2 (2023), 822-853 (part b), Kourovka Archive, Problem 12.22: "a) No, not always; moreover, `D_n(G)/γ_n(G)` need not be contained in any term of the upper central series of `G/γ_n(G)` with fixed number" and "b) No, not always", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.DimensionSubgroupLowerCentralKourovka12Problem22Wanted.dimensionQuotientExponentTwo_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DimensionSubgroupLowerCentralKourovka12Problem22Wanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/dimension-subgroups/index.html#dimension-quotient-exponent-two-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dimension subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/dimension-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/group-rings/dimension-subgroups)
