# Ringed spaces

> Full ringed-space restriction, open-cover gluing and inverse-image factorization; scalar extension of module presheaves and sheaves; a concrete inverse-image module-presheaf Hom adjunction for arbitrary continuous maps; and root-exported continuous module-sheaf inverse image with a bundled linear Hom adjunction; and root-exported full-morphism module pushforward and explicit sheafified right-tensor pullback with their adjunction and native comparison; and identity/composition coherence, commutative-square push-pull mates, and horizontal and vertical pasting laws for those actual module functors; and constant-closed full ringed morphisms to local affine spectra from ring maps to global sections, with an all-affine-induced-map exclusion when such a map sends a maximal-ideal element to a unit of a nontrivial commutative target ring; and continuous-function sheaves, evaluation, functorial maps and open immersions of ringed spaces over topological commutative rings, with local stalks and corresponding locally ringed-space maps and open immersions over T1 topological fields; and finite-order chart-dependent scalar-function sheaves over nontrivially normed fields, with local stalks, smooth-to-finite comparison and a natural order-zero isomorphism to the existing continuous-function sheaf; and pullbacks along finite-regularity maps with locally ringed-space identity and composition laws and smooth/continuous endpoint naturality.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/formalization.yaml) of [FormalFrontier/ringed-spaces](https://github.com/FormalFrontier/ringed-spaces) at commit [052015f0](https://github.com/FormalFrontier/ringed-spaces/tree/052015f070ef0b3e42c724eb9a8f9a1a1b916682), Apache-2.0.*

2 articles: 2 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/ringed-spaces](https://github.com/FormalFrontier/ringed-spaces), read at commit [052015f0](https://github.com/FormalFrontier/ringed-spaces/tree/052015f070ef0b3e42c724eb9a8f9a1a1b916682) (2026-10-29).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “self-assessed”.
- Review notes: “This metadata describes the library and does not self-certify independent acceptance of any new release, rights clearance, proof integrity or source coverage. Revision-specific review and release evidence is recorded separately.”
- Automation: agent; framework “Agent-assisted Lean development”; tool setup “Agent-assisted Lean development with the repository-pinned Lean and mathlib revisions and kernel checking. Mathematical statements, attribution and release acceptance require independent review.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Ringed-space restrictions, gluing and module change of rings*, Atlas (Formal Frontier mathematical author), Formal Frontier Agents (original-proof; formalizes).
- [Mathlib algebraic-geometric gluing transition construction](https://github.com/leanprover-community/mathlib4/blob/83abb3e776bdefcbc447a1e44d0debe4010039e5/Mathlib/AlgebraicGeometry/Gluing.lean), Andrew Yang (other; adapts).
- [Mathlib continuous-function sheaves and open-subtype methods](https://github.com/leanprover-community/mathlib4/blob/83abb3e776bdefcbc447a1e44d0debe4010039e5/Mathlib/Topology/Sheaves/CommRingCat.lean), Kim Morrison, Andrew Yang, Johan Commelin, Heather Macbeth, Adam Topaz, Other mathlib contributors (other; adapts).
- [Mathlib smooth scalar-function sheaf](https://github.com/leanprover-community/mathlib4/blob/83abb3e776bdefcbc447a1e44d0debe4010039e5/Mathlib/Geometry/Manifold/Sheaf/Smooth.lean), Heather Macbeth, Adam Topaz, Other mathlib contributors (other; adapts).
- [Mathlib smooth-manifold local scalar stalks](https://github.com/leanprover-community/mathlib4/blob/83abb3e776bdefcbc447a1e44d0debe4010039e5/Mathlib/Geometry/Manifold/Sheaf/LocallyRingedSpace.lean), Heather Macbeth (other; adapts).

## Builds on

- [Complex analysis](../../analysis/complex-analysis/README.md) (a Lake dependency, pinned at 2c0ad1d2)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/README.md#headline-results) of [FormalFrontier/ringed-spaces](https://github.com/FormalFrontier/ringed-spaces) at commit [052015f0](https://github.com/FormalFrontier/ringed-spaces/tree/052015f070ef0b3e42c724eb9a8f9a1a1b916682), Apache-2.0.*

**Restriction and indexed gluing.** For `X Y : RingedSpace.{u, u}`,
[`RingedSpace.isPullback_restrictInf`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/Restriction.lean) identifies
the literal intersection of two opens with the pullback of their full
restrictions. Compatible morphisms on any `J : Type u`-indexed open cover
glue uniquely to a full morphism `X ⟶ Y`, also when `J` and `X` are empty;
[`OpenCover.existsUnique_gluing_of_intersection`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/OpenCover.lean)
accepts literal-intersection compatibility.
To compare morphisms glued on different covers, the
[cross-cover guide](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/open-cover-comparison.md) applies the existing
restriction, gluing and full-morphism extensionality equations.

**Inverse-image factorization.** For `Y : RingedSpace.{u, u}` and a continuous
map `g : T ⟶ Y.carrier`, `T : TopCat.{u}`,
[`RingedSpace.inverseImage`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/InverseImage.lean) has literal
carrier `T` and mathlib's inverse-image ring sheaf. Every full `f : X ⟶ Y`
factors through it by [`toInverseImage_ofInverseImage`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/InverseImage.lean);
this is *not* a categorical ringed-space fiber product.

- [Continuous-function spaces](continuous-function-spaces.md)
- [Finite-regularity scalar functions](finite-regularity-scalar-functions.md)

**Indexed chart balls and smooth scalar functions.** For any regularity
`n : ℕ∞ω`, a self-model manifold has chart coordinates on a neighborhood
diffeomorphic to an **entire** positive-radius model ball, with no dimension
or completeness assumption. At smooth regularity `∞`, the restricted ambient
canonical smooth scalar locally ringed space is isomorphic to the canonical
one on that ball; its whole arrows and full-composite germ and section
evaluations are explicit. See the [chart-ball guide](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/chart-local-ball.md).

**Recovering smooth maps from scalar-preserving morphisms.** For canonical
smooth scalar presheaves on charted spaces over a nontrivially normed field,
preservation of global field constants is equivalent to preservation on every
open. The evaluation law
identifies pullbacks of arbitrary sections with precomposition, without
dimensionality or completeness requirements. For arbitrary canonical charted
targets, scalar-preserving full morphisms with the same base map coincide;
a separately supplied smoothness proof identifies the full induced morphism.
If the target is an open subset of a finite-dimensional normed space over a
complete field, smoothness of the base map follows; no dimensionality or
manifold-regularity assumption is imposed on the source. For real scalars,
preservation of constants follows from uniqueness of real ring endomorphisms;
for complex scalars it is an explicit hypothesis. The scalar field and space
carriers share a universe; source model universes are independent. See
[`SmoothScalarReconstruction`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/ChartedSpace/SmoothScalarReconstruction.lean).

**Holomorphic scalar sections.** On open and nested-open subtypes of the
finite-dimensional complex normed spaces, complex differentiability into
complete complex normed spaces is equivalent to complex smoothness. For
scalar-valued functions, the canonical smooth scalar sheaf accepts
[them directly as sections](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/ChartedSpace/HolomorphicSections.lean),
with pointwise evaluation, restriction,
and sheaf and locally ringed-space maps that precompose representatives on
inverse-image opens.
The chartwise version assumes a smooth manifold structure; it does not
upgrade a merely holomorphic atlas or identify arbitrary structure sheaves.
The scalar-sheaf API retains Mathlib's common-universe restriction.

**Finite-dimensional complex atlas regularity.** On a given charted space over a
boundaryless complex model with finite-dimensional coordinates, differentiability
of every ordered chart transition in model coordinates on its exact transition
domain implies analytic manifold regularity at `ω`, hence complex smoothness at
`∞`. An order-one manifold structure also gives analytic regularity; neither
construction replaces the original atlas. The hypotheses concern transitions,
not an arbitrary structure sheaf. Apply
`isManifold_omega_of_differentiableOn_chartTransitions` explicitly to the existing
charts; importing the module does not install a global upgrade instance.
See [complex atlas regularity](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/Complex/AtlasRegularity.lean).

**Mixed-compatible atlases.** For two specified atlases on
one topological space, membership of every ordered mixed chart transition in
a structure groupoid gives both atlases' own regularity and equality of their
maximal atlases, without assuming either is already regular. For mixed `C^n`
transitions, the point-preserving comparison is a `C^n` diffeomorphism to a
typed `ULift` copy retaining the entire second atlas. See
[`CompatibleAtlases`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/ChartedSpace/CompatibleAtlases.lean).

**Compatible-atlas smooth scalar sheaves.** Two specified smooth-compatible
atlases on the same topology give an identity-base isomorphism between their
canonical smooth scalar locally ringed spaces. The complete forward and inverse
maps are smooth precomposition; their section-ring equivalences preserve
values and scalar constants on every open, commute with restriction, and
preserve germ evaluation. No dimension, completeness or separation hypothesis
is needed. This compares canonical sheaves, not an arbitrary structure sheaf.
See [`CompatibleAtlasSheaf`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/ChartedSpace/CompatibleAtlasSheaf.lean).

**Change of coefficient sheaves.** A full natural map of commutative-ring
presheaves induces a tensor-presheaf/restriction-of-scalars adjunction;
with the required site sheafification witnesses, a full map of ring sheaves
gives the [sheafified adjunction](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/Modules/SheafChangeOfRings.lean).
Right-factor tensor extension is naturally isomorphic to left-factor
extension. See [scalar extension](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/module-change-of-rings.md) and
[right-factor symmetry](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/change-of-rings-symmetry.md).

**Continuous inverse images of modules.** Neighborhood-colimit module
presheaf inverse image and its genuine sheafification have bundled linear
Hom adjunctions to the corresponding native pushforwards, with whole
additive-sheaf comparisons; the additive comparison alone does not provide
coefficient transport. See the [presheaf](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/presheaf-inverse-image-hom.md)
and [sheaf](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/sheaf-inverse-image.md) guides.

**Full-morphism module functors.** For any full `f : X ⟶ Y`, the original
ring-sheaf structure map defines module pushforward; explicit sheafified
right-tensor pullback is its left adjoint, with a comparison to native
pullback. Composition and identity comparisons and the push–pull mate of
**any commutative square** satisfy horizontal and vertical pasting laws;
no general invertibility of that mate is claimed. See the
[pushforward](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/ringed-space-pushforward.md),
[pullback](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/ringed-space-pullback.md),
[coherence](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/ringed-module-coherence-base-change.md) and
[pasting](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/ringed-module-base-change-pasting.md) guides.

**Constant closed-point morphisms.** For a commutative local ring `R`, any
ring map from `R` to global sections of a ringed space constructs a full
morphism with constant closed-point base. For same-universe commutative
`R, S`, `[Nontrivial S]`, and a map `alpha : R →+* S` sending an element
of `IsLocalRing.maximalIdeal R` to a unit, this morphism `Spec S ⟶ Spec R`
differs from **every** affine-induced full morphism. Neither construction
asserts a scheme morphism. See the [constructor](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/closed-point-hom.md)
and [non-affineness](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/closed-point-nonaffine.md) guides.
