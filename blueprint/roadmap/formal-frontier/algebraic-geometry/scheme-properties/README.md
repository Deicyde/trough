# Scheme properties

> Reusable Lean theory of ring-valued point criteria, affine density, dimension bounds, single-cover subfunctor and group-object extensions, local scheme properties, components, modules, native rational maps and ring-pullback open immersions. See README.md and docs/Guide.md for exact hypotheses.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/formalization.yaml) of [FormalFrontier/scheme-properties](https://github.com/FormalFrontier/scheme-properties) at commit [09db7d88](https://github.com/FormalFrontier/scheme-properties/tree/09db7d881a2fab0967f5785b06c52aad22b45b39), Apache-2.0.*

1 article, for highlights of its formalization.yaml. The headline results in its README are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/scheme-properties](https://github.com/FormalFrontier/scheme-properties), read at commit [09db7d88](https://github.com/FormalFrontier/scheme-properties/tree/09db7d881a2fab0967f5785b06c52aad22b45b39) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “self-assessed”
- Review notes: “Self-assessment of this repository, not certification of each result or any selected-source correspondence.”
- Automation: agent; framework “Formal Frontier agent-assisted Lean development”

## Scope

Extension from one-cover dense subfunctors for morphism classes with relative pullbacks and base-change stability, assuming singleton descent only for the target; no identity or composition stability or source/subfunctor sheaf condition. Isomorphisms between two one-cover dense subfunctors extend uniquely when both ambient presheaves satisfy singleton descent, with prescribed restrictions and compatibility with identities, inverses and composition. A group law on a one-cover-dense subfunctor extends uniquely to a group-object law on the exact target presheaf, compatible with inclusion, when the cover class admits relative pullbacks and is stable under base change and composition and the target satisfies singleton descent. The proper dense two-point fixture tests the operations and recovery; no represented group scheme or source correspondence is asserted. The represented specialization concerns finite-type schemes over a field, tested on finitely generated algebras with faithfully flat covers, using Mathlib fpqc descent rather than a full induced-site equivalence or Milne's ring-level proof. Isomorphisms of two such dense restricted-points subfunctors extend uniquely to isomorphisms of finite-type schemes, without affine, separated or group hypotheses or a chosen-small-category identification. Unit-power images are one-cover dense over any commutative base ring for positive exponents; Laurent nonmembership and failure of singleton descent require a field and exponent at least two. The zero additive subfunctor is not one-cover dense over a field. Ring-pullback restricted Spec arrows over arbitrary commutative-ring maps, with exact opposite-kernel ranges forming a possibly empty disjoint cover of the common-kernel complement. No surjectivity, nontriviality, field or finite-type assumption; not unrestricted Spec-map immersions or connected components. Ring equivalences of independently universed commutative semirings preserve reducedness at corresponding prime localizations and openness of the full reduced-localization locus. For an injective family of points over an arbitrary field, that locus in the square-zero polynomial point quotient is open precisely when the family has finite image; no criterion for nonseparated families or identification with a particular source ring is asserted. Local algebra, finite presentations, components, tensors, dense-open rational maps, relative categories and function fields. Generic-point field maps need no finite-type premise; the chosen-base generic-point rational arrow is noninvertible for a nontrivial Jacobson integral target despite its reversed field-map isomorphism. Inverse reflection requires original-source local finite type, whereas reconstruction requires target-map local finite type. Exact rational inverses require independently dominant quotients; literal chosen-base overness needs the forward quotient base law. No total-scheme isomorphism, unrestricted category equivalence or source-coverage claim. Selected declaration pointers below are not a census; see docs/Guide.md.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/formalization.yaml) of [FormalFrontier/scheme-properties](https://github.com/FormalFrontier/scheme-properties) at commit [09db7d88](https://github.com/FormalFrontier/scheme-properties/tree/09db7d881a2fab0967f5785b06c52aad22b45b39), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Original project proofs of reusable scheme-property and module interfaces* (original-proof; independently-proves).
- *Formal Frontier ring-pullback proof expression* (original-proof; adapts).
- *The Rising Sea: Foundations of Algebraic Geometry*, Ravi Vakil (book; background).
- *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, J. S. Milne (book; adapts).
- *The K-book: An Introduction to Algebraic K-theory*, Charles A. Weibel (book; adapts).
- *mathlib: function-field stalk maps and native rational composition* (software; adapts).
- *mathlib: birational, Jacobson and reduced-spectrum tools* (software; adapts).
- *mathlib: generic stalks and native function-field maps* (software; adapts).
- *mathlib: native partial and rational maps, composition, and topological density* (software; adapts).
- *Multivariate Polynomials, Group Theory and Mathlib: polynomial closed-point orbit topology* (software; adapts).

## Builds on

- [Coherent modules](../../commutative-algebra/coherent-modules/README.md) (a Lake dependency, pinned at 33941aae)
- [Finite étale algebras](../finite-etale-algebras/README.md) (a Lake dependency, pinned at 79575f65)
- [Graded rings](../../commutative-algebra/graded-rings/README.md) (a Lake dependency, pinned at cb0f2e43)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 9d82a1f4)
- [Homological algebra](../../homological-algebra-and-category-theory/homological-algebra/README.md) (a Lake dependency, pinned at 6c7f755c)
- [Minimal primes](../../commutative-algebra/minimal-primes/README.md) (a Lake dependency, pinned at a82f1509)
- [Multivariate polynomials](../../commutative-algebra/multivariate-polynomials/README.md) (a Lake dependency, pinned at 9230f70a)

## Used by

- [Algebraic groups](../algebraic-groups/README.md)
- [Projective space](../projective-space/README.md)

## Highlights

- [Finiteness near all component generic points](finiteness-near-all-component-generic-points.md)

## Headline results

**Finiteness near all component generic points.** a locally finite type, quasi-compact morphism with finite ordinary point-fibres
over every component generic point becomes finite on the whole preimage of a
dense open containing all those points, provided their canonical inherited
subspace topology is discrete. In particular, this holds when the target has
finitely many irreducible components. No separatedness, quasi-separatedness,
reducedness or Noetherian hypothesis is required; empty fibres are allowed.
The [single-point criterion](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericFiniteness.lean) treats a
given generic point of the whole target directly. The accompanying
[openness theorem](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericFiniteness/Openness.lean) makes a
finite morphism an open map after restricting around a given generic point,
without assuming the target reduced or the fibre nonempty.

**Ranges of finitely generated algebras.** over any commutative ring, taking the range of an algebra map with finitely
generated domain is left adjoint to the inclusion of finitely generated
subalgebra stages. The stage functor is therefore final. The ambient algebra
need not be finitely generated, the base and carrier universes are independent,
and neither the given map nor the scalar map need be injective.

**Factorization on finite-type points.** over any commutative ring `K`, a morphism `f : X ⟶ Y` with `X` locally of
finite type over `Spec K` factors through a monomorphism `i : N ⟶ Y` if and
only if every point of `X` over a finitely generated `K`-algebra lifts through
`i` after composition with `f`. The factorization is in schemes over the
same `Spec K`. No finiteness, affineness or separatedness condition is
imposed on `N` or `Y`; the source's local finite-type hypothesis is needed.

**Points over finitely generated subalgebras.** for any given tower of commutative rings `K → R → S`, every `S`-point of a
scheme locally of finite type over `Spec K` factors through a finitely
generated `R`-subalgebra `A ⊆ S`. The forward map is the algebra-spectrum
map of the inclusion, and the composite equals the original point over the
original `Spec K`. Two stage points agreeing over `S` agree over a common
finitely generated subalgebra. No affineness, quasi-compactness or separatedness
of the tested scheme, injectivity of either tower map, or finite generation
of `R` over `K` is required. These statements concern subalgebra inclusions,
not arbitrary filtered algebra colimits.

**Morphisms from dense affine-point subfunctors.** for arbitrary schemes `X` and `Y` over any base scheme `B`, let `N_B` be
the full affine-point functor over `B`. If `D ⊆ N_B(X)` is one-cover-dense
for flat, surjective morphisms of affine `B`-schemes, every natural
transformation `α : D ⟶ N_B(Y)` is induced by a unique morphism
`f : X ⟶ Y` over the same base, with `D.ι ≫ N_B.map f = α`
(`Scheme.existsUnique_hom_of_isOneCoverDense`). No sheaf condition on `X`
or `D`, finite-product condition on `D`, or finiteness or separatedness
hypothesis is required.

**Faithful flatness of finite families.** a finite family of flat commutative-ring maps that is jointly surjective on
prime spectra induces a faithfully flat map to the product. The spectrum
implication also holds for arbitrary families of commutative semirings,
without flatness. Empty index types and zero rings are included.

**Flatness under source precomposition.** for arbitrary scheme morphisms `p : X ⟶ Y` and `f : Y ⟶ Z`, flatness and
point-surjectivity of `p`, together with flatness of `p ≫ f`, imply flatness
of `f`, without quasi-compactness or finiteness assumptions. The
[ring-tower theorem](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RingTheory/FlatSourceCancellation.lean)
cancels a faithfully flat second map from a flat composite of commutative
ring maps in independent universes; the composite need not be faithfully flat.

**Closed points of scheme pullbacks.** for specified locally finite-type arrows to the spectrum of any field, the
original projections of any specified pullback give a surjection onto pairs
of closed points. Over a separably closed field this is a canonical set
equivalence, with pairing, projection, uniqueness, eta, diagonal and
fixed-base naturality laws. No global finite-type, quasi-compactness,
separation or reducedness assumption is imposed. This does not identify the
Zariski closed-point topology with the ordinary product topology.

**Locally closed points in continuous preimages.** for arbitrary topological spaces and a continuous map, every nonempty preimage
of a locally constructible set has a member at which that same preimage is
locally closed. No separation, compactness or Noetherian hypothesis is needed;
the result does not assert preservation of constructibility by continuous maps.
A [dense-preimage application](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemePropertiesExamples/LocallyConstructiblePreimage.lean)
shows that a dense such preimage in a nonempty source has nonempty interior.

**Closedness through closed points.** in any Jacobson topological space, a locally closed subset is closed if and only
if its trace in the closed-point subspace is closed. Local closedness is required
for the full subset, not just its trace; no separation or finiteness hypothesis
is imposed.

**Cofinite closed-point topology.** in any preirreducible Noetherian topological space of Krull dimension at most
one, a subset of the closed-point subspace is closed exactly when it is the
whole space or finite. Its given topology is therefore cofinite, without
separation, sobriety or Jacobson hypotheses. The Zariski closed-point topology
of `Spec K[X]` and the Zariski topology of `MaximalSpectrum K[X]` are cofinite
over every field `K`. For any algebraic closure `L` of `K`, the
[automorphism-orbit homeomorphism](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/Topology/PolynomialClosedPointOrbits.lean)
identifies the existing `(L ≃ₐ[K] L)`-orbit quotient of cofinite `L` with this
Zariski maximal spectrum, retaining Multivariate Polynomials' underlying
equivalence. The evaluation-kernel classifier from `L` is a quotient map.
The fields may have independent universes, using the given `K`-algebra
structure on `L`; no perfection, separability or infinitude assumption on
`K` is required.

**Fibres of polynomial spectra under field extension.** for independently universed fields `K` and `L` with their given `K`-algebra,
the coefficient-extension spectrum map has finite fibre over a prime `p`
exactly when `p` is nonzero or `L` is algebraic over `K`. All ordinary point
fibres are finite exactly for algebraic extensions, and then the generic
fibre consists precisely of the zero prime of `L[X]`. Infinite algebraic
extensions and inseparable extensions are included; these are not geometric
field-valued lift fibres or a quasi-finiteness assertion.

**Locally constructible closed-point traces.** in any Jacobson topological space, a subset satisfying Mathlib's
`Topology.IsLocallyConstructible` has a dense closed-point trace, and is closed
exactly when that trace is closed in the original closed-point subspace.
Closed-point traces also detect inclusion and equality between such subsets,
with no separation or Noetherian hypothesis. The proofs use density after
intersection with arbitrary locally closed subsets, without assuming those
subsets are locally constructible. A common density theorem for arbitrary
unions of locally closed sets recovers Mathlib's locally closed density theorem
by a singleton-index specialization; this union theorem does not assert trace
conservativity.

**Maximal-point locally ringed spaces.** for any commutative Jacobson ring `R`, construct a locally ringed space on the
closed-point subspace of `Spec R`. Its inclusion induces an isomorphism of
full sheaves after pushforward, principal-open rings are `R_f`, stalks are
`R_m`, and global sections recover `R`, with nilpotents and supplied scalars.
[Localization-basis recognition](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/MaximalPointSheaf.lean)
identifies any full sheaf with compatible coordinate actions and the same
localization property. [Morphisms](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/MaximalPointMorphisms.lean)
are contravariant for homomorphisms whose contractions preserve maximal
ideals; this preservation is derived for finite-type homomorphisms from a
Jacobson ring. [Full component uniqueness](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/MaximalPointSheafMaps.lean)
identifies a supplied sheaf component from its global coordinates, without
assuming that component is already local. The inclusion need not be an
isomorphism of spaces, and no general Scheme structure is asserted for the
maximal-point space.

**Lifts to closed-point targets.** for a Jacobson locally ringed target `Y` and an arbitrary locally ringed source
`X`, `closedPointInclusionHomEquiv` identifies maps `X ⟶ C(Y)` with original
morphisms `X ⟶ Y` whose every image point is closed. The inverse is the unique
full locally ringed-space lift through the given inclusion. Its section,
stalk and global-section maps read back the original maps through the given
comparisons. It is natural in every source morphism and in closed-point-preserving
morphisms between Jacobson targets, and retains supplied structure-map triangles.
Its [affine specialization](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/MaximalPointLifts.lean)
identifies maps `X ⟶ C(R)` with original maps `X ⟶ Spec R` whose image ideals
are all maximal, for any commutative Jacobson ring `R`, and reads back the
original homomorphism `R → Γ(X)`. No Jacobson hypothesis is imposed on `X`
or its global-section ring.

**Hom recovery for maximal-point spaces.** for commutative Jacobson rings `R` and `S`, `maximalPointHomEquiv` identifies
ring homomorphisms `R →+* S` preserving maximal ideals under contraction with
all locally ringed space morphisms `C(S) ⟶ C(R)`, where
`C(R) = Spec.maximalPointSpace R`. The inverse is
`χS⁻¹ ∘ Γ(g) ∘ χR` for the original coordinate isomorphisms, so the full
morphism is recovered from its global-section map. This equivalence restricts
to supplied scalar maps. For given `K`-algebra actions in a common universe,
it identifies maximal-contraction-preserving algebra homomorphisms with
morphisms over `Spec K`; if `S` is finite type over `K`, every algebra
homomorphism corresponds, with no finite-type assumption on `R`.

**Locality of full ringed morphisms.** for commutative Jacobson rings `R,S`, a ringed morphism `g : C(S) ⟶ C(R)`
is local if and only if its original global-coordinate homomorphism
preserves maximal ideals under contraction. Under this condition the entire
original morphism is the forgotten `maximalPointMap`, and its unique locally
ringed lift retains all supplied components and respects composition.
For given `K`-algebra structures over any commutative ring `K`, scalar
compatibility and finite type of `S` over `K` imply locality, with no
finite-type hypothesis on `R`. The full sheaves retain nilpotents and the
zero ring is included.

**The integers are Jacobson.** the canonical integer ring is a Jacobson ring. A
[polynomial evaluation example](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemePropertiesExamples/IntegerMaximalPointEvaluation.lean)
identifies the maximal-point morphism over `Spec ℤ` induced by evaluation at
zero, `ℤ[X] →ₐ[ℤ] ℤ`, together with its recovered ring map and the value `X ↦ 0`.

**Reduced projective spectra.** for any
`ℕ`-graded commutative ring `A` with grading `𝒜`, `Proj 𝒜` is reduced whenever
`A` is reduced, with no nonemptiness or finiteness assumption.

**Polynomial projective coordinate separation.** over any nontrivial commutative ring and any nontrivial variable type, the
total-degree polynomial projective spectrum has at least two underlying points.
Coordinate points over the same coefficient prime are distinct for distinct
indices; each lies in exactly its own coordinate basic open. This includes the
projective line over the two-element field, without a domain or field-size bound.

**Local normality of polynomial rings.** over any commutative locally normal base ring, multivariate polynomial rings
with arbitrary variable types are locally normal.

**Global sections under flat scalar extension.** for a quasicompact quasiseparated scheme over a commutative ring `k` and a flat
commutative `k`-algebra `K`, the canonical equivalence identifies the global
sections of the base change with `K ⊗[k] Γ(X, ⊤)`. Its scalar, section and pure
tensor formulas retain the two pullback projections. Identity and tower
coherence are also available for field extensions.

**Global sections and affine targets.** if
`p : X ⟶ S` induces an isomorphism on global sections and `T` is affine,
precomposition is a bijection `(S ⟶ T) → (X ⟶ T)`, for arbitrary `X` and
`S`. A reduced connected scheme universally closed over a field has a
field of global sections. For a reduced preconnected scheme universally
closed over a field, a rational section identifies its global sections
with the base field, so every morphism to an affine scheme is constant at
that rational point. Direct import for the field criterion and the
canonical global-sections isomorphism: `SchemeProperties.GlobalSections.Field`.

**Proper affine point criterion.** for any
field `K : Type u` and `X : Scheme.{u}`, a morphism
`f : X ⟶ Spec (CommRingCat.of K)` with
`[IsProper f] [IsAffine X] [PreconnectedSpace X]` gives `Subsingleton X`
(`AlgebraicGeometry.Scheme.Hom.subsingleton_of_isProper_of_isAffine`).
The underlying point set has at most one point; `X` may be empty or nonreduced.
This does not assert a scheme isomorphism or uniqueness of scheme morphisms.
Direct import: `SchemeProperties.ProperAffineField`.

**Finite-variable polynomial Proj.** is proper over the original `Spec R` for every commutative ring `R : Type (max u v)` and finite `σ : Type v`, including zero rings and empty `σ`; see the [guide](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/docs/SpectraAndGlobalGeometry.md#polynomial-proj-properness).

**Rigidity from a collapsed fibre.** for a
field `K`, a proper integral `K`-scheme `X` whose structure map has a
`K`-rational section, a preconnected `K`-scheme `Y` with an arbitrary chosen
point `y₀`, and a `K`-scheme `Z` separated over `K`, a compatible `K`-morphism
`h : X ×[K] Y ⟶ Z` factors uniquely as `h = snd ≫ g` for a `K`-morphism
`g : Y ⟶ Z` if the topological image under `h` of the projection fibre over
`y₀` is subsingleton. The factorization is equality of scheme morphisms.
The parameter need not be reduced, and `y₀` need not be rational or closed.
Direct import: `SchemeProperties.Rigidity`.

**Real–complex residue degrees.** the coproduct `Spec ℝ ⨿ Spec ℂ`, over `Spec ℝ` by the identity and the
standard real-algebra map to `ℂ`, has two distinct closed points. Their
original residue real algebras are canonically equivalent to `ℝ` and `ℂ`
and have real dimensions one and two, respectively.

## Main results

The 149 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `AlgebraicGeometry.Scheme.Hom.exists_isFinite_morphismRestrict_of_discreteTopology_genericPoints` | theorem | [SchemeProperties/GenericFiniteness/Components.lean, line 84](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericFiniteness/Components.lean#L84) |  |
| `AlgebraicGeometry.Scheme.Hom.exists_isFinite_morphismRestrict_of_finite_irreducibleComponents` | theorem | [SchemeProperties/GenericFiniteness/Components.lean, line 160](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericFiniteness/Components.lean#L160) |  |
| `PrimeSpectrum.isReduced_atPrime_homeomorphOfRingEquiv_iff` | theorem | [SchemeProperties/ReducedLocusEquiv.lean, line 34](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/ReducedLocusEquiv.lean#L34) |  |
| `PrimeSpectrum.isOpen_isReduced_atPrime_iff_ringEquiv` | theorem | [SchemeProperties/ReducedLocusEquiv.lean, line 53](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/ReducedLocusEquiv.lean#L53) |  |
| `MvPolynomial.isOpen_reduced_atPrime_pointSquareZeroQuotient_iff_finite_range` | theorem | [SchemeProperties/PolynomialPointSquareZeroReducedLocus.lean, line 45](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PolynomialPointSquareZeroReducedLocus.lean#L45) |  |
| `CategoryTheory.Subfunctor.IsOneCoverDense` | def | [SchemeProperties/SingleCoverExtension.lean, line 55](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/SingleCoverExtension.lean#L55) |  |
| `CategoryTheory.Subfunctor.oneCoverExtensionEquiv` | def | [SchemeProperties/SingleCoverExtension.lean, line 252](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/SingleCoverExtension.lean#L252) |  |
| `CategoryTheory.Subfunctor.IsOneCoverDense.grpObj` | def | [SchemeProperties/SingleCoverGroup.lean, line 404](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/SingleCoverGroup.lean#L404) |  |
| `CategoryTheory.Subfunctor.IsOneCoverDense.grpObj_isMonHom` | theorem | [SchemeProperties/SingleCoverGroup.lean, line 635](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/SingleCoverGroup.lean#L635) |  |
| `CategoryTheory.Subfunctor.IsOneCoverDense.grpObj_unique` | theorem | [SchemeProperties/SingleCoverGroup.lean, line 646](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/SingleCoverGroup.lean#L646) |  |
| `CategoryTheory.Subfunctor.extendOneCoverIso` | def | [SchemeProperties/SingleCoverExtension.lean, line 365](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/SingleCoverExtension.lean#L365) |  |
| `AlgebraicGeometry.algebraicOverPoints_isSheafFor_faithfullyFlat` | theorem | [SchemeProperties/FiniteTypeSingleCover.lean, line 150](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/FiniteTypeSingleCover.lean#L150) |  |
| `AlgebraicGeometry.algebraicOverOneCoverEquiv` | def | [SchemeProperties/FiniteTypeSingleCover.lean, line 216](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/FiniteTypeSingleCover.lean#L216) |  |
| `AlgebraicGeometry.extendAlgebraicOverIso` | def | [SchemeProperties/FiniteTypeSingleCover.lean, line 275](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/FiniteTypeSingleCover.lean#L275) |  |
| `AlgebraicGeometry.powerImage_isOneCoverDense` | theorem | [SchemeProperties/PowerImage.lean, line 191](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PowerImage.lean#L191) |  |
| `AlgebraicGeometry.laurentUnit_not_mem_powerImage` | theorem | [SchemeProperties/PowerImage.lean, line 239](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PowerImage.lean#L239) |  |
| `AlgebraicGeometry.powerImage_not_isSheafFor_root` | theorem | [SchemeProperties/PowerImage.lean, line 292](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PowerImage.lean#L292) |  |
| `AlgebraicGeometry.zeroAdditiveSubfunctor_not_oneCoverDense` | theorem | [SchemeProperties/PowerImage.lean, line 309](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PowerImage.lean#L309) |  |
| `SheafOfModules.Presentation.isFinite_map` | theorem | [SchemeProperties/SheafFinitePresentationTransport.lean, line 43](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/SheafFinitePresentationTransport.lean#L43) |  |
| `SheafOfModules.Presentation.isFinitePresentation` | theorem | [SchemeProperties/SheafFinitePresentationTransport.lean, line 68](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/SheafFinitePresentationTransport.lean#L68) |  |
| `AlgebraicGeometry.Scheme.Modules.isFinite_presentationRestrict` | theorem | [SchemeProperties/ModuleFinitePresentation.lean, line 49](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/ModuleFinitePresentation.lean#L49) |  |
| `AlgebraicGeometry.isFinitePresentation_tilde` | theorem | [SchemeProperties/ModuleFinitePresentation.lean, line 77](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/ModuleFinitePresentation.lean#L77) |  |
| `AlgebraicGeometry.Scheme.Modules.exists_isOpenCover_isFinite_presentation` | theorem | [SchemeProperties/ModuleFinitePresentation.lean, line 96](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/ModuleFinitePresentation.lean#L96) |  |
| `AlgebraicGeometry.Scheme.PartialMap.isOver_comp_of_isDominant_first` | theorem | [SchemeProperties/RationalMapComposition.lean, line 34](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapComposition.lean#L34) |  |
| `AlgebraicGeometry.Scheme.RationalMap.isOver_comp_of_isDominant_first` | theorem | [SchemeProperties/RationalMapComposition.lean, line 62](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapComposition.lean#L62) |  |
| `AlgebraicGeometry.Scheme.PartialMap.PullsDenseOpens` | def | [SchemeProperties/DenseOpenPullback.lean, line 30](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullback.lean#L30) |  |
| `AlgebraicGeometry.Scheme.PartialMap.pullsDenseOpens_iff_of_equiv` | theorem | [SchemeProperties/DenseOpenPullback.lean, line 41](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullback.lean#L41) |  |
| `AlgebraicGeometry.Scheme.PartialMap.pullsDenseOpens_restrict_iff` | theorem | [SchemeProperties/DenseOpenPullback.lean, line 67](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullback.lean#L67) |  |
| `AlgebraicGeometry.Scheme.PartialMap.pullsDenseOpens_of_isOpenMap` | theorem | [SchemeProperties/DenseOpenPullback.lean, line 73](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullback.lean#L73) |  |
| `AlgebraicGeometry.Scheme.PartialMap.pullsDenseOpens_of_isDominant` | theorem | [SchemeProperties/DenseOpenPullback.lean, line 82](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullback.lean#L82) |  |
| `AlgebraicGeometry.Scheme.RationalMap.PullsDenseOpens` | def | [SchemeProperties/DenseOpenPullback.lean, line 94](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullback.lean#L94) |  |
| `AlgebraicGeometry.Scheme.PartialMap.pullsDenseOpens_toRationalMap_iff` | theorem | [SchemeProperties/DenseOpenPullback.lean, line 102](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullback.lean#L102) |  |
| `AlgebraicGeometry.Scheme.RationalMap.pullsDenseOpens_representative_iff` | theorem | [SchemeProperties/DenseOpenPullback.lean, line 115](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullback.lean#L115) |  |
| `AlgebraicGeometry.Scheme.PartialMap.compOfPullsDenseOpens` | def | [SchemeProperties/DenseOpenComposition.lean, line 42](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenComposition.lean#L42) |  |
| `AlgebraicGeometry.Scheme.RationalMap.compOfPullsDenseOpens` | def | [SchemeProperties/DenseOpenComposition.lean, line 141](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenComposition.lean#L141) |  |
| `AlgebraicGeometry.Scheme.PartialMap.compOfPullsDenseOpens_equiv_of_equiv` | theorem | [SchemeProperties/DenseOpenComposition.lean, line 108](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenComposition.lean#L108) |  |
| `AlgebraicGeometry.Scheme.RationalMap.toRationalMap_compOfPullsDenseOpens` | theorem | [SchemeProperties/DenseOpenComposition.lean, line 157](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenComposition.lean#L157) |  |
| `AlgebraicGeometry.Scheme.PartialMap.compOfPullsDenseOpens_toPartialMap` | theorem | [SchemeProperties/DenseOpenComposition.lean, line 119](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenComposition.lean#L119) |  |
| `AlgebraicGeometry.Scheme.RationalMap.compOfPullsDenseOpens_toRationalMap` | theorem | [SchemeProperties/DenseOpenComposition.lean, line 169](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenComposition.lean#L169) |  |
| `AlgebraicGeometry.Scheme.PartialMap.compOfPullsDenseOpens_eq_comp` | theorem | [SchemeProperties/DenseOpenComposition.lean, line 129](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenComposition.lean#L129) |  |
| `AlgebraicGeometry.Scheme.RationalMap.compOfPullsDenseOpens_eq_comp` | theorem | [SchemeProperties/DenseOpenComposition.lean, line 177](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenComposition.lean#L177) |  |
| `AlgebraicGeometry.Scheme.PartialMap.isOver_compOfPullsDenseOpens` | theorem | [SchemeProperties/DenseOpenCompositionOver.lean, line 46](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionOver.lean#L46) |  |
| `AlgebraicGeometry.Scheme.RationalMap.isOver_compOfPullsDenseOpens` | theorem | [SchemeProperties/DenseOpenCompositionOver.lean, line 75](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionOver.lean#L75) |  |
| `AlgebraicGeometry.Scheme.PartialMap.pullsDenseOpens_compOfPullsDenseOpens` | theorem | [SchemeProperties/DenseOpenCompositionClosure.lean, line 51](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionClosure.lean#L51) |  |
| `AlgebraicGeometry.Scheme.RationalMap.pullsDenseOpens_compOfPullsDenseOpens` | theorem | [SchemeProperties/DenseOpenCompositionClosure.lean, line 63](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionClosure.lean#L63) |  |
| `AlgebraicGeometry.Scheme.PartialMap.compOfPullsDenseOpens_assoc` | theorem | [SchemeProperties/DenseOpenCompositionAssociativity.lean, line 43](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionAssociativity.lean#L43) |  |
| `AlgebraicGeometry.Scheme.RationalMap.compOfPullsDenseOpens_assoc` | theorem | [SchemeProperties/DenseOpenCompositionAssociativity.lean, line 65](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionAssociativity.lean#L65) |  |
| `AlgebraicGeometry.Scheme.PartialMap.pullsDenseOpens_id` | theorem | [SchemeProperties/DenseOpenCompositionUnits.lean, line 43](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionUnits.lean#L43) |  |
| `AlgebraicGeometry.Scheme.PartialMap.id_compOfPullsDenseOpens` | theorem | [SchemeProperties/DenseOpenCompositionUnits.lean, line 52](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionUnits.lean#L52) |  |
| `AlgebraicGeometry.Scheme.PartialMap.compOfPullsDenseOpens_id` | theorem | [SchemeProperties/DenseOpenCompositionUnits.lean, line 66](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionUnits.lean#L66) |  |
| `AlgebraicGeometry.Scheme.RationalMap.pullsDenseOpens_id` | theorem | [SchemeProperties/DenseOpenCompositionUnits.lean, line 76](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionUnits.lean#L76) |  |
| `AlgebraicGeometry.Scheme.RationalMap.id_compOfPullsDenseOpens` | theorem | [SchemeProperties/DenseOpenCompositionUnits.lean, line 80](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionUnits.lean#L80) |  |
| `AlgebraicGeometry.Scheme.RationalMap.compOfPullsDenseOpens_id` | theorem | [SchemeProperties/DenseOpenCompositionUnits.lean, line 90](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenCompositionUnits.lean#L90) |  |
| `AlgebraicGeometry.Scheme.PartialMap.isDominant_of_pullsDenseOpens` | theorem | [SchemeProperties/DenseOpenPullbackDominance.lean, line 31](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullbackDominance.lean#L31) |  |
| `AlgebraicGeometry.Scheme.PartialMap.pullsDenseOpens_iff_isDominant` | theorem | [SchemeProperties/DenseOpenPullbackDominance.lean, line 43](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullbackDominance.lean#L43) |  |
| `AlgebraicGeometry.Scheme.RationalMap.isDominant_of_pullsDenseOpens` | theorem | [SchemeProperties/DenseOpenPullbackDominance.lean, line 56](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullbackDominance.lean#L56) |  |
| `AlgebraicGeometry.Scheme.RationalMap.pullsDenseOpens_iff_isDominant` | theorem | [SchemeProperties/DenseOpenPullbackDominance.lean, line 64](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenPullbackDominance.lean#L64) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme` | structure | [SchemeProperties/DenseOpenRationalCategory.lean, line 30](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L30) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.of` | def | [SchemeProperties/DenseOpenRationalCategory.lean, line 37](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L37) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.Hom` | structure | [SchemeProperties/DenseOpenRationalCategory.lean, line 40](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L40) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.hom` | def | [SchemeProperties/DenseOpenRationalCategory.lean, line 46](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L46) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.toRationalMap_hom` | theorem | [SchemeProperties/DenseOpenRationalCategory.lean, line 49](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L49) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.hom_ext` | theorem | [SchemeProperties/DenseOpenRationalCategory.lean, line 54](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L54) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.toRationalMap_id` | theorem | [SchemeProperties/DenseOpenRationalCategory.lean, line 76](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L76) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.toRationalMap_comp` | theorem | [SchemeProperties/DenseOpenRationalCategory.lean, line 79](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L79) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.homEquivDominant` | def | [SchemeProperties/DenseOpenRationalCategory.lean, line 87](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L87) |  |
| `AlgebraicGeometry.DenseOpenRationalScheme.homEquivDominant_apply_val` | theorem | [SchemeProperties/DenseOpenRationalCategory.lean, line 103](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategory.lean#L103) |  |
| `AlgebraicGeometry.IntegralDominantRationalScheme` | structure | [SchemeProperties/IntegralDominantRationalCategory.lean, line 69](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategory.lean#L69) |  |
| `AlgebraicGeometry.IntegralDominantRationalScheme.Hom` | structure | [SchemeProperties/IntegralDominantRationalCategory.lean, line 84](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategory.lean#L84) |  |
| `AlgebraicGeometry.IntegralDominantRationalScheme.toRationalMap_id` | theorem | [SchemeProperties/IntegralDominantRationalCategory.lean, line 120](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategory.lean#L120) |  |
| `AlgebraicGeometry.IntegralDominantRationalScheme.toRationalMap_comp` | theorem | [SchemeProperties/IntegralDominantRationalCategory.lean, line 123](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategory.lean#L123) |  |
| `AlgebraicGeometry.IntegralDenseOpenRationalScheme` | abbrev | [SchemeProperties/IntegralDominantRationalCategory.lean, line 36](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategory.lean#L36) |  |
| `AlgebraicGeometry.IntegralDenseOpenRationalScheme.toNative` | def | [SchemeProperties/IntegralDominantRationalCategory.lean, line 145](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategory.lean#L145) |  |
| `AlgebraicGeometry.IntegralDominantRationalScheme.toDenseOpen` | def | [SchemeProperties/IntegralDominantRationalCategory.lean, line 186](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategory.lean#L186) |  |
| `AlgebraicGeometry.integralDenseOpenEquivalence` | def | [SchemeProperties/IntegralDominantRationalCategory.lean, line 235](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategory.lean#L235) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver` | structure | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 30](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L30) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.of` | def | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 39](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L39) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.Hom` | structure | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 50](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L50) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.hom` | def | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 59](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L59) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.toRationalMap_hom` | theorem | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 64](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L64) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.isOver_iff_compHom` | theorem | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 73](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L73) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.hom_ext` | theorem | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 87](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L87) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.toRationalMap_id` | theorem | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 121](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L121) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.toRationalMap_comp` | theorem | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 124](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L124) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.forget` | def | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 131](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L131) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.forget_obj_toScheme` | theorem | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 137](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L137) |  |
| `AlgebraicGeometry.DenseOpenRationalSchemeOver.forget_map_toRationalMap` | theorem | [SchemeProperties/DenseOpenRationalCategoryOver.lean, line 140](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/DenseOpenRationalCategoryOver.lean#L140) |  |
| `AlgebraicGeometry.IntegralDenseOpenRationalSchemeOver` | abbrev | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 35](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L35) |  |
| `AlgebraicGeometry.IntegralDominantRationalSchemeOver` | structure | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 68](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L68) |  |
| `AlgebraicGeometry.IntegralDominantRationalSchemeOver.Hom` | structure | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 86](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L86) |  |
| `AlgebraicGeometry.IntegralDominantRationalSchemeOver.isOver_iff_compHom` | theorem | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 116](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L116) |  |
| `AlgebraicGeometry.IntegralDenseOpenRationalSchemeOver.toNative` | def | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 183](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L183) |  |
| `AlgebraicGeometry.IntegralDominantRationalSchemeOver.toDenseOpen` | def | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 222](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L222) |  |
| `AlgebraicGeometry.integralDenseOpenEquivalenceOver` | def | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 270](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L270) |  |
| `AlgebraicGeometry.IntegralDenseOpenRationalSchemeOver.forget` | def | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 284](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L284) |  |
| `AlgebraicGeometry.IntegralDominantRationalSchemeOver.forget` | def | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 320](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L320) |  |
| `AlgebraicGeometry.IntegralDenseOpenRationalSchemeOver.forgetInclusionIso` | def | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 346](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L346) |  |
| `AlgebraicGeometry.IntegralDenseOpenRationalSchemeOver.forgetNativeIso` | def | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 359](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L359) |  |
| `AlgebraicGeometry.IntegralDominantRationalSchemeOver.forgetDenseOpenIso` | def | [SchemeProperties/IntegralDominantRationalCategoryOver.lean, line 386](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/IntegralDominantRationalCategoryOver.lean#L386) |  |
| `AlgebraicGeometry.Scheme.RationalMap.fromFunctionField_closedPoint` | theorem | [SchemeProperties/RationalFunctionFieldPullback.lean, line 74](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldPullback.lean#L74) |  |
| `AlgebraicGeometry.Scheme.RationalMap.functionFieldMap` | def | [SchemeProperties/RationalFunctionFieldPullback.lean, line 82](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldPullback.lean#L82) |  |
| `AlgebraicGeometry.Scheme.RationalMap.functionFieldMap_eq_of_fromFunctionField_eq` | theorem | [SchemeProperties/RationalFunctionFieldPullback.lean, line 97](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldPullback.lean#L97) |  |
| `AlgebraicGeometry.Scheme.RationalMap.fromFunctionField_comp` | theorem | [SchemeProperties/RationalFunctionFieldPullback.lean, line 165](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldPullback.lean#L165) |  |
| `AlgebraicGeometry.Scheme.RationalMap.functionFieldMap_id` | theorem | [SchemeProperties/RationalFunctionFieldPullback.lean, line 197](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldPullback.lean#L197) |  |
| `AlgebraicGeometry.Scheme.RationalMap.functionFieldMap_comp` | theorem | [SchemeProperties/RationalFunctionFieldPullback.lean, line 177](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldPullback.lean#L177) |  |
| `AlgebraicGeometry.IntegralDominantRationalScheme.functionFieldFunctor` | def | [SchemeProperties/RationalFunctionFieldPullback.lean, line 218](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldPullback.lean#L218) |  |
| `AlgebraicGeometry.Scheme.RationalMap.eq_of_functionFieldMap_eq` | theorem | [SchemeProperties/RationalFunctionFieldFaithfulness.lean, line 57](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldFaithfulness.lean#L57) |  |
| `AlgebraicGeometry.Scheme.RationalMap.ofFunctionFieldMap` | def | [SchemeProperties/RationalFunctionFieldReconstruction.lean, line 47](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldReconstruction.lean#L47) |  |
| `AlgebraicGeometry.Scheme.RationalMap.ofFunctionFieldMap_compHom` | theorem | [SchemeProperties/RationalFunctionFieldReconstruction.lean, line 54](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldReconstruction.lean#L54) |  |
| `AlgebraicGeometry.Scheme.RationalMap.isDominant_ofFunctionFieldMap` | theorem | [SchemeProperties/RationalFunctionFieldReconstruction.lean, line 84](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldReconstruction.lean#L84) |  |
| `AlgebraicGeometry.Scheme.RationalMap.ofFunctionFieldMap_isDominant` | instance | [SchemeProperties/RationalFunctionFieldReconstruction.lean, line 136](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldReconstruction.lean#L136) |  |
| `AlgebraicGeometry.Scheme.RationalMap.functionFieldMap_ofFunctionFieldMap` | theorem | [SchemeProperties/RationalFunctionFieldReconstruction.lean, line 144](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldReconstruction.lean#L144) |  |
| `AlgebraicGeometry.Scheme.RationalMap.functionFieldMap_compatible` | theorem | [SchemeProperties/RationalFunctionFieldReconstruction.lean, line 161](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldReconstruction.lean#L161) |  |
| `AlgebraicGeometry.Scheme.RationalMap.ofFunctionFieldMap_functionFieldMap` | theorem | [SchemeProperties/RationalFunctionFieldReconstruction.lean, line 179](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldReconstruction.lean#L179) |  |
| `AlgebraicGeometry.IntegralDominantRationalSchemeOver.isIso_functionFieldMap` | theorem | [SchemeProperties/RationalFunctionFieldInverse.lean, line 82](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldInverse.lean#L82) |  |
| `AlgebraicGeometry.IntegralDominantRationalSchemeOver.isIso_iff_isIso_functionFieldMap` | theorem | [SchemeProperties/RationalFunctionFieldInverse.lean, line 112](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalFunctionFieldInverse.lean#L112) |  |
| `AlgebraicGeometry.Scheme.RationalMap.exists_partialIso_of_inverse` | theorem | [SchemeProperties/RationalMapPartialIso.lean, line 248](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapPartialIso.lean#L248) |  |
| `AlgebraicGeometry.Scheme.RationalMap.exists_partialIso_of_inverse_over` | theorem | [SchemeProperties/RationalMapPartialIso.lean, line 267](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapPartialIso.lean#L267) |  |
| `AlgebraicGeometry.Scheme.PartialIso.toRationalMap_isDominant` | instance | [SchemeProperties/RationalMapPartialIso.lean, line 370](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapPartialIso.lean#L370) |  |
| `AlgebraicGeometry.Scheme.PartialIso.toRationalMap_comp_symm` | theorem | [SchemeProperties/RationalMapPartialIso.lean, line 375](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapPartialIso.lean#L375) |  |
| `AlgebraicGeometry.Scheme.PartialIso.symm_toRationalMap_comp` | theorem | [SchemeProperties/RationalMapPartialIso.lean, line 384](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapPartialIso.lean#L384) |  |
| `AlgebraicGeometry.Scheme.PartialIso.toRationalMap_compHom_of_isOver` | theorem | [SchemeProperties/RationalMapPartialIso.lean, line 398](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapPartialIso.lean#L398) |  |
| `AlgebraicGeometry.Scheme.PartialIso.symm_toRationalMap_compHom_of_isOver` | theorem | [SchemeProperties/RationalMapPartialIso.lean, line 408](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/RationalMapPartialIso.lean#L408) |  |
| `AlgebraicGeometry.Scheme.PartialIso.subsingleton_target` | theorem | [SchemeProperties/JacobsonBirationalObstruction.lean, line 33](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/JacobsonBirationalObstruction.lean#L33) |  |
| `AlgebraicGeometry.Scheme.not_birational_of_subsingleton_of_jacobson` | theorem | [SchemeProperties/JacobsonBirationalObstruction.lean, line 53](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/JacobsonBirationalObstruction.lean#L53) |  |
| `AlgebraicGeometry.Scheme.nontrivial_spec_polynomial` | theorem | [SchemeProperties/JacobsonBirationalObstruction.lean, line 59](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/JacobsonBirationalObstruction.lean#L59) |  |
| `AlgebraicGeometry.Scheme.not_birational_spec_field_spec_polynomial` | theorem | [SchemeProperties/JacobsonBirationalObstruction.lean, line 69](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/JacobsonBirationalObstruction.lean#L69) |  |
| `AlgebraicGeometry.Scheme.fromSpecStalk_genericPoint_isDominant` | instance | [SchemeProperties/GenericPointFunctionField.lean, line 46](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointFunctionField.lean#L46) |  |
| `AlgebraicGeometry.Scheme.fromSpecStalk_genericPoint_toRationalMap_isDominant` | instance | [SchemeProperties/GenericPointFunctionField.lean, line 55](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointFunctionField.lean#L55) |  |
| `AlgebraicGeometry.Scheme.genericPoint_functionFieldMap_specMap` | theorem | [SchemeProperties/GenericPointFunctionField.lean, line 62](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointFunctionField.lean#L62) |  |
| `AlgebraicGeometry.Scheme.genericPoint_functionFieldMap_isIso` | instance | [SchemeProperties/GenericPointFunctionField.lean, line 81](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointFunctionField.lean#L81) |  |
| `AlgebraicGeometry.Scheme.not_locallyOfFiniteType_fromSpecStalk_genericPoint` | theorem | [SchemeProperties/GenericPointFunctionField.lean, line 106](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointFunctionField.lean#L106) |  |
| `AlgebraicGeometry.Scheme.not_locallyOfFiniteType_fromSpecStalk_genericPoint_comp` | theorem | [SchemeProperties/GenericPointFunctionField.lean, line 127](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointFunctionField.lean#L127) |  |
| `AlgebraicGeometry.Scheme.RationalMap.not_twoSidedInverse_of_subsingleton_of_jacobson` | theorem | [SchemeProperties/GenericPointRationalNoninvertibility.lean, line 35](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointRationalNoninvertibility.lean#L35) |  |
| `AlgebraicGeometry.Scheme.genericPointRationalHom` | def | [SchemeProperties/GenericPointRationalNoninvertibility.lean, line 54](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointRationalNoninvertibility.lean#L54) |  |
| `AlgebraicGeometry.Scheme.genericPointRationalHom_toRationalMap` | theorem | [SchemeProperties/GenericPointRationalNoninvertibility.lean, line 69](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointRationalNoninvertibility.lean#L69) |  |
| `AlgebraicGeometry.Scheme.genericPointRationalHom_boundary` | theorem | [SchemeProperties/GenericPointRationalNoninvertibility.lean, line 76](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/GenericPointRationalNoninvertibility.lean#L76) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.ker_fst_mul_ker_snd` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 46](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L46) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.ker_toBase` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 65](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L65) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.awayMap_fst_bijective` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 104](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L104) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.awayMap_snd_bijective` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 135](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L135) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.fstTarget_inf_sndTarget` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 216](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L216) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.fstTarget_sup_sndTarget` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 225](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L225) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.isOpenImmersion_fstOpenMap` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 288](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L288) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.isOpenImmersion_sndOpenMap` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 348](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L348) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.range_fstOpenMap` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 414](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L414) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.range_sndOpenMap` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 448](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L448) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.disjoint_ranges` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 482](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L482) |  |
| `AlgebraicGeometry.PullbackOpenImmersion.union_ranges` | theorem | [SchemeProperties/PullbackOpenImmersion.lean, line 491](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/SchemeProperties/PullbackOpenImmersion.lean#L491) |  |
