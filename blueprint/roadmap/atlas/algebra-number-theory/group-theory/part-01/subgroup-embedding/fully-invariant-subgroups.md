---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FullyInvariantSubgroupsCyclicKourovka16Problem61Wanted.fullyInvariantSubgroupsOfEachOrderCyclic, MathlibExt.GroupTheory.FullyInvariantSubgroupsCyclicKourovka16Problem61Wanted.fullyInvariantSubgroupsOfEachOrderCyclic_refuted
statement: formalized
---

# Fully invariant subgroups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/fully-invariant-subgroups/index.html).

## MacHale's question on fully invariant subgroups (Kourovka 16.61)

The statement that every
finite group $G$ having, for every divisor $d$ of $|G|$, a fully invariant subgroup of order $d$
(a subgroup $H$ with $\varphi(H) \le H$ for every endomorphism $\varphi$ of $G$) is cyclic.

Formalized by `MathlibExt.GroupTheory.FullyInvariantSubgroupsCyclicKourovka16Problem61Wanted.fullyInvariantSubgroupsOfEachOrderCyclic`, a definition declared in [WantedExt/GroupTheory/FullyInvariantSubgroupsCyclicKourovka16Problem61Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullyInvariantSubgroupsCyclicKourovka16Problem61Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/fully-invariant-subgroups/index.html#fully-invariant-subgroups-of-each-order).

## Fully invariant subgroups of every order do not force cyclicity

Not every finite group $G$
having, for every divisor $d$ of $|G|$, a fully invariant subgroup of order $d$ (a subgroup $H$
with $\varphi(H) \le H$ for every endomorphism $\varphi$ of $G$) is cyclic.

The Kourovka Archive answers 16.61 "No" (Abdollahi): take $G = C_p \times C_{p^2}$, where $C_p$
and $C_{p^2}$ are cyclic $p$-groups of orders $p$ and $p^2$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.61 (D. MacHale); resolution: A. Abdollahi, letter of 4 March 2009, as recorded in the Kourovka Archive, Kourovka Archive, Problem 16.61 (No: G = C_p × C_{p²}).

Stated but not proved: `MathlibExt.GroupTheory.FullyInvariantSubgroupsCyclicKourovka16Problem61Wanted.fullyInvariantSubgroupsOfEachOrderCyclic_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FullyInvariantSubgroupsCyclicKourovka16Problem61Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullyInvariantSubgroupsCyclicKourovka16Problem61Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/fully-invariant-subgroups/index.html#fully-invariant-subgroups-of-each-order-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fully invariant subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/fully-invariant-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/subgroup-embedding/fully-invariant-subgroups)
