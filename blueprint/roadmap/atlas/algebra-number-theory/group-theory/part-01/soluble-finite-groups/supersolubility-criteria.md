---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.IsSupersoluble, MathlibExt.GroupTheory.NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.nonSupersolubleHasUncomplementedSylowMaximal, MathlibExt.GroupTheory.NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.nonSupersolubleHasUncomplementedSylowMaximal_holds
statement: formalized
---

# Supersolubility criteria

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersolubility-criteria/index.html).

## Supersoluble group (Kourovka 15.81)

A group $G$ is supersoluble when it has a series
$1 = H_0 \le H_1 \le \cdots \le H_n = G$ of subgroups, each normal in $G$, such that every factor
$H_{i+1}/H_i$ is cyclic.

Formalized by `MathlibExt.GroupTheory.NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.IsSupersoluble`, a definition declared in [WantedExt/GroupTheory/NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersolubility-criteria/index.html#is-supersoluble).

## Uncomplemented maximal subgroups of Sylow subgroups (Kourovka 15.81, Skiba)

The statement
that every finite group $G$ that is not supersoluble has, for some prime $p$, a non-cyclic Sylow
$p$-subgroup $P$ with a maximal subgroup $M$ of $P$ that has no proper complement in $G$, that is,
there is no subgroup $K \ne G$ with $MK = G$ and $M \cap K = 1$.

Formalized by `MathlibExt.GroupTheory.NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.nonSupersolubleHasUncomplementedSylowMaximal`, a definition declared in [WantedExt/GroupTheory/NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersolubility-criteria/index.html#non-supersoluble-has-uncomplemented-sylo).

## Finite non-supersoluble groups have uncomplemented maximal subgroups of Sylow subgroups

For
every finite group $G$ that is not supersoluble, there are a prime $p$ and a non-cyclic Sylow
$p$-subgroup $P$ of $G$ with a maximal subgroup $M$ of $P$ that has no proper complement in $G$:
there is no subgroup $K \ne G$ with $MK = G$ and $M \cap K = 1$. This answers Kourovka
Problem 15.81 in the affirmative.

The Kourovka Archive answers 15.81 "Yes, it is" (Wang and Wei).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.81 (A. N. Skiba); resolution: Wang Yanming and Wei Huaquan, Sci. China Ser. A 47 (2004), no. 1, 96-103, Kourovka Archive, Problem 15.81 (answer: Yes, it is).

Stated but not proved: `MathlibExt.GroupTheory.NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.nonSupersolubleHasUncomplementedSylowMaximal_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NonSupersolubleUncomplementedMaximalKourovka15Problem81Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersolubility-criteria/index.html#non-supersoluble-has-uncomplemented-sylo-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Supersolubility criteria](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersolubility-criteria/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/supersolubility-criteria)
