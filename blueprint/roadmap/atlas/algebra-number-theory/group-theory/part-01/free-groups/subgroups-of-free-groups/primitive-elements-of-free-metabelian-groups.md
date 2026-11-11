---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.FreeMetabelianGroup, MathlibExt.GroupTheory.FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.IsPrimitive, MathlibExt.GroupTheory.FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.primitivePreservingEndomorphismIsAutomorphism, MathlibExt.GroupTheory.FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.primitivePreservingEndomorphismIsAutomorphism_holds
statement: formalized
---

# Primitive elements of free metabelian groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/primitive-elements-of-free-metabelian-groups/index.html).

## Free metabelian group $M_n$ (Kourovka 14.85)

For a natural number $n$, the free metabelian
group $M_n = F_n / F_n''$ of rank $n$: the quotient of the free group $F_n$ on $n$ generators by
its second derived subgroup $F_n'' = [[F_n, F_n], [F_n, F_n]]$.

Formalized by `MathlibExt.GroupTheory.FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.FreeMetabelianGroup`, an abbreviation declared in [WantedExt/GroupTheory/FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/primitive-elements-of-free-metabelian-groups/index.html#free-metabelian-group).

## Primitive elements of the free metabelian group

Let $F_n$ be the free group on $n$
generators, let $F_n''$ be its second derived subgroup, and let $M_n = F_n / F_n''$ be the free
metabelian group of rank $n$. Let $x_0, \dots, x_{n-1}$ be the images in $M_n$ of the free
generators of $F_n$. An element $y$ of $M_n$ is primitive when $y = \sigma(x_i)$ for some
automorphism $\sigma$ of $M_n$ and some index $i$; that is, $y$ is the image of a standard basis
element under an automorphism of $M_n$.

Formalized by `MathlibExt.GroupTheory.FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.IsPrimitive`, a definition declared in [WantedExt/GroupTheory/FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/primitive-elements-of-free-metabelian-groups/index.html#is-primitive).

## Primitive-preserving endomorphism problem for free metabelian groups (Kourovka 14.85)

The statement, posed by E. I. Timoshenko and V. Shpilrain, that for every natural number $n$,
every endomorphism $\varphi$ of the free metabelian group $M_n$ of rank $n$ that maps every
primitive element of $M_n$ to a primitive element is bijective, hence an automorphism.

Formalized by `MathlibExt.GroupTheory.FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.primitivePreservingEndomorphismIsAutomorphism`, a definition declared in [WantedExt/GroupTheory/FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/primitive-elements-of-free-metabelian-groups/index.html#primitive-preserving-endomorphism-is-aut).

## Primitive-preserving endomorphisms of free metabelian groups are automorphisms

For every
natural number $n$, every endomorphism $\varphi$ of the free metabelian group $M_n$ of rank $n$
that maps every primitive element of $M_n$ to a primitive element is bijective, hence an
automorphism of $M_n$. This answers Kourovka Problem 14.85 positively.

Ionin and Semidetnov (Section 1, Answer 1.2) prove that every primitive-preserving endomorphism of
the free metabelian group $M_n$ is an automorphism; the Kourovka Notebook (21st issue) answers
Problem 14.85 "Yes, it is".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.85 (E. I. Timoshenko, V. Shpilrain); resolution: V. Ionin and A. Semidetnov, On some more problems from the Kourovka Notebook, preprint, arXiv:2608.29219 (2026), Section 1, Answer 1.2: every primitive-preserving endomorphism of M_n is an automorphism (the abstract states that the solutions were found with the assistance of large language models and checked by the authors); the Kourovka Notebook (21st issue) marks 14.85 solved (Yes, it is), https://arxiv.org/abs/2608.29219.

Stated but not proved: `MathlibExt.GroupTheory.FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.primitivePreservingEndomorphismIsAutomorphism_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeMetabelianPrimitivePreservingKourovka14Problem85Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/primitive-elements-of-free-metabelian-groups/index.html#primitive-preserving-endomorphism-is-aut-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primitive elements of free metabelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/primitive-elements-of-free-metabelian-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/primitive-elements-of-free-metabelian-groups)
