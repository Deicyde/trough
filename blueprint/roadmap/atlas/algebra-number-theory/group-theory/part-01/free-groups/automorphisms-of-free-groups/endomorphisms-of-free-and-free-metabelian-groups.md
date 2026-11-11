---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.FreeMetabelianGroup, MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.DeterminedByTwoElements, MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.freeGroupEndomorphismsDeterminedByTwoElements, MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.freeMetabelianEndomorphismsDeterminedByTwoElements, MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.freeGroupEndomorphismsDeterminedByTwoElements_holds, MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.freeMetabelianEndomorphismsDeterminedByTwoElements_refuted
statement: formalized
---

# Endomorphisms of free and free metabelian groups

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups/index.html).

## The free metabelian group $M_n$

For a natural number $n$, the free metabelian group of
rank $n$ is the quotient $F_n / F_n''$ of the free group $F_n$ on $n$ generators by its second
derived subgroup $F_n'' = [F_n', F_n']$, where $F_n' = [F_n, F_n]$ is the derived subgroup of
$F_n$.

Formalized by `MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.FreeMetabelianGroup`, an abbreviation declared in [WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups/index.html#free-metabelian-group).

## Groups whose endomorphisms with non-cyclic images are determined by two elements

A group
$F$ has this property when there exist elements $g, h \in F$ such that any two endomorphisms
$\varphi, \psi$ of $F$ whose images are not cyclic subgroups and which satisfy
$\varphi(g) = \psi(g)$ and $\varphi(h) = \psi(h)$ are equal.

Formalized by `MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.DeterminedByTwoElements`, a definition declared in [WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups/index.html#determined-by-two-elements).

## Shpil'rain's two-element problem for free groups (Kourovka 13.66(a))

For every natural
number $n$, the free group $F_n$ of rank $n$ contains two elements $g$ and $h$ such that any two
endomorphisms of $F_n$ whose images are not cyclic subgroups and which agree at $g$ and at $h$
are equal; that is, $F_n$ has its endomorphisms with non-cyclic images determined by two
elements.

Formalized by `MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.freeGroupEndomorphismsDeterminedByTwoElements`, a definition declared in [WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups/index.html#free-group-endomorphisms-determined-by-t).

## Shpil'rain's two-element problem for free metabelian groups (Kourovka 13.66(b))

For every
natural number $n$, the free metabelian group $M_n = F_n / F_n''$ of rank $n$ (the quotient of the
free group $F_n$ of rank $n$ by its second derived subgroup) contains two elements $g$ and $h$
such that any two endomorphisms of $M_n$ whose images are not cyclic subgroups and which agree at
$g$ and at $h$ are equal.

Formalized by `MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.freeMetabelianEndomorphismsDeterminedByTwoElements`, a definition declared in [WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups/index.html#free-metabelian-endomorphisms-determined).

## Endomorphisms of free groups with non-cyclic images are determined by two elements

For every
natural number $n$, the free group $F_n$ of rank $n$ contains two elements $g$ and $h$ such that
any two endomorphisms $\varphi, \psi$ of $F_n$ whose images are not cyclic subgroups and which
satisfy $\varphi(g) = \psi(g)$ and $\varphi(h) = \psi(h)$ are equal.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.66 (V. E. Shpil'rain); resolution: (a) D. Lee, J. Algebra 247 (2002), no. 2, 509-540; (b) E. I. Timoshenko, Math. Notes 62 (1998), no. 5-6, 767-770, Kourovka Archive, Problem 13.66 (answers: a) Yes, one can; b) No, not always).

Stated but not proved: `MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.freeGroupEndomorphismsDeterminedByTwoElements_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups/index.html#free-group-endomorphisms-determined-by-t-2).

## Endomorphisms of free metabelian groups are not always determined by two elements

For a
natural number $n$, let $M_n = F_n / F_n''$ be the free metabelian group of rank $n$, the quotient
of the free group $F_n$ of rank $n$ by its second derived subgroup. There is an $n$ such that for
all elements $g, h \in M_n$ there are endomorphisms $\varphi \ne \psi$ of $M_n$ whose images are
not cyclic subgroups and which satisfy $\varphi(g) = \psi(g)$ and $\varphi(h) = \psi(h)$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.66 (V. E. Shpil'rain); resolution: (a) D. Lee, J. Algebra 247 (2002), no. 2, 509-540; (b) E. I. Timoshenko, Math. Notes 62 (1998), no. 5-6, 767-770, Kourovka Archive, Problem 13.66 (answers: a) Yes, one can; b) No, not always).

Stated but not proved: `MathlibExt.GroupTheory.EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.freeMetabelianEndomorphismsDeterminedByTwoElements_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismsDeterminedByTwoElementsKourovka13Problem66Wanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups/index.html#free-metabelian-endomorphisms-determined-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Endomorphisms of free and free metabelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/endomorphisms-of-free-and-free-metabelian-groups)
