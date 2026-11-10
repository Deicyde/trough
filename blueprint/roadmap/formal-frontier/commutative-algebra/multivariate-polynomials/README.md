# Multivariate polynomials

> Reusable multivariate-polynomial results on infinite-variable ideals, coordinate-difference evaluation ideals, polynomial maximal-spectrum infinitude and the classification of univariate polynomial closed points by algebraic-closure automorphism orbits without separability, normal-extension automorphism orbits as minimal-polynomial root sets with cardinality equal to separable degree and full degree exactly for separable elements, homogeneous evaluation, disjoint-block substitution and its iteration, finite-variable origins of finite collections of polynomial fractions over integral domains in arbitrary fraction-ring representations, and a Krull-dimension bound for subsemirings by their finite-variable fraction-stage preimage dimensions, not the whole stage fields, degree, coefficient extraction and linear evaluation, chosen linear division, existential monic lifts and scalar-top first-variable lex degree. The univariate Hilbert basis theorem holds for any left-Noetherian ring, without coefficient commutativity, using a central variable and the canonical left self-module. The same holds for finitely many central natural-number coordinates via AddMonoidAlgebra, with independent coefficient and coordinate universes. Central Laurent polynomial rings over left-Noetherian rings are likewise left-Noetherian, including noncommutative and zero coefficient rings. The Laurent argument clears negative exponents by units and reuses the arbitrary-ring polynomial theorem. A polynomial point quotient by indexed squares and linear point relations has a canonical map to a square-zero extension of evaluation quotients; that same map is an algebra equivalence under pairwise unit differences. See README.md and docs/API.md for precise hypotheses and limitations.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/formalization.yaml) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

55 articles: 55 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials), read at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “Review evidence is revision-specific”.
- Review notes: “Independent review, builds and axiom audits apply only to the declarations and exact source revisions they cover. This metadata does not certify a successful build or complete standard-axiom audit for every selected result, nor does it establish source-specific correspondence.”
- Automation: agent; tool setup “Formal Frontier AI agents used Lean, Lake and mathlib for proof development, examples and documentation, with independent review.”
- Automation notes: “Mathlib's polynomial, ideal and finitely supported-function APIs support the degree, coefficient, substitution and division results. Their statements specify the relevant coefficient and order hypotheses.”

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

Its formalization.yaml lists 54 main results, and the scan finds 54 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
