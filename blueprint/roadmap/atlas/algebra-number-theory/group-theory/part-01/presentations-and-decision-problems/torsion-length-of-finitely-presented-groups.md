---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SolubleTorsionLengthKourovka19Problem23Wanted.torsionSeries, MathlibExt.GroupTheory.SolubleTorsionLengthKourovka19Problem23Wanted.TorsionLengthGtTwo, MathlibExt.GroupTheory.SolubleTorsionLengthKourovka19Problem23Wanted.existsFinitelyPresentedSolubleTorsionLengthGtTwo, MathlibExt.GroupTheory.SolubleTorsionLengthKourovka19Problem23Wanted.existsFinitelyPresentedSolubleTorsionLengthGtTwo_holds
statement: formalized
---

# Torsion length of finitely presented groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-length-of-finitely-presented-groups/index.html).

## Torsion series

For a group $G$, the torsion series of Chiodo and Vyas is the sequence of
subgroups $\mathrm{Tor}_i(G)$ of $G$ defined by $\mathrm{Tor}_0(G) = 1$, the trivial subgroup,
and, for each $i$, $\mathrm{Tor}_{i+1}(G)$ is the normal closure in $G$ of the set of elements $g$
such that $g^n \in \mathrm{Tor}_i(G)$ for some integer $n > 0$.

This is the preimage of $\mathrm{Tor}_1(G / \mathrm{Tor}_i(G))$, the normal closure of the torsion
elements of $G / \mathrm{Tor}_i(G)$, since normal closures commute with the quotient map and
$\mathrm{Tor}_i(G)$ lies in that set.

Formalized by `MathlibExt.GroupTheory.SolubleTorsionLengthKourovka19Problem23Wanted.torsionSeries`, a definition declared in [WantedExt/GroupTheory/SolubleTorsionLengthKourovka19Problem23Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolubleTorsionLengthKourovka19Problem23Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-length-of-finitely-presented-groups/index.html#torsion-series).

## Torsion length greater than two

A group $G$ has torsion length greater than $2$ when
$G / \mathrm{Tor}_2(G)$ is not torsion-free, where $\mathrm{Tor}_2(G)$ is the second term of the
torsion series of $G$: some element $g \in G$ outside $\mathrm{Tor}_2(G)$ has a power $g^n$ with
$n > 0$ in $\mathrm{Tor}_2(G)$.

Then $G / \mathrm{Tor}_1(G)$ is not torsion-free either, so neither $1$ nor $2$ is the torsion
length of $G$.

Formalized by `MathlibExt.GroupTheory.SolubleTorsionLengthKourovka19Problem23Wanted.TorsionLengthGtTwo`, a definition declared in [WantedExt/GroupTheory/SolubleTorsionLengthKourovka19Problem23Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolubleTorsionLengthKourovka19Problem23Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-length-of-finitely-presented-groups/index.html#torsion-length-gt-two).

## Kourovka Problem 19.23 (Chiodo–Vyas), finitely presented form

The statement that there is
a finitely presented soluble group $G$ of torsion length greater than $2$, that is, such that
$G / \mathrm{Tor}_2(G)$ is not torsion-free, where $\mathrm{Tor}_2(G)$ is the second term of the
torsion series of $G$.

Formalized by `MathlibExt.GroupTheory.SolubleTorsionLengthKourovka19Problem23Wanted.existsFinitelyPresentedSolubleTorsionLengthGtTwo`, a definition declared in [WantedExt/GroupTheory/SolubleTorsionLengthKourovka19Problem23Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolubleTorsionLengthKourovka19Problem23Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-length-of-finitely-presented-groups/index.html#exists-finitely-presented-soluble-torsio).

## Finitely presented soluble groups of torsion length greater than two

Resolved true: the Kourovka Archive answers 19.23 "Yes, such groups exist"; Leary and Minasyan
(Theorem 2.14) construct polycyclic groups, which are finitely presented and soluble, of every
torsion length `n ≥ 1`, in particular of torsion length `3`. Source: E. I. Khukhro and V. D. Mazurov
(eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49
(2026), Archive of Solved Problems, Problem 19.23 (M. Chiodo, R. Vyas); resolution: I. J. Leary and
A. Minasyan, A note on torsion length and torsion subgroups, J. Group Theory 26 (2023), no. 4,
741-750 (arXiv:2112.14546), Theorem 2.14: for every integer n ≥ 1 there is a polycyclic group of
torsion length n (their torsion length counts G₀ = G, G_{n+1} = G_n / Tor(G_n) from 0 and agrees
with the Notebook's for n ≥ 1); Kourovka Archive, Problem 19.23: Yes, such groups exist,
https://arxiv.org/abs/2112.14546.

Stated but not proved: `MathlibExt.GroupTheory.SolubleTorsionLengthKourovka19Problem23Wanted.existsFinitelyPresentedSolubleTorsionLengthGtTwo_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SolubleTorsionLengthKourovka19Problem23Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolubleTorsionLengthKourovka19Problem23Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-length-of-finitely-presented-groups/index.html#exists-finitely-presented-soluble-torsio-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Torsion length of finitely presented groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-length-of-finitely-presented-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/torsion-length-of-finitely-presented-groups)
