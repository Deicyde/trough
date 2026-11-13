---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.CentralizerLatticeModularKourovka11Problem4Wanted.IsCentralizer, MathlibExt.GroupTheory.CentralizerLatticeModularKourovka11Problem4Wanted.centralizerSublatticeModular, MathlibExt.GroupTheory.CentralizerLatticeModularKourovka11Problem4Wanted.centralizerSublatticeModular_refuted
statement: formalized
---

# Lattices of centralizers

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/lattices-of-centralizers/index.html).

## Centralizer subgroups

A subgroup $H$ of a group $G$ is a centralizer if $H = C_G(X)$ for
some subset $X \subseteq G$, where $C_G(X)$ is the subgroup of elements of $G$ that commute with
every element of $X$.

Formalized by `MathlibExt.GroupTheory.CentralizerLatticeModularKourovka11Problem4Wanted.IsCentralizer`, a definition declared in [WantedExt/GroupTheory/CentralizerLatticeModularKourovka11Problem4Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CentralizerLatticeModularKourovka11Problem4Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/lattices-of-centralizers/index.html#is-centralizer).

## Modularity of centralizer sublattices (Kourovka 11.4)

Call a subgroup of a group $G$ a
centralizer if it equals $C_G(X)$ for some subset $X \subseteq G$. This is the proposition that for
every group $G$ in which the join (in the subgroup lattice) of any two centralizers is again a
centralizer, any three centralizers $A$, $B$, $C$ of $G$ with $A \le C$ satisfy the modular law
$(A \sqcup B) \sqcap C = A \sqcup (B \sqcap C)$, where $\sqcup$ and $\sqcap$ are the join and meet
in the subgroup lattice of $G$.

Centralizers are always closed under intersection, so the hypothesis says that they form a
sublattice of the subgroup lattice. The question is due to V. A. Antonov.

Formalized by `MathlibExt.GroupTheory.CentralizerLatticeModularKourovka11Problem4Wanted.centralizerSublatticeModular`, a definition declared in [WantedExt/GroupTheory/CentralizerLatticeModularKourovka11Problem4Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CentralizerLatticeModularKourovka11Problem4Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/lattices-of-centralizers/index.html#centralizer-sublattice-modular).

## Lattices of centralizers need not be modular (Kourovka 11.4)

Call a subgroup of a group
$G$ a centralizer if it equals $C_G(X)$ for some subset $X \subseteq G$. Modularity of centralizer
sublattices fails: there is a group $G$ in which the join (in the subgroup lattice) of any two
centralizers is again a centralizer, but which has centralizers $A$, $B$, $C$ with $A \le C$ and
$(A \sqcup B) \sqcap C \ne A \sqcup (B \sqcap C)$, where $\sqcup$ and $\sqcap$ are the join and meet
in the subgroup lattice of $G$.

The Kourovka Archive answers 11.4 "No, not always" (Obraztsov); for finite groups the answer is
yes.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.4 (V. A. Antonov); resolution: V. N. Obraztsov, J. Algebra 199, no. 1 (1998), 337-343, Kourovka Archive, Problem 11.4: "No, not always", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.CentralizerLatticeModularKourovka11Problem4Wanted.centralizerSublatticeModular_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/CentralizerLatticeModularKourovka11Problem4Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CentralizerLatticeModularKourovka11Problem4Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/lattices-of-centralizers/index.html#centralizer-sublattice-modular-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lattices of centralizers](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/lattices-of-centralizers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/subgroup-embedding/lattices-of-centralizers)
