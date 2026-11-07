An **adjunction** is a relationship between two [functors](trough:CategoryTheory.Functor)
running in opposite directions between two [categories](trough:CategoryTheory.Category),
$F \colon \mathcal{C} \to \mathcal{D}$ and $G \colon \mathcal{D} \to \mathcal{C}$, in which
morphisms $F(X) \to Y$ in $\mathcal{D}$ correspond exactly, naturally in $X$ and $Y$, to
morphisms $X \to G(Y)$ in $\mathcal{C}$. The functor $F$ is then called the left adjoint and $G$ the right adjoint, and one
writes $F \dashv G$. Adjunctions occur throughout mathematics: free
constructions, the discrete topology functor, currying of functions and Galois connections all
give adjunctions. They are weaker than equivalences of categories but still strong enough to
force preservation of limits and to produce monads.

## Definition

Let $F \colon \mathcal{C} \to \mathcal{D}$ and $G \colon \mathcal{D} \to \mathcal{C}$ be functors.
An adjunction $F \dashv G$ consists of two
[natural transformations](trough:CategoryTheory.NatTrans), the unit
$\eta \colon 1_{\mathcal{C}} \Rightarrow G F$ and the counit
$\varepsilon \colon F G \Rightarrow 1_{\mathcal{D}}$, satisfying the two triangle identities

$$\varepsilon_{F(X)} \circ F(\eta_X) = 1_{F(X)}, \qquad G(\varepsilon_Y) \circ \eta_{G(Y)} = 1_{G(Y)}$$

for every object $X$ of $\mathcal{C}$ and $Y$ of $\mathcal{D}$.

An equivalent description uses hom-sets. An adjunction yields
a bijection

$$\operatorname{Hom}_{\mathcal{D}}(F(X), Y) \cong \operatorname{Hom}_{\mathcal{C}}(X, G(Y))$$

sending $f \colon F(X) \to Y$ to $G(f) \circ \eta_X$, with inverse sending
$g \colon X \to G(Y)$ to $\varepsilon_Y \circ F(g)$. This bijection is natural in both variables:
it is compatible with precomposition by morphisms of $\mathcal{C}$
and with postcomposition by morphisms of $\mathcal{D}$.
Conversely, any family of bijections natural in this sense determines an adjunction,
whose unit at $X$ is the morphism corresponding to the identity of $F(X)$, and whose counit at
$Y$ is the morphism corresponding to the identity of $G(Y)$.

## Examples

- **Free and forgetful functors.** Homomorphisms from the [free group](trough:FreeGroup) on a
  set $S$ to a [group](trough:Group) $H$ correspond exactly to functions from $S$ to the
  underlying set of $H$: every function extends uniquely to a homomorphism. This makes
  the free group functor left adjoint to the forgetful functor from groups to sets.
- **Discrete and indiscrete topologies.** Every function out of a discrete space is continuous,
  so the discrete topology functor is left adjoint to the forgetful functor from topological spaces to sets
  (see [the category of topological spaces](trough:TopCat)). Dually, every function into an
  indiscrete space is continuous, so
  the forgetful functor is left adjoint to the indiscrete topology functor.
- **Galois connections.** A preorder is a category with at most one morphism between any two
  objects, and a functor between preorders is a monotone map. An adjunction between monotone
  maps $l$ and $u$ is then the condition that $l(x) \le y$ holds exactly when $x \le u(y)$, so
  every Galois connection between preorders is an adjunction.
- **Currying.** In the category of sets, functions $A \times X \to Y$ correspond to functions
  $X \to Y^A$, so taking the product with $A$ is left adjoint to taking functions out of $A$.
  More generally, in a [closed monoidal category](trough:CategoryTheory.MonoidalClosed),
  tensoring with $A$ on the left is left adjoint to the internal hom out of $A$.
- **Equivalences.** Every equivalence of categories is an adjunction,
  and conversely an adjunction whose unit and counit have invertible components is an equivalence.

## Properties

- **Uniqueness.** Adjoints are unique up to natural [isomorphism](trough:CategoryTheory.Iso): if
  $F$ and $F'$ are both left adjoint to $G$, then
  $F$ and $F'$ are naturally isomorphic, and
  likewise two right adjoints of the same functor are naturally isomorphic.
- **Composition.** If $F \dashv G$ with $F \colon \mathcal{C} \to \mathcal{D}$ and $H \dashv I$
  with $H \colon \mathcal{D} \to \mathcal{E}$, then
  $H F$ is left adjoint to $G I$.
- **Limits.** A left adjoint preserves all colimits
  and a right adjoint preserves all limits
  (see [limits](trough:CategoryTheory.Limits.IsLimit)). For instance, the underlying set of a
  product of groups is the product of the underlying sets, and the free group on a disjoint union
  of sets is the free product (the coproduct in the category of groups) of the free groups on the pieces.
- **Monads.** For an adjunction $F \dashv G$, the composite $G F$ is a functor from
  $\mathcal{C}$ to itself, and it becomes
  a monad on $\mathcal{C}$ with unit $\eta$ and
  multiplication $G \varepsilon F \colon G F G F \Rightarrow G F$; see
  [monad](trough:CategoryTheory.Monad).
- **Fully faithful adjoints.** If the right adjoint is full and faithful, the counit is an isomorphism,
  and if the counit is an isomorphism, the right adjoint is fully faithful.
  A full and faithful right adjoint is called reflective, its essential image is a reflective
  subcategory, and its left adjoint is called the reflector. For instance, the inclusion of
  abelian groups into groups is full and faithful, and
  abelianization is left adjoint to it.

## Related concepts

An adjunction can also be described through universal arrows. Given $F \dashv G$ and an object
$A$ of $\mathcal{C}$, consider the [comma category](trough:CategoryTheory.Comma) whose objects
are pairs $(B, f)$ of an object $B$ of $\mathcal{D}$ and an arrow $f \colon A \to G(B)$, with
morphisms $(B, f) \to (B', f')$ the maps $h \colon B \to B'$ satisfying $G(h) \circ f = f'$. This
category has the unit $\eta_A \colon A \to G(F(A))$ as an initial object, and
$G$ has a left adjoint exactly when each of these categories has an initial object.
Combining this with a smallness condition gives the general adjoint functor theorem: if $\mathcal{D}$
is locally small and has all small limits, and $G$ preserves them and satisfies the solution
set condition (for each $A$ there is a set of arrows $A \to G(B_i)$ through which every arrow
$A \to G(X)$ factors), then
$G$ has a left adjoint.
Representable functors give another reading (see [Yoneda embedding](trough:CategoryTheory.yoneda)):
$F \dashv G$ says that for each object $X$ of $\mathcal{C}$,
the covariant functor $Y \mapsto \operatorname{Hom}(X, G(Y))$ is corepresented by $F(X)$,
that is, it is naturally isomorphic to $Y \mapsto \operatorname{Hom}(F(X), Y)$.

## In Mathlib

Mathlib takes the unit and counit with the triangle identities as the definition, and derives the
hom-set bijection from them. Other constructors build an adjunction from a natural bijection of
hom-sets, or build the adjoint functor itself from its values on objects together with suitable
bijections of hom-sets. An adjunction is data, not a proposition: a pair of functors can
carry several adjunction structures, and the theorems above about uniqueness, composition and
equivalences are constructions producing specific natural isomorphisms and adjunctions. The mere
existence of an adjoint is recorded separately as the property of being a left or a right adjoint,
from which a chosen adjoint can be extracted. Preservation of limits is proved for limits indexed
by categories of every size, not only small ones. Smallness in the adjoint functor theorem is
measured relative to a universe level, which plays the role of the class of sets; in that
statement the solution sets, the limits and the hom-sets of $\mathcal{D}$ are all small with
respect to the same level.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Natural transformation](trough:CategoryTheory.NatTrans)
