# Scheme properties

> Reusable Lean theory of ring-valued point criteria, affine density, dimension bounds, single-cover subfunctor and group-object extensions, local scheme properties, components, modules, native rational maps and ring-pullback open immersions. See README.md and docs/Guide.md for exact hypotheses.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/formalization.yaml) of [FormalFrontier/scheme-properties](https://github.com/FormalFrontier/scheme-properties) at commit [09db7d88](https://github.com/FormalFrontier/scheme-properties/tree/09db7d881a2fab0967f5785b06c52aad22b45b39), Apache-2.0.*

1 article: 1 for highlights of its formalization.yaml whose declarations the scan finds. The headline results in its README are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/scheme-properties](https://github.com/FormalFrontier/scheme-properties), read at commit [09db7d88](https://github.com/FormalFrontier/scheme-properties/tree/09db7d881a2fab0967f5785b06c52aad22b45b39) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “self-assessed”.
- Review notes: “Self-assessment of this repository, not certification of each result or any selected-source correspondence.”
- Automation: agent; framework “Formal Frontier agent-assisted Lean development”; notes “AI-assisted Lean proofs, examples and documentation, with mathematical review; no uniform model or cost claim.”

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
- [Finite étale algebras](../../commutative-algebra/finite-etale-algebras/README.md) (a Lake dependency, pinned at 79575f65)
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

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/scheme-properties/blob/09db7d881a2fab0967f5785b06c52aad22b45b39/README.md#headline-results) of [FormalFrontier/scheme-properties](https://github.com/FormalFrontier/scheme-properties) at commit [09db7d88](https://github.com/FormalFrontier/scheme-properties/tree/09db7d881a2fab0967f5785b06c52aad22b45b39), Apache-2.0.*

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

Its formalization.yaml lists 149 main results, and the scan finds 149 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
