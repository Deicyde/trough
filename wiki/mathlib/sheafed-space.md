A **sheafed space** is a [topological space](trough:TopologicalSpace) together with a sheaf on it with values in a fixed [category](trough:CategoryTheory.Category) $\mathcal{C}$: an object of $\mathcal{C}$ for each open set, with restriction maps, such that data given locally on an open cover and agreeing on overlaps glue uniquely. It is the common frame for spaces described by their local functions. Smooth manifolds with their smooth functions, and spectra of commutative rings with their structure sheaves, are sheafed spaces over commutative rings. The sheafed spaces over commutative rings are the ringed spaces, and [locally ringed spaces](trough:AlgebraicGeometry.LocallyRingedSpace) and [schemes](trough:AlgebraicGeometry.Scheme) are ringed spaces with further conditions.

## Definition

Let $\mathcal{C}$ be a category and $X$ a topological space. A presheaf $\mathcal{F}$ on $X$ with values in $\mathcal{C}$ assigns to each open set $U$ an object $\mathcal{F}(U)$ and to each inclusion $V \subseteq U$ a restriction morphism $\mathcal{F}(U) \to \mathcal{F}(V)$, compatibly with identities and composition. When $\mathcal{C}$ is the category of sets, or of groups or rings, elements of $\mathcal{F}(U)$ are called sections over $U$, and the restriction of a section $s$ to $V$ is written $s|_V$.

Such a presheaf is a sheaf if, for every open set $U$ and every cover $U = \bigcup_i U_i$ by open sets, each family of sections $s_i \in \mathcal{F}(U_i)$ that is compatible, meaning

$$s_i|_{U_i \cap U_j} = s_j|_{U_i \cap U_j} \quad \text{for all } i, j,$$

comes from exactly one section $s \in \mathcal{F}(U)$ with $s|_{U_i} = s_i$ for every $i$. For presheaves of sets, Mathlib's sheaf condition is
equivalent to this unique gluing condition. For a general category $\mathcal{C}$ there are no elements to glue, and the condition is imposed on morphisms instead: for every object $A$ of $\mathcal{C}$, the presheaf of sets $U \mapsto \mathrm{Hom}(A, \mathcal{F}(U))$ must satisfy unique gluing. When $\mathcal{C}$ has products, this says that
$\mathcal{F}(U)$ is the equalizer of the two restriction maps from $\prod_i \mathcal{F}(U_i)$ to $\prod_{i,j} \mathcal{F}(U_i \cap U_j)$.

A sheafed space over $\mathcal{C}$ is a [presheafed space](trough:AlgebraicGeometry.PresheafedSpace) $(X, \mathcal{O}_X)$ whose presheaf $\mathcal{O}_X$ is a sheaf. A morphism $(X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$ is a pair $(f, f^\#)$ of a [continuous map](trough:Continuous) $f \colon X \to Y$ and a morphism of presheaves

$$f^\# \colon \mathcal{O}_Y \to f_*\mathcal{O}_X, \qquad (f_*\mathcal{O}_X)(V) = \mathcal{O}_X(f^{-1}(V)),$$

so no condition is added to morphisms: forgetting the sheaf condition is
a fully faithful functor from sheafed spaces to presheafed spaces. The sheafed spaces over commutative rings are called ringed spaces.

## Examples

- **Continuous functions.** For spaces $X$ and $T$, sending an open set $U \subseteq X$ to the set of continuous maps $U \to T$ gives
  a sheaf of sets on $X$: continuous maps that agree on overlaps glue to a unique continuous map, because continuity is a local property.
- **Smooth manifolds.** On a smooth [manifold](trough:IsManifold) $M$, the smooth functions on open subsets with values in a fixed smooth commutative ring, such as $\mathbb{R}$, form
  a sheaf of commutative rings, which makes $M$ a ringed space.
- **Spectra of rings.** The [prime spectrum](trough:PrimeSpectrum) of a commutative ring $R$, with its [Zariski topology](trough:PrimeSpectrum.zariskiTopology) and structure sheaf, is
  a sheafed space over commutative rings. A ring homomorphism $R \to S$ induces a morphism in the opposite direction, from the spectrum of $S$ to that of $R$, and this makes the spectrum
  a contravariant functor from commutative rings to sheafed spaces.
- **The trivial sheaf.** Over the category with one object and one morphism,
  every presheaf is a sheaf, so any topological space becomes
  a sheafed space over that category.

The empty set is covered by the empty family, and gluing the empty family uniquely forces
the value of a sheaf on the empty set to be a terminal object. So a presheaf whose value on the empty set is not terminal, such as a constant presheaf with value a nonzero ring, is not a sheaf.

## Properties

- **Underlying space and global sections.** Forgetting the sheaf gives
  a functor to the category of topological spaces (see [the category of topological spaces](trough:TopCat)), and taking sections over the whole space gives
  a contravariant functor to $\mathcal{C}$.
- **Restriction.** The restriction of a sheaf to an open subset is again a sheaf, so for an open embedding $j \colon U \to X$ the presheafed space restriction is
  a sheafed space on $U$, and
  restricting to all of $X$ gives back $(X, \mathcal{O}_X)$ up to isomorphism.
- **Stalks determine sections and morphisms.** Suppose $\mathcal{C}$ is a category of algebraic structures such as sets, abelian groups or commutative rings; precisely, a concrete category with all limits and colimits whose forgetful functor to sets preserves limits and filtered colimits and reflects isomorphisms. Then two sections of a sheaf over $U$
  are equal if their germs agree at every point of $U$. Consequently,
  two morphisms of sheafed spaces are equal if they have the same continuous map and induce the same maps on all stalks. Under the same hypotheses, a morphism whose continuous map is injective and whose maps on stalks are epimorphisms
  is a monomorphism, and a morphism whose continuous map is surjective and whose maps on stalks are monomorphisms
  is an epimorphism.
- **Colimits.** When $\mathcal{C}$ has all limits, colimits of sheafed spaces exist and are formed as for presheafed spaces, since a limit of sheaves is a sheaf; gluing sheafed spaces along open subsets is a special case.

## Related concepts

A presheafed space drops the sheaf condition. A locally ringed space is a ringed space whose stalks are local rings, with morphisms required to induce local homomorphisms on stalks, and a scheme is a locally ringed space that is covered by open pieces isomorphic to spectra of commutative rings. On the other side, the sheaf condition on a topological space is the special case, for the open sets of $X$ and their open covers, of the sheaf condition for a [Grothendieck topology](trough:CategoryTheory.GrothendieckTopology).

## In Mathlib

Mathlib defines a sheafed space as a presheafed space carrying a proof that its presheaf is a sheaf, with the value category arbitrary. Its official sheaf condition is the one for the Grothendieck topology of open covers on the open sets of the space, phrased through morphisms out of each object of $\mathcal{C}$ as above, so it needs no limits in $\mathcal{C}$; the unique gluing and equalizer formulations are theorems with their own hypotheses. The category of sheafed spaces is defined as the full subcategory of presheafed spaces it determines, and ringed spaces are not a separate structure but the case of commutative rings. Restriction is taken along any open embedding, not only the inclusion of an open subset. In the equalizer formulation, the products are indexed by types of the same size as the points of the space. The stalk results require the points of the space to live in the same universe as the morphisms of $\mathcal{C}$. Colimits of sheafed spaces are provided as instances, created by the forgetful functor to presheafed spaces, for sheafed spaces whose points live in that universe and for diagrams of that size.

## Depends on

- [Presheafed space](trough:AlgebraicGeometry.PresheafedSpace)
- [Topological space](trough:TopologicalSpace)
- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Continuous function](trough:Continuous)
