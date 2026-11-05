---
article_id: af_0badd595deb39739c17abd65
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Comma
mathlib_file: Mathlib/CategoryTheory/Comma/Basic.lean
---

# Comma category

A **comma category** is a [category](category.md) built from two
[functors](functor.md) with a common target: its objects are morphisms
from the image of the first functor to the image of the second, and its morphisms are
commutative squares relating them. The construction packages many familiar categories in
one definition, among them slice and coslice categories, arrow categories and categories
of structured arrows, and it gives a uniform language for universal properties: a functor
has a left adjoint exactly when certain comma categories have initial objects. The name
comes from the comma in the notation $(L, R)$ for the comma category of $L$ and $R$; this
article writes $(L \downarrow R)$, which is also common.

## Definition

Let $L \colon \mathcal A \to \mathcal T$ and $R \colon \mathcal B \to \mathcal T$ be
functors. The [comma category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Basic.html#CategoryTheory.Comma) $(L \downarrow R)$ has as objects
the triples $(a, b, h)$ where $a$ is an object of $\mathcal A$, $b$ is an object of
$\mathcal B$, and $h \colon L(a) \to R(b)$ is a morphism of $\mathcal T$. A morphism
$(a, b, h) \to (a', b', h')$ is a pair $(f, g)$ of morphisms $f \colon a \to a'$ in
$\mathcal A$ and $g \colon b \to b'$ in $\mathcal B$ such that the square

$$h' \circ L(f) = R(g) \circ h$$

commutes in $\mathcal T$. Composition and identities are taken componentwise; the
composite of two commutative squares placed side by side is again commutative, so this is
a category.

## Examples

- **Slice categories.** Take $L$ to be the identity functor of a category $\mathcal C$
  and $R$ the functor from the one-object category picking out an object $X$. The
  result is the [slice category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Over/Basic.html#CategoryTheory.Over) $\mathcal C / X$, whose
  objects are morphisms $Y \to X$ and whose morphisms are morphisms $Y \to Y'$ making
  the triangle over $X$ commute. In it,
  [the identity of $X$ is a terminal object](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Over/Basic.html#CategoryTheory.Over.mkIdTerminal).
- **Coslice categories.** Exchanging the roles gives the
  [coslice category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Over/Basic.html#CategoryTheory.Under) $X / \mathcal C$ of morphisms out of
  $X$, in which [the identity of $X$ is an initial object](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Over/Basic.html#CategoryTheory.Under.mkIdInitial).
  For instance,
  [the category of commutative algebras over a commutative ring $k$ is equivalent to the coslice category of commutative rings under $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/CommAlgCat/Basic.html#commAlgCatEquivUnder):
  a commutative [algebra](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md) over $k$ is the same thing as a commutative
  ring together with a ring homomorphism from $k$.
- **Arrow categories.** When both functors are the identity of $\mathcal C$, the
  comma category is the [arrow category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Arrow.html#CategoryTheory.Arrow) of $\mathcal C$:
  objects are morphisms of $\mathcal C$ and morphisms are commutative squares.
- **Structured arrows.** For a functor $G \colon \mathcal D \to \mathcal C$ and an
  object $c$ of $\mathcal C$, taking $L$ to pick out $c$ and $R = G$ gives the
  [category of structured arrows](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/StructuredArrow/Basic.html#CategoryTheory.StructuredArrow)
  $(c \downarrow G)$, whose objects are pairs $(d, h)$ with $h \colon c \to G(d)$. The
  dual construction, with morphisms $G(d) \to c$, is the
  [category of costructured arrows](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/StructuredArrow/Basic.html#CategoryTheory.CostructuredArrow).
- **Products.** If $\mathcal T$ is the category with one object and one morphism,
  every square commutes, and
  [the comma category is equivalent to the product category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Basic.html#CategoryTheory.Comma.equivProd)
  $\mathcal A \times \mathcal B$.

## Properties

- **Projections.** There are forgetful functors $P_1$ from $(L \downarrow R)$ to
  $\mathcal A$ and $P_2$ to $\mathcal B$; the first is
  [the projection $(a, b, h) \mapsto a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Basic.html#CategoryTheory.Comma.fst). The morphisms
  $h$ themselves are the components of
  [a natural transformation from $L \circ P_1$ to $R \circ P_2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Basic.html#CategoryTheory.Comma.natTrans).
- **Duality.** Reversing all arrows exchanges the two sides:
  [$(L \downarrow R)$ is equivalent to the opposite of $(R^{\mathrm{op}} \downarrow L^{\mathrm{op}})$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Basic.html#CategoryTheory.Comma.opEquiv).
  In particular
  [the coslice category of $X$ in $\mathcal C^{\mathrm{op}}$ is equivalent to the opposite of the slice category $\mathcal C / X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Over/Basic.html#CategoryTheory.Under.opEquivOpOver).
- **Limits.** If $\mathcal A$ and $\mathcal B$ have all [limits](limits.md)
  of a given shape $J$ and $R$ preserves them, then
  [$(L \downarrow R)$ has all limits of shape $J$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Limits/Comma.html#CategoryTheory.Comma.hasLimitsOfShape);
  no condition on $L$ is needed, and the limit is computed separately in each component.
  Slice categories also have limits that this theorem does not give: the functor
  picking out $X$ does not preserve products, but if $\mathcal C$ has pullbacks, then
  [every slice category $\mathcal C / X$ has binary products](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Limits/Constructions/Over/Products.html#CategoryTheory.Over.ConstructProducts.over_binaryProduct_of_pullback),
  the product of $Y \to X$ and $Z \to X$ being the pullback $Y \times_X Z$ with its
  map to $X$.
- **Adjunctions.** Universal arrows are initial objects of structured arrow
  categories. If $F$ is left adjoint to $G \colon \mathcal D \to \mathcal C$, then for
  each object $c$ of $\mathcal C$
  [the unit $c \to G(F(c))$ is an initial object of $(c \downarrow G)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Adjunction/Comma.html#CategoryTheory.mkInitialOfLeftAdjoint).
  Conversely, if every category $(c \downarrow G)$ has an initial object, then
  [$G$ has a left adjoint](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Adjunction/Comma.html#CategoryTheory.isRightAdjointOfStructuredArrowInitials);
  see [adjunction](adjunction.md).

## Related concepts

Slice categories over an object $X$ of the category of topological spaces or of schemes
are categories of spaces or schemes "over $X$", the setting of relative geometry, and
coslice categories under a one-point set or space give pointed sets and pointed spaces.
A presheaf $P$ on $\mathcal C$, viewed as a functor on $\mathcal C^{\mathrm{op}}$, has a
category of elements whose objects are the pairs $(c, x)$ with $x \in P(c)$, and
[the opposite of this category of elements is equivalent to the category of costructured arrows from the Yoneda embedding to $P$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Elements.html#CategoryTheory.Functor.Elements.costructuredArrowYonedaEquivalence)
(see [Yoneda embedding](yoneda-embedding.md)). When the functors land in a
2-category, such as the 2-category of categories, one may allow the squares to commute
only up to a specified 2-cell (a [natural transformation](natural-transformation.md),
in the case of categories); this leads to lax comma constructions in higher category
theory.

## In Mathlib

Mathlib defines the comma category of two functors into a common category for categories
in arbitrary universes, as a structure whose data are the two objects and the connecting
morphism; morphisms are pairs of morphisms with the square condition as a field. Slice and
coslice categories, arrow categories and the categories of structured and costructured
arrows are not separate constructions but are defined as comma categories, with the
one-object category represented by a discrete category on a one-element type. As a
result, every general theorem about comma categories, such as the existence of limits and
the duality equivalence, applies to all of these special cases at once.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Category](category.md)
- [Functor](functor.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Comma`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Basic.html#CategoryTheory.Comma)
- [Source of `CategoryTheory.Comma` in Mathlib/CategoryTheory/Comma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Comma/Basic.lean#L64)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L11)
