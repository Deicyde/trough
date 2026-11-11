---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.IsMetanilpotentByFinite, MathlibExt.GroupTheory.FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.finitelyPresentedSolubleMetanilpotentByFinite, MathlibExt.GroupTheory.FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.finitelyPresentedSolubleMetanilpotentByFinite_refuted
statement: formalized
---

# Finitely presented soluble groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finitely-presented-soluble-groups/index.html).

## Metanilpotent-by-finite groups

A group $G$ is (nilpotent-by-nilpotent)-by-finite when it
has a normal subgroup $M$ of finite index and a normal subgroup $N$ of $M$ such that $N$ and $M/N$
are both nilpotent.

Formalized by `MathlibExt.GroupTheory.FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.IsMetanilpotentByFinite`, a definition declared in [WantedExt/GroupTheory/FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finitely-presented-soluble-groups/index.html#is-metanilpotent-by-finite).

## Groves's question (Kourovka 16.35)

The proposition that every finitely presented soluble
group $G$ is (nilpotent-by-nilpotent)-by-finite, that is, $G$ has a normal subgroup $M$ of finite
index and a normal subgroup $N$ of $M$ such that $N$ and $M/N$ are both nilpotent.

Formalized by `MathlibExt.GroupTheory.FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.finitelyPresentedSolubleMetanilpotentByFinite`, a definition declared in [WantedExt/GroupTheory/FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finitely-presented-soluble-groups/index.html#finitely-presented-soluble-metanilpotent).

## Groves's question (Kourovka 16.35) has a negative answer

Not every finitely presented
soluble group is (nilpotent-by-nilpotent)-by-finite: there is a finitely presented soluble group
$G$ such that for no normal subgroup $M$ of finite index in $G$ is there a normal subgroup $N$ of
$M$ with $N$ and $M/N$ both nilpotent.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.35 (J. R. J. Groves); resolution: V. V. Bludov, letter of 27 April 2007, as recorded in the Kourovka Archive, Kourovka Archive, Problem 16.35 (No: for a prime p, ⟨a, b, c, d | b^a = b^p, c^a = c^p, d^a = d, c^b = c, d^c = d d^b, [d, d^b] = 1, d^p = 1⟩ is soluble of derived length 3 but not metanilpotent-by-finite).

Stated but not proved: `MathlibExt.GroupTheory.FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.finitelyPresentedSolubleMetanilpotentByFinite_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FinitelyPresentedSolubleMetanilpotentKourovka16Problem35Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finitely-presented-soluble-groups/index.html#finitely-presented-soluble-metanilpotent-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finitely presented soluble groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/finitely-presented-soluble-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/finitely-presented-soluble-groups)
