---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SolubleOneRelatorQuotientKourovka18Problem75Wanted.solubleGroupImageOfOneRelatorGroups, MathlibExt.GroupTheory.SolubleOneRelatorQuotientKourovka18Problem75Wanted.solubleGroupImageOfOneRelatorGroups_holds
statement: formalized
---

# Finite quotients of one-relator groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finite-quotients-of-one-relator-groups/index.html).

## Finite soluble groups as images of one-relator groups (Kourovka 18.75)

The statement,
posed by A. Yu. Olshanskii, that every finite soluble group $G$ has a natural number $d$ such that
for every element $w$ of the free group on $x_1, \dots, x_d$ there is a surjective homomorphism
from the one-relator group $\langle x_1, \dots, x_d \mid w \rangle$ onto $G$.

Formalized by `MathlibExt.GroupTheory.SolubleOneRelatorQuotientKourovka18Problem75Wanted.solubleGroupImageOfOneRelatorGroups`, a definition declared in [WantedExt/GroupTheory/SolubleOneRelatorQuotientKourovka18Problem75Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleOneRelatorQuotientKourovka18Problem75Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finite-quotients-of-one-relator-groups/index.html#soluble-group-image-of-one-relator-group).

## Finite soluble groups are images of one-relator groups

Every
finite soluble group $G$ has a natural number $d$ such that for every element $w$ of the free
group on $x_1, \dots, x_d$ there is a surjective homomorphism from the one-relator group
$\langle x_1, \dots, x_d \mid w \rangle$ onto $G$. That is, Kourovka Problem 18.75 has a positive
answer.

Resolved true: the Kourovka Archive answers 18.75 "Yes, it does" (N. Nikolov and D. Segal, 2007).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.75 (A. Yu. Olshanskii); resolution: N. Nikolov and D. Segal, Bull. London Math. Soc. 39 (2007), no. 2, 209-213, Kourovka Archive, Problem 18.75: Yes, it does, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SolubleOneRelatorQuotientKourovka18Problem75Wanted.solubleGroupImageOfOneRelatorGroups_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SolubleOneRelatorQuotientKourovka18Problem75Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleOneRelatorQuotientKourovka18Problem75Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finite-quotients-of-one-relator-groups/index.html#soluble-group-image-of-one-relator-group-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite quotients of one-relator groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finite-quotients-of-one-relator-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/finite-quotients-of-one-relator-groups)
