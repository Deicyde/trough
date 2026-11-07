A **presheafed space** is a [topological space](trough:TopologicalSpace) together with a presheaf on it, an assignment of an object of a fixed [category](trough:CategoryTheory.Category) $\mathcal{C}$ to each open set, with restriction maps between them. It is a very general setting for "a space with functions on it", with the functions replaced by objects of an arbitrary category, and the structures of geometry are built from it by adding conditions: a [sheafed space](trough:AlgebraicGeometry.SheafedSpace) asks the presheaf to be a sheaf, a [locally ringed space](trough:AlgebraicGeometry.LocallyRingedSpace) further asks for commutative rings with local stalks and for morphisms inducing local homomorphisms on stalks, and a [scheme](trough:AlgebraicGeometry.Scheme) is a locally ringed space that is locally isomorphic to the spectrum of a commutative ring. Many constructions, such as gluing, colimits and restriction to open subsets, are simplest at the level of presheafed spaces, and the richer notions are often built from them by checking that the extra conditions survive.

## Definition

Let $\mathcal{C}$ be a category. For a topological space $X$, the open sets of $X$ ordered by inclusion form a category, and a presheaf on $X$ with values in $\mathcal{C}$ is a contravariant [functor](trough:CategoryTheory.Functor) $\mathcal{O}$ from it to $\mathcal{C}$: it gives an object $\mathcal{O}(U)$ for each open $U$ and a restriction morphism $\mathcal{O}(U) \to \mathcal{O}(V)$ whenever $V \subseteq U$, compatible with composition and identities.

A presheafed space over $\mathcal{C}$ is a pair $(X, \mathcal{O}_X)$ of a topological space $X$ and a presheaf $\mathcal{O}_X$ on $X$ with values in $\mathcal{C}$.

A continuous map $f \colon X \to Y$ pushes a presheaf $\mathcal{F}$ on $X$ forward to the presheaf $f_*\mathcal{F}$ on $Y$ given by $(f_*\mathcal{F})(V) = \mathcal{F}(f^{-1}(V))$. A morphism of presheafed spaces $(X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$ is a pair $(f, f^\#)$ of a [continuous map](trough:Continuous) $f \colon X \to Y$ and a morphism of presheaves on $Y$

$$f^\# \colon \mathcal{O}_Y \to f_*\mathcal{O}_X,$$

called the comorphism of the morphism, that is, a [natural transformation](trough:CategoryTheory.NatTrans) with components $\mathcal{O}_Y(V) \to \mathcal{O}_X(f^{-1}(V))$. The map on spaces goes forward while the map on presheaves goes backward, as pulling back functions along a map does. Morphisms compose by $(g, g^\#) \circ (f, f^\#) = (g \circ f,\ g_*(f^\#) \circ g^\#)$, and with this composition
presheafed spaces over $\mathcal{C}$ form a category.

## Examples

- **Continuous functions.** Any topological space $X$ carries the presheaf of commutative rings sending $U$ to the ring of continuous real-valued functions on $U$, with restriction of functions as the restriction maps. A continuous map $f \colon X \to Y$ gives a morphism whose comorphism sends a function $h$ on $V$ to $h \circ f$ on $f^{-1}(V)$.
- **Manifolds and schemes.** A smooth manifold with its presheaf of smooth functions, and the spectrum of a commutative ring with its structure sheaf, are presheafed spaces over commutative rings; in both cases the presheaf is in fact a sheaf.
- **Constant presheaves.** For a space $X$ and an object $Z$ of $\mathcal{C}$, the presheaf with $\mathcal{O}(U) = Z$ for every open $U$ and identity restriction maps gives
  a presheafed space. It is not a sheaf unless $Z$ is a terminal object, because the sheaf condition forces the value on the empty set to be terminal; this is a typical example of a presheafed space that is not a sheafed space.

## Properties

- **Underlying space.** Forgetting the presheaf gives
  a functor to the category of topological spaces (see [the category of topological spaces](trough:TopCat)).
- **Isomorphisms.** If $f$ is a [homeomorphism](trough:Homeomorph) and $f^\#$ is an [isomorphism](trough:CategoryTheory.Iso) of presheaves, then
  $(f, f^\#)$ is an isomorphism of presheafed spaces. Conversely, for an isomorphism of presheafed spaces
  the underlying continuous map is an isomorphism of spaces, that is, a homeomorphism, and
  the comorphism is an isomorphism of presheaves.
- **Global sections.** Sending $(X, \mathcal{O}_X)$ to $\mathcal{O}_X(X)$ and $(f, f^\#)$ to the component of $f^\#$ at $Y$ defines
  a contravariant functor from presheafed spaces to $\mathcal{C}$.
- **Restriction.** For an open embedding $j \colon U \to X$, setting $\mathcal{O}_U(V) = \mathcal{O}_X(j(V))$ gives
  the restriction of $(X, \mathcal{O}_X)$ to $U$, which comes with a morphism to $(X, \mathcal{O}_X)$.
- **Stalks.** When $\mathcal{C}$ has colimits, the stalk $\mathcal{O}_{X,x}$ at a point $x$ is the colimit of $\mathcal{O}_X(U)$ over the open neighbourhoods $U$ of $x$, and a morphism $(f, f^\#)$ induces
  a morphism of stalks $\mathcal{O}_{Y,f(x)} \to \mathcal{O}_{X,x}$. These maps are functorial:
  the stalk map of $g \circ f$ at $x$ is the stalk map of $f$ at $x$ composed after that of $g$ at $f(x)$. Restriction to an open subset does not change stalks:
  the morphism from a restriction induces isomorphisms on all stalks.
- **Colimits.** If $\mathcal{C}$ has all limits, then
  the category of presheafed spaces over $\mathcal{C}$ has all colimits, and
  the underlying space of a colimit is the colimit of the underlying spaces. The colimit presheaf is the [limit](trough:CategoryTheory.Limits.IsLimit) of the pushforwards of the given presheaves to the colimit space. Applied to diagrams whose maps are open embeddings, this construction glues presheafed spaces.
- **Change of values.** A functor $F \colon \mathcal{C} \to \mathcal{D}$ applied to every value of the presheaf gives
  a functor from presheafed spaces over $\mathcal{C}$ to presheafed spaces over $\mathcal{D}$; for instance, forgetting ring structure turns a presheaf of rings into a presheaf of sets.

## Related concepts

A sheafed space is a presheafed space whose presheaf satisfies the sheaf condition: sections that agree on overlaps glue uniquely. Ringed spaces are sheafed spaces over commutative rings, locally ringed spaces are those whose stalks are local rings and whose morphisms induce local homomorphisms on stalks, and schemes are a further special case. Each of these notions keeps the morphisms of presheafed spaces, adding at most a condition on them.

## In Mathlib

Mathlib bundles a presheafed space as an object of the category of topological spaces together with a presheaf on it, where a presheaf is a functor out of the opposite of the category of open sets. The value category is arbitrary. A morphism stores the continuous map and the comorphism into the pushforward, in the direction used above. Two morphisms with the same underlying continuous map can differ in their comorphisms, so Mathlib deliberately gives presheafed spaces no structure of a concrete category over sets. Restriction is defined along any open embedding, not only the inclusion of an open subset. For the results on stalks and colimits, the points of the spaces are taken in the same universe as the morphisms of $\mathcal{C}$, and "all limits" and "all colimits" mean those indexed by categories of that size. Sheafed spaces and locally ringed spaces are built as extensions of this structure, so the constructions above apply to their underlying presheafed spaces; Mathlib provides separate versions of restriction and colimits that stay within the richer categories.

## Depends on

- [Topological space](trough:TopologicalSpace)
- [Continuous function](trough:Continuous)
- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Natural transformation](trough:CategoryTheory.NatTrans)
