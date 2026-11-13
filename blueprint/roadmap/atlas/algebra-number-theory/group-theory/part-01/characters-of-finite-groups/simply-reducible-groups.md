---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SimplyReducibleSolubleKourovka11Problem94Wanted.IsSimplyReducible, MathlibExt.GroupTheory.SimplyReducibleSolubleKourovka11Problem94Wanted.simplyReducibleSoluble, MathlibExt.GroupTheory.SimplyReducibleSolubleKourovka11Problem94Wanted.simplyReducibleSoluble_holds
statement: formalized
---

# Simply reducible groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/simply-reducible-groups/index.html).

## Simply reducible group

A group $G$ is simply reducible when the character of every
irreducible finite-dimensional complex representation of $G$ is real-valued, and for all
irreducible finite-dimensional complex representations $U$, $V$ and $W$ of $G$, the space
$\mathrm{Hom}_G(U, V \otimes W)$ of $G$-equivariant linear maps from $U$ to the tensor product
$V \otimes W$ has complex dimension at most $1$.

For finite $G$, by Maschke's and Schur's theorems this dimension is the multiplicity of $U$ in
$V \otimes W$, so the second condition says that $V \otimes W$ has no repeated irreducible
constituents.

Formalized by `MathlibExt.GroupTheory.SimplyReducibleSolubleKourovka11Problem94Wanted.IsSimplyReducible`, a definition declared in [WantedExt/GroupTheory/SimplyReducibleSolubleKourovka11Problem94Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SimplyReducibleSolubleKourovka11Problem94Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/simply-reducible-groups/index.html#is-simply-reducible).

## Solubility of finite simply reducible groups (Kourovka 11.94)

The statement, asked by
S. P. Strunkov as Kourovka Problem 11.94, that every finite simply reducible group is soluble.

Formalized by `MathlibExt.GroupTheory.SimplyReducibleSolubleKourovka11Problem94Wanted.simplyReducibleSoluble`, a definition declared in [WantedExt/GroupTheory/SimplyReducibleSolubleKourovka11Problem94Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SimplyReducibleSolubleKourovka11Problem94Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/simply-reducible-groups/index.html#simply-reducible-soluble).

## Finite simply reducible groups are soluble

Every finite simply reducible group is soluble;
that is, the statement of Kourovka Problem 11.94 holds.

This was proved by Kazarin and Chankov; the Kourovka Archive answers 11.94 "Yes, it is".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.94 (S. P. Strunkov); resolution: L. S. Kazarin and E. I. Chankov, Sb. Math. 201, no. 5 (2010), 655-668, Kourovka Archive, Problem 11.94: "Yes, it is", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SimplyReducibleSolubleKourovka11Problem94Wanted.simplyReducibleSoluble_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SimplyReducibleSolubleKourovka11Problem94Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SimplyReducibleSolubleKourovka11Problem94Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/simply-reducible-groups/index.html#simply-reducible-soluble-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simply reducible groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/simply-reducible-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/characters-of-finite-groups/simply-reducible-groups)
