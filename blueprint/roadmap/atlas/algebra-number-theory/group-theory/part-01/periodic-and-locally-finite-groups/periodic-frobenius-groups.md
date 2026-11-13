---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FrobeniusGroupShared.IsFrobeniusGroup, MathlibExt.GroupTheory.PeriodicSelfCentralizingAbelianFrobeniusKourovka20Problem96Wanted.periodicSelfCentralizingAbelianNormalFrobenius, MathlibExt.GroupTheory.PeriodicSelfCentralizingAbelianFrobeniusKourovka20Problem96Wanted.periodicSelfCentralizingAbelianNormalFrobenius_holds
statement: formalized
---

# Periodic Frobenius groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/periodic-frobenius-groups/index.html).

## Frobenius group with given kernel and complement

For subgroups $F$ and $H$ of a group $G$,
$G$ is a Frobenius group with kernel $F$ and complement $H$ (Kourovka 6.53) if $G = F \rtimes H$
(that is, $F$ is normal in $G$, $F \cap H = 1$ and $FH = G$), $F \ne 1$, $H \ne 1$,
$H \cap gHg^{-1} = 1$ for every $g \in G \setminus H$, and the non-trivial elements of $F$ are
exactly the elements of $G$ that lie in no conjugate $gHg^{-1}$ of $H$.

Formalized by `MathlibExt.GroupTheory.FrobeniusGroupShared.IsFrobeniusGroup`, a definition declared in [WantedExt/GroupTheory/FrobeniusGroupShared.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FrobeniusGroupShared.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/periodic-frobenius-groups/index.html#is-frobenius-group).

## Kourovka Problem 20.96 (periodic Frobenius groups)

The statement, posed by A. I. Sozutov,
that for every group $G$ in which every element has finite order and every normal abelian subgroup
$A$ of $G$ that is neither trivial nor all of $G$ and such that for every $a \in A$ with $a \ne 1$
the centralizer $C_G(a)$ of $a$ in $G$ is contained in $A$, there are subgroups $F$ and $H$ of $G$
such that $G$ is a Frobenius group with kernel $F$ and complement $H$.

Formalized by `MathlibExt.GroupTheory.PeriodicSelfCentralizingAbelianFrobeniusKourovka20Problem96Wanted.periodicSelfCentralizingAbelianNormalFrobenius`, a definition declared in [WantedExt/GroupTheory/PeriodicSelfCentralizingAbelianFrobeniusKourovka20Problem96Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PeriodicSelfCentralizingAbelianFrobeniusKourovka20Problem96Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/periodic-frobenius-groups/index.html#periodic-self-centralizing-abelian-norma).

## Lytkina–Mazurov theorem on periodic Frobenius groups

Let $G$ be a group in which every element
has finite order, and let $A$ be a normal abelian subgroup of $G$ that is neither trivial nor all of
$G$ and such that for every $a \in A$ with $a \ne 1$ the centralizer $C_G(a)$ of $a$ in $G$ is
contained in $A$. Then there are subgroups $F$ and $H$ of $G$ such that $G$ is a Frobenius group
with kernel $F$ and complement $H$. This answers Kourovka Problem 20.96 (A. I. Sozutov) in the
affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.96 (A. I. Sozutov); resolution: D. V. Lytkina and V. D. Mazurov, Periodic Frobenius groups, Siberian Math. J. 64 (2023), no. 6, 1351-1355 (Sibirsk. Mat. Zh. 64 (2023), no. 6, 1224-1228), abstract: conditions for a strongly isolated normal subgroup of a periodic group to have a complement; Kourovka Notebook (21st issue), Problem 20.96: Yes, it is, https://www.mathnet.ru/eng/smj7826.

Stated but not proved: `MathlibExt.GroupTheory.PeriodicSelfCentralizingAbelianFrobeniusKourovka20Problem96Wanted.periodicSelfCentralizingAbelianNormalFrobenius_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PeriodicSelfCentralizingAbelianFrobeniusKourovka20Problem96Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PeriodicSelfCentralizingAbelianFrobeniusKourovka20Problem96Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/periodic-frobenius-groups/index.html#periodic-self-centralizing-abelian-norma-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Periodic Frobenius groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/periodic-frobenius-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/periodic-frobenius-groups)
