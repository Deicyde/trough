---
declaration: section
origin: cited
lean: MvPolynomial.coeffL1Norm, MvPolynomial.coeffL1Norm_eq_sum, MvPolynomial.coeffL1Norm_nonneg, MvPolynomial.coeffL1Norm_zero, MvPolynomial.coeffL1Norm_add_le, MvPolynomial.coeffL1Norm_sum_le, MvPolynomial.coeffL1Norm_smul, MvPolynomial.coeffL1Norm_monomial
statement: formalized
proof: formalized
---

# Coefficient L1 norm of multivariate polynomials

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html).

## Coefficient L1 norm of a multivariate polynomial

The rational sum of the absolute values of a polynomial's coefficients.

Formalized by `MvPolynomial.coeffL1Norm`, a definition declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm).

## Coefficient L1 norm as a sum over a larger index set

Enlarging the summation set beyond the support does not change the sum.

Formalized by `MvPolynomial.coeffL1Norm_eq_sum`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-eq-sum).

## Nonnegativity of the coefficient L1 norm

The coefficient L1 norm is nonnegative.

Formalized by `MvPolynomial.coeffL1Norm_nonneg`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-nonneg).

## Coefficient L1 norm of the zero polynomial

The zero polynomial has coefficient L1 norm zero.

Formalized by `MvPolynomial.coeffL1Norm_zero`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-zero).

## Triangle inequality for the coefficient L1 norm

Adding polynomials increases the coefficient L1 norm by at most the sum.

Formalized by `MvPolynomial.coeffL1Norm_add_le`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-add-le).

## Coefficient L1 norm of a finite sum

The norm of a finite sum is bounded by the sum of the coefficient norms.

Formalized by `MvPolynomial.coeffL1Norm_sum_le`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-sum-le).

## Coefficient L1 norm of a scalar multiple

Rational scalar multiplication scales the norm by the scalar's absolute value.

Formalized by `MvPolynomial.coeffL1Norm_smul`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-smul).

## Coefficient L1 norm of a monomial

A monomial's coefficient L1 norm is the absolute value of its coefficient,
including when the coefficient is zero.

Formalized by `MvPolynomial.coeffL1Norm_monomial`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-monomial).

## Upper bound on the coefficient L1 norm of a monomial

The coefficient L1 norm of a monomial is at most its absolute coefficient.

Formalized by `MvPolynomial.coeffL1Norm_monomial_le`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-monomial-le).

## Submultiplicativity of the coefficient L1 norm

The coefficient convolution in a product is bounded by the product of the
coefficient L1 norms; cancellation can make this inequality strict.

Formalized by `MvPolynomial.coeffL1Norm_mul_le`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#coeff-l1-norm-mul-le).

## Coefficient L1 norm as an $\ell^1$ distance

The real cast of the coefficient L1 norm agrees with the explicit exponent-one
metric on the exact rational coefficient Finsupp carrier.

Formalized by `MvPolynomial.dist_coeff_zero_eq_coeffL1Norm`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/CoefficientL1.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html#dist-coeff-zero-eq-coeff-l1-norm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coefficient L1 norm of multivariate polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/polynomials/coefficient-l1-norm-of-multivariate-polynomials)
