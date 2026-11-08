# Multivariate polynomials

> Reusable multivariate-polynomial results on infinite-variable ideals, coordinate-difference evaluation ideals, polynomial maximal-spectrum infinitude and the classification of univariate polynomial closed points by algebraic-closure automorphism orbits without separability, normal-extension automorphism orbits as minimal-polynomial root sets with cardinality equal to separable degree and full degree exactly for separable elements, homogeneous evaluation, disjoint-block substitution and its iteration, finite-variable origins of finite collections of polynomial fractions over integral domains in arbitrary fraction-ring representations, and a Krull-dimension bound for subsemirings by their finite-variable fraction-stage preimage dimensions, not the whole stage fields, degree, coefficient extraction and linear evaluation, chosen linear division, existential monic lifts and scalar-top first-variable lex degree. The univariate Hilbert basis theorem holds for any left-Noetherian ring, without coefficient commutativity, using a central variable and the canonical left self-module. The same holds for finitely many central natural-number coordinates via AddMonoidAlgebra, with independent coefficient and coordinate universes. Central Laurent polynomial rings over left-Noetherian rings are likewise left-Noetherian, including noncommutative and zero coefficient rings. The Laurent argument clears negative exponents by units and reuses the arbitrary-ring polynomial theorem. A polynomial point quotient by indexed squares and linear point relations has a canonical map to a square-zero extension of evaluation quotients; that same map is an algebra equivalence under pairwise unit differences. See README.md and docs/API.md for precise hypotheses and limitations.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/formalization.yaml) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

55 articles, for headline results in its README whose declaration link names a declaration the linked file declares. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials), read at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “Review evidence is revision-specific”
- Review notes: “Independent review, builds and axiom audits apply only to the declarations and exact source revisions they cover. This metadata does not certify a successful build or complete standard-axiom audit for every selected result, nor does it establish source-specific correspondence.”
- Automation: agent; tool setup “Formal Frontier AI agents used Lean, Lake and mathlib for proof development, examples and documentation, with independent review.”
- Automation notes: “Mathlib's polynomial, ideal and finitely supported-function APIs support the degree, coefficient, substitution and division results. Their statements specify the relevant coefficient and order hypotheses.”

## Scope

Fifty-four selected public declarations over seventeen leaves and the aggregate: finite collections in an abstract fraction ring of MvPolynomial over an integral domain come from one finite-variable fraction ring, without a field coefficient or target hypothesis; the univariate polynomial maximal spectrum is infinite over any nontrivial commutative ring, and the multivariate maximal spectrum is infinite exactly when the coefficient ring is nontrivial and either a variable exists or the coefficient maximal spectrum is infinite, with independent universes; for independently universed fields K and L with their given Algebra K L and Normal K L, the automorphism orbit of each x in L is the root set of minpoly K x, its ncard is the polynomial's natSepDegree, and equality with natDegree is equivalent to IsSeparable K x, without perfectness, separability of the extension or finite-dimensionality; coordinate-difference ideals equal evaluation kernels over CommRing coefficients for arbitrary variables, with a vanishing membership criterion and a singleton-vanishing-ideal bridge over fields; the quotient of MvPolynomial (Option ι) R by only indexed squares and linear point relations has a canonical R[X]-algebra map to TrivSqZeroExt of the direct sum of evaluation quotients without separation, and that same map is bijective and an algebra equivalence when differences between distinct points are units, for any CommRing R (including the zero ring) and any independently-universed index type; non-finite generation of the variable ideal for Nontrivial CommSemiring coefficients and Infinite variables; scaling under arbitrary CommSemiring with fixed coefficient homomorphism; disjoint-block substitution with distinct forward-only and iff vanishing; structural renaming, association, units and iteration over CommSemiring; conditional attained iteration degree powers (not all large degrees); arbitrary-input exact degree under NoZeroDivisors; polynomial-parameter coefficient extraction preserving homogeneous labels; linear coefficient maps commuting with evaluation at base-valued points; chosen linear division over CommRing with unit leading coefficients, cone avoidance and preservation of all coefficient ideals; scalar-top first-variable maximum lex degree over CommSemiring and pointwise first-variable exponent cones; and existential monic lifts under surjective coefficient maps for arbitrary variables and CommRings, including the zero target. Division also exposes six public helpers beyond the selected results. No canonical division, Groebner assertion, general base-form construction, multiplicative linear functional, or source-specific completion is claimed. See README.md and docs/API.md for the detailed module map and guides.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/formalization.yaml) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Mathlib*, Mathlib Contributors, https://github.com/leanprover-community/mathlib4 (software; background).
- *Minimal Primes*, Formal Frontier Agents, https://github.com/FormalFrontier/minimal-primes/tree/c069147fd1754e4a87be7e09003439f1d2250bfd (software; background).
- *Algebraic Direct Limits*, Formal Frontier Agents, https://github.com/FormalFrontier/algebraic-direct-limits/tree/5959888b3d648cf1f72038459f63d804093d6c54 (software; background).
- *Foundations of Rigid Geometry I*, Kazuhiro Fujiwara, Fumiharu Kato, arXiv:1308.4734v5 (book; background).
- *A non-finitely-generated variable ideal: finite-support proof exposition*, Formal Frontier Agents (original-proof; adapts).
- *The Rising Sea: Foundations of Algebraic Geometry*, Ravi Vakil, October 21, 2025 draft, Exercise 6.7.E, PDF page 199 (book; background).
- *Structural block substitution and the two iteration orders*, Beacon (original-proof; adapts).
- *Exact total degree of substitution into disjoint blocks*, Formal Frontier Agents (original-proof; adapts).
- *Polynomial-parameter coefficients of homogeneous multivariate polynomials*, Formal Frontier Agents (original-proof; background).
- *Polynomial equations in finite-basis coordinates*, Beacon (original-proof; background).

## Builds on

- [Algebraic direct limits](../algebraic-direct-limits/README.md) (a Lake dependency, pinned at 5959888b)
- [Coherent modules](../coherent-modules/README.md) (a Lake dependency, pinned at e848789e)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 41da4c03)
- [Minimal primes](../minimal-primes/README.md) (a Lake dependency, pinned at c069147f)

## Used by

- [Adic modules](../adic-modules/README.md)
- [Algebraic groups](../../algebraic-geometry/algebraic-groups/README.md)
- [Formal power series](../formal-power-series/README.md)
- [Group rings](../../ring-theory/group-rings/README.md)
- [Norm forms](../../number-theory/norm-forms/README.md)
- [Scheme properties](../../algebraic-geometry/scheme-properties/README.md)
- [Toric ideals](../toric-ideals/README.md)
- [Valuation integers](../../number-theory/valuation-integers/README.md)

## [Heights of homogeneous… to Jacobson radicals of…](part-01/README.md)

- [Heights of homogeneous polynomial evaluations](part-01/heights-of-homogeneous-polynomial-evaluations.md)
- [Homogeneous polynomial maps on projective coordinate spaces](part-01/homogeneous-polynomial-maps-on-projective-coordi.md)
- [Polynomial closed points and algebraic-closure orbits](part-01/polynomial-closed-points-and-algebraic-closure-o.md)
- [Infinitely many maximal ideals of polynomial rings](part-01/infinitely-many-maximal-ideals-of-polynomial-rin.md)
- [Factorization uniqueness from a regular crossed resultant](part-01/factorization-uniqueness-from-a-regular-crossed.md)
- [Nonconstant coefficients of polynomial units](part-01/nonconstant-coefficients-of-polynomial-units.md)
- [Polynomial units over commutative semirings](part-01/polynomial-units-over-commutative-semirings.md)
- [Prime coefficient extensions over commutative semirings](part-01/prime-coefficient-extensions-over-commutative-se.md)
- [Maximal coefficient extensions over commutative semirings](part-01/maximal-coefficient-extensions-over-commutative.md)
- [Finite coefficient-product equations determine whole products](part-01/finite-coefficient-product-equations-determine-w.md)
- [Radicals of coefficient-ideal extensions](part-01/radicals-of-coefficient-ideal-extensions.md)
- [Scalar annihilators and non-zero-divisors](part-01/scalar-annihilators-and-non-zero-divisors.md)
- [The degree-zero homogeneous component](part-01/the-degree-zero-homogeneous-component.md)
- [Coefficient ideals over commutative semirings](part-01/coefficient-ideals-over-commutative-semirings.md)
- [Square witnesses for failure of subtractivity](part-01/square-witnesses-for-failure-of-subtractivity.md)
- [Powers of augmented coefficient ideals](part-01/powers-of-augmented-coefficient-ideals.md)
- [Primary coefficient ideals](part-01/primary-coefficient-ideals.md)
- [Supplied primary families and deletion irredundance](part-01/supplied-primary-families-and-deletion-irredunda.md)
- [Nilpotent coefficients and irreducible polynomial spectra](part-01/nilpotent-coefficients-and-irreducible-polynomia.md)
- [Jacobson radicals of coefficient ideals](part-01/jacobson-radicals-of-coefficient-ideals.md)

## [Integral elements over… to Fraction-ring renaming is…](part-02/README.md)

- [Integral elements over coefficient rings](part-02/integral-elements-over-coefficient-rings.md)
- [Integral closure in arbitrarily many variables](part-02/integral-closure-in-arbitrarily-many-variables.md)
- [Flatness of commutative-ring variable renaming](part-02/flatness-of-commutative-ring-variable-renaming.md)
- [Canonical unique-variable degree](part-02/canonical-unique-variable-degree.md)
- [Injectivity and surjectivity of variable renaming](part-02/injectivity-and-surjectivity-of-variable-renamin.md)
- [Formal smoothness of variable renaming](part-02/formal-smoothness-of-variable-renaming.md)
- [Smoothness of variable renaming](part-02/smoothness-of-variable-renaming.md)
- [Formal unramifiedness of variable renaming](part-02/formal-unramifiedness-of-variable-renaming.md)
- [Integrality of polynomial variable renaming](part-02/integrality-of-polynomial-variable-renaming.md)
- [Algebraicity of polynomial variable renaming](part-02/algebraicity-of-polynomial-variable-renaming.md)
- [Finite presentation of commutative-ring variable renaming](part-02/finite-presentation-of-commutative-ring-variable.md)
- [Zero-variable presentations and semiring renaming](part-02/zero-variable-presentations-and-semiring-renamin.md)
- [Variable renaming has an exact relative finite-type criterion](part-02/variable-renaming-has-an-exact-relative-finite-t.md)
- [Variable renaming has an exact relative essentially finite-type criterion](part-02/variable-renaming-has-an-exact-relative-essentia.md)
- [Module finiteness of variable renaming has a sharper criterion](part-02/module-finiteness-of-variable-renaming-has-a-sha.md)
- [Quasi-finiteness of commutative-ring variable renaming](part-02/quasi-finiteness-of-commutative-ring-variable-re.md)
- [Finite coefficient aggregation has an exact injectivity criterion](part-02/finite-coefficient-aggregation-has-an-exact-inje.md)
- [Joint degree-and-support profiles recover bivariate coefficients only for trivial coefficients](part-02/joint-degree-and-support-profiles-recover-bivari.md)
- [Variable-renaming kernels have an exact presentation and finite-generation criterion](part-02/variable-renaming-kernels-have-an-exact-presenta.md)
- [Fraction-ring renaming is surjective, equivalently integral, exactly when it covers all variables](part-02/fraction-ring-renaming-is-surjective-equivalentl.md)

## [Omitted variables are… to Comparison with Lagrange…](part-03/README.md)

- [Omitted variables are algebraically independent over the source fraction ring](part-03/omitted-variables-are-algebraically-independent.md)
- [Omitted variables form a transcendence basis over the source fraction ring](part-03/omitted-variables-form-a-transcendence-basis-ove.md)
- [The image of evaluating one polynomial at two points](part-03/the-image-of-evaluating-one-polynomial-at-two-po.md)
- [Finite simultaneous polynomial evaluation has an exact surjectivity criterion](part-03/finite-simultaneous-polynomial-evaluation-has-an.md)
- [Evaluation-kernel powers are detected by translated coefficients](part-03/evaluation-kernel-powers-are-detected-by-transla.md)
- [Hilbert basis theorem for left-Noetherian rings](part-03/hilbert-basis-theorem-for-left-noetherian-rings.md)
- [Artinian polynomial-semiring criteria](part-03/artinian-polynomial-semiring-criteria.md)
- [Univariate coefficient-module Noetherianity and Artinianity each characterize trivial coefficients](part-03/univariate-coefficient-module-noetherianity-and.md)
- [Radical coefficient-ideal extensions are characterized by subtractivity](part-03/radical-coefficient-ideal-extensions-are-charact.md)
- [Coefficient-and-variable ideals have an exact finite-generation criterion](part-03/coefficient-and-variable-ideals-have-an-exact-fi.md)
- [The variable ideal is not finitely generated](part-03/the-variable-ideal-is-not-finitely-generated.md)
- [Antichain coefficients of monomial ideals](part-03/antichain-coefficients-of-monomial-ideals.md)
- [Variable classes form the augmentation cotangent basis](part-03/variable-classes-form-the-augmentation-cotangent.md)
- [Degree-controlled finite interpolation](part-03/degree-controlled-finite-interpolation.md)
- [Comparison with Lagrange interpolation](part-03/comparison-with-lagrange-interpolation.md)

## Main results

The 54 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `Normal.orbit_eq_rootSet_minpoly` | theorem | [MultivariatePolynomials/PolynomialRootOrbits.lean, line 39](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PolynomialRootOrbits.lean#L39) |  |
| `Normal.ncard_orbit_eq_natSepDegree` | theorem | [MultivariatePolynomials/PolynomialRootOrbits.lean, line 49](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PolynomialRootOrbits.lean#L49) |  |
| `Normal.ncard_orbit_eq_natDegree_iff_isSeparable` | theorem | [MultivariatePolynomials/PolynomialRootOrbits.lean, line 58](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PolynomialRootOrbits.lean#L58) |  |
| `MaximalSpectrum.infinite_polynomial` | theorem | [MultivariatePolynomials/PrimeSpectrum.lean, line 190](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimeSpectrum.lean#L190) |  |
| `MaximalSpectrum.infinite_mvPolynomial_iff` | theorem | [MultivariatePolynomials/PrimeSpectrum.lean, line 202](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimeSpectrum.lean#L202) |  |
| `MvPolynomial.exists_finset_fractionRing_map_range` | theorem | [MultivariatePolynomials/FractionRingFiniteVariables.lean, line 51](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FractionRingFiniteVariables.lean#L51) |  |
| `MvPolynomial.ideal_span_X_sub_C_eq_ker_eval` | theorem | [MultivariatePolynomials/EvaluationIdeal.lean, line 222](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L222) |  |
| `MvPolynomial.mem_ideal_span_X_sub_C_iff` | theorem | [MultivariatePolynomials/EvaluationIdeal.lean, line 249](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L249) |  |
| `MvPolynomial.ideal_span_X_sub_C_eq_vanishingIdeal_singleton` | theorem | [MultivariatePolynomials/EvaluationIdeal.lean, line 348](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L348) |  |
| `MvPolynomial.pointSquareZeroForward` | def | [MultivariatePolynomials/PointSquareZeroPresentation.lean, line 230](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PointSquareZeroPresentation.lean#L230) |  |
| `MvPolynomial.pointSquareZeroForward_bijective` | theorem | [MultivariatePolynomials/PointSquareZeroQuotient.lean, line 125](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PointSquareZeroQuotient.lean#L125) |  |
| `MvPolynomial.pointSquareZeroAlgEquiv` | def | [MultivariatePolynomials/PointSquareZeroQuotient.lean, line 216](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PointSquareZeroQuotient.lean#L216) |  |
| `MvPolynomial.idealOfVars_not_fg` | theorem | [MultivariatePolynomials/IdealOfVars.lean, line 162](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IdealOfVars.lean#L162) |  |
| `MvPolynomial.IsWeightedHomogeneous.eval₂Hom_scaleVariables` | theorem | [MultivariatePolynomials/HomogeneousEvaluation.lean, line 34](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/HomogeneousEvaluation.lean#L34) |  |
| `MvPolynomial.IsHomogeneous.eval₂Hom_mul_left` | theorem | [MultivariatePolynomials/HomogeneousEvaluation.lean, line 67](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/HomogeneousEvaluation.lean#L67) |  |
| `MvPolynomial.blockSubst` | def | [MultivariatePolynomials/BlockSubstitution.lean, line 33](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitution.lean#L33) |  |
| `MvPolynomial.eval_blockSubst` | theorem | [MultivariatePolynomials/BlockSubstitution.lean, line 38](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitution.lean#L38) |  |
| `MvPolynomial.eval_blockSubst_eq_zero_imp` | theorem | [MultivariatePolynomials/BlockSubstitution.lean, line 47](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitution.lean#L47) |  |
| `MvPolynomial.eval_blockSubst_eq_zero_iff` | theorem | [MultivariatePolynomials/BlockSubstitution.lean, line 60](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitution.lean#L60) |  |
| `MvPolynomial.ne_zero_of_eval_eq_zero_imp` | theorem | [MultivariatePolynomials/BlockSubstitution.lean, line 79](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitution.lean#L79) |  |
| `MvPolynomial.iteratedBlockSubst` | def | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 40](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L40) |  |
| `MvPolynomial.iteratedBlockSubst_zero` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 47](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L47) |  |
| `MvPolynomial.iteratedBlockSubst_succ` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 50](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L50) |  |
| `MvPolynomial.eval_iteratedBlockSubst_zero` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 57](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L57) |  |
| `MvPolynomial.eval_iteratedBlockSubst_succ` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 61](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L61) |  |
| `MvPolynomial.eval_iteratedBlockSubst_eq_zero_imp` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 69](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L69) |  |
| `MvPolynomial.eval_iteratedBlockSubst_eq_zero_iff` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 89](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L89) |  |
| `MvPolynomial.isHomogeneous_iteratedBlockSubst` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 112](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L112) |  |
| `MvPolynomial.iteratedBlockSubst_ne_zero` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 131](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L131) |  |
| `MvPolynomial.iteratedBlockSubst_totalDegree` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 137](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L137) |  |
| `MvPolynomial.exists_iteratedBlockSubst_totalDegree_gt` | theorem | [MultivariatePolynomials/IteratedBlockSubstitution.lean, line 145](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IteratedBlockSubstitution.lean#L145) |  |
| `MvPolynomial.rename_blockSubst` | theorem | [MultivariatePolynomials/BlockSubstitutionLaws.lean, line 38](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitutionLaws.lean#L38) |  |
| `MvPolynomial.blockSubst_assoc` | theorem | [MultivariatePolynomials/BlockSubstitutionLaws.lean, line 47](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitutionLaws.lean#L47) |  |
| `MvPolynomial.blockSubst_X_left` | theorem | [MultivariatePolynomials/BlockSubstitutionLaws.lean, line 60](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitutionLaws.lean#L60) |  |
| `MvPolynomial.blockSubst_X_right` | theorem | [MultivariatePolynomials/BlockSubstitutionLaws.lean, line 65](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitutionLaws.lean#L65) |  |
| `MvPolynomial.iteratedBlockSubst_one` | theorem | [MultivariatePolynomials/BlockSubstitutionLaws.lean, line 138](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitutionLaws.lean#L138) |  |
| `MvPolynomial.iteratedBlockSubst_add` | theorem | [MultivariatePolynomials/BlockSubstitutionLaws.lean, line 184](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitutionLaws.lean#L184) |  |
| `MvPolynomial.iteratedBlockSubst_snoc` | theorem | [MultivariatePolynomials/BlockSubstitutionLaws.lean, line 211](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitutionLaws.lean#L211) |  |
| `MvPolynomial.totalDegree_blockSubst` | theorem | [MultivariatePolynomials/BlockSubstitutionDegree.lean, line 308](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/BlockSubstitutionDegree.lean#L308) |  |
| `MvPolynomial.IsHomogeneous.coeff_polynomial_interchange` | theorem | [MultivariatePolynomials/PolynomialCoefficientHomogeneity.lean, line 108](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PolynomialCoefficientHomogeneity.lean#L108) |  |
| `MvPolynomial.eval_addMonoidAlgebraMap_of_linearMap` | theorem | [MultivariatePolynomials/LinearCoefficientEvaluation.lean, line 38](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearCoefficientEvaluation.lean#L38) |  |
| `MonomialOrder.linearDivisionQuotient` | def | [MultivariatePolynomials/LinearDivision.lean, line 66](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L66) |  |
| `MonomialOrder.linearDivisionRemainder` | def | [MultivariatePolynomials/LinearDivision.lean, line 73](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L73) |  |
| `MonomialOrder.linearDivision_decomposition` | theorem | [MultivariatePolynomials/LinearDivision.lean, line 96](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L96) |  |
| `MonomialOrder.linearDivision_remainder_support` | theorem | [MultivariatePolynomials/LinearDivision.lean, line 152](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L152) |  |
| `MonomialOrder.linearMap_preserves_coeffsIn` | theorem | [MultivariatePolynomials/LinearDivision.lean, line 168](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L168) |  |
| `MonomialOrder.linearDivision_remainder_coeffsIn` | theorem | [MultivariatePolynomials/LinearDivision.lean, line 184](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L184) |  |
| `MonomialOrder.linearDivision_quotient_coeffsIn` | theorem | [MultivariatePolynomials/LinearDivision.lean, line 192](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L192) |  |
| `MonomialOrder.linearDivision_remainder_of_reduced` | theorem | [MultivariatePolynomials/LinearDivision.lean, line 202](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L202) |  |
| `MonomialOrder.linearDivision_quotient_of_reduced` | theorem | [MultivariatePolynomials/LinearDivision.lean, line 221](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/LinearDivision.lean#L221) |  |
| `MonomialOrder.exists_monic_lift` | theorem | [MultivariatePolynomials/MonicLift.lean, line 38](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/MonicLift.lean#L38) |  |
| `Finsupp.cons_zero_le_cons_iff` | theorem | [MultivariatePolynomials/FirstVariableLex.lean, line 31](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FirstVariableLex.lean#L31) |  |
| `MonomialOrder.lex_le_cons_zero_of_le` | theorem | [MultivariatePolynomials/FirstVariableLex.lean, line 47](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FirstVariableLex.lean#L47) |  |
| `MonomialOrder.lex_degree_of_finSuccEquiv_scalar_top` | theorem | [MultivariatePolynomials/FirstVariableLex.lean, line 60](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FirstVariableLex.lean#L60) |  |
