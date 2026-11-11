---
declaration: section
origin: cited
lean: MvPolynomial.IsHomogeneous.coeff_mul_eq_sum_support, Polynomial.mulLinearCoeffList, Polynomial.length_mulLinearCoeffList, Polynomial.getD_mulLinearCoeffList, Polynomial.ofCoeffList_mulLinearCoeffList, Finset.prod_C_add_X_mul_C_eq_sum, Finset.prod_C_add_X_mul_C_coeff, Finset.prod_C_add_X_mul_C_natDegree_le
statement: formalized
proof: formalized
---

# Coefficients of products with linear factors

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html).

## Coefficients of a product with a homogeneous linear polynomial

The coefficient of `p * q`, when `p` is homogeneous of degree one, is the
sum obtained by removing one occurrence of each variable in the monomial.

Formalized by `MvPolynomial.IsHomogeneous.coeff_mul_eq_sum_support`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/LinearProduct.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MvPolynomial/LinearProduct.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#coeff-mul-eq-sum-support).

## Coefficient list after multiplication by a linear polynomial

The dense little-endian coefficients after left multiplication by `C r + X * C c`.

Formalized by `Polynomial.mulLinearCoeffList`, a definition declared in [MathlibExt/Algebra/Polynomial/LinearCoeffList.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/LinearCoeffList.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#mul-linear-coeff-list).

## Length of the coefficient list after a linear multiplication

A linear-coefficient update always adds one dense coefficient.

Formalized by `Polynomial.length_mulLinearCoeffList`, a theorem declared in [MathlibExt/Algebra/Polynomial/LinearCoeffList.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/LinearCoeffList.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#length-mul-linear-coeff-list).

## Coefficient recurrence for multiplication by a linear polynomial

The coefficient at every index, including beyond the dense output, follows the source
recurrence `r * l[j] + c * l[j - 1]`.

Formalized by `Polynomial.getD_mulLinearCoeffList`, a theorem declared in [MathlibExt/Algebra/Polynomial/LinearCoeffList.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/LinearCoeffList.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#get-d-mul-linear-coeff-list).

## Coefficient-list multiplication agrees with polynomial multiplication

Interpreting the dense output as a little-endian polynomial is left multiplication by the
linear polynomial `C r + X * C c`.

Formalized by `Polynomial.ofCoeffList_mulLinearCoeffList`, a theorem declared in [MathlibExt/Algebra/Polynomial/LinearCoeffList.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/LinearCoeffList.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#of-coeff-list-mul-linear-coeff-list).

## Expansion of a product of affine linear polynomials

Expand a product of affine linear polynomials by the subset of factors
from which the linear term is selected.

Formalized by `Finset.prod_C_add_X_mul_C_eq_sum`, a theorem declared in [MathlibExt/RingTheory/Polynomial/AffineProduct.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Polynomial/AffineProduct.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#prod-c-add-x-mul-c-eq-sum).

## Coefficients of a product of affine linear polynomials

The coefficient of degree `i` in a product of affine linear polynomials is
the sum over the `i` factors from which the linear term is selected.

Formalized by `Finset.prod_C_add_X_mul_C_coeff`, a theorem declared in [MathlibExt/RingTheory/Polynomial/AffineProduct.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Polynomial/AffineProduct.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#prod-c-add-x-mul-c-coeff).

## Degree bound for a product of affine linear polynomials

A product of affine linear polynomials has degree at most the number of
factors.

Formalized by `Finset.prod_C_add_X_mul_C_natDegree_le`, a theorem declared in [MathlibExt/RingTheory/Polynomial/AffineProduct.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Polynomial/AffineProduct.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#prod-c-add-x-mul-c-nat-degree-le).

## Binomial bound on coefficients of a product of affine polynomials

If every constant and linear coefficient is at most one in absolute value,
then the absolute value of coefficient `i` is at most `S.card.choose i`.

Formalized by `Finset.abs_prod_C_add_X_mul_C_coeff_le_choose`, a theorem declared in [MathlibExt/RingTheory/Polynomial/AffineProduct.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Polynomial/AffineProduct.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html#abs-prod-c-add-x-mul-c-coeff-le-choose).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coefficients of products with linear factors](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/coefficients-of-products-with-linear-factors)
