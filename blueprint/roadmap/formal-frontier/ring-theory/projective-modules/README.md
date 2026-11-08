# Projective modules

> Row-finite linear systems with target satisfying Module.Baer have full solutions whenever every finite set of rows has a solution. Over a semisimple ring this holds for every left module, including modules over division rings; scalars, targets, rows and coordinates have independent universes. Solutions are arbitrary coordinate functions, not necessarily finitely supported functions. Reusable Lean theory of projective modules: finite-projective dual and evaluation base change, invertible modules, exterior algebras and powers, determinants, bounded cancellation and countable absorption, infinite free coordinates, finite stable presentations and IBN-only integer-rank independence, balanced tensor products, right scalar extension and chosen right-free coefficient transport along arbitrary unital semiring homomorphisms, exactness, local and PID freeness, preadditive stable module categories, countably generated submodules over left-Noetherian rings, and locally constant rank and componentwise-free classification. Noncommutative and commutative results retain their distinct hypotheses; rank classification is not asserted for all finite projectives over arbitrary rings. Given an equivalence of module categories over arbitrary rings, finite generation is preserved and reflected with independent scalar and carrier universes. Finite projectivity is preserved with an unrestricted source carrier and target carrier at its scalar/carrier maximum, and is reflected when both carriers are at their corresponding maxima. No linearity, commutativity or freeness premise is imposed on this equivalence interface. Ordinary-coefficient evaluation gives an R-linear equivalence M ≃ₗ[R] ((M →ₗ[R] R) →ₗ[Rᵐᵒᵖ] R) for any semiring R and finitely generated projective left R-module M with additive commutative monoid structure. The first Hom uses the canonical right-regular Rᵐᵒᵖ-action on coefficient R and the second its left-regular R-action. Scalar and source universes are independent; no right action on M, additive inverses or freeness is assumed. Evaluation, inverse and naturality laws accompany the equivalence. Over commutative semirings, two inverse inner-scalar restrictions compare it with Mathlib's Module.evalEquiv, preserving coefficient R and outer scalars R. For commutative semirings and finitely generated projective modules with additive commutative monoid structure, contraction gives a linear endomorphism trace without choosing a basis. Its rank-one evaluation, conjugation and dual-map invariance, cyclicity for maps between two finite projective modules and finite-free comparison with the finite-basis trace retain independent scalar and carrier universes. If the module is an additive commutative group, additivity and cyclicity give trace zero on additive commutators; no ring structure on the scalar semiring is required. For two finite projective additive-commutative-monoid modules, tensoring endomorphisms multiplies their traces, with independent scalar and factor universes. Both bilinear and pointwise forms are provided. Partial trace over a finite projective factor M contracts arbitrary linear maps M tensor N → M tensor P to maps N → P, linearly in the whole input. The untraced factors are arbitrary, with four independent universes. On a tensor product of maps a and b it is trace(a) times b, without normalization. On nonfree projectives the scalar trace need not be a natural multiple of the scalar unit. Product endomorphisms have the sum of their factor traces; diagonal inclusion-projection blocks have the factor traces and off-diagonal blocks have trace zero. An arbitrary block endomorphism of a product of finite projective factors has the sum of its diagonal traces. The off-diagonal formulas assume finite projectivity only of the product, without bases, additive inverses or coupled carrier universes. An arbitrary endomorphism of a finite dependent product of finite projective modules has the finite sum of the traces of its diagonal coordinate composites. The index need only be finite, with independent scalar, index and carrier universes. Over arbitrary rings, the library also describes stably-free kernels of surjections onto finitely generated stably-free targets, finite-coordinate kernel presentations and surjective right-linear matrix kernels. Rectangular right-coordinate maps need finite source coordinates but allow arbitrary target indices; transporting a supplied equivalence needs both indices finite. These constructions use left coefficients and right scalars, without commutativity, injectivity, IBN or equal index cardinalities. Finite projective categories over arbitrary rings are essentially small in the ring universe at independent carrier universes. Ring-universe representatives and linear equivalences give a common reference skeleton for comparing arbitrary input classes. Over a commutative semiring, an idempotent-generated ideal is free exactly for the zero and unit idempotents, without a nontriviality assumption. Right scalar-extension comparisons satisfy pointwise unit and triple-composition associativity laws over arbitrary rings and right modules, with five independent scalar and module universes. A unit semiconjugating two homomorphisms of arbitrary rings induces a fixed-right-target linear equivalence on their scalar extensions, with left multiplication by the unit and its inverse on tensor coefficients. Principal right ideals over arbitrary source and target rings have an image-one scalar-extension equivalence without idempotence, and an image-zero annihilation theorem with idempotence. An idempotent right ideal and its scalar extension are bundled as finite projectives over arbitrary rings, including noncentral matrix idempotents. The right-ideal bundle has an identity linear equivalence to its canonical principal ideal, identifying zero and scalar action. Canonical right regular modules on ordinary semiring carriers are finite and free, including zero semirings. A finite projective common stabilizer can be replaced by a common standard finite free one, without finiteness or projectivity assumptions on the ambient modules. Finite ranks are preserved by ring-universe representatives; finitely generated free categorical objects are classified by finite rank over rings satisfying the strong rank condition, not all finite projectives over arbitrary rings. Finite projective right-module classes form a ring-sized direct-sum monoid and additive Grothendieck group, with arbitrary-carrier generators, universal properties and common finite-projective or finite-free stabilization criteria over arbitrary rings. Over division rings, canonical natural-valued class and integer-valued group dimensions give additive equivalences with ℕ and ℤ, with finite-coordinate and all-integer regular-generator inverses. Scalar extension along arbitrary unital maps between division rings preserves both dimensions and induces bijective class and K₀ maps. For a division-ring source and any ring target, the whole induced maps are independent of the chosen scalar homomorphism. Subsingleton rings give trivial class monoids and groups, not division-ring dimension invariants. Every unital ring homomorphism induces additive scalar-extension maps on right-module classes and K₀, with arbitrary-carrier evaluation and entire-map identity and composition laws over noncommutative and zero rings. The free-word zero-generator augmentation returns the coefficient of the empty word, fixing constants and killing letter monomials. The full-letter linear combination has range equal to its canonical semilinear kernel, under the left regular word-semiring action. These results allow arbitrary, possibly noncommutative or trivial coefficient semirings and empty or infinite alphabets, with independent coefficient and alphabet universes. Over a commutative base ring R and an arbitrary target ring S, right scalar extension agrees with the module-first Mathlib tensor product, with the specified homomorphism-induced coefficient action and right multiplication on coefficients. For commutative S, a separate pointwise comparison lands in the right-module view of Mathlib's scalar-first extension. Pure-tensor, inverse and map-naturality laws retain independent scalar and carrier universes without finiteness or centrality hypotheses.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/formalization.yaml) of [FormalFrontier/projective-modules](https://github.com/FormalFrontier/projective-modules) at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), Apache-2.0.*

7 articles: 3 for highlights of its formalization.yaml whose declarations the scan finds and 4 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/projective-modules](https://github.com/FormalFrontier/projective-modules), read at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”.
- Review notes: “Independent AI-agent review is reported. This metadata is not acceptance, build or axiom-check evidence and establishes neither source correspondence nor rights clearance. No human review, book-author endorsement or complete-book formalization is claimed.”
- Automation: agent; framework “AI agents using Lean and Lake”; tool setup “Formal Frontier AI agents contributed Lean code and documentation using mathlib. Separately authored mathematics and expression adaptations are credited in docs/CREDITS.md.”; prompting notes “AI assistance focused on exact hypotheses, handedness, independent universes and reusable mathematical APIs.”
- Automation notes: “Code and documentation include AI-agent contributions. AI generation alone establishes no originality, proof correctness or rights clearance.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [The K-book: An Introduction to Algebraic K-theory](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf), Charles A. Weibel, Complete-book build dated 2013-08-29, Chapter I module and projective-module material, including Definition I.1.2 on finite stable coordinates, Example I.2.1.2 and the exterior-power Sum Formula on displayed pages 18-19 (physical PDF pages 26-27), and Chapter II group completion, projective-module K₀, stabilization and division-ring dimension (book; adapts).

## Builds on

- [Adic modules](../../commutative-algebra/adic-modules/README.md) (a Lake dependency, pinned at 4487e8c4)
- [Algebraic direct limits](../../commutative-algebra/algebraic-direct-limits/README.md) (a Lake dependency, pinned at e5d0dea1)
- [Coherent modules](../../commutative-algebra/coherent-modules/README.md) (a Lake dependency, pinned at 4d48748c)
- [General linear groups](../../group-theory/general-linear-groups/README.md) (a Lake dependency, pinned at c9705889)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at f9e80eca)
- [Homological algebra](../../homological-algebra-and-category-theory/homological-algebra/README.md) (a Lake dependency, pinned at 6c7f755c)
- [Stable range](../stable-range/README.md) (a Lake dependency, pinned at 70231e01)

## Used by

- [Algebraic groups](../../algebraic-geometry/algebraic-groups/README.md)
- [Simplicial objects](../../homological-algebra-and-category-theory/simplicial-objects/README.md)
- [Valuation integers](../../number-theory/valuation-integers/README.md)
- [Vector bundles](../../topology/vector-bundles/README.md)

## Highlights

- [Sylvester's determinant identity for finite projective modules](sylvesters-determinant-identity-for-finite-proje.md)
- [Tensor-product determinants and rank powers](tensor-product-determinants-and-rank-powers.md)
- [Projective modules lift across nilpotent ideals](projective-modules-lift-across-nilpotent-ideals.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results) of [FormalFrontier/projective-modules](https://github.com/FormalFrontier/projective-modules) at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), Apache-2.0.*

**Annihilator order duality.** For a reflexive projective module with projective dual over a commutative ring,
annihilator and coannihilator give an order anti-isomorphism between submodules
with projective original quotient and dual submodules with projective original
quotient. Finite projective modules satisfy these ambient hypotheses.
The correspondence uses canonical evaluation and has pointwise membership
and forward/inverse carrier formulas, with independent ring/module universes.

**Projective-class and K₀ comparisons for directed limits.** For a nonempty directed system of unital rings, the additive direct limits of
finite-projective right-module class monoids and K₀ groups are canonically
additively equivalent to the corresponding objects over the ring limit.
The forward comparisons composed with the canonical direct-limit stage maps
are the original scalar-extension maps; their inverses send each such image
to its canonical direct-limit image. Compatible additive maps extend uniquely
from the stages.
No commutativity or injective-transition assumption is needed, and index and
coefficient universes are independent. For projective classes, equality is
detected at a common upper stage and every limit class descends to a stage.

**Multiplicative opposite-ring duality.** For every commutative ring `R`, including zero rings, canonical duality gives
a semiring equivalence of finite-projective right-module classes over `R` and
`Rᵐᵒᵖ`, and a ring equivalence of their K₀ rings. These preserve tensor
products and have the canonical duality equivalences as their underlying
additive equivalences.

**Finite-projective descent along directed limits.** Over a nonempty directed limit of arbitrary unital rings, every finitely generated
projective right module is linearly equivalent to scalar extension of a finite
idempotent matrix range from some stage, along the canonical stage map. The stage
may depend on the module; transition maps need not be injective. Index, ring and
module universes are independent, and zero rings and size-zero matrices are allowed.
This is existence of a stage representative; it does not assert continuity of K₀.

**Eventual equivalence of idempotent ranges.** For two prescribed finite idempotent matrices at possibly different stages of a
nonempty directed semiring system, their mapped right-column ranges over the limit
are linearly equivalent exactly when their images are linearly equivalent at one
common upper stage. Over rings the same criterion holds for the canonical scalar
extensions of the original ranges. The finite dimensions may differ or be empty;
transition maps need not be injective. This compares existence of equivalences,
not the lifting of a specified equivalence, and does not assert continuity of K₀.

**Scalar extension of idempotent images.** Over arbitrary rings, extension of scalars carries the original range of an
idempotent endomorphism to the range of its extended endomorphism, through the
original range inclusion and corestriction. No flatness or finiteness is needed.
The [finite-matrix comparison](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/RightExtensionMatrixRange.lean)
has the entrywise target matrix and the column formula `f (x i) * s`, without a
caller equality-decision instance; empty indices and zero rings are included.

**Artinian and semisimple module-category invariance.** Ordinary equivalences preserve and reflect Artinianness and semisimplicity of
modules over arbitrary rings, with independent scalar and carrier universes.
The forward ring theorems use a target carrier universe containing its ring;
the ring equivalence theorems use this bound on both sides. Zero rings are
included, without finite-generation or commutativity assumptions.

**Jacobson-kernel reduction injectivity.** For a surjective ring homomorphism `f : R →+* S` between arbitrary rings with
`RingHom.ker f ≤ Ideal.jacobson (⊥ : Ideal R)`, scalar extension is injective on
isomorphism classes of finitely generated projective right modules and on `K₀`.
The rings may lie in independent universes; zero rings are included.

**Stable freeness and the regular class.** Over any unital ring `R`, the canonical homomorphism `ℤ → K₀(R)` sending
`n` to `n[R]` is surjective exactly when every finitely generated projective
right `R`-module is stably free. It is bijective exactly when this condition
holds and `R` has invariant basis number. This concerns the specified regular
class, not an arbitrary abstract isomorphism `K₀(R) ≅ ℤ`; zero rings are included.

- [Algebra-valued pairing matrices](algebra-valued-pairing-matrices.md)
- [Normalized pairing regulators](normalized-pairing-regulators.md)
- [Nilpotence from characteristic polynomials](nilpotence-from-characteristic-polynomials.md)

**Quadratic powers of projective modules.** Over a commutative ring, antisymmetrization embeds the second exterior power of any projective module in its tensor square. The tensor square is noncanonically the product of its second exterior and symmetric powers, with the canonical antisymmetrization and symmetric quotient as inclusion and projection. No finite-generation or characteristic restriction is required. See [`ExteriorPower/QuadraticProjective.lean`](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/QuadraticProjective.lean).

**Nilpotent characteristic polynomials.** For a nilpotent endomorphism of a finite projective module over a commutative
ring, its intrinsic characteristic polynomial differs from that of zero by a
nilpotent polynomial. Over a reduced ring the two are equal. No freeness,
constant rank or nontriviality hypothesis is required; zero modules and zero
rings are included.

**Scalar determinants and functorial rank-dependent powers.** Over a commutative ring, scaling any endomorphism of a finite projective module
multiplies its canonical determinant by `Module.rankPower R P r`. This
multiplicative scalar power is characterized on every rank fiber by the usual
power with that fiber's rank. No constant-rank or invertibility assumption is
needed. Canonical determinants and rank-dependent powers commute with arbitrary
scalar extension, without flatness. The power homomorphism is invariant under
linear equivalence and multiplies pointwise under binary module products.
For a zero module it is one, including at the scalar zero.

**Schur determinants.** For finite projective modules over a commutative ring, a block endomorphism
whose upper-left block is a linear equivalence `e` has determinant
`det(e) * det(d - c ∘ e⁻¹ ∘ b)`. Neither the complement nor the full block
needs to be invertible. Varying rank and nonfaithful modules are allowed;
finite bases identify the scalar determinant with the block matrix determinant.

**Determinants in short exact sequences.** For a short exact sequence `0 → P → M → Q → 0` of finite projective modules
over a commutative ring and compatible endomorphisms, the determinant on `M`
is the product of the determinants on `P` and `Q`. No equivariant splitting
or invertibility assumption is needed. An invariant finite projective submodule
with finite projective quotient gives the restriction/quotient formula.

**Tensor determinants.** For finite projective modules over a commutative ring, the determinant of a
tensor product of arbitrary endomorphisms is the product of the cross
rank-dependent powers of their determinants. Tensor products compose the
multiplicative scalar powers. Neither constant rank nor invertibility is needed.

**Exterior-power coproduct.** Over an arbitrary commutative ring and arbitrary modules, the homogeneous
coproduct maps have coefficient-one signed coshuffle formulas, commute with
linear maps, and satisfy graded symmetry and associativity. The degree-zero
and exterior-square formulas include the zero ring and characteristic two.

**Finite consistency of row-finite linear systems.** For a ring `R` and any
left `R`-module `M` satisfying `Module.Baer R M`, a system with finitely
supported coefficient rows has a full solution whenever every finite set of
rows has a solution (`Module.Baer.exists_solution_of_finite`). Over a semisimple
ring, this is equivalent to finite consistency for every left module
(`Finsupp.exists_solution_iff_finite`), hence applies to division rings and
real vector spaces. The scalar, target, row and coordinate types have
independent universes; no countability or dimension bound is required.
Solutions are arbitrary coordinate functions, not finitely supported
functions, and the assignments for finite subsystems need not be compatible.
See [`Module.FiniteConsistency`](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/FiniteConsistency.lean)
for the extension argument and its Mathlib formalization credits.

**Finite orthogonal idempotent endomorphisms.** Over a possibly noncommutative
semiring `R`, a finite orthogonal idempotent family `e` on an additive
commutative `R`-module `M`, whose sum is the identity, gives the canonical
equivalence `CompleteOrthogonalIdempotents.linearEquivPiRange`:
`M ≃ₗ[R] (Π i, LinearMap.range (e i))`. Its coordinates are `e i m` and its
inverse sums the ambient values. The API includes extensionality and
naturality for arbitrary linear intertwiners, with no projectivity, topology,
rank or nontriviality premise. An empty index type forces `M`, not `R`, to be
zero. See [`Module.OrthogonalIdempotentRanges`](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/OrthogonalIdempotentRanges.lean).

**Endomorphism range ideals.** For any semiring `R` and additive commutative `R`-module `M`,
`Module.End.rangeIdeal U` is the right ideal of endomorphisms with range
in `U`, expressed as an ideal of `(Module.End R M)ᵐᵒᵖ`.
`Module.End.idealRange I` is the supremum of their ranges, or equivalently
the `R`-span of all evaluations. These form a Galois connection:
`idealRange I ≤ U ↔ I ≤ rangeIdeal U`. The principal right ideal generated
by any endomorphism evaluates to its range. Scalar and module universes
are independent; neither additive inverses nor finiteness, projectivity,
commutativity or full invariance of `U` is assumed. This is not an
unrestricted lattice equivalence.

**Internal pairs and complementary endomorphism ideals.** Over a semiring, an internal ordered Bool pair of submodules has
complementary range ideals, which evaluate back to the original pair.
This direction only needs `AddCommMonoid M`.
If `M` is an additive commutative group, complementary ideals conversely
evaluate to an internal pair. Each internal pair has a unique complementary
ideal pair evaluating to it, and each complementary ideal pair has a unique
internal pair with those range ideals. Bool `true` is the first coordinate;
these are not inverse maps on the full lattices.

**Simultaneous idempotent conjugation.** Let `R` be any ring, `ι` a finite index type, and `a b : ι → R` two
orthogonal idempotent families with `b i - a i ∈ I` for a two-sided ideal
`I ≤ Ring.jacobson R`. The unit
`u = OrthogonalIdempotents.conjugatingUnit ha I hI hab` has value
`(∑ i, b i * a i) + (1 - ∑ i, b i) * (1 - ∑ i, a i)`, satisfies
`(u : R) - 1 ∈ I`, and simultaneously conjugates `a i` to `b i`:
`u * a i * u⁻¹ = b i`. Neither family must sum to one; noncommutative
and zero rings are allowed, and an empty family gives the identity unit.
The coefficient needs no orthogonality, and its unit construction needs
only orthogonality of `a`; both families' orthogonality enters conjugacy.
For any ring homomorphism `f`, equal-image orthogonal families admit this
conjugating unit with `f u = 1` if `ker f ≤ Ring.jacobson R`, or if every
element of the whole kernel is nilpotent. No surjectivity or uniform
nilpotence exponent is required; source, target and index universes are
independent.
The [construction naturality API](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/RingTheory/IdempotentConjugationNaturality.lean)
sends the coefficient of arbitrary `a b : ι → R` to that of `f ∘ a, f ∘ b`
under any unital `f : R →+* S`, without orthogonality or ideal hypotheses.
For orthogonal `a`, `Units.map f.toMonoidHom u` equals the target constructed
unit in `Sˣ` when the source uses a two-sided `I ≤ Ring.jacobson R` with
`b i - a i ∈ I` for every `i`, and the target uses its own two-sided
`J ≤ Ring.jacobson S` with `f (b i) - f (a i) ∈ J` for every `i`.
No ideal-image containment, radical-preservation, injectivity or surjectivity
assumption is imposed. Joint reindexing of both families by `e : κ ≃ ι`
between finite types leaves the coefficient and unit unchanged. Only `a`
must be orthogonal for the unit identities; `b` may be nonidempotent, so these
are construction-transport laws, not conjugacy in that generality. Neither
family must sum to one; noncommutative and zero rings, empty finite indices,
and independent source, target and index universes are included.

**Total symmetric-power series on `K0`.** For every commutative ring `R`,
`KTheory.K0.totalSymmetricSeries` sends addition in `K0 R` to multiplication
of units of `PowerSeries (K0 R)`. On a finite projective right module, its
coefficients are the classes of the symmetric powers. The linear coefficient
recovers every virtual class, and the negative regular-module class has series
`1 - X`. This is a fixed-ring additive construction, not an identification with
the exterior-power λ-series.

**Exterior–symmetric series identity.** Over every commutative ring `R` and for every virtual class `x : K0 R`,
the exterior- and symmetric-power series satisfy
`λₓ(-t) σₓ(t) = 1` and `λₓ(t) σₓ(-t) = 1`.
Their coefficients on finite projective right modules are the respective
power classes. The proof uses the homogeneous Koszul complex and its
integer-signed Euler identity, with no freeness, constant-rank or
characteristic assumptions.

**Idempotent-matrix classification.** Over any semiring `R`, a right semimodule `P` is finitely generated and projective
iff it is `Rᵐᵒᵖ`-linearly equivalent to the range of an idempotent finite
`R`-matrix acting on `R`-valued columns by `x ↦ e *ᵥ x`, with pointwise
right action `(MulOpposite.op a • x) i = x i * a`. No finiteness or projectivity
is assumed in advance; scalar and carrier universes are independent, and size
zero, zero semirings and the zero semimodule are included.

**Quadratic tensor exactness.** The exterior-square image is the kernel of the symmetric-square quotient over a
commutative ring; projective modules admit a quotient section.

**Kernel families.** Over an arbitrary semiring, two supplied split linear
retractions with a common section into a fixed module with a topological
additive-group structure have homeomorphic total kernel spaces whenever their
ambient projection difference is jointly continuous. The section-domain modules
may vary and need no topology. Both total spaces retain their subspace topologies
in the parameter–ambient product. Writing `Δ = Γr - Γq`, transport is
`(t,a) ↦ (t,a + Δ(t,a))`, with inverse `(t,a) ↦ (t,a - Δ(t,a))`.

**Kernels with a common section.** Over a semiring, continuous linear maps `r, s : A →L[K] H` sharing a right inverse
`Γ : H →L[K] A` have canonically continuously linearly equivalent kernels, via
`a ↦ a - Γ (s a)`. Here `H` is an additive commutative monoid with a module
structure and a given topology, and `A` is an additive commutative group with a
module structure and a given topological additive group topology. The comparison
uses the induced kernel topologies and satisfies identity, inverse and composition
laws; no topology on the scalar semiring or separation axiom is required.

Tensoring over a commutative semiring with a projective factor preserves joint pair
injectivity of arbitrary dependent families. The canonical comparison
`P ⊗[R] (∀ i, B i) → ∀ i, P ⊗[R] B i` is injective, but is not generally surjective;
see [tensor products and products](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/TensorProduct/Pi.lean).

**Finite generation and residue rank.** An arbitrary projective module over a commutative ring is finitely generated iff
its prime residue-field tensor ranks are finite cardinals and their
Cardinal-valued function is locally constant. No uniform rank, finite-generation,
finite-presentation, Noetherian or nontrivial-ring premise is needed; scalar and
carrier universes remain independent. The rank is a cardinal, not `finrank`.
[Rank one or any fixed natural rank at all maximal fibers](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/FiniteOfFiberRank.lean)
also suffices, including rank zero and the zero ring; in rank zero the module is
[subsingleton](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/ZeroOfFiberRank.lean).
For arbitrary modules over commutative rings, the
[residue-rank calculus](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/docs/HeadlineResults.md#finite-generation-from-locally-constant-finite-residue-rank)
covers base change, cyclic quotients, tensor products and arbitrary algebraic direct
sums, without finite generation, flatness or projectivity, with cardinal lifts for
independent universes.

**Schanuel kernel comparison.** Over any semiring, supplied lifts between two linear maps from additive
commutative groups to a common additive commutative monoid give
`(ker p × Q) ≃ₗ[R] (ker q × P)`, with formulas retaining both lifts.
The core needs neither surjectivity nor projectivity. For surjections from
projective source modules, the
[projective presentation theorem](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/ProjectiveKernelComparison.lean)
obtains such an equivalence from the projective lifting property.
The common target needs no additive inverses; all universes are independent.

**Noetherian and PID freeness.** over a left-Noetherian, possibly noncommutative ring, submodules of sequence-spanned
modules are sequence-spanned, with independent universes and no ambient Noetherian,
free, projective or finite premise. Commutative PID freeness covers arbitrary-rank projectives
and submodules of arbitrary-rank free modules, not general Noetherian submodules.

[Noetherian submodules](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/CountablyGenerated/Noetherian.lean) · [PID](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/PID.lean)

**Finite simultaneous decomposition.** for any semiring `R`, additive commutative group `M` with an `R`-module structure,
finite index type `I`, and supplied pairwise commuting idempotent endomorphisms
`p : I → Module.End R M`, `LinearMap.commutingIdempotentsPiEquiv` identifies the
original `M` with the product of all Boolean-selected intersections of the original
ranges and kernels. Its components are the commuting products of `p i` or `1 - p i`,
and its inverse sums the block inclusions. Zero blocks and the empty constraint
family are retained; scalar, module and index universes are independent. No freeness,
finite generation, finite dimension or commutativity of `R` is assumed.

**Unimodular contraction.** for every quadratic form over a commutative ring, contraction by a surjective covector
has range equal to its kernel. A vector pairing to one gives a
[linear splitting](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorAlgebra/ContractionSplitting.lean) into two
copies of that kernel, with explicit forward and inverse formulas. Left multiplication
squares to the quadratic value, not necessarily to zero; no invertibility of two,
finiteness or freeness is required.

**Symmetric powers.** For arbitrary semimodules over commutative semirings,
[concatenation](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/SymmetricPower/Tensor.lean) on arbitrary
labels is natural and surjective, not generally an equivalence.
The [binomial decomposition](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/SymmetricPower/Prod.lean)
identifies every finite degree of `M × N` with the finite direct sum of tensors
of complementary symmetric degrees, with coefficient one per labelled subset
and naturality in both modules. Degree zero preserves the scalar unit;
the degree-one target is ordered `N × M`.
[Plethysm](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/SymmetricPower/Plethysm.lean) flattens finite
outer and arbitrary inner labels; `Sym^p (Sym^q M) → Sym^(p*q) M` is natural
and surjective for all natural degrees, with coefficient one on labelled grids.
Projectivity of `M` gives a linear section, not a canonical or natural choice.
[Base change](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/SymmetricPower/BaseChange.lean) along any
commutative-semiring algebra `R → S` commutes with every finite degree, without
flatness or projectivity; both directions have natural labelled pure-tensor
formulas. See the [full statements and unit comparisons](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/docs/HeadlineResults.md#symmetric-powers).

**Exterior series under invertible twists.** For an invertible right module L over a commutative ring R,
λⁿ([L]x) = [L]ⁿ λⁿ(x) for every virtual class x ∈ K₀(R) and every degree n.
Equivalently, λ_([L]x)(t) = λ_x([L]t).

**Exterior twists by invertible lines.** over a commutative ring `R`, an invertible module `L` and an arbitrary module `P`
have the canonical equivalence
`TensorPower R n L ⊗[R] exteriorPower R n P ≃ₗ[R] exteriorPower R n (L ⊗[R] P)`
in every degree, including zero. It sends `tprod(l) ⊗ ιMulti(p)` to
`ιMulti(fun i => l i ⊗ p i)` and is natural for arbitrary linear maps of the
invertible lines and the other modules. Independent universes and zero rings
are included; `P` need not be flat, finite, free or projective.

**Determinant lines.** for finite projective
modules over arbitrary commutative rings, the dependent product of top exterior
powers over attained stalk-rank fibers is invertible. Rank zero, zero rings and
independent universes are included. `Module.DeterminantLine.congr` is the
canonical equivalence induced by a linear equivalence, acting on each attained
fiber in its top exterior degree. It respects identity, composition and inverses,
and respects intertwining of arbitrary endomorphisms. Rank-fiber recovery,
zero-module and invertible-module normalizations assert existence of linear
isomorphisms. For any commutative `R`-algebra `S` supported on a rank fiber,
the scalar-extended line is isomorphic to the homogeneous exterior power of
`S ⊗[R] P` in that fiber's rank.
The tensor product of the determinant lines of two finite projective modules
is isomorphic to the determinant line of their product.
The [scalar determinant](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Endomorphism.lean)
of any endomorphism is the unique scalar inducing its action on the line.
It is multiplicative under composition and invariant under intertwining linear
equivalences, hence under conjugation.

**Scalar determinants.** Over any commutative ring `R`, for a finite projective
`R`-module `P` of possibly variable stalk rank,
`Module.determinant R P : Module.End R P →* R` is multiplicative under
endomorphism composition. `Module.determinant_eq_iff_map_eq_smul` characterizes
it as the unique scalar giving the induced action on the determinant line.
For finite free `P`, `Module.determinant_eq_det` identifies it with
`LinearMap.det`; on the zero module its value is `1`.
For any finite free ambient module and specified split presentation,
`Module.determinant_eq_det_stabilization` computes this scalar as the ordinary
determinant of the endomorphism extended by the identity on the complement.
The retract need not be free or have constant stalk rank, and
`LinearMap.det_stabilization_eq_of_retractions` compares different presentations.
For arbitrary finite projective factors, `Module.determinant_prodMap` gives
`det(f × g) = det(f) * det(g)`, even when their stalk ranks vary.
[Linear duality](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Endomorphism/Dual.lean)
preserves this determinant. Upper and lower block-triangular endomorphisms have
the product of their diagonal determinants, with no condition on the off-diagonal
block. The [unit criterion](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Endomorphism/Units.lean)
says that an endomorphism is a unit exactly when its scalar determinant is a unit.
None of these formulas requires freeness or constant stalk rank.
For finite projective `R`-modules `P` and `Q` in independent universes and
arbitrary `R`-linear maps `f : P →ₗ[R] Q` and `g : Q →ₗ[R] P`, the
[intrinsic Sylvester identity](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Endomorphism/Sylvester.lean),
`Module.determinant_one_add_comp_comm`, states
`det_P(1 + g ∘ f) = det_Q(1 + f ∘ g)`. Neither module need be free or have
constant rank; their ranks may differ, and neither endomorphism is assumed
invertible.
See [determinant-line endomorphisms](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Endomorphism.lean),
[finite-free stabilization](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Stabilization.lean),
and [product endomorphisms](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine/Endomorphism/Product.lean).

[Determinant lines](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/ExteriorPower/DeterminantLine.lean)

**Characteristic polynomials.** for an endomorphism `f` of a finite projective module over any commutative ring,
`Module.charpoly R P f` is the determinant over `R[X]` of the universal scalar
pencil `X • id - f.baseChange R[X]`. Evaluation in every commutative algebra and
arbitrary scalar extension are characterized by `Module.eval₂_charpoly` and
`Module.charpoly_baseChange`; the finite-free construction agrees with Mathlib's.
`Module.aeval_self_charpoly` gives Cayley–Hamilton in the endomorphism ring,
without a faithfulness assumption. Varying ranks and zero rings are included:
the polynomial need not be monic, and on the zero module it is `1`.
For maps `f : P →ₗ[R] Q` and `g : Q →ₗ[R] P` between finite projective modules,
the [composition formulas](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/LinearAlgebra/Charpoly/Composition.lean)
give `χ(g ∘ f) χ(0_Q) = χ(0_P) χ(f ∘ g)`, retaining the zero-map polynomials
rather than a global rank. The rank-one case is
`χ(φ.smulRight v) X = χ(0_P) (X - C (φ v))`.
The [unit and spectrum criteria](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/LinearAlgebra/Charpoly/Spectrum.lean)
give `IsUnit ((Module.charpoly R P f).eval r) ↔ IsUnit (r • 1 - f)`.
Thus the algebraic spectrum is the set of scalars with nonunit polynomial value,
and `f` is invertible exactly when the constant coefficient is a unit.
[Zero compositions](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/LinearAlgebra/Charpoly/ZeroComp.lean) satisfy
`charpoly(f) * charpoly(g) = charpoly(f + g) * charpoly(0)` whenever `f.comp g = 0`;
no reverse-zero or commutation hypothesis is needed. As a special case,
[complementary idempotents](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/LinearAlgebra/Charpoly/Idempotent.lean)
satisfy `charpoly(f) * charpoly(1 - f) = charpoly(0) * charpoly(1)`, with all four
polynomials taken on the original module, without a global rank or freeness assumption.

**Partial trace.** over a commutative
semiring `R`, contraction in a finite-projective tensor factor `M` defines an
`R`-linear operator from maps `M ⊗[R] N →ₗ[R] M ⊗[R] P` to maps `N →ₗ[R] P`.
The untraced semimodules `N` and `P` are arbitrary, with independent universes.
On `TensorProduct.map a b`, its value is `tr_M(a) • b`.
Precomposition by `b.lTensor M` and postcomposition by `c.lTensor M` commute
with contraction, separately and together, for every input map and arbitrary
`b : N' →ₗ[R] N`, `c : P →ₗ[R] P'`. These are stock `TensorProduct.map` maps
with identity on `M`; all untraced factors are arbitrary, with independent scalar/carrier universes.
For two finite-projective traced factors `M` and `N`, contraction over `M ⊗[R] N`
agrees with successive contractions, first over `M` and then over `N`, after
inverse-associator input and forward-associator output transport. The remaining
input and output semimodules are arbitrary, with independent universes.

**Tensor-family zero detection.** over a
commutative semiring, tensoring a jointly zero-detecting family with a projective
module on either side preserves zero detection. The family's source and dependent
targets are arbitrary additive commutative monoids. For two jointly zero-detecting
families `f i : A →ₗ[R] B i` and `g j : C →ₗ[R] D j`, the maps `f i ⊗ g j`
jointly detect zero when `C` and every `B i` are projective; no projectivity of
`A` or `D j` is required. Universes are independent, index types may be empty,
and no finite-generation assumption is needed. This is zero detection, not
separation of arbitrary pairs.

**Tensor-image membership.** over a
commutative ring, if `W ≤ V` has projective quotient, any jointly zero-detecting
family `f i : A →ₗ[R] B i` detects membership in the image of
`W ⊗[R] A → V ⊗[R] A`. This image equals the infimum of the comaps of the
corresponding images in `V ⊗[R] B i`. The source and dependent targets are
arbitrary modules, and the index type may be infinite or empty.

**Local freeness.** every projective right module
is free over a ring with a proper two-sided ideal and unit complement, with no
generation bound. The `IsLocalRing` form permits noncommutative rings and independent
universes; split-range assembly itself requires explicitly free increments.

[arbitrary local freeness](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/ArbitraryLocalProjectiveFree.lean) · [local scalar interface](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Module/LocalRing.lean)

**Submodule lattices and length.** ordinary equivalences `e : ModuleCat.{vR} R ≌ ModuleCat.{vS} S` over arbitrary
rings give the canonical order isomorphism
`ModuleCat.submoduleOrderIsoOfEquivalence e X` on all submodules. For every
module `X`, `ModuleCat.length_eq_of_equivalence e X` gives
`Module.length S (e.functor.obj X) = Module.length R X` in `ℕ∞`, including `⊤`;
`ModuleCat.isFiniteLength_iff_of_equivalence e X` preserves and reflects the
proposition `IsFiniteLength`. Scalar and carrier universes are independent,
with no maximum-universe or finite-generation hypothesis. This compares a
module with its image, not the two regular modules: the matrix equivalence
sends `ℚ` to the simple column module `Fin 2 → ℚ` of length 1 over
`Matrix (Fin 2) (Fin 2) ℚ`, whose left regular module instead has length 2.

**Product comparisons and uniform rank bounds.** the [canonical additive comparison](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/KTheory/Product.lean) maps
K₀ of any product of rings to the product of their K₀ groups. For a family of
possibly noncommutative division rings, it is injective and its image consists
exactly of families whose integer ranks have one uniform absolute bound.
More generally, every K₀ element of an arbitrary ring `R` has uniformly bounded
absolute integer ranks under any indexed family of unital maps `R →+* D i` to
division rings. For an infinite product of division rings, the comparison is
not surjective.

**Lifting across nil kernels.** A surjective homomorphism from a commutative ring to a ring induces a surjection
on finitely generated projective right-module isomorphism classes whenever every
element of its kernel is nilpotent. The nilpotence exponent may depend on the
kernel element; no uniform exponent for the whole kernel is required.

**Nil-kernel injectivity and nilpotent-kernel invariance.** for a surjective unital homomorphism of arbitrary, possibly noncommutative rings,
scalar extension is injective on finite-projective right-module isomorphism
classes whenever every kernel element is nilpotent; no common exponent is
required. If some power of the two-sided kernel ideal is zero, the
scalar-extension maps on finite-projective right-module isomorphism-class monoids
and on K₀ are additive equivalences.

**Locally constant module rank.** `Module.rankLocallyConstant R M` assigns a locally constant natural-valued
function on `Spec R` to each finite projective left module over a commutative
ring. It is invariant under linear isomorphism, sends subsingleton modules to
zero and the regular module to one, adds under finite dependent products and
binary products, and multiplies under tensor products. Arbitrary commutative
algebra base change pulls this function back along the induced map on prime
spectra. Scalar, module and index universes are independent; empty products
and zero rings are included. These are module-level laws, not a class or K₀ map.

- [Frobenius functionals and self-injectivity](frobenius-functionals-and-self-injectivity.md)

### Detailed results

[Detailed headline results](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/docs/HeadlineResults.md)

**Quotients, kernels and presentations.**

**Freeness, cancellation and free words.**

**Idempotents and projections.**

**Exterior algebra and contraction.**

**Symmetric powers.**

**Determinants.**

**Duality, Hom and tensor tests.**

**Traces.**

**Topology.**

**Coefficient products and right extension.**

**Categories, size and length.**

**Right classes and K0 structures.**

**K0 calculations and simple types.**

**Stalk rank and component models.**

**Tensor families and finite residue rank.**

## Main results

Its formalization.yaml lists 210 main results, and the scan finds 210 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
