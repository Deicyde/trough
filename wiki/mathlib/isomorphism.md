---
article_id: af_f5880a97e21f478109c1f58e
concept: CategoryTheory.Iso
---

An **isomorphism** in a [category](trough:CategoryTheory.Category) is a morphism that can be
undone: a morphism $f\colon X \to Y$ for which there is a morphism back from $Y$ to $X$ whose
composites with $f$, in either order, are identities. Two objects joined by an isomorphism are
indistinguishable by anything the category can express, so isomorphism, rather than equality, is
the natural notion of sameness for objects. It specializes to bijections of sets, isomorphisms of
groups and rings, and homeomorphisms of spaces.

## Definition

Let $X$ and $Y$ be objects of a category $\mathcal{C}$. An isomorphism from $X$ to $Y$ is
[a morphism $f\colon X \to Y$ for which there is a morphism $g\colon Y \to X$ with
$g \circ f = 1_X$ and $f \circ g = 1_Y$](lean:CategoryTheory.Iso). The morphism $g$ is the
inverse of $f$, written
$f^{-1}$. The objects $X$ and $Y$ are called isomorphic, written $X \cong Y$, when some
isomorphism between them exists.

The inverse is determined by $f$, and even one of the two equations pins it down: if $f$ is an
isomorphism and a morphism $h\colon Y \to X$ satisfies $h \circ f = 1_X$, then
[$h$ is the inverse of $f$](lean:CategoryTheory.Iso.inv_ext). Consequently
[two isomorphisms with the same forward morphism are equal](lean:CategoryTheory.Iso.ext), and
being an isomorphism is a property of a morphism rather than extra data.

## Examples

- **Sets.** In the category of sets and functions,
  [a function is an isomorphism exactly when it is bijective](lean:CategoryTheory.isIso_iff_bijective);
  its inverse is the inverse function.
- **Algebraic structures.** In a concrete category whose forgetful functor to sets reflects
  isomorphisms, as for groups with group homomorphisms or rings with ring homomorphisms,
  [a morphism is an isomorphism exactly when its underlying function is
  bijective](lean:CategoryTheory.ConcreteCategory.isIso_iff_bijective). For groups this recovers
  the usual notion: a bijective [group morphism](trough:MonoidHom) has a homomorphic inverse.
- **Topological spaces.** In the [category of topological spaces](trough:TopCat), with
  [continuous maps](trough:Continuous) as morphisms,
  [the isomorphisms are exactly the homeomorphisms](lean:TopCat.isIso_iff_isHomeomorph) (see
  [homeomorphism](trough:Homeomorph)). Here bijectivity is not enough: the identity function from
  a two-point set with the discrete topology to the same set with the indiscrete topology is a
  continuous bijection whose inverse is not continuous.
- **Preorders.** In a category with at most one morphism between any two objects, such as a
  preordered set viewed as a category,
  [a morphism from $x$ to $y$ is an isomorphism exactly when some morphism from $y$ to $x$
  exists](lean:CategoryTheory.isIso_iff_of_thin). So $x \cong y$ means $x \le y$ and $y \le x$,
  and in a partially ordered set isomorphic objects are equal.
- **Monoids.** In the one-object category of a monoid $M$, the isomorphisms are the invertible
  elements of $M$.

## Properties

- **Identities, inverses and composites.** For each object $X$,
  [the identity $1_X$ is an isomorphism](lean:CategoryTheory.IsIso.id); the inverse $f^{-1}$ of an
  isomorphism [is an isomorphism with inverse $f$](lean:CategoryTheory.Iso.symm); and if
  $f\colon X \to Y$ and $g\colon Y \to Z$ are isomorphisms,
  [so is $g \circ f$](lean:CategoryTheory.Iso.trans), with
  [$(g \circ f)^{-1} = f^{-1} \circ g^{-1}$](lean:CategoryTheory.IsIso.inv_comp). Hence
  [being isomorphic is an equivalence relation on objects](lean:CategoryTheory.isIsomorphicSetoid).
- **Automorphisms.** The isomorphisms from an object $X$ to itself, its
  [automorphisms](lean:CategoryTheory.Aut), form a group under composition. The automorphism group
  of a set is its [permutation group](trough:Equiv.Perm).
- **Functors.** Every [functor](trough:CategoryTheory.Functor) $F$ preserves isomorphisms:
  [if $f$ is an isomorphism then so is $F(f)$](lean:CategoryTheory.Functor.map_isIso), with
  inverse $F(f^{-1})$. The converse fails in general, but if $F$ is full and faithful and $F(f)$
  is an isomorphism, then [$f$ is an isomorphism](lean:CategoryTheory.isIso_of_fully_faithful).
- **Cancellation.** An isomorphism is both a
  [monomorphism](lean:CategoryTheory.IsIso.mono_of_iso) and an
  [epimorphism](lean:CategoryTheory.IsIso.epi_of_iso): it can be cancelled from either side of an
  equation between composites. The converse fails in some categories: in the category of rings the
  inclusion of the integers into the rationals is a monomorphism and an epimorphism but not an
  isomorphism. A category in which every morphism that is both is an isomorphism is called
  balanced; there
  [the isomorphisms are exactly the morphisms that are monomorphisms and
  epimorphisms](lean:CategoryTheory.isIso_iff_mono_and_epi). The category of sets is balanced.

## Related concepts

A category in which every morphism is an isomorphism is a
[groupoid](lean:CategoryTheory.Groupoid); a group amounts to a groupoid with a single object. An isomorphism in
the category of functors from $\mathcal{C}$ to $\mathcal{D}$, whose morphisms are
[natural transformations](trough:CategoryTheory.NatTrans), is a natural isomorphism, and
[a natural transformation is an isomorphism exactly when each of its components
is](lean:CategoryTheory.NatTrans.isIso_iff_isIso_app). Weakening the equations
$g \circ f = 1$ and $f \circ g = 1$ to natural isomorphisms between functors leads to equivalences
of categories. The isomorphism theorems of algebra, such as the
[first isomorphism theorem](trough:QuotientGroup.quotientKerEquivRange), produce particular
isomorphisms between groups.

## In Mathlib

Mathlib treats an isomorphism as bundled data: a structure holding the forward morphism, the
inverse morphism and the two equations. Separately, the property of a single morphism being an
isomorphism is a proposition that only asserts that some inverse exists; the inverse is then
recovered by choice, which is harmless because it is unique. Composition is written in diagrammatic
order, first $f$ then $g$, so Mathlib's form of $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ lists
$g^{-1}$ first. Many familiar isomorphisms, such as bijections between types, group isomorphisms
and homeomorphisms, are also defined directly as structures of their own, outside category theory,
and Mathlib provides translations between those and isomorphisms in the corresponding categories.
The dual statement that an isomorphism is a monomorphism is generated automatically from the one
about epimorphisms.

## Depends on

- [Category](trough:CategoryTheory.Category)
