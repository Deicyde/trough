---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ResiduallyFinitePGroupTorsionFreeNilpotentKourovka14Problem52Wanted.residuallyFinitePImpliesResiduallyTorsionFreeNilpotent, MathlibExt.GroupTheory.ResiduallyFinitePGroupTorsionFreeNilpotentKourovka14Problem52Wanted.residuallyFinitePImpliesResiduallyTorsionFreeNilpotent_refuted
statement: formalized
---

# Residually finite p-groups and residual nilpotence

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/residually-finite-p-groups-and-residual-nilpoten/index.html).

## Kuz'min's question on residually finite $p$-groups (Kourovka 14.52)

The statement that
every finitely generated group $G$ that is residually a finite $p$-group for every prime $p$ is
residually torsion-free nilpotent. Here $G$ is residually a finite $p$-group when every element
$g \ne 1$ lies outside some normal subgroup $N$ such that $G/N$ is a finite $p$-group, and
residually torsion-free nilpotent when every element $g \ne 1$ lies outside some normal subgroup
$N$ such that $G/N$ is nilpotent and has no nontrivial elements of finite order.

Formalized by `MathlibExt.GroupTheory.ResiduallyFinitePGroupTorsionFreeNilpotentKourovka14Problem52Wanted.residuallyFinitePImpliesResiduallyTorsionFreeNilpotent`, a definition declared in [WantedExt/GroupTheory/ResiduallyFinitePGroupTorsionFreeNilpotentKourovka14Problem52Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ResiduallyFinitePGroupTorsionFreeNilpotentKourovka14Problem52Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/residually-finite-p-groups-and-residual-nilpoten/index.html#residually-finite-pimplies-residually-to).

## Residual $p$-finiteness for all $p$ does not imply residual torsion-free nilpotence

It is not
the case that every finitely generated group that is residually a finite $p$-group for every prime
$p$ is residually torsion-free nilpotent. Here a group $G$ is residually a finite $p$-group when
every element $g \ne 1$ lies outside some normal subgroup $N$ such that $G/N$ is a finite
$p$-group, and residually torsion-free nilpotent when every element $g \ne 1$ lies outside some
normal subgroup $N$ such that $G/N$ is nilpotent and has no nontrivial elements of finite order.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.52 (Yu. V. Kuz'min); resolution: B. Hartley, in: Symposia Mathematica XVII (Convegno sui Gruppi Infiniti, INDAM, Roma, 1973), Academic Press, London, 1976, 225-234, Kourovka Archive, Problem 14.52 (answer: Not always).

Stated but not proved: `MathlibExt.GroupTheory.ResiduallyFinitePGroupTorsionFreeNilpotentKourovka14Problem52Wanted.residuallyFinitePImpliesResiduallyTorsionFreeNilpotent_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ResiduallyFinitePGroupTorsionFreeNilpotentKourovka14Problem52Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ResiduallyFinitePGroupTorsionFreeNilpotentKourovka14Problem52Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/residually-finite-p-groups-and-residual-nilpoten/index.html#residually-finite-pimplies-residually-to-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Residually finite p-groups and residual nilpotence](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/residually-finite-p-groups-and-residual-nilpoten/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/residually-finite-p-groups-and-residual-nilpoten)
