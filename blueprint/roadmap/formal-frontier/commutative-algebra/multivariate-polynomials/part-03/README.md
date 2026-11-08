---
navigation: transparent
---

# Omitted variables are… to Comparison with Lagrange…

- [Omitted variables are algebraically independent over the source fraction ring](omitted-variables-are-algebraically-independent.md)
- [Omitted variables form a transcendence basis over the source fraction ring](omitted-variables-form-a-transcendence-basis-ove.md)

**Zeros are closed points of polynomial quotients.** For any ideal `I` in
`MvPolynomial σ K` with `K` algebraically closed and `σ` finite, the
[canonical point-set equivalence](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/QuotientClosedPoints.lean)
identifies `MvPolynomial.zeroLocus K I` with closed points of the spectrum
of `MvPolynomial σ K ⧸ I`. The forward prime is the kernel of descended
evaluation; polynomial membership and inverse coordinates have explicit
laws. The field and variables may inhabit different universes, and `I` may
be the unit ideal or define a nonreduced quotient. This point-set result
itself does not assert a topological or sheaf equivalence.

- [The image of evaluating one polynomial at two points](the-image-of-evaluating-one-polynomial-at-two-po.md)
- [Finite simultaneous polynomial evaluation has an exact surjectivity criterion](finite-simultaneous-polynomial-evaluation-has-an.md)
- [Evaluation-kernel powers are detected by translated coefficients](evaluation-kernel-powers-are-detected-by-transla.md)

**Separated polynomial point quotients are square-zero extensions.** Over
any commutative ring, including the zero ring, and any index type, the
[generator-prescribed forward map](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PointSquareZeroPresentation.lean)
from the quotient by coordinate squares and point relations is bijective
when differences of distinct evaluation points are units. The resulting
[polynomial-algebra equivalence](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PointSquareZeroQuotient.lean)
has forward coordinate laws and an inverse law on the evaluation summands;
no mixed-product relations are added to the defining ideal. See the
[API guide](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/docs/API.md) for the two modules and their boundary examples.

**Subset-weight-one valuations have full rational residue fields.** For any
field, any variable type and subset containing a chosen pivot, the
[weight-one construction](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/WeightOneValuation.lean)
identifies the multivariate function field birationally with a univariate
rational function field over the field of unweighted variables and pivot
ratios. Minimum subset weight gives a surjective rank-one discrete valuation;
its pivot is a uniformizer, and its entire residue field is the rational
function field in those unweighted variables and ratios. The equal-order
fraction law computes residues from initial coefficients. For the empty
subset, the separate trivial valuation has no discrete-valuation claim.

- [Hilbert basis theorem for left-Noetherian rings](hilbert-basis-theorem-for-left-noetherian-rings.md)

**Noetherian polynomial-ring criteria.** The
[Noetherian module](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Noetherian.lean) proves the
coefficient-and-variable characterization over arbitrary commutative rings:
`MvPolynomial σ R` is Noetherian for its self-action exactly when `R` is
Noetherian and either
`σ` is finite or `R` is the zero ring. For nontrivial commutative semirings,
Noetherianity of the polynomial semiring forces `σ` to be finite; no
semiring Hilbert-basis sufficiency is asserted. The nontrivial-ring form
removes the zero-ring alternative without imposing a domain hypothesis.
The coefficient and variable universes are independent. The
[examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/Noetherian.lean) distinguish empty,
finite and infinite variables over the integers, `ZMod 6`, and `ZMod 1`.

- [Artinian polynomial-semiring criteria](artinian-polynomial-semiring-criteria.md)
- [Univariate coefficient-module Noetherianity and Artinianity each characterize trivial coefficients](univariate-coefficient-module-noetherianity-and.md)
- [Radical coefficient-ideal extensions are characterized by subtractivity](radical-coefficient-ideal-extensions-are-charact.md)
- [Coefficient-and-variable ideals have an exact finite-generation criterion](coefficient-and-variable-ideals-have-an-exact-fi.md)
- [The variable ideal is not finitely generated](the-variable-ideal-is-not-finitely-generated.md)
- [Antichain coefficients of monomial ideals](antichain-coefficients-of-monomial-ideals.md)
- [Variable classes form the augmentation cotangent basis](variable-classes-form-the-augmentation-cotangent.md)
- [Degree-controlled finite interpolation](degree-controlled-finite-interpolation.md)
- [Comparison with Lagrange interpolation](comparison-with-lagrange-interpolation.md)

The [full results guide](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/docs/Results.md) also covers simultaneous finite-fraction
origins and their preimage dimension bounds, polynomial Zariski topology,
valuation naturality, evaluation kernels, coefficient-module Noetherianity and
Artinianity, polynomial self-Artinianity, and the substitution, degree, division
and lifting interfaces, with all their hypotheses and boundary cases.
Its [fraction examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/docs/Results.md#fraction-origins-and-traces-in-use)
explain how to use the common finite stage and why whole stage fields do not
provide the subsemiring dimension bound.
