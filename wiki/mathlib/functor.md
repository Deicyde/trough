---
article_id: af_c67a0a9b35918cb8b77925b8
concept: CategoryTheory.Functor
---

A **functor** is a structure-preserving map between two
[categories](trough:CategoryTheory.Category): it sends objects to objects and
morphisms to morphisms, respecting identities and composition. Functors are the
basic way of comparing categories, and many constructions of algebra and topology,
such as taking the fundamental groupoid of a space, the homology of a chain complex
or the underlying set of a group, are functors. Saying that a construction is
functorial means that it acts on morphisms as well as on objects, compatibly with
composition.

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be categories. A
[functor $F$ from $\mathcal{C}$ to $\mathcal{D}$](lean:CategoryTheory.Functor),
written $F \colon \mathcal{C} \to \mathcal{D}$, consists of

- for each object $X$ of $\mathcal{C}$, an object $F(X)$ of $\mathcal{D}$;
- for each morphism $f \colon X \to Y$ of $\mathcal{C}$, a morphism
  $F(f) \colon F(X) \to F(Y)$ of $\mathcal{D}$,

subject to two axioms: $F$
[preserves identities](lean:CategoryTheory.Functor.map_id), and $F$
[preserves composition](lean:CategoryTheory.Functor.map_comp):

$$F(\mathrm{id}_X) = \mathrm{id}_{F(X)}, \qquad F(g \circ f) = F(g) \circ F(f)$$

for every object $X$ and all composable morphisms $f \colon X \to Y$ and
$g \colon Y \to Z$.

Every category has an [identity functor](lean:CategoryTheory.Functor.id), and
functors $F \colon \mathcal{C} \to \mathcal{D}$ and $G \colon \mathcal{D} \to \mathcal{E}$
have a [composite](lean:CategoryTheory.Functor.comp) $G \circ F$, acting by
$X \mapsto G(F(X))$ and $f \mapsto G(F(f))$. Composition of functors is
[associative](lean:CategoryTheory.Functor.assoc), and composing with an identity functor changes nothing:
[$F \circ \mathrm{id}_{\mathcal{C}} = F$](lean:CategoryTheory.Functor.id_comp) and
[$\mathrm{id}_{\mathcal{D}} \circ F = F$](lean:CategoryTheory.Functor.comp_id). Consequently
categories and functors themselves form a category, the
[category of categories](lean:CategoryTheory.Cat.category), provided one restricts to
categories of a bounded size so as to avoid set-theoretic paradoxes.

A **contravariant functor** from $\mathcal{C}$ to $\mathcal{D}$ reverses the direction
of morphisms, sending $f \colon X \to Y$ to $F(f) \colon F(Y) \to F(X)$ and satisfying
$F(g \circ f) = F(f) \circ F(g)$. It is the same thing as an ordinary functor from the
opposite category $\mathcal{C}^{\mathrm{op}}$ to $\mathcal{D}$, and this is how it is
usually treated.

## Examples

- **Forgetful functors.** Sending a group, ring or topological space to its underlying
  set, and a homomorphism or continuous map to its underlying function, is a functor to
  the category of sets. More generally every category whose objects are sets with
  structure carries [a forgetful functor to sets](lean:CategoryTheory.forget).
- **Monoids and groups.** A monoid can be viewed as a category with a
  single object whose morphisms are its elements. For monoids $M$ and $N$,
  [functors between these one-object categories correspond exactly to
  monoid homomorphisms from $M$ to $N$](lean:CategoryTheory.SingleObj.mapHom); in
  particular functors between groups viewed this way are
  [group homomorphisms](trough:MonoidHom).
- **Preorders.** A preordered set can be viewed as a category with at most one morphism from $x$ to
  $y$, present exactly when $x \le y$.
  [Every monotone map gives a functor](lean:Monotone.functor), and
  [every functor between preorders is monotone on objects](lean:CategoryTheory.Functor.monotone).
- **Topology.** Sending a topological space to its fundamental groupoid, and a
  continuous map to the induced map on homotopy classes of paths, is
  [a functor from topological spaces to groupoids](lean:FundamentalGroupoid.fundamentalGroupoidFunctor).
- **Homology.** In a category in which homology is defined, such as an
  [abelian category](trough:CategoryTheory.Abelian), taking the $i$th
  [homology](trough:HomologicalComplex.homology) of a
  [chain complex](trough:ChainComplex) is
  [a functor from complexes to the category itself](lean:HomologicalComplex.homologyFunctor).
- **Duality.** Sending a vector space $V$ over a field $K$ to its
  [dual space](trough:Module.Dual) $V^*$, and a linear map to its transpose, is a
  contravariant functor from $K$-vector spaces to themselves.
- **Hom functors.** In a category whose morphisms between any two objects form a set,
  fix an object $A$. Sending $X$ to the set of morphisms
  $A \to X$ is a functor to sets, and sending $X$ to the set of morphisms $X \to A$
  is a contravariant one; letting $A$ vary in the second gives the
  [Yoneda embedding](trough:CategoryTheory.yoneda).

## Properties

An [isomorphism](trough:CategoryTheory.Iso) is a morphism $f$ with a two-sided inverse
$g$. A functor [sends isomorphisms to isomorphisms](lean:CategoryTheory.Functor.map_isIso),
since it carries the equations $g \circ f = \mathrm{id}$ and $f \circ g = \mathrm{id}$
to the same equations for $F(f)$ and $F(g)$. The converse fails in general: the
forgetful functor from topological spaces to sets sends a continuous bijection whose
inverse is not continuous to an isomorphism of sets.

For objects $X$ and $Y$ of $\mathcal{C}$, a functor induces a map from the morphisms
$X \to Y$ to the morphisms $F(X) \to F(Y)$. The functor is
[faithful](lean:CategoryTheory.Functor.Faithful) if each of these maps is injective, and
[full](lean:CategoryTheory.Functor.Full) if each is surjective. Forgetful functors are
typically faithful but not full. A composite of
[faithful functors is faithful](lean:CategoryTheory.Functor.Faithful.comp), and a
composite of [full functors is full](lean:CategoryTheory.Functor.Full.comp). A functor
that is both full and faithful does detect isomorphisms:
[if $F(f)$ is an isomorphism, so is $f$](lean:CategoryTheory.isIso_of_fully_faithful).

A functor is [essentially surjective](lean:CategoryTheory.Functor.EssSurj) if every object
of $\mathcal{D}$ is isomorphic to $F(X)$ for some object $X$ of $\mathcal{C}$. A functor
that is full, faithful and essentially surjective is an
[equivalence of categories](lean:CategoryTheory.Functor.IsEquivalence): this is the
appropriate notion of "sameness" for categories, weaker than isomorphism, and it holds
exactly when there is a functor $G$ in the other direction with $G \circ F$ and
$F \circ G$ isomorphic to the identity functors.

## Related concepts

Functors from $\mathcal{C}$ to $\mathcal{D}$ are themselves the objects of a category,
[the functor category](lean:CategoryTheory.Functor.category), whose morphisms are
[natural transformations](trough:CategoryTheory.NatTrans). Two functors in opposite
directions related by a natural bijection of morphism sets form an
[adjunction](trough:CategoryTheory.Adjunction), and a functor from a category to itself
equipped with suitable natural transformations is a [monad](trough:CategoryTheory.Monad).
Functors from a small index category are the diagrams whose
[limits](trough:CategoryTheory.Limits.IsLimit) are studied in category theory, and
contravariant functors to sets are presheaves, the starting point of sheaf theory.

## In Mathlib

Mathlib bundles a functor as a structure recording its action on objects, its action on
morphisms, and proofs of the two axioms; a separate function recovers
[its underlying map of directed graphs](lean:CategoryTheory.Functor.toPrefunctor), a
prefunctor between the underlying quivers. Composition of morphisms is written in diagrammatic order,
first $f$ then $g$, so the composition axiom reads with the factors in that order.
Categories carry two universe levels, one for objects and one for morphisms, and a
functor may join categories of different sizes. Functors are compared up to natural
isomorphism rather than equality whenever possible, and the identity and associativity
laws for composition hold by definition. A contravariant functor is formalized as a
functor out of the opposite category. Mathlib has two forms of equivalence of categories:
[a structure](lean:CategoryTheory.Equivalence) recording a functor together with an
inverse functor, unit and counit natural isomorphisms and a triangle law, and a property
of a single functor, being an equivalence, defined as being full, faithful and
essentially surjective. It shows that
[a functor with an inverse up to natural isomorphism is an equivalence](lean:CategoryTheory.Functor.IsEquivalence.mk').
The category of categories is formed for each pair of universe levels, and its
morphisms are functors wrapped in a thin structure.

## Depends on

- [Category](trough:CategoryTheory.Category)
