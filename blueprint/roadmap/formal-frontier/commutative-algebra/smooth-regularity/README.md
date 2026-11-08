# Smooth regularity

> First-order conormal criteria and formally étale cotangent-space comparisons over commutative rings, presentation-relation and local Jacobian criteria, smooth-to-regular implications over fields, Artinian regularity criteria, and Dedekind consequences for commutative algebras and affine schemes.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/formalization.yaml) of [FormalFrontier/smooth-regularity](https://github.com/FormalFrontier/smooth-regularity) at commit [fbc0ee82](https://github.com/FormalFrontier/smooth-regularity/tree/fbc0ee8256971d0527033b71ef3886e9f2428420), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 5 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/smooth-regularity](https://github.com/FormalFrontier/smooth-regularity), read at commit [fbc0ee82](https://github.com/FormalFrontier/smooth-regularity/tree/fbc0ee8256971d0527033b71ef3886e9f2428420) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”
- Review notes: “Independent non-author agent review covers the Lean mathematics, module migration, ordinary-import clients and conormal evaluation API. External proofs using definitional reduction for conormal evaluation must migrate to the propositional theorems; backward definitional compatibility is not claimed. This review status does not assert human mathematical review or complete source coverage. Generated API signatures are documentation, not independent proof certification.”
- Automation: agent; tool setup “Formal Frontier AI agents used Lean and Lake with pinned mathlib and independent non-author agent development review.”
- Automation notes: “AI-assisted development under human project direction. No human mathematical review, model identity, total expenditure or elapsed-time total is asserted.”

## Scope

Canonical conormal injectivity from first-order sections, conormal equivalences for formally étale quotient targets, and local cotangent-space comparisons over commutative rings, without ambient smoothness or a residue section. Split-residue comparisons require only formal unramifiedness and a supplied section. Presentation-relation APIs, conditional local Jacobian criteria, smooth-to-regular implications over fields, and dimension-at-most-one Dedekind consequences. The general converse from regularity to smoothness is not included. Relation selection alone does not establish generation, quotient regularity or target smoothness. Affine Dedekind results retain integrality, affineness, smoothness and the topological dimension bound. Complete source formalization is not claimed.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/formalization.yaml) of [FormalFrontier/smooth-regularity](https://github.com/FormalFrontier/smooth-regularity) at commit [fbc0ee82](https://github.com/FormalFrontier/smooth-regularity/tree/fbc0ee8256971d0527033b71ef3886e9f2428420), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *The Stacks Project*, The Stacks Project Authors, Tags 00TR and 00TT (online mathematical reference; background).
- *Smooth regularity and cotangent-relation constructions*, Formal Frontier Agents (original project proofs; formalizes).

## Builds on

No other Formal Frontier library.

## Used by

- [Algebraic groups](../../algebraic-geometry/algebraic-groups/README.md)


## Headline results

**First-order conormal maps.** For an arbitrary extension `P → S` of
commutative algebras over a commutative ring `K`, a `K`-algebra section of
`P/I² → S` makes [the canonical conormal map](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/Conormal.lean)
`I/I² → S ⊗[P] Ω[P⁄K]` injective. If `S` is formally étale over `K`, this
map is an equivalence. Neither result assumes smoothness of `P` or a section
into `P`. The equivalence's forward map is Mathlib's `cotangentComplex`,
with an evaluation law on every kernel class.

**Cotangent spaces and differentials.** For a local algebra over a
commutative ring, [the residue-field equivalence](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/Conormal.lean)
identifies its cotangent space with the residue-field base change of Kähler
differentials when the residue field is formally étale over the base; no
residue section is needed. It agrees with the split-residue construction
when a section is supplied. The latter requires only formal unramifiedness
of the residue field, and also applies to a supplied residue-field algebra
equivalence with the base. At a maximal ideal of a finite-type algebra over
an algebraically closed field, [the closed-point comparison](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/AlgClosed.lean#L48)
applies. Formal étaleness of the residue extension is not automatic.

**Presentation relations and local Jacobian criteria.** A finite presentation
admits a [linearly independent selection](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/CotangentRelations.lean#L35)
of relations spanning its residue-field cotangent kernel at any prime over a
commutative base; [dimension and localization](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/CotangentDimension.lean)
provide related comparison tools. To infer formal smoothness of a local target,
[the relation criterion](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/RelationJacobian.lean#L33) additionally
requires a formally smooth presenting algebra with finite free differentials,
a finite family *generating the presentation kernel*, and independence of its
residue-field cotangent images. The [quotient criterion](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/QuotientRelationJacobian.lean#L32)
derives generation only with a finite-dimensional **domain quotient** and the
stated Krull-dimension comparison; it does not require the target to be a domain.

**Smooth implies regular.** A [standard-smooth field-algebra](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/StandardSmooth.lean#L446)
has regular prime localizations. The [smooth-at-prime result](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/SmoothAt.lean#L24)
requires a finite-type algebra over a field, and the
[smooth-locus result](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/SmoothLocus.lean#L25) requires a scheme
locally of finite type over a field; smooth points have regular local stalks.
The general converse, regular implies smooth, is **not** proved here.

**Dedekind consequences.** [Smooth field-algebras are regular](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/Dedekind.lean),
and a [regular domain of dimension at most one](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/Dedekind.lean#L36)
is Dedekind (including the zero-dimensional field case). Thus a smooth domain
over a field with that dimension bound is Dedekind. For schemes, the
[global-sections theorem](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/AffineDedekind.lean#L27) requires an
**integral, affine, smooth** scheme over a field of topological dimension at
most one; it does not assert the nonaffine, nonintegral or higher-dimensional
cases.

The [Artinian criteria](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/SmoothRegularity/Artinian.lean) state that a commutative
Artinian local ring is regular if and only if it is a field, and that a
commutative Artinian ring is regular if and only if it is reduced, including
the zero ring. The proofs use the dimension-zero and localization criteria
from Mathlib. See the [signature and boundary guide](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/docs/Artinian.md).

See the [generated API reference](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/docs/API.md) for all fourteen Conormal
signatures with their commutative-ring hypotheses, independent universes and
canonical-map laws, alongside 22 older native display entries for other modules.
The [documentation guide](https://github.com/FormalFrontier/smooth-regularity/blob/fbc0ee8256971d0527033b71ef3886e9f2428420/docs/README.md) distinguishes the source-header and
native input bindings. The Artinian signatures are documented separately.
