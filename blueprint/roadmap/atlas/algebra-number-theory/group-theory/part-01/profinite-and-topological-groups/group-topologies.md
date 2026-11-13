---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.IntegerGroupTopologyPowerSumKourovka15Problem79Wanted.integerGroupTopologyPowSumTendstoZero, MathlibExt.GroupTheory.IntegerGroupTopologyPowerSumKourovka15Problem79Wanted.integerGroupTopologyPowSumTendstoZero_holds, MathlibExt.GroupTheory.LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.nilpotentGroupTopologyLatticeNotModular, MathlibExt.GroupTheory.LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.countableNilpotentNonabelianTopologyLatticeNotModular, MathlibExt.GroupTheory.LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.nilpotentGroupTopologyLatticeNotModular_holds, MathlibExt.GroupTheory.LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.countableNilpotentNonabelianTopologyLatticeNotModular_refuted
statement: formalized
---

# Group topologies

6 results, 3 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies/index.html).

## Kourovka Problem 15.79 (Protasov's question on the integers)

The statement that there is a
topology on $\mathbb{Z}$ that makes $(\mathbb{Z}, +)$ a Hausdorff topological group and in which
the sequence $(2^n + 3^n)_{n \in \mathbb{N}}$ converges to $0$.

Formalized by `MathlibExt.GroupTheory.IntegerGroupTopologyPowerSumKourovka15Problem79Wanted.integerGroupTopologyPowSumTendstoZero`, a definition declared in [WantedExt/GroupTheory/IntegerGroupTopologyPowerSumKourovka15Problem79Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegerGroupTopologyPowerSumKourovka15Problem79Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies/index.html#integer-group-topology-pow-sum-tendsto-z).

## A Hausdorff group topology on the integers in which 2ⁿ + 3ⁿ tends to zero

There is a
topology on $\mathbb{Z}$ that makes $(\mathbb{Z}, +)$ a Hausdorff topological group and in which
the sequence $(2^n + 3^n)_{n \in \mathbb{N}}$ converges to $0$. That is, Kourovka Problem 15.79 has
a positive answer.

The Kourovka Archive answers 15.79 "Yes, there does", as follows from Theorem 3 of Ruzsa; another
solution is due to Skresanov.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.79 (I. V. Protasov); resolution: I. Z. Ruzsa, in: Proc. Conf. Number Theory (Budapest, 1987), Vol. I, Colloq. Math. Soc. János Bolyai 51, North-Holland, Amsterdam, 1990, 473-504; S. V. Skresanov, Group topologies on integers and S-unit equations, Siberian Math. J. 61 (2020), no. 3, 542-544, arXiv:1911.11963, Ruzsa, Theorem 3, as applied in the Kourovka Archive, Problem 15.79 (answer: Yes, there does); another solution by Skresanov, abstract (for a finite set of primes S, a Hausdorff group topology on ℤ in which every growing sequence of S-integers tends to 0; as a corollary, 2ⁿ + 3ⁿ tends to 0 in a Hausdorff group topology), https://arxiv.org/abs/1911.11963.

Stated but not proved: `MathlibExt.GroupTheory.IntegerGroupTopologyPowerSumKourovka15Problem79Wanted.integerGroupTopologyPowSumTendstoZero_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/IntegerGroupTopologyPowerSumKourovka15Problem79Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegerGroupTopologyPowerSumKourovka15Problem79Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies/index.html#integer-group-topology-pow-sum-tendsto-z-2).

## Kourovka Problem 14.4(a) (nilpotent groups with non-modular topology lattice)

This
proposition states that some nilpotent group $G$ has a non-modular lattice $\mathcal{L}(G)$ of all
(not necessarily Hausdorff) group topologies.

Formalized by `MathlibExt.GroupTheory.LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.nilpotentGroupTopologyLatticeNotModular`, a definition declared in [WantedExt/GroupTheory/LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies/index.html#nilpotent-group-topology-lattice-not-mod).

## Kourovka Problem 14.4(b) (countable nilpotent groups)

This proposition states that for
every countably infinite non-abelian nilpotent group $G$, the lattice $\mathcal{L}(G)$ of all (not
necessarily Hausdorff) group topologies on $G$ is not modular.

Formalized by `MathlibExt.GroupTheory.LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.countableNilpotentNonabelianTopologyLatticeNotModular`, a definition declared in [WantedExt/GroupTheory/LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies/index.html#countable-nilpotent-nonabelian-topology).

## A nilpotent group with non-modular lattice of group topologies

There is a nilpotent group $G$
whose lattice of all (not necessarily Hausdorff) group topologies is not modular.

Arnautov and Topală found such a group; the Kourovka Notebook (21st issue) answers 14.4(a) "Yes".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.4 (V. I. Arnautov); resolution: (a) V. Arnautov and A. Topală, Bul. Acad. Ştiinţe Repub. Mold. Mat. 1998, no. 2(27), 130-131; (b) D. Peng, On the lattice of group topologies, preprint, arXiv:2310.08269 (2023), (b) Theorem 1.1: there is a countably infinite non-abelian nilpotent group whose lattice of all (not necessarily Hausdorff) group topologies is modular; the Kourovka Notebook (21st issue) marks 14.4 solved: a) Yes; b) No, there are such groups with modular L(G), https://arxiv.org/abs/2310.08269.

Stated but not proved: `MathlibExt.GroupTheory.LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.nilpotentGroupTopologyLatticeNotModular_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies/index.html#nilpotent-group-topology-lattice-not-mod-2).

## A countable nilpotent group with modular lattice of group topologies

It is not the case that
for every countably infinite non-abelian nilpotent group $G$ the lattice of all (not necessarily
Hausdorff) group topologies on $G$ is not modular; that is, some countably infinite non-abelian
nilpotent group has a modular lattice of group topologies.

Peng constructs (Theorem 1.1) a countably infinite non-abelian nilpotent group whose lattice of
group topologies is modular; the Kourovka Notebook (21st issue) answers 14.4(b) "No".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.4 (V. I. Arnautov); resolution: (a) V. Arnautov and A. Topală, Bul. Acad. Ştiinţe Repub. Mold. Mat. 1998, no. 2(27), 130-131; (b) D. Peng, On the lattice of group topologies, preprint, arXiv:2310.08269 (2023), (b) Theorem 1.1: there is a countably infinite non-abelian nilpotent group whose lattice of all (not necessarily Hausdorff) group topologies is modular; the Kourovka Notebook (21st issue) marks 14.4 solved: a) Yes; b) No, there are such groups with modular L(G), https://arxiv.org/abs/2310.08269.

Stated but not proved: `MathlibExt.GroupTheory.LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.countableNilpotentNonabelianTopologyLatticeNotModular_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LatticeOfGroupTopologiesModularKourovka14Problem4Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies/index.html#countable-nilpotent-nonabelian-topology-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Group topologies](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/group-topologies)
