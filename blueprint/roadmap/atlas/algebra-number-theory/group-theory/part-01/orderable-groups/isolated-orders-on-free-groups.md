---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.IsBiOrder, MathlibExt.GroupTheory.FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.freeGroupHasIsolatedBiOrder, MathlibExt.GroupTheory.FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.freeGroupHasIsolatedBiOrder_refuted
statement: formalized
---

# Isolated orders on free groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/isolated-orders-on-free-groups/index.html).

## Bi-invariant strict total orders on a group

A relation $r$ on a group $G$ is a bi-invariant
order if $r$ is a strict total order on $G$ (irreflexive, transitive and trichotomous) and
$r(a, b)$ implies $r(cad, cbd)$ for all $a, b, c, d \in G$.

Formalized by `MathlibExt.GroupTheory.FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.IsBiOrder`, a definition declared in [WantedExt/GroupTheory/FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/isolated-orders-on-free-groups/index.html#is-bi-order).

## Kourovka Problem 12.51 (isolated bi-orders of free groups)

The statement that for some
natural number $n \ge 2$ there is a finite subset $S$ of the free group $F_n$ on $n$ generators
such that exactly one bi-invariant strict total order $<$ on $F_n$ (a strict total order such that
$a < b$ implies $cad < cbd$ for all $a, b, c, d \in F_n$) makes every element of $S$ positive, that
is, satisfies $1 < s$ for all $s \in S$. Such an order is an isolated point of the space of
bi-orders of $F_n$.

Formalized by `MathlibExt.GroupTheory.FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.freeGroupHasIsolatedBiOrder`, a definition declared in [WantedExt/GroupTheory/FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/isolated-orders-on-free-groups/index.html#free-group-has-isolated-bi-order).

## No free group of finite rank at least 2 has an isolated bi-order

For every natural number
$n \ge 2$ and every finite subset $S$ of the free group $F_n$ on $n$ generators, it is not the case
that exactly one bi-invariant strict total order $<$ on $F_n$ (a strict total order such that
$a < b$ implies $cad < cbd$ for all $a, b, c, d \in F_n$) satisfies $1 < s$ for every $s \in S$.

Resolved false: the Kourovka Notebook (21st issue) marks 12.51 solved, "No, it does not". Muliarchyk
(arXiv:2403.14779) proves that a free product of bi-ordered groups admits no isolated bi-ordering;
$F_n$ is the free product of $n \ge 2$ copies of $\mathbb{Z}$ (see also Dovhyi and Muliarchyk,
Groups Geom. Dyn. 17 (2023)).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 12.51 (S. McCleary); resolution: K. Muliarchyk, Free products of bi-orderable groups, preprint (2024), arXiv:2403.14779; S. Dovhyi and K. Muliarchyk, Groups Geom. Dyn. 17 (2023), 613-632, Muliarchyk, main theorem: a free product of bi-ordered groups admits no isolated bi-ordering; the Kourovka Notebook (21st issue) marks 12.51 solved, https://arxiv.org/abs/2403.14779.

Stated but not proved: `MathlibExt.GroupTheory.FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.freeGroupHasIsolatedBiOrder_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupIsolatedBiOrderKourovka12Problem51Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/isolated-orders-on-free-groups/index.html#free-group-has-isolated-bi-order-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Isolated orders on free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/isolated-orders-on-free-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orderable-groups/isolated-orders-on-free-groups)
