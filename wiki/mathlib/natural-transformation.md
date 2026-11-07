A **natural transformation** is a morphism between two [functors](trough:CategoryTheory.Functor)
with the same source and target [categories](trough:CategoryTheory.Category). It assigns to each
object of the source a morphism in the target, and these morphisms are compatible with every
morphism of the source. The notion makes precise the informal idea of a construction that is
"natural", one defined uniformly without arbitrary choices, and it is the basic ingredient of
functor categories, [adjunctions](trough:CategoryTheory.Adjunction),
[limits](trough:CategoryTheory.Limits.IsLimit) and the [Yoneda embedding](trough:CategoryTheory.yoneda).

## Definition

Let $C$ and $D$ be categories and $F, G : C \to D$ functors. A
natural transformation $\alpha : F \Rightarrow G$ consists of a
morphism $\alpha_X : F(X) \to G(X)$ in $D$ for every object $X$ of $C$, called the component of
$\alpha$ at $X$, such that for every morphism $f : X \to Y$ of $C$ the naturality square commutes:

$$G(f) \circ \alpha_X = \alpha_Y \circ F(f).$$

Both sides are morphisms $F(X) \to G(Y)$, so the condition says that applying $F$ and then the
component at $Y$ gives the same result as applying the component at $X$ and then $G$. A natural
transformation is determined by its components:
two natural transformations with the same components are equal.

## Examples

- **The double dual.** For a vector space $V$ over a field $k$, let $\mathrm{ev}_V : V \to V^{**}$
  send $v$ to the functional $\varphi \mapsto \varphi(v)$ on the [dual space](trough:Module.Dual).
  For a linear map $f : V \to W$ one checks $f^{**} \circ \mathrm{ev}_V = \mathrm{ev}_W \circ f$, so
  the maps $\mathrm{ev}_V$ form a natural transformation from the identity functor to the double
  dual functor. Each component is injective, and it is an isomorphism exactly when $V$ is
  finite-dimensional. By contrast, the isomorphisms between a finite-dimensional space and its
  dual that one usually writes down depend on a choice of basis, and since the dual is
  contravariant they do not form a natural transformation in this sense.
- **The determinant.** For a commutative ring $R$, the [determinant](trough:Matrix.det) is a group
  homomorphism from the [general linear group](trough:Matrix.GeneralLinearGroup) $GL_n(R)$ to the
  group of units $R^\times$. A ring homomorphism $\varphi : R \to S$ satisfies
  $\det(\varphi(A)) = \varphi(\det A)$, where $\varphi$ is applied entrywise, because the
  determinant is a polynomial with integer coefficients in the entries. So the determinant is a
  natural transformation between two functors from commutative rings to groups.
- **[Abelianization](trough:Abelianization).** The quotient maps $G \to G/[G,G]$ form a natural
  transformation from the identity functor on groups to the functor sending a group to its
  abelianization.
- **Cones.** A cone over a diagram $F : J \to C$ with apex $X$ is a family of morphisms from $X$ to
  the objects $F(j)$, compatible with the morphisms of $J$. This is exactly
  a natural transformation from the constant functor at $X$ to $F$
  (the functor sending every object of $J$ to $X$ and every morphism to $\mathrm{id}_X$), and limits are defined as universal cones.

## Properties

- **The functor category.** Natural transformations can be composed componentwise: for
  $\alpha : F \Rightarrow G$ and $\beta : G \Rightarrow H$,
  the vertical composite has components
  $(\beta \circ \alpha)_X = \beta_X \circ \alpha_X$, and
  the identity transformation of $F$ has components the
  identities of the objects $F(X)$. With these operations,
  functors from $C$ to $D$ and the natural transformations between them form a category.
- **Natural isomorphisms.** A natural isomorphism is an [isomorphism](trough:CategoryTheory.Iso) in
  the functor category. A natural transformation is an isomorphism if and only if each of its components is an isomorphism:
  the inverses of the components are automatically natural. Similarly,
  if every component is an epimorphism, the transformation is an epimorphism
  of the functor category, where a morphism $e$ is an epimorphism when $g \circ e = h \circ e$
  implies $g = h$.
- **Whiskering.** Given $\alpha : G \Rightarrow H$ between functors $D \to E$ and a functor
  $F : C \to D$, the transformation with components $\alpha_{F(X)}$
  goes from $GF$ to $HF$. Given instead $\alpha : G \Rightarrow H$ between functors $C \to D$ and
  $F : D \to E$, the components $F(\alpha_X)$ give a
  natural transformation from $FG$ to $FH$.
- **Horizontal composition.** For $\alpha : F \Rightarrow G$ between functors $C \to D$ and
  $\gamma : I \Rightarrow J$ between functors $D \to E$,
  the horizontal composite $\gamma * \alpha : IF \Rightarrow JG$
  has components $J(\alpha_X) \circ \gamma_{F(X)}$, which by naturality of $\gamma$ also equal
  $\gamma_{G(X)} \circ I(\alpha_X)$. For further transformations $\beta : G \Rightarrow H$ and
  $\delta : J \Rightarrow K$, the two compositions satisfy
  the interchange law

$$(\delta \circ \gamma) * (\beta \circ \alpha) = (\delta * \beta) \circ (\gamma * \alpha).$$

- **Transformations of the identity functor.** If $\alpha$ and $\beta$ are natural transformations
  from the identity functor of $C$ to itself, the naturality of $\alpha$ at the morphism $\beta_X$
  gives $\alpha_X \circ \beta_X = \beta_X \circ \alpha_X$, so
  such transformations commute. On abelian groups,
  multiplication by a fixed integer is an example.
- **The Yoneda lemma.** The opposite category of $C$ has the same objects as $C$ and every morphism
  reversed, so a functor $F$ from it to sets assigns a set $F(X)$ to each object $X$ of $C$ and a
  map $F(Y) \to F(X)$ to each morphism $X \to Y$. For such $F$ and an object $X$, sending a
  natural transformation $\eta$ from the represented functor $\mathrm{Hom}(-, X)$ to $F$ to the
  element $\eta_X(\mathrm{id}_X)$ is
  a bijection onto $F(X)$.

## Related concepts

The unit and counit of an [adjunction](trough:CategoryTheory.Adjunction) and the unit and
multiplication of a [monad](trough:CategoryTheory.Monad) are natural transformations. Two
categories are equivalent when
there are functors in both directions whose composites are naturally isomorphic to the identity functors. Categories, functors and natural transformations
together form the prototypical 2-category, in which natural transformations are the 2-morphisms.

## In Mathlib

Mathlib bundles a natural transformation as a structure with two fields: the family of components
and a proof of the naturality square for every morphism. The square is written with composition in
diagrammatic order, first $F(f)$ and then $\alpha_Y$, and the proof field is filled in by an
automatic category-theory tactic when the author supplies none. The morphisms of the functor
category are by definition the natural transformations, and its composition is vertical
composition, so a natural isomorphism is not a separate notion: it is an isomorphism in that
category, and the criterion via components is a theorem. Horizontal composition is a separate
operation, and its notation lists the factors in the opposite order from the one used here: the
transformation between the first pair of functors comes first, so the composite written
$\gamma * \alpha$ above appears with $\alpha$ first. An equivalence of categories also records
one triangle identity relating the two natural isomorphisms; given any pair of natural
isomorphisms, Mathlib adjusts one of them so that the identity holds. For a cone, Mathlib takes the definition by a natural
transformation from a constant functor literally. In the Yoneda lemma the functor $F$ takes values
in types of the same universe as the morphisms of $C$.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
