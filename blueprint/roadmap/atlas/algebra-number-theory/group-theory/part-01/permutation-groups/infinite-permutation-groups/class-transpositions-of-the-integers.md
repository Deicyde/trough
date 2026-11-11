---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.resClass, MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.IsClassTrans, MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.IsClassTransposition, MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.classTranspositionProductOrdersFinite, MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.classTranspositionProductOrdersFinite_holds
statement: formalized
---

# Class transpositions of the integers

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/class-transpositions-of-the-integers/index.html).

## Residue class

For integers $r$ and $m$, the residue class $r(m)$ is the set
$\{x \in \mathbb{Z} : x \equiv r \pmod{m}\} = \{r + k m : k \in \mathbb{Z}\}$.

Formalized by `MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.resClass`, a definition declared in [WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/class-transpositions-of-the-integers/index.html#res-class).

## Class transposition of two residue classes

For integers $r_1, m_1, r_2, m_2$, write
$r_1(m_1) = r_1 + m_1\mathbb{Z}$ and $r_2(m_2) = r_2 + m_2\mathbb{Z}$ for the residue classes. A
permutation $\sigma$ of $\mathbb{Z}$ is the class transposition $\tau_{r_1(m_1), r_2(m_2)}$ when
$0 \le r_1 < m_1$ and $0 \le r_2 < m_2$, the residue classes $r_1(m_1)$ and $r_2(m_2)$ are
disjoint, $\sigma$ interchanges $r_1 + k m_1$ and $r_2 + k m_2$ for every integer $k$, and
$\sigma$ fixes every integer outside $r_1(m_1) \cup r_2(m_2)$.

This is the definition of class transpositions in Kourovka Problem 17.57.

Formalized by `MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.IsClassTrans`, a definition declared in [WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/class-transpositions-of-the-integers/index.html#is-class-trans).

## Class transpositions of the integers

A permutation $\sigma$ of $\mathbb{Z}$ is a class
transposition when it is the class transposition $\tau_{r_1(m_1), r_2(m_2)}$ for some integers
$r_1, m_1, r_2, m_2$.

Formalized by `MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.IsClassTransposition`, a definition declared in [WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/class-transpositions-of-the-integers/index.html#is-class-transposition).

## Claim of Kourovka Problem 18.48

Only finitely many positive integers occur as orders of
products $\sigma\tau$ of two class transpositions $\sigma$ and $\tau$ of $\mathbb{Z}$.

Formalized by `MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.classTranspositionProductOrdersFinite`, a definition declared in [WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/class-transpositions-of-the-integers/index.html#class-transposition-product-orders-finit).

## Products of two class transpositions have only finitely many orders

The claim of Kourovka
Problem 18.48 holds: the set of positive integers $k$ such that $\sigma\tau$ has order $k$ for some
class transpositions $\sigma$ and $\tau$ of $\mathbb{Z}$ is finite.

Iskra (2026), accepted in the Kourovka Notebook (21st issue), proves that every finite order of a
product of two class transpositions divides $840$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.48 (S. Kohl); resolution: A. Iskra, Finite orders of products of two class transpositions divide 840, preprint, arXiv:2610.01793 (2026), abstract: if the product of two class transpositions has finite order, then its order divides 840 (sharp); this answers Question 18.48 affirmatively, as the Kourovka Notebook (21st issue) records, https://arxiv.org/abs/2610.01793.

Stated but not proved: `MathlibExt.GroupTheory.ClassTranspositionProductOrdersKourovka18Problem48Wanted.classTranspositionProductOrdersFinite_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassTranspositionProductOrdersKourovka18Problem48Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/class-transpositions-of-the-integers/index.html#class-transposition-product-orders-finit-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Class transpositions of the integers](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/class-transpositions-of-the-integers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/class-transpositions-of-the-integers)
