---
declaration: section
origin: cited
lean: MetaMathlibExt.polynomialDenominator, MetaMathlibExt.coeff_den_dvd_polynomialDenominator, MetaMathlibExt.polynomialDenominator_eq_one_iff
statement: formalized
proof: formalized
---

# Denominators of rational polynomials

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/denominators-of-rational-polynomials/index.html).

## Denominator of a rational polynomial

For a polynomial $P \in \mathbb{Q}[x]$, the
denominator $\operatorname{denom}(P)$ is the least common multiple of the denominators (in lowest
terms) of the nonzero coefficients of $P$; in particular $\operatorname{denom}(0) = 1$. Thus
$\operatorname{denom}(P) = 1$ exactly when $P \in \mathbb{Z}[x]$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 2 (notation `denom`).

Formalized by `MetaMathlibExt.polynomialDenominator`, a definition declared in [MathlibExt/Algebra/Polynomial/CoefficientDenominator.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/CoefficientDenominator.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/denominators-of-rational-polynomials/index.html#polynomial-denominator).

## Coefficient denominators divide the denominator of a polynomial

For every polynomial
$P \in \mathbb{Q}[x]$ and every $i \in \mathbb{N}$, the denominator (in lowest terms) of the
coefficient of $x^i$ in $P$ divides the denominator $\operatorname{denom}(P)$ of $P$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 2 (definition of `denom`).

Formalized by `MetaMathlibExt.coeff_den_dvd_polynomialDenominator`, a theorem declared in [MathlibExt/Algebra/Polynomial/CoefficientDenominator.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/CoefficientDenominator.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/denominators-of-rational-polynomials/index.html#coeff-den-dvd-polynomial-denominator).

## Denominator one characterizes integer polynomials

For every polynomial
$P \in \mathbb{Q}[x]$, its denominator $\operatorname{denom}(P)$ equals $1$ if and only if, for
every $i \in \mathbb{N}$, the coefficient of $x^i$ in $P$ is an integer.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 1 (`denom(B_n(x)) > 1` is equivalent to `B_n(x) ∉ ℤ[x]`).

Formalized by `MetaMathlibExt.polynomialDenominator_eq_one_iff`, a theorem declared in [MathlibExt/Algebra/Polynomial/CoefficientDenominator.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/CoefficientDenominator.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/denominators-of-rational-polynomials/index.html#polynomial-denominator-eq-one-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Denominators of rational polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/denominators-of-rational-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/polynomials/denominators-of-rational-polynomials)
