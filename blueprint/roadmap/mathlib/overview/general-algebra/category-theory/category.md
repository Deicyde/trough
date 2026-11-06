# Category

A **category** consists of objects and of arrows, called morphisms, between them, together with
a rule for composing arrows end to end that is associative and has an identity arrow at every
object. Sets with functions, groups with homomorphisms, and topological spaces with continuous
maps are all categories. The notion lets constructions and arguments that recur across algebra,
topology and logic be stated once, in terms of how objects relate to one another rather than what
they are made of, and it is the starting point of category theory.

## Definition

A [category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.Category) $\mathcal{C}$ consists of

- a collection of objects;
- for every two objects $X$ and $Y$, a collection $\operatorname{Hom}(X, Y)$ of morphisms from $X$
  to $Y$, a morphism $f$ in it being written $f\colon X \to Y$;
- for every object $X$, an identity morphism $1_X\colon X \to X$;
- for every three objects $X, Y, Z$, a composition rule sending $f\colon X \to Y$ and
  $g\colon Y \to Z$ to a morphism $g \circ f\colon X \to Z$.

These are required to satisfy three axioms. For $f\colon X \to Y$, the identities are neutral:
[$f \circ 1_X = f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.Category.id_comp) and
[$1_Y \circ f = f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.Category.comp_id). For $f\colon W \to X$,
$g\colon X \to Y$ and $h\colon Y \to Z$, composition is associative:
[$h \circ (g \circ f) = (h \circ g) \circ f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.Category.assoc).

The objects of a category need not form a set; the objects of the category of all sets do not.
A category whose objects and morphisms together form a set is called a
[small category](small-category.md), and one in which each
$\operatorname{Hom}(X, Y)$ is a set is called locally small.

## Examples

- **Sets.** Sets as objects and functions as morphisms, with the usual composition of functions,
  form [a category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Types/Basic.html#CategoryTheory.types).
- **Algebraic and topological structures.** Groups with group homomorphisms, rings with
  [ring homomorphisms](../rings/ring-morphism.md), modules over a ring with linear maps, and topological
  spaces with [continuous maps](../../topology/general-topology/part-01/continuous-function.md) each form a category; see
  [the category of rings](../rings/the-category-of-rings.md), [the category of modules](../../linear-algebra/fundamentals/the-category-of-modules-over-a-ring.md) and
  [the category of topological spaces](../../topology/general-topology/part-01/the-category-of-topological-spaces.md).
- **Monoids.** A monoid $M$ gives [a category with a single object whose morphisms are the elements of $M$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/SingleObj.html#CategoryTheory.SingleObj.category), in which
  [the composite of $f$ followed by $g$ is the product $g f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/SingleObj.html#CategoryTheory.SingleObj.comp_as_mul)
  and the identity morphism is the unit. When $M$ is a group every morphism has an inverse.
- **Preorders.** A preordered set $(P, \le)$ is
  [a category with a morphism from $x$ to $y$ exactly when $x \le y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Preorder.html#Preorder.smallCategory);
  composition expresses transitivity and the identities express reflexivity, and
  [there is at most one morphism between two objects](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Preorder.html#Preorder.subsingleton_hom).
- **Discrete categories.** Any set becomes
  [a category whose only morphisms are the identities](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Discrete/Basic.html#CategoryTheory.discreteCategory).
- **Opposite categories.** Keeping the objects of $\mathcal{C}$ and reversing the direction of
  every morphism gives [a category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Opposites.html#CategoryTheory.Category.opposite), the opposite category
  $\mathcal{C}^{\mathrm{op}}$.
- **Products.** For categories $\mathcal{C}$ and $\mathcal{D}$, pairs of objects and pairs of
  morphisms, composed componentwise, form [the product category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Products/Basic.html#CategoryTheory.prod')
  $\mathcal{C} \times \mathcal{D}$.

## Basic notions

- **Uniqueness of identities.** If a morphism $e\colon X \to X$ satisfies $g \circ e = g$ for every
  morphism $g$ out of $X$, then [$e$ is the identity $1_X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.id_of_comp_left_id).
  So the identities are determined by the composition.
- **Isomorphisms.** An [isomorphism](isomorphism.md) is
  [a morphism $f\colon X \to Y$ together with a morphism $g\colon Y \to X$ such that $g \circ f = 1_X$ and $f \circ g = 1_Y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Iso.html#CategoryTheory.Iso). The inverse is unique: if $f$
  is an isomorphism and $g \circ f = 1_X$, then
  [$g$ is the inverse of $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Iso.html#CategoryTheory.Iso.inv_ext). In the category of sets,
  [a function is an isomorphism exactly when it is bijective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Types/Basic.html#CategoryTheory.isIso_iff_bijective).
- **Monomorphisms and epimorphisms.** A morphism $f\colon X \to Y$ is a monomorphism if
  [$f \circ g = f \circ h$ implies $g = h$ for all morphisms $g, h$ into $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.Mono),
  and an epimorphism if
  [$g \circ f = h \circ f$ implies $g = h$ for all morphisms $g, h$ out of $Y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.Epi).
  In the category of sets
  [the monomorphisms are exactly the injective functions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Types/Basic.html#CategoryTheory.mono_iff_injective)
  and [the epimorphisms are exactly the surjective functions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Types/Basic.html#CategoryTheory.epi_iff_surjective).
  In other categories the analogy can fail: in the category of rings the inclusion of the integers
  into the rationals is an epimorphism without being surjective.
- **Duality.** A monomorphism in $\mathcal{C}$ is the same thing as an epimorphism in
  $\mathcal{C}^{\mathrm{op}}$. More generally, each statement expressed in terms of objects, morphisms,
  composition and identities has a dual, obtained by reversing every arrow and the order of every composite, and if a statement
  holds in every category then so does its dual.

## Related concepts

Maps between categories that preserve identities and composition are
[functors](functor.md), and maps between functors are
[natural transformations](natural-transformation.md). These lead to the
[Yoneda embedding](yoneda-embedding.md), [adjunctions](adjunction.md),
[limits](limits.md) and [monads](monad.md). Categories
with extra structure include [monoidal categories](monoidal-category.md) and
[abelian categories](abelian-category.md), and new categories are built from old ones
as [comma categories](comma-category.md).

## In Mathlib

Mathlib makes a category structure on a type of objects: for each pair of objects there is a type
of morphisms, so every category is locally small with respect to the universe in which its
morphisms live, and the universes of objects and of morphisms are independent parameters. The
structure is split in two:
[the data of identities and composition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.CategoryStruct), which extends
[a quiver](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Quiver/Basic.html#Quiver) (a directed graph that may have several arrows between two vertices), and
the three axioms on top of it. Composition is written in diagrammatic order, first $f$ then $g$,
so Mathlib's form of $f \circ 1_X = f$ puts the identity first. An isomorphism is a structure
carrying its inverse as data, while being invertible is a separate property of a morphism, the
one used in the statement about bijections above; the two are interchangeable, since an
invertible morphism determines its inverse. The category of sets is modelled by the category of
types of a fixed universe, whose morphisms are functions wrapped in a one-field structure, so
that they correspond exactly to functions. In the one-object category of a monoid, following first $f$ and then $g$
is the product $g f$, which agrees with the convention used above.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Category`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.Category)
- [Source of `CategoryTheory.Category` in Mathlib/CategoryTheory/Category/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Category/Basic.lean#L226)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L3)
