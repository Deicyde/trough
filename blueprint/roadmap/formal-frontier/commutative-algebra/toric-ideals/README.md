# Toric ideals

> Reusable Lean theory of coefficient-independent finite binomial kernels for monomial evaluation on finite variable types over arbitrary commutative rings, with any commutative target monoid and independent coefficient, variable and target universes, re-exported GroupRings coefficientwise fiber-normalization criteria for additive monoid algebras over arbitrary rings, gcd-reduced bivariate natural-weight kernel presentations for pairs not both zero and coprime all-coefficient binomial membership over arbitrary possibly noncommutative rings, and the Hankel-minor presentation of the degree-n rational normal curve's monomial-map kernel for positive n over arbitrary commutative rings, with low-degree boundaries, a quotient-to-image equivalence, domain-dependent consequences, all-degree freeness, flatness and faithful flatness of the full Hankel quotient for its canonical coefficient action over arbitrary commutative rings in all coefficient universes, including zero rings and degree zero, all-degree standard-graded homogeneity of the original Hankel ideal, explicit bases indexed by Fin (n*d+1) and finite coordinates for every degree-d component of the full Hankel quotient over arbitrary commutative rings, with basis vectors preserved by arbitrary coefficient homomorphisms in independent universes, all-degree coefficient criteria for domain, reduced, Noetherian and Jacobson Hankel quotient rings, the all-degree criterion that the Hankel quotient is Artinian over itself exactly for zero coefficient rings, finiteness of its canonical coefficient module exactly for zero coefficient rings in every degree, and an arithmetic characterization of the natural exponent image, full-target raw-map surjectivity exactly in degree one or over subsingleton coefficients for arbitrary commutative semirings in every degree, finite type of the raw parametrization over its full source in every degree, module finiteness of its full target over that source exactly when n is nonzero or the coefficient semiring is subsingleton, freeness of the full target over the full raw-map source exactly in degree one or over subsingleton coefficients for arbitrary commutative semirings in every degree, and full-source ring-map flatness exactly in degree one or over subsingleton coefficients for arbitrary commutative rings in every degree, and regularity of every coordinate class in every degree, with an injective coordinate-localization client over arbitrary commutative rings. The split-quadric coordinate algebra has an all-coefficient determinant kernel, an injective quotient parametrization, a range equivalence, coefficient domain and primality criteria, and localization chart comparisons over arbitrary commutative rings.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/formalization.yaml) of [FormalFrontier/toric-ideals](https://github.com/FormalFrontier/toric-ideals) at commit [593116e0](https://github.com/FormalFrontier/toric-ideals/tree/593116e0783dee84353f7a76ef65001cb814b01e), Apache-2.0.*

3 articles: 3 for highlights of its formalization.yaml whose declarations the scan finds. The headline results in its README are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/toric-ideals](https://github.com/FormalFrontier/toric-ideals), read at commit [593116e0](https://github.com/FormalFrontier/toric-ideals/tree/593116e0783dee84353f7a76ef65001cb814b01e) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed mathematical development”.
- Review notes: “Independent agent review covers the Hankel presentation, exponent-image criterion and quotient criteria, including their module and test interfaces.”
- Automation: agent; tool setup “AI-assisted Lean development in a pinned Lean 4 and mathlib Lake project.”
- Automation notes: “AI agents developed the mathematical code and documentation. Independent agent review covers the Hankel presentation, exponent-image criterion and quotient criteria. No human-review claim is made here.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *The Rising Sea: Foundations of Algebraic Geometry*, Ravi Vakil, Exercise 3.6.F (book; adapts).
- [Group Rings: fiber normalization and uniform binomial kernels](https://github.com/FormalFrontier/group-rings), Formal Frontier Agents (software; adapts).
- *Terminal exponents, exponent images and Hankel quotient criteria* (original-proof; independently-proves).
- *The Rising Sea: Foundations of Algebraic Geometry*, Ravi Vakil, Section 4.4 (book; adapts).

## Builds on

- [Coherent modules](../coherent-modules/README.md) (a Lake dependency, pinned at b9bb2333)
- [Group rings](../../ring-theory/group-rings/README.md) (a Lake dependency, pinned at 8a10fb8c)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 07948c98)
- [Integral closure](../integral-closure/README.md) (a Lake dependency, pinned at 3e89fa94)
- [Minimal primes](../minimal-primes/README.md) (a Lake dependency, pinned at 537058e2)
- [Multivariate polynomials](../multivariate-polynomials/README.md) (a Lake dependency, pinned at 616945c1)

## Highlights

- [Uniform monomial-evaluation kernels](uniform-monomial-evaluation-kernels.md)
- [Monomial conductors](monomial-conductors.md)
- [Own-fraction normalization of monomial algebras](own-fraction-normalization-of-monomial-algebras.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/README.md#headline-results) of [FormalFrontier/toric-ideals](https://github.com/FormalFrontier/toric-ideals) at commit [593116e0](https://github.com/FormalFrontier/toric-ideals/tree/593116e0783dee84353f7a76ef65001cb814b01e), Apache-2.0.*

- [Uniform monomial-evaluation kernels](uniform-monomial-evaluation-kernels.md)

**Monomial conductors and canonical principal localization.** For a finitely
generated `S : AddSubmonoid (σ →₀ ℕ)`, there is `c ∈ S` such that `c + n ∈ S`
whenever `(∃ b ∈ S, b + n ∈ S) ∧ ∃ k > 0, k • n ∈ S`. Its coefficient-one
monomial clears every element of the relative-root monomial algebra, not only
its generators. Inverting this same monomial gives a canonical algebra
equivalence over the original monomial algebra. Clearing and this comparison
work over every commutative semiring, including zero coefficients; for a fixed
conductor they need no finite generation. For an integrally closed coefficient
domain, the own-fraction normalization has a no-finite-generation algebra
comparison with the relative-root extension, and localizing it at the same
image monomial gives the normalization-side comparison. Both relative exponent
witnesses, canonical scalar actions and independent coefficient/variable
universes are retained. Finite generation is sufficient, not claimed necessary.
See [`MonomialConductor`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MvPolynomial/MonomialConductor.lean) and
[`MonomialFinite`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MvPolynomial/MonomialFinite.lean).

**Integral closedness of polynomial power subalgebras.** For any commutative
ring `R`, the subalgebra generated by `X ^ n` for `n ∈ AddSubmonoid.multiples d`
is integrally closed iff `R[X]` is when `0 < d`, and iff `R` is when `d = 0`.
In particular every degree works over an integrally closed domain, by the existing
`Polynomial.isIntegrallyClosed_adjoin_X_pow_multiples` in
[MonomialIntegralClosure.lean](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialIntegralClosure.lean).
The degree-zero coefficient equivalence already works over commutative semirings,
without nontriviality. See
[MonomialIntegrallyClosed.lean](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialIntegrallyClosed.lean)
and [MonomialSubalgebra.lean](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialSubalgebra.lean).

**Finite natural-exponent monomial extensions.** For an additive submonoid
`S` of `ℕ` and any subset `U`, a finite `E ⊆ U` with `U ⊆ S + E` exists
exactly when `S ≠ ⊥` or `U` is finite. For a submonoid target `T`, the
criterion is `S ≠ ⊥ ∨ T = ⊥`, without requiring `S ≤ T`; these are covers,
not equalities. If `S ≤ T` and `R : Type u` is any commutative semiring,
the canonical left inclusion module between the coefficient-one monomial
adjoins for `S` and `T` in `AddMonoidAlgebra R ℕ` is finite exactly when
`Subsingleton R ∨ S ≠ ⊥ ∨ T = ⊥`. Thus zero coefficients are included,
without a ring, domain, Noetherian, finite-generation or extra positive-generator
hypothesis. See
[`NatFiniteRemainder`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/AddSubmonoid/NatFiniteRemainder.lean) and
[`NatMonomialFinite`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/AddMonoidAlgebra/NatMonomialFinite.lean).

**Finite relative-root extensions and normalization.** For a finitely generated
`S : AddSubmonoid (σ →₀ ℕ)`, there is a finite set of relative-root exponents
`E` such that every exponent satisfying
`(∃ b ∈ S, b + n ∈ S) ∧ ∃ k > 0, k • n ∈ S` is `s + e` with `s ∈ S`
and `e ∈ E`. The corresponding coefficient-one monomial adjoin is a finite
module over the original `S`-monomial adjoin, over every commutative semiring,
for the canonical inclusion action. For an integrally closed commutative
domain of coefficients, `integralClosure A (FractionRing A)` is finite over
its own `A`. Variables and coefficients have independent universes; variables
may be infinite, and there is no coefficient-Noetherian assumption. Both
relative exponent witnesses are retained; this is not ambient saturation.
See [`FiniteRemainder`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/AddSubmonoid/FiniteRemainder.lean) and
[`MvPolynomial/MonomialFinite.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MvPolynomial/MonomialFinite.lean).

**Normalization image of multivariate monomial subalgebras.** Let `R : Type u`
be an integrally closed commutative domain, `σ : Type v` arbitrary, and
`S : AddSubmonoid (σ →₀ ℕ)`. Let `A` be the `R`-adjoin of the monomials
`monomial s 1` for `s ∈ S`. Under the canonical map from `Frac(A)` to
`Frac(MvPolynomial σ R)`, the image of `integralClosure A (Frac(A))` is the
image of the `R`-adjoin of the monomials `monomial n 1` satisfying
`(∃ b ∈ S, b + n ∈ S) ∧ ∃ k > 0, k • n ∈ S`. The equality is between
`R`-subalgebras, restricting scalars on the integral closure first. This is
normalization in `A`'s own fraction field, not ambient integral closure or
ambient saturation; even exponents remain even. There are no finiteness,
nonempty-variable, field, Noetherian or characteristic assumptions, and the
universes are independent. See
[`MvPolynomial/MonomialNormalization.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MvPolynomial/MonomialNormalization.lean).

**Finite gcd monomial extensions.** For an arbitrary additive submonoid `S` of
`ℕ` and a commutative semiring `R`, the subalgebra generated by powers of `X`
with exponents in `multiples (Nat.setGcd S)` is finite over the exponent
subalgebra for `S`, through their canonical inclusion. Over commutative rings
the same extension is integral. Gcd zero gives constants; no coefficient-domain,
Noetherian, finite-generation or positive-gcd hypothesis is required. See
[`MonomialFinite`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialFinite.lean).

**Fine components of integral polynomials.** Over any commutative ring `R`,
an arbitrary additive submonoid `S` of `σ →₀ ℕ` defines the subalgebra generated
by `monomial s 1` for `s ∈ S`. If `f` is integral over this subalgebra, then
each `monomial n (f.coeff n)` is integral over it. An integral monomial with
non-nilpotent coefficient has `k • n ∈ S` for some `k > 0`; over a reduced ring this
applies to every exponent in the support of `f`. Variables and coefficients
have independent universes, with no finiteness or characteristic restriction.
These are powers of individual monomials, not a claim that some power of `f`
lies in the subalgebra. See
[`MvPolynomial/MonomialIntegralClosure.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MvPolynomial/MonomialIntegralClosure.lean).

**Intrinsic normality of multivariate monomial subalgebras.** Let `R : Type u`
be any commutative domain, `σ : Type v` any independently universed variable type,
and `S` any additive submonoid of `σ →₀ ℕ`. The `R`-subalgebra generated by
`monomial s 1` for `s ∈ S` is integrally closed in its own fraction field **if
and only if** `R` is integrally closed and `b ∈ S`, `b + n ∈ S`, `0 < k` and
`k • n ∈ S` imply `n ∈ S`. Coefficient normality is an output of necessity,
not an initial hypothesis. There is no finite-variable, finite-generation,
field, Noetherian or characteristic hypothesis. The difference conditions
distinguish this relative root closure from ambient saturation; even-exponent
subalgebras need not contain the variables. See
[`MvPolynomial/MonomialIntegralClosure.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MvPolynomial/MonomialIntegralClosure.lean).
The accompanying [support API](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MvPolynomial/MonomialSubalgebra.lean)
identifies the underlying module with `MvPolynomial.restrictSupport` over every
commutative semiring, including the zero semiring.

**Arithmetic gcd recognition.** For every additive submonoid `S` of `ℕ`, there
is a unique `d : ℕ` such that every element of `S` is divisible by `d` and only
finitely many multiples of `d` are missing from `S`. This `d` is the canonical
`Nat.setGcd (S : Set ℕ)`. The zero submonoid has `d = 0`; no finite-generation,
positivity or coprimality hypothesis is needed. The gaps are relative to the
multiples of `d`, not the full complement of `S`. See
[`NumberTheory/FrobeniusNumber.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/NumberTheory/FrobeniusNumber.lean).

**Integral closedness forces normal coefficients.** Over a commutative domain
`R`, let `S` be any additive submonoid of `ℕ`. If the subalgebra generated by
`X ^ s` for `s ∈ S` is integrally closed in its own fraction field, then `R`
is integrally closed. No base-normality input or positive exponent is needed;
the bottom and top submonoids are included. The proof restricts evaluation at
zero to an `R`-linear scalar retraction. See
[`Polynomial/MonomialIntegralClosure.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialIntegralClosure.lean).

**Integral closedness of polynomial exponent subalgebras.** Over an integrally
closed commutative domain `R`, the subalgebra generated by `X ^ s` for an arbitrary
additive submonoid `S` of `ℕ` is integrally closed if and only if
`S = AddSubmonoid.multiples d` for some `d : ℕ`. Degree zero gives the constants;
positive degree gives an algebra isomorphic to `R[X]`. The necessity direction
holds over every coefficient domain, without base normality. No field,
finite-generation, Noetherian or characteristic hypothesis is needed. See
[`Polynomial/MonomialIntegralClosure.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialIntegralClosure.lean).

Normality is absolute, in the subalgebra's own fraction ring. For example,
`ℤ[X²]` is normal but proper in `ℤ[X]`: `X` is absent, although it is integral
over `ℤ[X²]` by the monic equation `Y² - X²`. Normality therefore does not mean
integral closedness inside the ambient polynomial ring.

**Monomial gaps obstruct integral closedness.** Over any commutative domain `R`,
let `S` be an additive submonoid of `ℕ`. If the subalgebra generated by `X ^ s`
for `s ∈ S` is integrally closed, then `b ∈ S`, `b + n ∈ S`, `0 < k` and
`k * n ∈ S` imply `n ∈ S`. The contrapositive shows that `R[X², X³]` is not
integrally closed, in every characteristic. See
[`Polynomial/MonomialIntegralClosure.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialIntegralClosure.lean).

**Power-substitution range and equivalence.** Over any commutative semiring `R`,
the range of `Polynomial.expand R d` is the existing exponent subalgebra for
`AddSubmonoid.multiples d`, including `d = 0`. For positive `d`,
`Polynomial.expandEquivAdjoinXPow` gives the actual `R`-algebra equivalence
from `R[X]`; its forward map is power substitution, and its inverse reads the
coefficient at `n * d` for the coefficient at `n`. See
[`Polynomial/MonomialSubalgebra.lean`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialSubalgebra.lean).

**Monomial exponent subalgebras.** Over any commutative semiring, including the zero
semiring, the polynomial subalgebra generated by `X^s` for `s` in an additive
submonoid `S` of `ℕ` has a basis indexed by `S`, with polynomial coefficients as
coordinates and a finite reconstruction formula. Its canonical module is free
by `Module.Free.of_basis`. See
[MonomialSubalgebra.lean](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/MonomialSubalgebra.lean).

Write `Q(R,n) = R[X₀,…,Xₙ]/I(R,n)` for the full quotient by the `2 × 2` Hankel
minors and `f = rncMap R n : Source R n →+* Target R` for `Xᵢ ↦ U^(n-i)V^i`.
Unless stated otherwise, `R` is any commutative ring and `n : ℕ` includes zero.
In particular, `Q(R,0) = R[X₀]`, **not** the raw parametrization image `R`.
Here `Subsingleton R` means the zero coefficient ring or semiring.

**Two-generator polynomial conductor.** For a commutative semiring `R` and
coprime natural numbers `a, b`, the greatest ideal of `R[X]` contained in
the canonical subalgebra `R[X^a, X^b]` is `(X^((a - 1)*(b - 1)))`.
If `a, b` are not coprime, the greatest contained ambient ideal is zero.
These statements concern every ambient polynomial ideal, include exponents
zero and one (also `(a, b) = (0, 0)`), and permit the zero semiring.
Membership in the subalgebra is also characterized by the additive submonoid
containing the support. See
[the conductor theorem](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/Conductor.lean) and its
[natural-coefficient examples](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdealsTest/PolynomialConductor.lean).

**Polynomial subalgebras containing a power.** For every commutative semiring
`R : Type u`, `A : Subalgebra R R[X]`, and positive natural number `n` with
`X ^ n ∈ A`, `Polynomial.span_X_pow_eq_top_of_X_pow_mem` shows that the first
`n` powers of `X` span `R[X]` for the canonical multiplication action of `A`.
`Polynomial.moduleFinite_of_X_pow_mem` consequently gives `Module.Finite A R[X]`.
For arbitrary `ι : Type v` and `a : ι → ℕ`, `Polynomial.moduleFinite_adjoin_X_pow_iff`
says that `R[X]` is finite over `Algebra.adjoin R (Set.range (fun i => X ^ a i))`
exactly when `(∃ i, 0 < a i) ∨ Subsingleton R`. The index universe is independent
of the coefficient universe; empty and all-zero families are included.
No ring, domain, nontriviality or Noetherian hypothesis is needed, and no basis
or freeness is asserted. See [finite polynomial subalgebras](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Polynomial/FiniteSubalgebra.lean).

**Coefficient change on full Hankel quotients.** For commutative rings
`R : Type u`, `S : Type v` in independent universes and any `φ : R →+* S`, the
induced stock ideal quotient map `Q(R,n) →+* Q(S,n)` is injective exactly when
`φ` is injective, and surjective exactly when `φ` is surjective, in every degree.
No flatness, domain, nontriviality or `Algebra R S` is assumed. See the
[coefficient-map criteria](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/CoefficientMap.lean).

**Coefficientwise normalization and monomial kernels (GroupRings API).** Over
any ring, an additive source monoid and an arbitrary index function to a bare
type, suppose **every monomial and coefficient** is congruent modulo a left ideal to the term
at a source exponent chosen by its target index. Elements whose coefficients
sum to zero along fibers then belong to the ideal, in independent universes.
Additive exponent homomorphisms give kernel containment; equality and a
membership criterion additionally need the reverse ideal inclusion. No
commutativity, section or surjectivity is needed; an arbitrary index function
need not induce a ring map. The canonical results are in the root
`AddMonoidAlgebra` namespace of `GroupRings.MonoidAlgebra.FiberNormalization`.
The root `ToricIdeals` import retains their former `ToricIdeals.AddMonoidAlgebra`
names as deprecated aliases through the compatibility module. See the
[normalization contract](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/docs/FiberNormalization.md).

**Coprime weighted fibers.** In `AddMonoidAlgebra R (Fin 2 →₀ ℕ)` for any
ring `R`, `Nat.Coprime a b` and equal weights
`b*d(0)+a*d(1) = b*e(0)+a*e(1)` imply that
`single d c - single e c` belongs to the principal **left** ideal generated
by `X₀^a - X₁^b`, for every `c : R`. Noncommutative coefficient rings, zero
rings and the coprime axes `(0,1)` and `(1,0)` are included. See
[`single_sub_single_mem_span_of_coprime_weight_eq`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MonoidAlgebra/CoprimeWeights.lean).
The same module proves
`ker_mapDomainRingHom_weight_eq_span_of_coprime`: the kernel of the stock
`Finsupp.weight` pushforward for weights `(b,a)` is exactly this left ideal.
`mem_span_iff_mapDomain_weight_eq_zero_of_coprime` detects membership by
vanishing of that image. No full-target surjectivity is asserted: weights
`(3,2)` miss `1`.

**Gcd-reduced natural-weight kernels.** For any `R : Type u` with `[Ring R]`
and `a,b : ℕ` with `a ≠ 0 ∨ b ≠ 0`, the same stock pushforward for weights
`(b,a)` has kernel generated as a **left** ideal by
`X₀^(a / Nat.gcd a b) - X₁^(b / Nat.gcd a b)`.
[`ker_mapDomainRingHom_weight_eq_span`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MonoidAlgebra/NaturalWeights.lean)
and `mem_span_iff_mapDomain_weight_eq_zero` include noncommutative rings,
zero rings and both axes: `(0,b)` gives `1-X₁` for `b ≠ 0`, and `(a,0)`
gives `X₀-1` for `a ≠ 0`. Weights `(6,4)` give `X₀²-X₁³`.
The pair `(0,0)` is excluded; its kernel generally needs both `X₀-1` and
`X₁-1`. No full-target surjectivity is assumed or asserted.

**Hankel presentation.** For `1 ≤ n`,
[`hankelIdeal_eq_ker`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve.lean) identifies `I(R,n)`
with the kernel of `f` and the quotient with its **image subring**, not the
full target. At `n = 0` the inclusion is strict for nontrivial `R`; at `n = 1`
the raw map is injective. The module proves energy-decreasing reduction and
terminal uniqueness; chosen representatives are classical, not executable canonical forms.

**Raw-map injectivity, surjectivity and freeness.** Over any **commutative
semiring** `R`, each holds exactly when `n = 1 ∨ Subsingleton R`
([injectivity](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/Injectivity.lean),
[surjectivity](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/MapSurjectivity.lean),
[freeness](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/Freeness.lean)). Source and target are
the full polynomial semirings. Freeness uses `p • q = f(p) * q` and an arbitrary,
not necessarily finite, basis. At degree zero `X₀` maps to `1`.

**Relative finiteness and flatness.** Over commutative semirings, the raw map
is [of finite type in every degree](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/ParametrizationFinite.lean);
its full target is a finite **source**-module iff `n ≠ 0 ∨ Subsingleton R`.
Over commutative rings, [raw-map flatness](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/MapFlatness.lean)
and [formal unramifiedness](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/MapUnramified.lean)
each hold iff `n = 1 ∨ Subsingleton R`, via `f.toAlgebra`, not coefficient-`R`
or quotient scalars. The [full-quotient-to-full-target map](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/QuotientMapFlatness.lean)
has the same flatness criterion, with action `q • p = quotientMap R n q * p`.

**Coefficient modules and endpoints.** `Q(R,n)` is
[free and faithfully flat over `R`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/CoefficientAlgebra.lean)
in every degree. Coefficient-module finite generation, Noetherianity and
Artinianity each hold iff `Subsingleton R`. The
[endpoint map](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/EndpointMap.lean) makes it integral
and finite over `MvPolynomial (Fin 2) R` in every degree; for `1 ≤ n` it is
injective with `Fin n`-indexed basis `1, X₁, …, Xₙ₋₁`, using exactly
`Algebra.toModule` for `endpointMap.toAlgebra`: `p • q = endpointMap n p * q`.
The [augmentation](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/Augmentation.lean) kills **all**
variables and retracts `R`; the separate [axis projection](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/AxisProjection.lean)
retains `X₀`, splits onto `R[X]`, and is an isomorphism at `n = 0`.

**Ring criteria and regular coordinates.** In every degree `Q(R,n)` is a
domain, reduced, Noetherian or Jacobson iff `R` has the respective property;
primality and radicality of `I(R,n)` detect a domain and a reduced ring.
Artinianity **over itself** holds iff `Subsingleton R`, not merely if `R` is
Artinian. Every [coordinate class is regular](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/CoordinateRegularity.lean),
even over nilpotent coefficients and zero rings: both multiplication maps are
injective, not a regular-sequence assertion. [Detailed criteria](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/docs/Results.md).

**Integral closedness and dimension.** For a **commutative domain** `R`,
[`quotient_isIntegrallyClosed_iff`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/IntegralClosure.lean)
says `Q(R,n)` is integrally closed iff `R` is. For a **Noetherian commutative
ring** `R`, [Krull dimension](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/Dimension.lean) is
`ringKrullDim Q(R,n) = ringKrullDim R + (if n = 0 then 1 else 2)` in `WithBot ℕ∞`,
including zero rings of dimension `⊥` and infinite coefficient dimension.

**Formal smoothness over coefficients.** For every commutative ring `R`,
[`quotient_formallySmooth_iff`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/FormallySmooth.lean)
states `Algebra.FormallySmooth R Q(R,n) ↔ n ≤ 1 ∨ Subsingleton R` for the canonical
coefficient algebra. This includes `Q(R,0) = R[X₀]`, zero rings and characteristic
two; it is not formal unramifiedness of the raw map over its full source.

**Grading, homogeneous coordinates and vertex cotangents.** The
[source Hankel ideal is homogeneous](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/Homogeneous.lean).
The full quotient has its standard multiplicative grading and unique finite
homogeneous reconstruction. Its degree-`d` component has a coefficient basis
indexed by `Fin (n*d+1)`; at `n = 0` its vector is `[X₀^d]`. The augmentation
kernel `J` has cotangent module `J/J²` with a `Fin (n+1)`-indexed coefficient
basis of variable classes; coordinates are raw linear coefficients of
representatives with zero constant coefficient. At `n = 0` its vector is `[X₀]`.
Indexed bases over zero rings assert no numerical rank. Both
[GradedAlgebra](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/GradedAlgebra.lean) and
[Cotangent](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/Cotangent.lean) require **direct imports**.

**Arbitrary base change.** For commutative rings `R`, `S` with `[Algebra R S]`
in independent universes, [`S ⊗[R] Q(R,n) ≃ₐ[S] Q(S,n)`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/BaseChange.lean)
in every degree, without flatness or injectivity. [Homogeneous-component bases](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/HomogeneousBasis.lean)
retain their indices under arbitrary coefficient change; their scalar-extension
equivalences commute with inclusions into the full quotients and base change.
Zero and nilpotent coefficients are included.

**Arithmetic exponent image.** The [coefficient-free criterion](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/RationalNormalCurve/ExponentImage.lean)
for a target `t : Fin 2 →₀ ℕ` is `n ∣ (t 0 + t 1)`, including `n = 0`,
when only the zero target occurs.

**The split quadric.** For any commutative ring `A`, substitution
`(w,x,y,z) ↦ (W,WT,Y,YT)` has kernel `(wz - xy)`; the quotient identifies with
the **range**, not the whole target. Its domain/primality criterion is `IsDomain A`.
The coefficient-free exponent image is `t ≤ u+v`, with unique reduced
representatives; the total selector is a preimage only there and is not additive.
The `w`- and `W`-charts are equivalent for independent localization models with
both `A`-scalar towers, without domain or nontriviality hypotheses. See the
[split-quadric guide](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/docs/SplitQuadric.md).

**Uniform exponents from finite translate covers.** In a cancellative commutative
monoid, a cover `T ⊆ S * E` with finite `E ⊆ T` gives `t ^ E.ncard.factorial ∈ S`
for every `t ∈ T`, without containment or finite-generation assumptions on the
submonoids. Thus a finite canonical left inclusion module between coefficient-one
monomial adjoins forces either subsingleton coefficients or one positive exponent
working for every target exponent. Additively, the same positive natural-number
multiplier sends every target exponent into the source submonoid. See
[`FiniteCover`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/Submonoid/FiniteCover.lean),
[`MonoidAlgebra/MonomialFinite`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/MonoidAlgebra/MonomialFinite.lean), and
[`AddMonoidAlgebra/MonomialFinite`](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/ToricIdeals/AddMonoidAlgebra/MonomialFinite.lean).

This library does not classify general toric ideals or prove rational-normal-curve
results outside the stated parametrization and hypotheses. Source-passage
correspondence and coverage are tracked separately, not claimed here. See the
[full result statements and scalar conventions](https://github.com/FormalFrontier/toric-ideals/blob/593116e0783dee84353f7a76ef65001cb814b01e/docs/Results.md).

## Main results

Its formalization.yaml lists 1 main result, and the scan finds 1 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
