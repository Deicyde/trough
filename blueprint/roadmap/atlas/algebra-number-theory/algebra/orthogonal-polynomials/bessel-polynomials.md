---
declaration: section
origin: cited
lean: MetaMathlibExt.besselPolynomial, MetaMathlibExt.besselPolynomial_eq_sum, MetaMathlibExt.besselPolynomial_zero, MetaMathlibExt.besselPolynomial_one, MetaMathlibExt.besselPolynomial_two
statement: formalized
proof: formalized
---

# Bessel polynomials

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/bessel-polynomials/index.html).

## Bessel polynomial

For a natural number $n$, the $n$-th classical Bessel polynomial
$y_n$ is the polynomial with rational coefficients
$y_n(x) = \sum_{k=0}^{n} \frac{(n+k)!}{2^k \, k! \, (n-k)!} \, x^k$.

## Sources

- Schork, lines 285-288.

Formalized by `MetaMathlibExt.besselPolynomial`, a definition declared in [MathlibExt/Algebra/Polynomial/BesselPolynomial.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BesselPolynomial.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/bessel-polynomials/index.html#bessel-polynomial).

## Explicit formula for the Bessel polynomials

For every natural number $n$, the Bessel
polynomial $y_n \in \mathbb{Q}[x]$ equals
$\sum_{k=0}^{n} \frac{(n+k)!}{2^k \, k! \, (n-k)!} \, x^k$.

This is the defining formula, so the identity holds by definition.

## Sources

- Schork, lines 285-288.

Formalized by `MetaMathlibExt.besselPolynomial_eq_sum`, a theorem declared in [MathlibExt/Algebra/Polynomial/BesselPolynomial.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BesselPolynomial.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/bessel-polynomials/index.html#bessel-polynomial-eq-sum).

## The zeroth Bessel polynomial

The Bessel polynomial $y_0$ is the constant
polynomial $1$.

## Sources

- Schork, lines 285-288.

Formalized by `MetaMathlibExt.besselPolynomial_zero`, a theorem declared in [MathlibExt/Algebra/Polynomial/BesselPolynomial.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BesselPolynomial.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/bessel-polynomials/index.html#bessel-polynomial-zero).

## The first Bessel polynomial

The Bessel polynomial $y_1$ equals $1 + x$.

## Sources

- Schork, lines 285-288.

Formalized by `MetaMathlibExt.besselPolynomial_one`, a theorem declared in [MathlibExt/Algebra/Polynomial/BesselPolynomial.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BesselPolynomial.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/bessel-polynomials/index.html#bessel-polynomial-one).

## The second Bessel polynomial

The Bessel polynomial $y_2$ equals $1 + 3x + 3x^2$.

## Sources

- Schork, lines 285-288.

Formalized by `MetaMathlibExt.besselPolynomial_two`, a theorem declared in [MathlibExt/Algebra/Polynomial/BesselPolynomial.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BesselPolynomial.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/bessel-polynomials/index.html#bessel-polynomial-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bessel polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/bessel-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/orthogonal-polynomials/bessel-polynomials)
