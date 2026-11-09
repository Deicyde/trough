# Small category

A **small category** is a [category](category.md) whose objects form a set and whose
morphisms form a set, rather than a proper class. Smallness is the size condition
under which a category can be handled like any other set-sized mathematical
object: diagrams are indexed by small categories, functors from a small category to a
locally small category form a locally small category, and categories of presheaves on a small category
are the setting of sheaf theory. The categories that collect every structure of a
given kind, such as all sets or all groups, are not small, and the distinction
between the two kinds of category runs through the whole subject.

## Definition

A category $C$ is **small** if its objects form a set and the collection of all
its morphisms forms a set. Since the morphisms are the union of the hom-sets
$\operatorname{Hom}(X, Y)$ over all pairs of objects, this is the same as asking
that the objects form a set and that each $\operatorname{Hom}(X, Y)$ is a set. A
category is **locally small** if every $\operatorname{Hom}(X, Y)$ is a set, with no
condition on the objects, and **large** if it is not small.

The words set and class depend on the foundations. In a set theory with classes,
small means set-sized. In a framework with a Grothendieck universe $\mathcal U$,
a category is $\mathcal U$-small when its objects and morphisms form sets that are
elements of $\mathcal U$. Mathlib's type theory has a hierarchy of universes that
plays the same role: there [a small category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.SmallCategory)
is one whose objects and morphisms lie in the same universe $u$, while
[a large category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.LargeCategory) has its objects one universe
higher than its morphisms.

## Examples

- **Finite categories.** Any category with finitely many morphisms is small, for
  instance the category with two objects and a single non-identity arrow between
  them.
- **Preorders.** A set $P$ with a preorder $\le$ is
  [a small category with a morphism from $x$ to $y$ exactly when $x \le y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Preorder.html#Preorder.smallCategory);
  reflexivity gives the identities, transitivity gives composition, and
  [there is at most one morphism between two objects](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Preorder.html#Preorder.subsingleton_hom).
- **Monoids.** A monoid $M$ gives
  [a category with one object whose morphisms are the elements of $M$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/SingleObj.html#CategoryTheory.SingleObj.category),
  the composite $g \circ f$ being the product $gf$ and the identity being the unit. A
  [group](../group-theory/part-01/group.md) gives in this way a one-object category in which every
  morphism is invertible.
- **Sets.** Any set $S$ is
  [a small category whose only morphisms are identities](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Discrete/Basic.html#CategoryTheory.discreteCategory),
  the discrete category on $S$.
- **Functor categories.** For categories $C$ and $D$,
  [the functors from $C$ to $D$ and the natural transformations between them form a category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Functor/Category.html#CategoryTheory.Functor.category).
  When $C$ and $D$ are small, so is this category: a [functor](functor.md) between small categories
  is a set-sized piece of data, and a [natural transformation](natural-transformation.md) is a family of morphisms
  indexed by the set of objects of $C$.

The category of all sets, the category of all groups and the category of all
topological spaces are locally small but not small, since their objects form a
proper class. In Mathlib's terms,
[the types of a universe $u$ with functions between them form a category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Types/Basic.html#CategoryTheory.types)
whose morphisms lie in $u$ while the collection of objects lies in the next
universe, so this category is large.

## Properties

- **The category of small categories.** Small categories and functors form a
  category. It is not itself small, because it contains the discrete category on
  every set.
- **Small limits.** A category is complete when every diagram indexed by a small
  category has a [limit](limits.md). The categories of sets and of groups are complete.
  Mathlib asks for
  [limits of every diagram indexed by a small category in the universe of the target's morphisms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Limits/HasLimits.html#CategoryTheory.Limits.HasLimits).
- **Small complete categories are preorders.** If a small category $C$ has all
  products indexed by sets, then between two objects $X$ and $Y$ there is at most
  one morphism. Indeed, let $\kappa$ be the cardinality of the set of all
  morphisms of $C$ and suppose $\operatorname{Hom}(X, Y)$ had two elements.
  Morphisms from $X$ to the product of $\kappa$ copies of $Y$ correspond to
  $\kappa$-tuples of morphisms from $X$ to $Y$, so there would be at least
  $2^\kappa$ of them, more than $\kappa$ by
  [Cantor's theorem](../../../hundred-theorems/part-03/cantors-theorem.md), although all of
  them are among the $\kappa$ morphisms of $C$.
  Completeness is therefore a severe restriction on small categories, and the
  interesting complete categories are large.
- **Presheaves.** For a small category $C$ the presheaves on $C$, the functors
  from the opposite category of $C$ to sets, form a locally small category, since a
  natural transformation between two presheaves is a family of functions indexed by
  a set. The [Yoneda embedding](yoneda-embedding.md) embeds $C$ into this category, and sheaves for a
  [Grothendieck topology](grothendieck-topology.md) on a small category form a full subcategory of it.

## Essentially small categories

Many large categories are small up to equivalence. A category is
[essentially small](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/EssentiallySmall.html#CategoryTheory.EssentiallySmall) if it is equivalent to a
small category. The category of finite sets is an example: its objects form a
proper class, but every finite set is [isomorphic](isomorphism.md) to $\{1, \dots, n\}$ for some
$n$, so the full subcategory on these sets is small and equivalent to the whole.
In general, relative to a universe,
[a category is essentially small if and only if its isomorphism classes of objects form a small set and it is locally small](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/EssentiallySmall.html#CategoryTheory.essentiallySmall_iff),
where [locally small](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/EssentiallySmall.html#CategoryTheory.LocallySmall) means that every hom-set
is small. Since smallness is measured against a universe,
[every category is essentially small relative to a universe that contains its objects and its morphisms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/EssentiallySmall.html#CategoryTheory.essentiallySmallSelf).

## In Mathlib

A category in Mathlib carries two independent universe levels, one for the type of
objects and one for the morphisms. A small category is not a separate structure
but the name for a category in which the two levels agree, so every small category
is a category without conversion. Most of the library is stated for an arbitrary
pair of levels, and smallness appears only where a result needs it, for example for
the shapes of diagrams. A small category is small relative to the universe of its
own objects; essentially small and locally small take the universe they measure
against as a universe parameter. The one-object category of a monoid keeps its single object in the
lowest universe, so it fits the small pattern literally only for a monoid in that
universe, although it is small in the set-theoretic sense in every case. Mathlib's
[category of categories](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Cat.html#CategoryTheory.Cat) is indexed by both levels, and
the small categories of level $u$ are the case where they coincide. The theorem on
small complete categories is an unnamed instance stating that a small category with
all products of its own size has at most one morphism between any two objects; it
concludes this about the hom-sets rather than producing a preorder.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Category](category.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-03/cantors-theorem.md)
- [Limits](limits.md)

## Sources

- [Mathlib documentation: `CategoryTheory.SmallCategory`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.SmallCategory)
- [Source of `CategoryTheory.SmallCategory` in Mathlib/CategoryTheory/Category/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/CategoryTheory/Category/Basic.lean#L261)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L4)
