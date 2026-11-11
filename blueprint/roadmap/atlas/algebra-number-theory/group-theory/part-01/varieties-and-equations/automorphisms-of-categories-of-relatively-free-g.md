---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.relativelyFreeGroup, MathlibExt.GroupTheory.VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.ThetaZero, MathlibExt.GroupTheory.VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.existsVarietyWithNonInnerCategoryAutomorphism, MathlibExt.GroupTheory.VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.existsVarietyWithNonInnerCategoryAutomorphism_holds
statement: formalized
---

# Automorphisms of categories of relatively free groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/automorphisms-of-categories-of-relatively-free-g/index.html).

## Free group of a variety on a finite set

Let $W$ be a set of words in the free group
$F(\mathbb{N})$ on $x_0, x_1, \ldots$, defining a variety $\Theta$, and let $X \subseteq \mathbb{N}$
be finite. The free group $F_\Theta(X)$ of $\Theta$ on $X$ is the quotient of the free group $F(X)$
on $X$ by its verbal subgroup, the normal closure of the set of values $\varphi(w)$ with $w \in W$
and $\varphi \colon F(\mathbb{N}) \to F(X)$ a homomorphism. This set of values is closed under
conjugation, so the verbal subgroup is also the subgroup it generates.

Formalized by `MathlibExt.GroupTheory.VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.relativelyFreeGroup`, an abbreviation declared in [WantedExt/GroupTheory/VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/automorphisms-of-categories-of-relatively-free-g/index.html#relatively-free-group).

## Plotkin's category of free groups of a variety

Let $W$ be a set of words in the free group
on $x_0, x_1, \ldots$, defining a variety $\Theta$. The category $\Theta^0$ has one object for each
finite subset $X$ of $X^0 = \mathbb{N}$, namely the free group $F_\Theta(X)$ of $\Theta$ on $X$, and
its morphisms are all group homomorphisms between these groups.

Formalized by `MathlibExt.GroupTheory.VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.ThetaZero`, an abbreviation declared in [WantedExt/GroupTheory/VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/automorphisms-of-categories-of-relatively-free-g/index.html#theta-zero).

## Plotkin's question on outer automorphisms of the category of free groups of a variety

The
statement that there is a set $W$ of words in the free group on $x_0, x_1, \ldots$ such that, for
the variety $\Theta$ with laws $W$, the category $\Theta^0$ of the free groups of $\Theta$ on the
finite subsets of $\mathbb{N}$ has an automorphism that is not inner: functors
$\Phi, \Psi \colon \Theta^0 \to \Theta^0$ whose composites $\Psi \circ \Phi$ and $\Phi \circ \Psi$
both equal the identity functor, with $\Phi$ not naturally isomorphic to the identity functor.
This is Kourovka Notebook Problem 20.72 (E. Plotkin).

Formalized by `MathlibExt.GroupTheory.VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.existsVarietyWithNonInnerCategoryAutomorphism`, a definition declared in [WantedExt/GroupTheory/VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/automorphisms-of-categories-of-relatively-free-g/index.html#exists-variety-with-non-inner-category-a).

## Some variety of groups has an outer automorphism of its category of free groups

There is a
set $W$ of words in the free group on $x_0, x_1, \ldots$ such that, for the variety $\Theta$ with
laws $W$, the category $\Theta^0$, whose objects are the free groups $F_\Theta(X)$ of $\Theta$ on
the finite subsets $X \subseteq \mathbb{N}$ and whose morphisms are all group homomorphisms, has an
automorphism that is not inner: there are functors $\Phi, \Psi \colon \Theta^0 \to \Theta^0$ whose
composites $\Psi \circ \Phi$ and $\Phi \circ \Psi$ both equal the identity functor, and $\Phi$ is
not naturally isomorphic to the identity functor.

Barbosa Fernandes and Tsurkov (Theorem 9.1) show that for the variety of metabelian groups of
exponent $4$ and nilpotency class at most $4$ (laws $x^4 = 1$, $((x_1, x_2), (x_3, x_4)) = 1$ and
$((((x_1, x_2), x_3), x_4), x_5) = 1$) the group of automorphisms of $\Theta^0$ modulo the inner
ones has order $2$. The 21st issue of the Kourovka Notebook marks 20.72 solved ("Yes, there is").

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.72 (E. Plotkin); resolution: R. Barbosa Fernandes and A. Tsurkov, Automorphisms of the category of finitely generated free groups of the some subvariety of the variety of all groups, preprint, arXiv:1909.05955 (2019), Theorem 9.1: for the variety Θ defined by x⁴ = 1, ((x₁, x₂), (x₃, x₄)) = 1 and ((((x₁, x₂), x₃), x₄), x₅) = 1, the quotient A/Y of the automorphism group of Θ⁰ by the inner automorphisms has order 2; Kourovka Notebook (21st issue), Problem 20.72: Yes, there is, https://arxiv.org/abs/1909.05955.

Stated but not proved: `MathlibExt.GroupTheory.VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.existsVarietyWithNonInnerCategoryAutomorphism_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/VarietyCategoryOuterAutomorphismKourovka20Problem72Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/automorphisms-of-categories-of-relatively-free-g/index.html#exists-variety-with-non-inner-category-a-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Automorphisms of categories of relatively free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/automorphisms-of-categories-of-relatively-free-g/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/varieties-and-equations/automorphisms-of-categories-of-relatively-free-g)
