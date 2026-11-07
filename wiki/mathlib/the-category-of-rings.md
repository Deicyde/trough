The **category of rings**, usually written $\mathbf{Ring}$, is the
[category](trough:CategoryTheory.Category) whose objects are
[rings](trough:Ring) and whose morphisms are [ring morphisms](trough:RingHom).
Viewing rings this way puts constructions such as products, quotients and
[polynomial rings](trough:Polynomial) in a common language of universal properties, and lets one
compare rings with other algebraic structures through
[functors](trough:CategoryTheory.Functor), for instance the functor that
forgets the multiplication of a ring and remembers only its additive group.

## Definition

Here a ring is associative and has a multiplicative identity $1$, but need not
be commutative, and a ring morphism $f \colon R \to S$ preserves addition,
multiplication and the identity: $f(1) = 1$. Mathlib defines
the category of rings with these data:

- an object is a ring $R$;
- a morphism from $R$ to $S$ is a ring morphism $R \to S$;
- the identity morphism of $R$ is
  the identity map of $R$, and
  the composite of $f \colon R \to S$ and $g \colon S \to T$ is the composite map $g \circ f$.

The category axioms hold because composition of functions is associative and
the identity map is neutral for it.

## Examples

- **Initial and terminal objects.** For every ring $R$ there is exactly one
  ring morphism $\mathbb{Z} \to R$, sending $n$ to $n \cdot 1$, so the
  [integers](trough:Int.instCommRing) form an initial object (one with exactly
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
  inclusion of the [subring](trough:Subring) $\{ r \in R : f(r) = g(r) \}$.
- **Coproducts.** The coproduct of two rings, the universal ring receiving a
  morphism from each, is their free product, which need not be commutative
  even when both factors are commutative: the coproduct
  of $\mathbb{Z}[x]$ and $\mathbb{Z}[y]$ is the ring of polynomials in two
  non-commuting variables. For commutative rings the tensor product over
  $\mathbb{Z}$ is the coproduct only within the category of commutative rings.
- **Quotients.** For a two-sided ideal $I$ of $R$, the projection
  $R \to R/I$ onto the [quotient ring](trough:Ideal.Quotient.ring) is the
  universal morphism out of $R$ that sends every element of $I$ to $0$.

## Properties

- **Isomorphisms.** The [isomorphisms](trough:CategoryTheory.Iso) of $\mathbf{Ring}$ are the ring
  isomorphisms: every ring isomorphism is an isomorphism in the category,
  and every isomorphism in the category yields a ring isomorphism.
  Moreover,
  a morphism whose underlying function is bijective is an isomorphism,
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
- **Limits.** A [limit](trough:CategoryTheory.Limits.IsLimit) of a diagram is a universal object with compatible morphisms to every object of the diagram; products and equalizers are examples. The category of rings has all small limits,
  and the forgetful functor to sets preserves them:
  the underlying set of a limit of rings is the limit of the underlying sets,
  with the operations defined pointwise.
  The same holds for the forgetful functor to abelian groups.
- **Colimits.** Colimits are the dual notion, with morphisms from the diagram into the universal object. The category of rings has all small colimits.
  The forgetful functor does not preserve them in general: the coproduct of
  $\mathbb{Z}$ with itself is $\mathbb{Z}$, since $\mathbb{Z}$ is initial, while
  the coproduct of the underlying sets, the disjoint union of two copies of
  $\mathbb{Z}$, maps onto $\mathbb{Z}$ by identifying the two copies, and this
  comparison map is not injective. It does
  preserve filtered colimits,
  colimits over nonempty diagrams in which any two objects map to a common one
  and any two parallel arrows are made equal by a further arrow, so a directed union of
  rings is computed on underlying sets.
- **Free rings.** The forgetful functor to sets has a left adjoint: a functor
  $F$ from sets to rings such that ring morphisms $F(X) \to R$ correspond to
  functions from $X$ to the underlying set of $R$, naturally in $X$ and $R$.
  It sends a set $X$ to the free ring on $X$, the ring of polynomials with
  integer coefficients in non-commuting variables indexed by $X$:
  ring morphisms from the free ring on $X$ to a ring $R$ correspond bijectively to functions from $X$ to $R$,
  the morphism attached to a function agrees with it on $X$,
  and a morphism out of the free ring is determined by its values on $X$.

## Related concepts

Commutative rings form a full subcategory of $\mathbf{Ring}$, one that keeps
every ring morphism between its objects. In other words,
the forgetful functor from commutative rings to rings is fully faithful:
it is bijective on each set of morphisms.
Likewise, the forgetful functor from rings to semirings is fully faithful,
because a semiring morphism between rings automatically preserves additive
inverses. [Fields](trough:Field) form a further full subcategory, in which every morphism is
injective, because
every ring morphism from a field to a nonzero ring is injective. For a commutative ring $k$, the
[category of $k$-algebras](trough:AlgCat) maps to $\mathbf{Ring}$ by forgetting
the structure map, and every ring $R$ has its own
[category of modules](trough:ModuleCat); a morphism of rings $R \to S$ turns
every $S$-module into an $R$-module by restriction of scalars.

## In Mathlib

Mathlib bundles each object as a type together with a ring structure on it.
Morphisms are wrapped in a separate structure rather than being ring morphisms
themselves, with translations in both directions:
turning a ring morphism into a morphism of the category and back returns it,
and turning a morphism into a ring morphism and back also returns it.
This keeps the category's composition, written in diagrammatic order, apart
from the composition of functions. The category is indexed by a universe
level: it contains the rings whose underlying type lives in a fixed universe,
and "small" limits and colimits are those indexed by categories of that size.
Commutative rings, semirings and commutative semirings each have a parallel
category, with forgetful functors between them.

## Depends on

- [Ring](trough:Ring)
- [Ring morphism](trough:RingHom)
- [Category](trough:CategoryTheory.Category)
