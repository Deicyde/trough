---
declaration: section
origin: cited
lean: PadicPolynomialDilatation, padicPolynomialDilatation_one_zero, padicPolynomialDilatation_exists, Polynomial.padicValuation, Polynomial.padicValuation_le_coeff, Polynomial.le_padicValuation, Polynomial.padicValuation_C
statement: formalized
proof: formalized
---

# p-adic valuations of polynomials

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html).

## Dilatation of a p-adic polynomial at a point

Let $p$ be a prime, $f \in \mathbb{Z}_p[X]$
and $x_0 \in \mathbb{Z}_p$. Dilatation data for $f$ at $x_0$ consist of a natural number $e$ and a
polynomial $g \in \mathbb{Z}_p[X]$ such that $g(X) = p^{-e} f(x_0 + pX)$ as polynomials over
$\mathbb{Q}_p$, and the reduction of $g$ modulo $p$ is nonzero.

Formalized by `PadicPolynomialDilatation`, a structure declared in [MathlibExt/NumberTheory/Padics/PadicPolynomialDilatation.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Padics/PadicPolynomialDilatation.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html#padic-polynomial-dilatation).

## Dilatation of the constant polynomial one at zero

For every prime $p$, the exponent
$e = 0$ and the polynomial $g = 1$ form dilatation data for the constant polynomial
$1 \in \mathbb{Z}_p[X]$ at the point $x_0 = 0$.

Formalized by `padicPolynomialDilatation_one_zero`, a definition declared in [MathlibExt/NumberTheory/Padics/PadicPolynomialDilatation.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Padics/PadicPolynomialDilatation.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html#padic-polynomial-dilatation-one-zero).

## Existence of dilatations of p-adic polynomials

Let $p$ be a prime and let
$f \in \mathbb{Z}_p[X]$ have nonzero reduction modulo $p$. Then for every $x_0 \in \mathbb{Z}_p$
there are a natural number $e$ and a polynomial $g \in \mathbb{Z}_p[X]$ with nonzero reduction
modulo $p$ such that $g(X) = p^{-e} f(x_0 + pX)$ as polynomials over $\mathbb{Q}_p$; that is,
dilatation data for $f$ at $x_0$ exist.

Formalized by `padicPolynomialDilatation_exists`, a theorem declared in [MathlibExt/NumberTheory/Padics/PadicPolynomialDilatation.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Padics/PadicPolynomialDilatation.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html#padic-polynomial-dilatation-exists).

## The $p$-adic valuation of an integer polynomial

Let $p$ be a prime and let
$f \in \mathbb{Z}[X]$ be a nonzero polynomial, with $a_n$ the coefficient of $X^n$ in $f$. Writing
$v_p(a)$ for the $p$-adic valuation of an integer $a$, the $p$-adic valuation of $f$ is the
natural number $v_p(f) = \min \{ v_p(a_n) : a_n \neq 0 \}$.

Formalized by `Polynomial.padicValuation`, a definition declared in [MathlibExt/NumberTheory/Padics/Polynomial.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Padics/Polynomial.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html#padic-valuation).

## The valuation of a polynomial is at most that of each nonzero coefficient

Let $p$ be a
prime, write $v_p(a)$ for the $p$-adic valuation of an integer $a$, let $f \in \mathbb{Z}[X]$ be a
nonzero polynomial with $a_n$ the coefficient of $X^n$ in $f$, and let
$v_p(f) = \min \{ v_p(a_n) : a_n \neq 0 \}$ be its $p$-adic valuation. If $a_n \neq 0$, then
$v_p(f) \le v_p(a_n)$.

Formalized by `Polynomial.padicValuation_le_coeff`, a theorem declared in [MathlibExt/NumberTheory/Padics/Polynomial.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Padics/Polynomial.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html#padic-valuation-le-coeff).

## Lower bounds for the valuation of a polynomial

Let $p$ be a prime, write $v_p(a)$ for
the $p$-adic valuation of an integer $a$, let $f \in \mathbb{Z}[X]$ be a nonzero polynomial with
$a_n$ the coefficient of $X^n$ in $f$, and let $v_p(f) = \min \{ v_p(a_n) : a_n \neq 0 \}$ be its
$p$-adic valuation. If $k$ is a natural number with $k \le v_p(a_n)$ for every $n$ with
$a_n \neq 0$, then $k \le v_p(f)$.

Formalized by `Polynomial.le_padicValuation`, a theorem declared in [MathlibExt/NumberTheory/Padics/Polynomial.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Padics/Polynomial.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html#le-padic-valuation).

## The valuation of a nonzero constant polynomial

Let $p$ be a prime and let $a$ be a
nonzero integer. The $p$-adic valuation of the constant polynomial $a \in \mathbb{Z}[X]$, the
minimum of the $p$-adic valuations of its nonzero coefficients, equals the $p$-adic valuation
$v_p(a)$ of the integer $a$.

Formalized by `Polynomial.padicValuation_C`, a theorem declared in [MathlibExt/NumberTheory/Padics/Polynomial.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Padics/Polynomial.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html#padic-valuation-c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: p-adic valuations of polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/p-adic-numbers/p-adic-valuations-of-polynomials)
