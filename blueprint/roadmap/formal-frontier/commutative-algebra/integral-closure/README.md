# Integral closure

> Integral-closure descent along linear retractions and normal-domain descent from arbitrary field scalar extensions of commutative algebras, with power criteria for integrality, finiteness and prime-spectrum embeddings, and locality of integral domains integral over henselian local rings.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/formalization.yaml) of [FormalFrontier/integral-closure](https://github.com/FormalFrontier/integral-closure) at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390), Apache-2.0.*

7 articles: 4 for highlights of its formalization.yaml whose declarations the scan finds and 3 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/integral-closure](https://github.com/FormalFrontier/integral-closure), read at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “other: independently reviewed”.
- Review notes: “Independent review covers the mathematical code, ordinary-import examples and documentation.”
- Automation: agent; tool setup “Formal Frontier AI agents used Lean and mathlib with reviewed project contributions, ordinary imports and pinned toolchain/dependency revisions.”
- Automation notes: “Atlas contributed the initial descent proofs; other Formal Frontier contributors developed the later mathematics, module interfaces and examples. Folio contributed the initial README headlines. No model, cost or performance measurements are reported here.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Integral-closure descent along linear retractions and arbitrary field scalar extensions* (original-proof; formalizes).
- *The Rising Sea: Foundations of Algebraic Geometry*, Ravi Vakil, October 21, 2025 draft, Exercise 5.4.M, physical/PDF page 169 (book; background).
- *Local Fields and Their Extensions*, I. B. Fesenko, S. V. Vostokov, Second edition, 2002 (book; background).

## Builds on

- [Adic modules](../adic-modules/README.md) (a Lake dependency, pinned at 2fb498d1)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 4791da69)

## Used by

- [Toric ideals](../toric-ideals/README.md)

## Highlights

- [Integral domains over henselian local rings are local](integral-domains-over-henselian-local-rings-are.md)
- [Integral closedness descends along linear retractions](integral-closedness-descends-along-linear-retrac.md)
- [Normal-domain descent from arbitrary field scalar extensions](normal-domain-descent-from-arbitrary-field-scala.md)
- [Prime-spectrum embeddings from powers in the image](prime-spectrum-embeddings-from-powers-in-the-ima.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/README.md#headline-results) of [FormalFrontier/integral-closure](https://github.com/FormalFrontier/integral-closure) at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390), Apache-2.0.*

**Local normal integral extensions of valuation domains are valuation domains.**
For commutative domains `R` and `S` in independent universes, an integral
homomorphism `f : R →+* S` from a valuation domain to a local integrally
closed domain gives `ValuationRing S` through
`RingHom.IsIntegral.isValuationRing_of_isLocalRing`.
The map may be noninjective. Neither module finiteness, Henselianity,
Noetherianity nor separability is assumed. Import
[`IntegralClosure.ValuationRing`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/ValuationRing.lean) or the
root `IntegralClosure`.
Its supporting theorem
`LocalSubring.mem_or_inv_mem_of_isUnit_coeff` applies to a local subring
integrally closed in any ambient field: a root of a polynomial with a unit coefficient
lies in that subring or has its inverse there. It uses the original subring
inclusion and requires the coefficient to be a unit in the subring itself.

**Integral domains over henselian local rings are local.** Let `R` and `S`
be commutative rings in independent universes, with a given `R`-algebra
structure on `S`. If `R` is henselian local, `S` is a nonzero domain and
`S` is integral over `R`, then
`HenselianLocalRing.isLocalRing_of_isIntegral R S` gives `IsLocalRing S`.
The base `R` need not be a domain or reduced; injectivity of the algebra
map, module finiteness, Noetherianity and completeness are not assumed.
Import [`IntegralClosure.Henselian`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Henselian.lean).
The unital-homomorphism form
`RingHom.isLocalRing_of_henselian_of_isIntegral alpha h` instead takes
`alpha : R →+* S` with `h : alpha.IsIntegral`, without a chosen algebra
structure.

For a homomorphism `f : A →+* B` of commutative rings, if each target element
has a positive power in the image, contraction is an order isomorphism from
radical ideals of `B` to radical ideals of `A` containing `RingHom.ker f`.
Its inverse is extension followed by radical. For any integral homomorphism
of commutative rings and any source ideal `I`,
`Ideal.comap f (Ideal.map f I).radical = (I ⊔ RingHom.ker f).radical`.
See the [ideal extension and contraction API](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Ideal.lean).

For a homomorphism `f : A →+* B` from a possibly noncommutative semiring `A` to a commutative semiring `B`, the [ideal API](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Ideal.lean) shows that positive powers of each target generator in the image of `f` suffice to identify the radicals of the generated ideal and the extension of its contraction. The exponent may vary with the generator. Under the global power-image hypothesis, contraction is injective on radical ideals of `B`; the existing prime-spectrum injectivity criterion follows because prime ideals are radical.

**Integrality reflects along nil kernels.** Let `K` be a commutative ring,
let `A` and `B` be possibly noncommutative rings with their given `K`-algebra
structures, and let `f : A →ₐ[K] B`. If every element killed by `f` is
nilpotent, then integrality over `K` of `f a` implies integrality of `a`.
The rings may lie in three independent universes; neither injectivity nor
surjectivity of `f`, nor a uniform nilpotence exponent for its kernel,
is required. The elementwise theorem
`IsIntegral.of_isNilpotent_of_map_eq_zero` and its whole-algebra counterpart
`Algebra.IsIntegral.of_isNilpotent_of_map_eq_zero` are in
[`IntegralClosure.RingHom`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean). The latter reflects
integrality of `B/K` to `A/K`; it does not require module finiteness.

- [Finiteness from powers of algebra generators](finiteness-from-powers-of-algebra-generators.md)
- [Prime-spectrum embeddings from powers in the image](prime-spectrum-embeddings-from-powers-in-the-ima.md)
- [Integral closedness descends along a linear retraction](integral-closedness-descends-along-linear-retrac.md)

**Normal-domain descent from any field scalar extension.** For any field
extension `l/k` and commutative `k`-algebra `A`, if `A ⊗[k] l` is a domain,
then so is `A`; if the tensor product is also integrally closed, then so is
`A`. The separate theorems
[`isDomain_left`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/TensorProduct.lean#L61) and
[`isIntegrallyClosed_left`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/TensorProduct.lean#L71) in
`Algebra.TensorProduct` require no finite-dimensionality, algebraicity or
separability assumption on the field extension.

**Tensor-factor evaluation gives linear retractions.** For the same fields
and algebra, any `k`-linear functional `f : l →ₗ[k] k` defines an `A`-linear
[`rightLinearMap`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/TensorProduct.lean#L45) from `A ⊗[k] l`
to `A`, taking `a ⊗ₜ[k] b` to `a * algebraMap k A (f b)`. When `f 1 = 1`,
[`rightLinearMap_includeLeft`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/TensorProduct.lean#L54)
proves it is a left inverse to `includeLeft`. Normalization is needed for
this retraction equation, not for constructing the evaluation map; the
functional and evaluation map need not be multiplicative.

**Monic relations at inverses of units.** For a division semiring `R`, a
semiring `S`, an arbitrary unital homomorphism `f : R →+* S` and a unit
`a : Sˣ`, any nonzero polynomial relation over `R` at `a` yields a monic
polynomial relation at `a⁻¹`. The results in
[`IntegralClosure.Polynomial`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Polynomial.lean) require no
coefficient centrality or commutativity of `S`. The more general semiring-source
theorem assumes that the reversed polynomial's leading coefficient is a unit
in `R`, without requiring the original polynomial to be nonzero.

**A unit-constant criterion for two monic relations.** For arbitrary semirings
`R` and `S`, a unital homomorphism `f : R →+* S` and `a : Sˣ`, monic
polynomial relations at both `a` and `a⁻¹` exist exactly when a monic relation
at `a` has constant coefficient a unit in `R`. When both relations exist,
that constant coefficient can be chosen to be `1`. These results in
[`IntegralClosure.Polynomial`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Polynomial.lean) use left
coefficients and require no coefficient centrality. The unit condition is
in the source semiring, not merely after applying `f`.

**Units descend from a monic inverse relation.** For arbitrary semirings `R`
and `S`, an injective homomorphism `f : R →+* S`, `r : R` and a unit
`a : Sˣ` with `↑a = f r`, a monic polynomial relation over `R` at `a⁻¹`
implies `IsUnit r`. The theorem
`RingHom.isUnit_of_monic_eval₂_units_inv_eq_zero` in
[`IntegralClosure.RingHom`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean) needs neither
commutativity nor a second relation at `a`. Although stated with semiring
instances, its hypotheses force both semirings to admit ring structures.

The five descent and tensor-evaluation declarations build on mathlib's
integral-closure, fraction-ring, tensor-product and projective-module duality
infrastructure. They establish
descent, not ascent, a converse or normalization. The descent theorems return
typeclass proofs for local use rather than installing global instances; the
tensor evaluation construction is noncomputable.

The reciprocal-evaluation lemmas generalize mathlib's commutative-target
identities using its polynomial-reversal and finite-sum APIs. Unit descent
refines its `RingHom.IsIntegral.isLocalHom` argument
and uses [Group Theory](https://github.com/FormalFrontier/group-theory)'s
zero-sum unit-transfer API. Subalgebra finiteness uses mathlib's adjoin-span
and adjoin-union formulas and finite generation of submodule products.

The valuation-domain criterion is standard commutative algebra. Its proof uses
Mathlib's valuation-overring intersection, explicit coefficients of division by
a linear monic polynomial, and total divisibility in a valuation domain. The
possibly noninjective map is handled through its image, a quotient of the
source; all fraction-field constructions are internal. Locality and normality
of the target remain hypotheses. This criterion alone does not identify a
canonical integral closure with an ambient integer ring or show that its
fraction field is an arbitrary specified extension field.

The motivating valuation-domain setting is Fesenko–Vostokov,
*Local Fields and Their Extensions*, second edition (2002). The generic criterion
and its linear-quotient proof are not claimed to reproduce a particular passage
or proof of that book.

The henselian locality result generalizes the valuation-ring setting of
I. B. Fesenko and S. V. Vostokov, *Local Fields and Their Extensions*, second
edition (2002), to henselian local base rings that need not be domains. Its
one-element annihilator argument uses lifted coprime factors and a
domain contradiction. It reuses `HenselianRing.exists_monic_factorization`
from Formal Frontier's [Adic Modules](https://github.com/FormalFrontier/adic-modules)
library.

Import [`IntegralClosure`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure.lean) for the descent, power and
unit-relation families; import `IntegralClosure.Henselian` for henselian locality.
The two descent leaves are `IntegralClosure.LinearRetract` and
`IntegralClosure.TensorProduct`. The [API and examples below](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/README.md#public-api-and-examples)
give the complete descent signatures, usage and proof explanations; the
[manual guide](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/docs/README.md) also covers power criteria and unit relations.

### Relative integrality and positive-power criteria

Let `R` be a commutative ring, `S` a possibly noncommutative ring, and
`f : R →+* S` a ring homomorphism; the rings may lie in independent universes.
An element `x : S` is integral relative to `f` (`f.IsIntegralElem x`) if some
monic polynomial `p : R[X]` satisfies `p.eval₂ f x = 0`.

- [Integrality is unchanged by positive powers](integrality-is-unchanged-by-positive-powers.md)
- [Positive powers in the range imply an integral homomorphism](positive-powers-in-the-range-imply-an-integral-h.md)

These criteria require no `Algebra` structure, centrality of coefficient images,
domain, nontriviality or finiteness hypothesis. Import `IntegralClosure.RingHom`
or the root `IntegralClosure`; the
[manual reference](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/docs/README.md#relative-integrality-and-power-criteria)
explains the arguments and the supporting polynomial evaluation lemmas.

### Jacobson radicals under integral homomorphisms

For arbitrary commutative rings `R` and `S` in independent universes and an
integral ring homomorphism `f : R →+* S`,
[`IntegralClosure.Jacobson`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Jacobson.lean) provides:

`Ideal.comap_jacobson_of_isIntegral`: for every target ideal `J : Ideal S`,
`J.jacobson.comap f = (J.comap f).jacobson`.

`Ideal.map_jacobson_le_of_isIntegral`: for every source ideal `I : Ideal R`,
`I.jacobson.map f ≤ (I.map f).jacobson`.

`Ideal.map_le_jacobson_bot_of_isIntegral`: for every source ideal `I`,
`I ≤ (⊥ : Ideal R).jacobson` implies
`I.map f ≤ (⊥ : Ideal S).jacobson`.

No injectivity, surjectivity or nontriviality assumption is required.
Mathlib's surjective Jacobson formula also applies to possibly noncommutative
rings; the integral formula here assumes commutativity.

## Main results

Its formalization.yaml lists 10 main results, and the scan finds 10 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
