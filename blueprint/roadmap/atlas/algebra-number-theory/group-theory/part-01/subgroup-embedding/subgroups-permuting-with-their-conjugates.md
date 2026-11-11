---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PermutingConjugatesSimpleGroupKourovka10Problem66Wanted.permutingConjugatesNotSimple, MathlibExt.GroupTheory.PermutingConjugatesSimpleGroupKourovka10Problem66Wanted.permutingConjugatesNotSimple_refuted
statement: formalized
---

# Subgroups permuting with their conjugates

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroups-permuting-with-their-conjugates/index.html).

## Permuting conjugates and simplicity (Kourovka 10.66)

The conjecture that a group $G$
containing nontrivial subgroups $A$ and $B$ such that the product set $AB$ is not all of $G$ and
$A \cdot gBg^{-1} = gBg^{-1} \cdot A$ for every $g \in G$ is not simple. Products of subgroups are
products of subsets of $G$.

This is Kourovka Problem 10.66 (A. N. Fomin, V. P. Shunkov).

Formalized by `MathlibExt.GroupTheory.PermutingConjugatesSimpleGroupKourovka10Problem66Wanted.permutingConjugatesNotSimple`, a definition declared in [WantedExt/GroupTheory/PermutingConjugatesSimpleGroupKourovka10Problem66Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PermutingConjugatesSimpleGroupKourovka10Problem66Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroups-permuting-with-their-conjugates/index.html#permuting-conjugates-not-simple).

## A simple group with permuting conjugate subgroups (Kourovka 10.66 refuted)

There exist a
simple group $G$ and nontrivial subgroups $A$ and $B$ of $G$ such that the product set $AB$ is not
all of $G$ and $A \cdot gBg^{-1} = gBg^{-1} \cdot A$ for every $g \in G$, where products of
subgroups are products of subsets of $G$. So the conjecture of Kourovka Problem 10.66 is false.

Bludov's example takes a simple linearly ordered group $G$ and nontrivial proper convex subgroups
$A$ and $B$. Conjugates of convex subgroups are convex and the convex subgroups form a chain, so
$A \cdot gBg^{-1}$ and $gBg^{-1} \cdot A$ both equal the larger of $A$ and $gBg^{-1}$, and
$AB \ne G$. Such subgroups exist: a nontrivial simple ordered group is not archimedean
(archimedean ordered groups are abelian, by Hölder), so it has nontrivial proper convex subgroups.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.66 (A. N. Fomin, V. P. Shunkov); resolution: V. V. Bludov, letter of 12 February 1997, recorded in the Kourovka Archive, Problem 10.66, Archive answer: "No; for example, for G being any simple linearly ordered group and A and B arbitrary proper convex subgroups of G".

Stated but not proved: `MathlibExt.GroupTheory.PermutingConjugatesSimpleGroupKourovka10Problem66Wanted.permutingConjugatesNotSimple_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/PermutingConjugatesSimpleGroupKourovka10Problem66Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PermutingConjugatesSimpleGroupKourovka10Problem66Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroups-permuting-with-their-conjugates/index.html#permuting-conjugates-not-simple-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgroups permuting with their conjugates](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroups-permuting-with-their-conjugates/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/subgroup-embedding/subgroups-permuting-with-their-conjugates)
