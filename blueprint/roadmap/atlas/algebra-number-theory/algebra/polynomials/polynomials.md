---
declaration: section
origin: cited
lean: Polynomial.symmetric_polynomial_in_esymm
statement: formalized
proof: formalized
---

# Polynomials and power series: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/index.html).

Univariate and multivariate polynomials and formal power series as algebraic objects: coefficients, derivations, symmetric polynomials, irreducibility, polynomial maps and rational series.

## Symmetric polynomials in the roots are polynomials in the coefficients

A symmetric polynomial is a polynomial in the elementary symmetric
polynomials, with a single witness `q` depending only on `f`; consequently,
for every monic split polynomial `P`, that same `q` evaluated at the signed
coefficients of `P` equals `f` evaluated at the roots of `P`. This is the
book's corollary that a symmetric polynomial in the roots of `P` can be
written as a polynomial in the coefficients of `P`; the signed coefficients
are the elementary symmetric polynomials in the roots, by Vieta's formulas.

Formalized by `Polynomial.symmetric_polynomial_in_esymm`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/SymmetricPolynomialInCoefficients.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MvPolynomial/SymmetricPolynomialInCoefficients.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/index.html#symmetric-polynomial-in-esymm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomials and power series](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials)
