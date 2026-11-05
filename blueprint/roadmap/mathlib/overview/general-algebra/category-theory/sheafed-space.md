---
article_id: af_026a7af788fe8665aeb5655c
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: AlgebraicGeometry.SheafedSpace
mathlib_file: Mathlib/Geometry/RingedSpace/SheafedSpace.lean
---

# Sheafed space

A **sheafed space** is a [topological space](../../topology/general-topology/part-01/topological-space.md) together with a sheaf on it with values in a fixed [category](category.md) $\mathcal{C}$: an object of $\mathcal{C}$ for each open set, with restriction maps, such that data given locally on an open cover and agreeing on overlaps glue uniquely. It is the common frame for spaces described by their local functions. Smooth manifolds with their smooth functions, and spectra of commutative rings with their structure sheaves, are sheafed spaces over commutative rings. The sheafed spaces over commutative rings are the ringed spaces, and [locally ringed spaces](../../geometry/algebraic-geometry/locally-ringed-space.md) and [schemes](../../geometry/algebraic-geometry/scheme.md) are ringed spaces with further conditions.

## Definition

Let $\mathcal{C}$ be a category and $X$ a topological space. A presheaf $\mathcal{F}$ on $X$ with values in $\mathcal{C}$ assigns to each open set $U$ an object $\mathcal{F}(U)$ and to each inclusion $V \subseteq U$ a restriction morphism $\mathcal{F}(U) \to \mathcal{F}(V)$, compatibly with identities and composition. When $\mathcal{C}$ is the category of sets, or of groups or rings, elements of $\mathcal{F}(U)$ are called sections over $U$, and the restriction of a section $s$ to $V$ is written $s|_V$.

Such a presheaf is a sheaf if, for every open set $U$ and every cover $U = \bigcup_i U_i$ by open sets, each family of sections $s_i \in \mathcal{F}(U_i)$ that is compatible, meaning

$$s_i|_{U_i \cap U_j} = s_j|_{U_i \cap U_j} \quad \text{for all } i, j,$$

comes from exactly one section $s \in \mathcal{F}(U)$ with $s|_{U_i} = s_i$ for every $i$. For presheaves of sets, Mathlib's sheaf condition is
[equivalent to this unique gluing condition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Sheaves/SheafCondition/UniqueGluing.html#TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types). For a general category $\mathcal{C}$ there are no elements to glue, and the condition is imposed on morphisms instead: for every object $A$ of $\mathcal{C}$, the presheaf of sets $U \mapsto \mathrm{Hom}(A, \mathcal{F}(U))$ must satisfy unique gluing. When $\mathcal{C}$ has products, this says that
[$\mathcal{F}(U)$ is the equalizer of the two restriction maps](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Sheaves/SheafCondition/EqualizerProducts.html#TopCat.Presheaf.isSheaf_iff_isSheafEqualizerProducts) from $\prod_i \mathcal{F}(U_i)$ to $\prod_{i,j} \mathcal{F}(U_i \cap U_j)$.

A [sheafed space over $\mathcal{C}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace) is a [presheafed space](presheafed-space.md) $(X, \mathcal{O}_X)$ whose presheaf $\mathcal{O}_X$ is a sheaf. A morphism $(X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$ is a pair $(f, f^\#)$ of a [continuous map](../../topology/general-topology/part-01/continuous-function.md) $f \colon X \to Y$ and a morphism of presheaves

$$f^\# \colon \mathcal{O}_Y \to f_*\mathcal{O}_X, \qquad (f_*\mathcal{O}_X)(V) = \mathcal{O}_X(f^{-1}(V)),$$

so no condition is added to morphisms: forgetting the sheaf condition is
[a fully faithful functor from sheafed spaces to presheafed spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.fullyFaithfulForgetToPresheafedSpace). The sheafed spaces over commutative rings are [called ringed spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/Basic.html#AlgebraicGeometry.RingedSpace).

## Examples

- **Continuous functions.** For spaces $X$ and $T$, sending an open set $U \subseteq X$ to the set of continuous maps $U \to T$ gives
  [a sheaf of sets on $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Sheaves/LocalPredicate.html#TopCat.sheafToTop): continuous maps that agree on overlaps glue to a unique continuous map, because continuity is a local property.
- **Smooth manifolds.** On a smooth [manifold](../../geometry/differentiable-manifolds/part-01/smooth-or-analytic-manifold-with-boundary-and-co.md) $M$, the smooth functions on open subsets with values in a fixed smooth commutative ring, such as $\mathbb{R}$, form
  [a sheaf of commutative rings](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Sheaf/Smooth.html#smoothSheafCommRing), which makes $M$ a ringed space.
- **Spectra of rings.** The [prime spectrum](../../geometry/algebraic-geometry/prime-spectrum.md) of a commutative ring $R$, with its [Zariski topology](../../geometry/algebraic-geometry/zariski-topology.md) and structure sheaf, is
  [a sheafed space over commutative rings](https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicGeometry/Spec.html#AlgebraicGeometry.Spec.sheafedSpaceObj). A ring homomorphism $R \to S$ induces a morphism in the opposite direction, from the spectrum of $S$ to that of $R$, and this makes the spectrum
  [a contravariant functor from commutative rings to sheafed spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicGeometry/Spec.html#AlgebraicGeometry.Spec.toSheafedSpace).
- **The trivial sheaf.** Over the category with one object and one morphism,
  [every presheaf is a sheaf](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Sheaves/Sheaf.html#TopCat.Presheaf.isSheaf_unit), so any topological space becomes
  [a sheafed space over that category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.unit).

The empty set is covered by the empty family, and gluing the empty family uniquely forces
[the value of a sheaf on the empty set to be a terminal object](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Sheaves/SheafCondition/Sites.html#TopCat.Sheaf.isTerminalOfEmpty). So a presheaf whose value on the empty set is not terminal, such as a constant presheaf with value a nonzero ring, is not a sheaf.

## Properties

- **Underlying space and global sections.** Forgetting the sheaf gives
  [a functor to the category of topological spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.forget) (see [the category of topological spaces](../../topology/general-topology/part-01/the-category-of-topological-spaces.md)), and taking sections over the whole space gives
  [a contravariant functor to $\mathcal{C}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.%CE%93).
- **Restriction.** The restriction of a sheaf to an open subset is again a sheaf, so for an open embedding $j \colon U \to X$ the presheafed space restriction is
  [a sheafed space on $U$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.restrict), and
  [restricting to all of $X$ gives back $(X, \mathcal{O}_X)$ up to isomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.restrictTopIso).
- **Stalks determine sections and morphisms.** Suppose $\mathcal{C}$ is a category of algebraic structures such as sets, abelian groups or commutative rings; precisely, a concrete category with all limits and colimits whose forgetful functor to sets preserves limits and filtered colimits and reflects isomorphisms. Then two sections of a sheaf over $U$
  [are equal if their germs agree at every point of $U$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Sheaves/Stalks.html#TopCat.Presheaf.section_ext). Consequently,
  [two morphisms of sheafed spaces are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.hom_stalk_ext) if they have the same continuous map and induce the same maps on all stalks. Under the same hypotheses, a morphism whose continuous map is injective and whose maps on stalks are epimorphisms
  [is a monomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.mono_of_base_injective_of_stalk_epi), and a morphism whose continuous map is surjective and whose maps on stalks are monomorphisms
  [is an epimorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace.epi_of_base_surjective_of_stalk_mono).
- **Colimits.** When $\mathcal{C}$ has all limits, colimits of sheafed spaces exist and are formed as for presheafed spaces, since a limit of sheaves is a sheaf; gluing sheafed spaces along open subsets is a special case.

## Related concepts

A presheafed space drops the sheaf condition. A locally ringed space is a ringed space whose stalks are local rings, with morphisms required to induce local homomorphisms on stalks, and a scheme is a locally ringed space that is covered by open pieces isomorphic to spectra of commutative rings. On the other side, the sheaf condition on a topological space is the special case, for the open sets of $X$ and their open covers, of the sheaf condition for a [Grothendieck topology](grothendieck-topology.md).

## In Mathlib

Mathlib defines a sheafed space as a presheafed space carrying a proof that its presheaf is a sheaf, with the value category arbitrary. Its official sheaf condition is the one for the Grothendieck topology of open covers on the open sets of the space, phrased through morphisms out of each object of $\mathcal{C}$ as above, so it needs no limits in $\mathcal{C}$; the unique gluing and equalizer formulations are theorems with their own hypotheses. The category of sheafed spaces is defined as the full subcategory of presheafed spaces it determines, and ringed spaces are not a separate structure but the case of commutative rings. Restriction is taken along any open embedding, not only the inclusion of an open subset. In the equalizer formulation, the products are indexed by types of the same size as the points of the space. The stalk results require the points of the space to live in the same universe as the morphisms of $\mathcal{C}$. Colimits of sheafed spaces are provided as instances, created by the forgetful functor to presheafed spaces, for sheafed spaces whose points live in that universe and for diagrams of that size.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Presheafed space](presheafed-space.md)
- [Topological space](../../topology/general-topology/part-01/topological-space.md)
- [Category](category.md)
- [Functor](functor.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)

## Sources

- [Mathlib documentation: `AlgebraicGeometry.SheafedSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace)
- [Source of `AlgebraicGeometry.SheafedSpace` in Mathlib/Geometry/RingedSpace/SheafedSpace.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/RingedSpace/SheafedSpace.lean#L42)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L14)
