---
article_id: af_faa8ecf56833d1577fef0763
concept: CategoryTheory.Limits.IsLimit
---

A **limit** of a diagram in a [category](trough:CategoryTheory.Category) is an object
equipped with morphisms to every object of the diagram, compatible with the arrows of
the diagram, through which every other such compatible family factors in exactly one
way. Products, equalizers, pullbacks, terminal objects and inverse limits are all
special cases, so the single notion lets one state and prove facts about all of them
at once. The dual notion, obtained by reversing every arrow, is a **colimit**.

## Definition

A diagram of shape $J$ in a category $C$ is a [functor](trough:CategoryTheory.Functor)
$F \colon J \to C$, where $J$ is a category whose objects index the objects $F(j)$ of
the diagram. A **cone** over $F$ with vertex $X$ is a family of morphisms
$\pi_j \colon X \to F(j)$, one for each object $j$ of $J$, such that

$$F(u) \circ \pi_i = \pi_j \quad \text{for every morphism } u \colon i \to j \text{ in } J.$$

Equivalently, a cone is [an object $X$ together with a natural transformation from the
constant functor at $X$ to $F$](lean:CategoryTheory.Limits.Cone) (see
[natural transformation](trough:CategoryTheory.NatTrans)).

A cone $(L, \pi)$ is a **limit cone** if
[for every cone $(X, \sigma)$ over $F$ there is a unique morphism $h \colon X \to L$
with $\pi_j \circ h = \sigma_j$ for all $j$](lean:CategoryTheory.Limits.IsLimit). The
object $L$ is then called a limit of $F$.

A morphism of cones $(X, \sigma) \to (L, \pi)$ is a morphism $h \colon X \to L$ with
$\pi_j \circ h = \sigma_j$ for all $j$; cones over $F$ and these morphisms form a
category. An object of a category is terminal if every object has exactly one
morphism to it. Said differently, then,
[a cone is a limit exactly when every cone admits exactly one cone morphism to
it](lean:CategoryTheory.Limits.IsLimit.isoUniqueConeMorphism), that is,
[a limit cone is the same as a terminal object of the category of cones over
$F$](lean:CategoryTheory.Limits.Cone.isLimitEquivIsTerminal).

Dually, a cocone consists of morphisms $F(j) \to X$ compatible with the diagram, and a
[colimit cocone](lean:CategoryTheory.Limits.IsColimit) is one from which there is a
unique compatible morphism to the vertex of every other cocone.

## Examples

- **Terminal objects.** When $J$ is empty, a cone is just an object, and
  [an object is a limit of the empty diagram exactly when every object has exactly one
  morphism to it](lean:CategoryTheory.Limits.isTerminalEquivUnique), that is, when it
  is a [terminal object](lean:CategoryTheory.Limits.IsTerminal).
- **Products.** When $J$ has no morphisms besides identities, a diagram is a family of
  objects, [a cone over it is a family of morphisms from one object to each member of
  the family](lean:CategoryTheory.Limits.Fan), and a product of the family is a limit
  cone; in particular [the family has a product exactly when that diagram has a
  limit](lean:CategoryTheory.Limits.HasProduct). In sets,
  [the Cartesian product $X \times Y$ with its two projections is a product of $X$ and
  $Y$](lean:CategoryTheory.Limits.Types.binaryProductLimit).
- **Equalizers.** For two parallel maps $f, g \colon Y \to Z$ of sets,
  [the subset $\{y \in Y : f(y) = g(y)\}$ with its inclusion is a limit of the pair](lean:CategoryTheory.Limits.Types.equalizerLimit),
  called their equalizer.
- **Pullbacks.** For maps $f \colon X \to Z$ and $g \colon Y \to Z$ of sets,
  [the set $\{(x, y) \in X \times Y : f(x) = g(y)\}$ with its two projections is a
  limit of the diagram formed by $f$ and $g$](lean:CategoryTheory.Limits.Types.pullbackLimitCone).
- **Diagrams of sets in general.** A compatible family for $F \colon J \to \mathbf{Set}$
  is a choice of $x_j \in F(j)$ for every $j$ with $F(u)(x_i) = x_j$ for every
  $u \colon i \to j$. [A cone over $F$ is a limit exactly when every compatible family
  is the image of exactly one element of its vertex](lean:CategoryTheory.Limits.Types.isLimit_iff).
  The ring of [$p$-adic integers](trough:PadicInt), for instance, is the limit of the
  rings $\mathbb{Z}/p^n\mathbb{Z}$ along the reduction maps.
- **Complete lattices.** A partially ordered set is a category with one morphism
  $a \to b$ when $a \le b$. In a complete lattice,
  [the infimum of the values of any diagram is its limit](lean:CategoryTheory.Limits.CompleteLattice.limitCone).

Dually, colimits include coproducts (disjoint unions of sets), coequalizers, pushouts,
initial objects and direct limits.

## Properties

- **Uniqueness.** [Any two limit cones over the same diagram are isomorphic as
  cones](lean:CategoryTheory.Limits.IsLimit.uniqueUpToIso), by the unique cone
  morphisms between them; in particular
  [their vertices are isomorphic](lean:CategoryTheory.Limits.IsLimit.conePointUniqueUpToIso)
  (see [isomorphism](trough:CategoryTheory.Iso)). For this reason one speaks of
  "the" limit.
- **Morphisms into a limit.** [Two morphisms into the vertex of a limit cone are equal
  when their composites with every projection $\pi_j$
  agree](lean:CategoryTheory.Limits.IsLimit.hom_ext), and
  [morphisms $W \to L$ correspond bijectively to cones over $F$ with vertex
  $W$](lean:CategoryTheory.Limits.IsLimit.homEquiv).
- **Representability.** The bijection above is natural in $W$, so
  [the vertex of a limit cone represents the functor sending $W$ to the set of cones
  over $F$ with vertex $W$](lean:CategoryTheory.Limits.IsLimit.representableBy);
  conversely, [a representing object of that functor is the vertex of a limit
  cone](lean:CategoryTheory.Limits.IsLimit.ofRepresentableBy). This links limits to
  the [Yoneda embedding](trough:CategoryTheory.yoneda).
- **Construction from products and equalizers.** For a diagram $F$ indexed by a
  [small category](trough:CategoryTheory.SmallCategory) $J$, if the product of all
  $F(j)$ exists, the product of the objects $F(j)$ indexed by the morphisms
  $u \colon i \to j$ of $J$ (one factor $F(j)$ for each $u$) exists, and $C$ has all
  equalizers, then [$F$ has a limit](lean:CategoryTheory.Limits.hasLimit_of_equalizer_and_product).
  The limit is the equalizer of two maps between these products.
- **Sets are complete.** [Every diagram of sets has a limit, provided its indexing
  category has no more objects than a set (in Mathlib: its objects are in bijection
  with a type in the universe of the sets, see below)](lean:CategoryTheory.Limits.Types.hasLimit);
  the limit is the set of compatible families.
- **Adjoints.** [A functor with a left adjoint preserves all
  limits](lean:CategoryTheory.Adjunction.rightAdjoint_preservesLimits): it
  [sends limit cones to limit cones](lean:CategoryTheory.Limits.PreservesLimit). See
  [adjunction](trough:CategoryTheory.Adjunction).
- **Functor categories.** For a diagram of functors $J \to (K \to C)$,
  [a cone is a limit as soon as, for each object $k$ of $K$, its evaluation at $k$ is a
  limit cone in $C$](lean:CategoryTheory.Limits.evaluationJointlyReflectsLimits), so
  limits of functors can be computed objectwise.

## Related concepts

[The category of cones over $F$ is equivalent to the comma category of the diagonal
functor $C \to C^J$ over $F$](lean:CategoryTheory.Limits.Cone.equivCostructuredArrow),
so a limit is a terminal object of a [comma category](trough:CategoryTheory.Comma). Kernels in an [abelian category](trough:CategoryTheory.Abelian) are
equalizers with a zero morphism, hence limits. The word "limit" also names a different
notion in analysis and topology, the
[limit of a map along a filter](trough:Filter.Tendsto); the two are not instances of
one another in general.

## In Mathlib

Mathlib defines being a limit as a structure on a cone that carries, for each other
cone, the chosen factoring morphism, its compatibility, and its uniqueness. This is
data rather than a mere proposition, but
[a cone carries at most one such structure](lean:CategoryTheory.Limits.IsLimit.subsingleton).
The mere existence of a limit is a separate property,
[the existence of some limit cone](lean:CategoryTheory.Limits.HasLimit), and from it
[a limit object is picked by choice](lean:CategoryTheory.Limits.limit). Colimits are
defined by their own dual structure rather than as limits in the opposite category.
Size is tracked by universe levels, a hierarchy of ever larger collections of types,
each type living in some universe: the indexing category and the hom-sets of $C$ may
live in different universes, and "having all limits" refers to indexing categories of
a given size. For sets, Mathlib's instance asks only that the objects of the indexing
category be in bijection with a type in the sets' universe; the size of its hom-sets
does not matter. That condition is sufficient but not necessary:
[a diagram of sets has a limit exactly when its compatible families are in bijection
with a type in the sets' universe](lean:CategoryTheory.Limits.Types.hasLimit_iff_small_sections).
Mathlib writes composition in diagrammatic order, so its compatibility conditions read
left to right.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Natural transformation](trough:CategoryTheory.NatTrans)
