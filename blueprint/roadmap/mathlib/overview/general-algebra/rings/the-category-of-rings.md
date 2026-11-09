# The category of rings

The **category of rings**, usually written $\mathbf{Ring}$, is the
[category](../category-theory/category.md) whose objects are
[rings](ring.md) and whose morphisms are [ring morphisms](ring-morphism.md).
Viewing rings this way puts constructions such as products, quotients and
[polynomial rings](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) in a common language of universal properties, and lets one
compare rings with other algebraic structures through
[functors](../category-theory/functor.md), for instance the functor that
forgets the multiplication of a ring and remembers only its additive group.

## Definition

Here a ring is associative and has a multiplicative identity $1$, but need not
be commutative, and a ring morphism $f \colon R \to S$ preserves addition,
multiplication and the identity: $f(1) = 1$. Mathlib defines
[the category of rings](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat) with these data:

- an object is a ring $R$;
- [a morphism from $R$ to $S$ is a ring morphism $R \to S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat.Hom);
- the identity morphism of $R$ is
  [the identity map of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat.hom_id), and
  [the composite of $f \colon R \to S$ and $g \colon S \to T$ is the composite map $g \circ f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat.hom_comp).

The category axioms hold because composition of functions is associative and
the identity map is neutral for it.

## Examples

- **Initial and terminal objects.** For every ring $R$ there is exactly one
  ring morphism $\mathbb{Z} \to R$, sending $n$ to $n \cdot 1$, so the
  [integers](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md) form an initial object (one with exactly
  one morphism to every object). The zero ring, in which $0 = 1$, receives
  exactly one morphism from every ring, so it is a terminal object (one with
  exactly one morphism from every object). A zero object, one that is both
  initial and terminal, would be isomorphic to the zero ring, since terminal
  objects are unique up to isomorphism; but the zero ring is not initial, as
  there is no ring morphism from it to $\mathbb{Z}$. So $\mathbf{Ring}$ has no
  zero object.
- **Products and equalizers.** The product of a family of rings is their
  cartesian product with componentwise operations, together with the
  projections. The equalizer of two morphisms $f, g \colon R \to S$, the
  universal morphism into $R$ whose composites with $f$ and $g$ agree, is the
  inclusion of the [subring](subring.md) $\{ r \in R : f(r) = g(r) \}$.
- **Coproducts.** The coproduct of two rings, the universal ring receiving a
  morphism from each, is their free product, which need not be commutative
  even when both factors are commutative: the coproduct
  of $\mathbb{Z}[x]$ and $\mathbb{Z}[y]$ is the ring of polynomials in two
  non-commuting variables. For commutative rings the tensor product over
  $\mathbb{Z}$ is the coproduct only within the category of commutative rings.
- **Quotients.** For a two-sided ideal $I$ of $R$, the projection
  $R \to R/I$ onto the [quotient ring](../ideals-and-quotients/quotient-ring.md) is the
  universal morphism out of $R$ that sends every element of $I$ to $0$.

## Properties

- **Isomorphisms.** The [isomorphisms](../category-theory/isomorphism.md) of $\mathbf{Ring}$ are the ring
  isomorphisms: [every ring isomorphism is an isomorphism in the category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingEquiv.toRingCatIso),
  and [every isomorphism in the category yields a ring isomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#CategoryTheory.Iso.ringCatIsoToRingEquiv).
  Moreover,
  [a morphism whose underlying function is bijective is an isomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat.forgetReflectIsos),
  because the inverse function is automatically a ring morphism.
- **Monomorphisms and epimorphisms.** A monomorphism is a morphism $f$ that can
  be cancelled on the left: $f \circ g = f \circ h$ implies $g = h$; an
  epimorphism is one that can be cancelled on the right. A morphism
  $f \colon R \to S$ is a monomorphism exactly when it is injective. An
  injective morphism is clearly a monomorphism. Conversely, morphisms
  $\mathbb{Z}[x] \to R$ correspond to elements of $R$, by evaluation at $x$;
  the variable $x$ may be sent to any element, because the image of
  $\mathbb{Z}$ in $R$ commutes with everything. If $f(a) = f(b)$, the morphisms
  sending $x$ to $a$ and to $b$ have the same composite with $f$, so they are
  equal and $a = b$. Epimorphisms need not be surjective. The inclusion $\mathbb{Z} \to \mathbb{Q}$ is an epimorphism,
  since a ring morphism out of $\mathbb{Q}$ must send $1/n$, for $n \neq 0$, to the
  inverse of the image of $n$ and is therefore determined by its values on $\mathbb{Z}$.
- **Limits.** A [limit](../category-theory/limits.md) of a diagram is a universal object with compatible morphisms to every object of the diagram; products and equalizers are examples. [The category of rings has all small limits](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Limits.html#RingCat.hasLimits),
  and [the forgetful functor to sets preserves them](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Limits.html#RingCat.forget_preservesLimits):
  the underlying set of a limit of rings is the limit of the underlying sets,
  with the operations defined pointwise.
  [The same holds for the forgetful functor to abelian groups](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Limits.html#RingCat.forget%E2%82%82AddCommGroup_preservesLimits).
- **Colimits.** Colimits are the dual notion, with morphisms from the diagram into the universal object. [The category of rings has all small colimits](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Colimits.html#RingCat.Colimits.hasColimits_ringCat).
  The forgetful functor does not preserve them in general: the coproduct of
  $\mathbb{Z}$ with itself is $\mathbb{Z}$, since $\mathbb{Z}$ is initial, while
  the coproduct of the underlying sets, the disjoint union of two copies of
  $\mathbb{Z}$, maps onto $\mathbb{Z}$ by identifying the two copies, and this
  comparison map is not injective. It does
  [preserve filtered colimits](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/FilteredColimits.html#RingCat.FilteredColimits.forget_preservesFilteredColimits),
  colimits over nonempty diagrams in which any two objects map to a common one
  and any two parallel arrows are made equal by a further arrow, so a directed union of
  rings is computed on underlying sets.
- **Free rings.** The forgetful functor to sets has a left adjoint: a functor
  $F$ from sets to rings such that ring morphisms $F(X) \to R$ correspond to
  functions from $X$ to the underlying set of $R$, naturally in $X$ and $R$.
  It sends a set $X$ to the free ring on $X$, the ring of polynomials with
  integer coefficients in non-commuting variables indexed by $X$:
  [ring morphisms from the free ring on $X$ to a ring $R$ correspond bijectively to functions from $X$ to $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/FreeRing.html#FreeRing.lift),
  [the morphism attached to a function agrees with it on $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/FreeRing.html#FreeRing.lift_of),
  and [a morphism out of the free ring is determined by its values on $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/FreeRing.html#FreeRing.hom_ext).

## Related concepts

Commutative rings form a full subcategory of $\mathbf{Ring}$, one that keeps
every ring morphism between its objects. In other words,
[the forgetful functor from commutative rings to rings is fully faithful](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#CommRingCat.fullyFaithfulForget%E2%82%82ToRingCat):
it is bijective on each set of morphisms.
Likewise, [the forgetful functor from rings to semirings is fully faithful](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat.fullyFaithfulForget%E2%82%82ToSemiRingCat),
because a semiring morphism between rings automatically preserves additive
inverses. [Fields](../field-theory/field.md) form a further full subcategory, in which every morphism is
injective, because
[every ring morphism from a field to a nonzero ring is injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/SimpleRing/Basic.html#RingHom.injective). For a commutative ring $k$, the
[category of $k$-algebras](../algebras-over-a-ring/the-category-of-algebras-over-a-ring.md) maps to $\mathbf{Ring}$ by forgetting
the structure map, and every ring $R$ has its own
[category of modules](../../linear-algebra/fundamentals/the-category-of-modules-over-a-ring.md); a morphism of rings $R \to S$ turns
every $S$-module into an $R$-module by restriction of scalars.

## In Mathlib

Mathlib bundles each object as a type together with a ring structure on it.
Morphisms are wrapped in a separate structure rather than being ring morphisms
themselves, with translations in both directions:
[turning a ring morphism into a morphism of the category and back returns it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat.hom_ofHom),
and [turning a morphism into a ring morphism and back also returns it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat.ofHom_hom).
This keeps the category's composition, written in diagrammatic order, apart
from the composition of functions. The category is indexed by a universe
level: it contains the rings whose underlying type lives in a fixed universe,
and "small" limits and colimits are those indexed by categories of that size.
Commutative rings, semirings and commutative semirings each have a parallel
category, with forgetful functors between them.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](ring.md)
- [Ring morphism](ring-morphism.md)
- [Category](../category-theory/category.md)

## Sources

- [Mathlib documentation: `RingCat`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Basic.html#RingCat)
- [Source of `RingCat` in Mathlib/Algebra/Category/Ring/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Category/Ring/Basic.lean#L188)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L67)
