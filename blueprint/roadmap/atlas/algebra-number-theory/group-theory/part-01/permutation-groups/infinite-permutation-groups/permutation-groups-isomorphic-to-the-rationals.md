---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.RationalPermutationGroupDisplacementKourovka20Problem98Wanted.rationalPermutationGroupInfiniteDisplacement, MathlibExt.GroupTheory.RationalPermutationGroupDisplacementKourovka20Problem98Wanted.rationalPermutationGroupInfiniteDisplacement_holds
statement: formalized
---

# Permutation groups isomorphic to the rationals

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/permutation-groups-isomorphic-to-the-rationals/index.html).

## Suchkov's question on displacements in permutation groups isomorphic to the rationals (Kourovka 20.98)

**Suchkov's question on displacements in permutation groups isomorphic to the rationals
(Kourovka 20.98).** The statement that for every subgroup $G$ of the group of permutations of
$\mathbb{N} = \{0, 1, 2, \dots\}$ that is isomorphic to the additive group $(\mathbb{Q}, +)$,
there is an element $g \in G$ such that the set of displacements $\{a - g(a) : a \in \mathbb{N}\}$,
computed in $\mathbb{Z}$, is infinite.

Kourovka 20.98 (N. M. Suchkov) is stated for permutations of the positive integers; shifting by
one does not change the displacements.

Formalized by `MathlibExt.GroupTheory.RationalPermutationGroupDisplacementKourovka20Problem98Wanted.rationalPermutationGroupInfiniteDisplacement`, a definition declared in [WantedExt/GroupTheory/RationalPermutationGroupDisplacementKourovka20Problem98Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/RationalPermutationGroupDisplacementKourovka20Problem98Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/permutation-groups-isomorphic-to-the-rationals/index.html#rational-permutation-group-infinite-disp).

## Permutation groups isomorphic to the rationals have infinite displacement (Kourovka 20.98)

For every subgroup $G$ of the group of permutations of $\mathbb{N} = \{0, 1, 2, \dots\}$ that is
isomorphic to the additive group $(\mathbb{Q}, +)$, there is an element $g \in G$ such that the
set of displacements $\{a - g(a) : a \in \mathbb{N}\}$, computed in $\mathbb{Z}$, is infinite.
That is, the answer to Kourovka Problem 20.98 is yes.

The 21st issue of the Kourovka Notebook marks 20.98 solved ("Yes, it must"), citing Suchkov,
Shlepkin and Taysnyov (2024).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.98 (N. M. Suchkov); resolution: N. M. Suchkov, A. A. Shlepkin and D. A. Taysnyov, On the existence of countable unlimited groups, Siberian Math. J. 65 (2024), no. 6, 1390-1394, abstract: the additive group of the rationals is not isomorphic to a subgroup of the group of all limited permutations of the naturals; Kourovka Notebook (21st issue), Problem 20.98: Yes, it must, https://www.mathnet.ru/eng/smj7921.

Stated but not proved: `MathlibExt.GroupTheory.RationalPermutationGroupDisplacementKourovka20Problem98Wanted.rationalPermutationGroupInfiniteDisplacement_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/RationalPermutationGroupDisplacementKourovka20Problem98Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/RationalPermutationGroupDisplacementKourovka20Problem98Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/permutation-groups-isomorphic-to-the-rationals/index.html#rational-permutation-group-infinite-disp-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutation groups isomorphic to the rationals](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/permutation-groups-isomorphic-to-the-rationals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/permutation-groups-isomorphic-to-the-rationals)
