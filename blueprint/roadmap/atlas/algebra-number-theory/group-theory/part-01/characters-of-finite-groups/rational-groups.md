---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.RationalGroupSylowTwoKourovka16Problem36Wanted.IsRationalGroup, MathlibExt.GroupTheory.RationalGroupSylowTwoKourovka16Problem36Wanted.sylowTwoOfRationalIsRational, MathlibExt.GroupTheory.RationalGroupSylowTwoKourovka16Problem36Wanted.sylowTwoOfRationalIsRational_refuted, MathlibExt.GroupTheory.SylowTwoSymmetricRationalKourovka15Problem25Wanted.IsRationalGroup, MathlibExt.GroupTheory.SylowTwoSymmetricRationalKourovka15Problem25Wanted.sylowTwoSubgroupSymmetricRational, MathlibExt.GroupTheory.SylowTwoSymmetricRationalKourovka15Problem25Wanted.sylowTwoSubgroupSymmetricRational_holds
statement: formalized
---

# Rational groups

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/rational-groups/index.html).

## Rational groups, conjugacy form

A group $G$ is rational if every element $g \in G$ is
conjugate to $g^k$ for every natural number $k$ coprime to the order of $g$, where an element of
infinite order has order $0$, so that only $k = 1$ is coprime to it. For finite groups this is the
classical equivalent form of the condition that all ordinary characters of $G$ are
rational-valued.

Formalized by `MathlibExt.GroupTheory.RationalGroupSylowTwoKourovka16Problem36Wanted.IsRationalGroup`, a definition declared in [WantedExt/GroupTheory/RationalGroupSylowTwoKourovka16Problem36Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RationalGroupSylowTwoKourovka16Problem36Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/rational-groups/index.html#is-rational-group).

## Darafsheh's question on Sylow 2-subgroups of rational groups (Kourovka 16.36)

The
conjecture that for every finite rational group $G$, every Sylow $2$-subgroup of $G$, viewed as a
group in its own right, is rational. Here a group is rational if every element $g$ is conjugate
to $g^k$ for every natural number $k$ coprime to the order of $g$.

Formalized by `MathlibExt.GroupTheory.RationalGroupSylowTwoKourovka16Problem36Wanted.sylowTwoOfRationalIsRational`, a definition declared in [WantedExt/GroupTheory/RationalGroupSylowTwoKourovka16Problem36Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RationalGroupSylowTwoKourovka16Problem36Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/rational-groups/index.html#sylow-two-of-rational-is-rational).

## Sylow 2-subgroups of rational groups need not be rational (Kourovka 16.36)

There is a
finite rational group with a Sylow $2$-subgroup that is not rational as a group in its own right.
Here a group is rational if every element $g$ is conjugate to $g^k$ for every natural number $k$
coprime to the order of $g$.

The Kourovka Archive answers 16.36 "No, not always", citing Isaacs and Navarro (2012).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.36 (M. R. Darafsheh); resolution: I. M. Isaacs and G. Navarro, Math. Z. 272 (2012), 937-945, Kourovka Archive, Problem 16.36 (No, not always).

Stated but not proved: `MathlibExt.GroupTheory.RationalGroupSylowTwoKourovka16Problem36Wanted.sylowTwoOfRationalIsRational_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/RationalGroupSylowTwoKourovka16Problem36Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RationalGroupSylowTwoKourovka16Problem36Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/rational-groups/index.html#sylow-two-of-rational-is-rational-refute).

## Rational group (conjugacy form, Kourovka 15.25)

A group $G$ is rational when every element
$g \in G$ is conjugate in $G$ to $g^k$ for every natural number $k$ coprime to the order of $g$ (an
element of infinite order counts as having order $0$, so for it only $k = 1$ qualifies).

For finite groups this is equivalent to every irreducible complex character taking only rational
values.

Formalized by `MathlibExt.GroupTheory.SylowTwoSymmetricRationalKourovka15Problem25Wanted.IsRationalGroup`, a definition declared in [WantedExt/GroupTheory/SylowTwoSymmetricRationalKourovka15Problem25Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SylowTwoSymmetricRationalKourovka15Problem25Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/rational-groups/index.html#is-rational-group-2).

## Kourovka Problem 15.25 (statement)

The statement that for every natural number $n$, every
Sylow $2$-subgroup $P$ of the symmetric group $S_{2^n}$ on $2^n$ points is rational as a group in
its own right: every $g \in P$ is conjugate within $P$ to $g^k$ for every natural number $k$ coprime
to the order of $g$.

Formalized by `MathlibExt.GroupTheory.SylowTwoSymmetricRationalKourovka15Problem25Wanted.sylowTwoSubgroupSymmetricRational`, a definition declared in [WantedExt/GroupTheory/SylowTwoSymmetricRationalKourovka15Problem25Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SylowTwoSymmetricRationalKourovka15Problem25Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/rational-groups/index.html#sylow-two-subgroup-symmetric-rational).

## Sylow 2-subgroups of the symmetric groups of degree $2^n$ are rational (Kourovka 15.25)

For
every natural number $n$, every Sylow $2$-subgroup $P$ of the symmetric group $S_{2^n}$ on $2^n$
points is rational as a group in its own right: every $g \in P$ is conjugate within $P$ to $g^k$ for
every natural number $k$ coprime to the order of $g$.

A Sylow $2$-subgroup $T_n$ of $S_{2^n}$ is the wreath product of $T_{n-1}$ with a group of order
$2$, which is rational when $T_{n-1}$ is (Kletzing, Corollary 70), so induction on $n$ applies.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.25 (Ya. G. Berkovich); resolution: A. Mann, letter of 1 October 2002, as recorded in the Kourovka Archive, Problem 15.25, using D. Kletzing, Structure and representations of Q-groups, Lecture Notes in Math. 1084, Springer, Berlin, 1984, Corollary 70, Kourovka Archive, Problem 15.25 (answer: Yes, they are; T_n = T_(n-1) wr C_2 and wreath products with C_2 preserve rationality), https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SylowTwoSymmetricRationalKourovka15Problem25Wanted.sylowTwoSubgroupSymmetricRational_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SylowTwoSymmetricRationalKourovka15Problem25Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SylowTwoSymmetricRationalKourovka15Problem25Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/rational-groups/index.html#sylow-two-subgroup-symmetric-rational-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rational groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/rational-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/characters-of-finite-groups/rational-groups)
