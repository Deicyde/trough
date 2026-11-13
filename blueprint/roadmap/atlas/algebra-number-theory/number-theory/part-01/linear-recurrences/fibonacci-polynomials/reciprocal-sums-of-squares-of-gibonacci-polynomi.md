---
declaration: section
origin: cited
lean: MetaMathlibExt.hasSum_gibonacciPoly_pow_ratio_telescoping, MetaMathlibExt.hasSum_fibPoly_sq_family, MetaMathlibExt.hasSum_lucasPoly_sq_family, MetaMathlibExt.tsum_gibonacciPoly_sq_sub_family, MetaMathlibExt.tsum_jacobsthalPoly_sq_sub_family
statement: formalized
---

# Reciprocal sums of squares of gibonacci polynomials

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/reciprocal-sums-of-squares-of-gibonacci-polynomi/index.html).

## A telescoping series of powers of gibonacci polynomial ratios

Let $x > 0$ be real, let
$\alpha = (x + \sqrt{x^2 + 4})/2$, and let $g_n$ be either the Fibonacci polynomials $f_n(x)$,
given by $f_0 = 0$ and $f_1 = 1$, or the Lucas polynomials $l_n(x)$, given by $l_0 = 2$ and
$l_1 = x$, where both satisfy $z_{n+2} = x z_{n+1} + z_n$. Let $k$, $r$, $t$, $\lambda$ be positive
integers and $p$ a natural number with $t \le 2p$. Then the series

$$\sum_{n=1}^{\infty} \left[ \left( \frac{g_{(2pn+t-2p)k+r}}{g_{(2pn+t-2p)k}} \right)^{\lambda} -
\left( \frac{g_{(2pn+t)k+r}}{g_{(2pn+t)k}} \right)^{\lambda} \right]$$

converges unconditionally, and its sum is
$\left( g_{tk+r} / g_{tk} \right)^{\lambda} - \alpha^{\lambda r}$.

The source takes $x$ to be an integer; the statement is made for real $x > 0$, which contains the
positive integers.

## Sources

- Thomas Koshy, *Sums Involving a Family of Gibonacci Polynomial Squares: Generalizations*, The Fibonacci Quarterly 62 (2024), Article koshy11112023, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.hasSum_gibonacciPoly_pow_ratio_telescoping` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GibonacciPolynomialSquareFamilyWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GibonacciPolynomialSquareFamilyWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/reciprocal-sums-of-squares-of-gibonacci-polynomi/index.html#has-sum-gibonacci-poly-pow-ratio-telesco).

## Series over a family of Fibonacci polynomial squares

Let $x > 0$ be real, let
$\alpha = (x + \sqrt{x^2 + 4})/2$, and let $f_n = f_n(x)$ be the Fibonacci polynomials, given by
$f_0 = 0$, $f_1 = 1$ and $f_{n+2} = x f_{n+1} + f_n$, evaluated at $x$. Let $k$, $r$, $t$ be
positive integers and $p$ a natural number with $t \le 2p$. Then the series

$$\sum_{n=1}^{\infty} \frac{(-1)^{tk} f_r f_{2pk}}{f_{(2pn+t-p)k}^2 - (-1)^{tk} f_{pk}^2}$$

converges unconditionally, and its sum is $f_{tk+r} / f_{tk} - \alpha^r$.

This is the Fibonacci-polynomial case of Theorem 3.1 of the source. The source takes $x$ to be an
integer; the statement is made for real $x > 0$, which contains the positive integers.

## Sources

- Thomas Koshy, *Sums Involving a Family of Gibonacci Polynomial Squares: Generalizations*, The Fibonacci Quarterly 62 (2024), Article koshy11112023, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.hasSum_fibPoly_sq_family` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GibonacciPolynomialSquareFamilyWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GibonacciPolynomialSquareFamilyWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/reciprocal-sums-of-squares-of-gibonacci-polynomi/index.html#has-sum-fib-poly-sq-family).

## Series over a family of Lucas polynomial squares

Let $x > 0$ be real, let
$\Delta = \sqrt{x^2 + 4}$ and $\alpha = (x + \Delta)/2$, and let $f_n$ and $l_n$ be the
Fibonacci and Lucas polynomials evaluated at $x$, given by $f_0 = 0$, $f_1 = 1$, $l_0 = 2$,
$l_1 = x$ and the recurrence $z_{n+2} = x z_{n+1} + z_n$ for both. Let $k$, $r$, $t$ be positive
integers and $p$ a natural number with $t \le 2p$. Then the series

$$\sum_{n=1}^{\infty} \frac{-(-1)^{tk} \Delta^2 f_r f_{2pk}}
{l_{(2pn+t-p)k}^2 + (-1)^{tk} \Delta^2 f_{pk}^2}$$

converges unconditionally, and its sum is $l_{tk+r} / l_{tk} - \alpha^r$.

This is the Lucas-polynomial case of Theorem 3.1 of the source. The source takes $x$ to be an
integer; the statement is made for real $x > 0$, which contains the positive integers.

## Sources

- Thomas Koshy, *Sums Involving a Family of Gibonacci Polynomial Squares: Generalizations*, The Fibonacci Quarterly 62 (2024), Article koshy11112023, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.hasSum_lucasPoly_sq_family` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GibonacciPolynomialSquareFamilyWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GibonacciPolynomialSquareFamilyWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/reciprocal-sums-of-squares-of-gibonacci-polynomi/index.html#has-sum-lucas-poly-sq-family).

## Reciprocal sums of shifted squares of Fibonacci and Lucas polynomials (Koshy–Gao, Theorem 2.1)

**Reciprocal sums of shifted squares of Fibonacci and Lucas polynomials (Koshy–Gao,
Theorem 2.1).** Let $f_n(x)$ and $l_n(x)$ be the Fibonacci and Lucas polynomials, given by
$z_{n+2} = x z_{n+1} + z_n$ with initial values $f_0 = 0$, $f_1 = 1$ and $l_0 = 2$, $l_1 = x$.
Let $x > 0$ be real, let $k$, $p$, $r$, $t$ be positive integers with $t \le 2p$, and let
$\alpha = (x + \sqrt{x^2 + 4})/2$. Then

$$
\sum_{n=0}^{\infty} \frac{(-1)^{tk} f_r(x) f_{2pk}(x)}
{f_{(2pn+p+t)k}(x)^2 - (-1)^{tk} f_{pk}(x)^2} =
\frac{f_{tk+r}(x)}{f_{tk}(x)} - \alpha^r
$$

and

$$
\sum_{n=0}^{\infty} \frac{(-1)^{tk+1} (x^2 + 4) f_r(x) f_{2pk}(x)}
{l_{(2pn+p+t)k}(x)^2 + (-1)^{tk} (x^2 + 4) f_{pk}(x)^2} =
\frac{l_{tk+r}(x)}{l_{tk}(x)} - \alpha^r.
$$

In the source the sums run over $n \ge 1$, with $(2pn + t - p)k$ in place of $(2pn + p + t)k$;
here the summation index is shifted to start at $n = 0$.

## Sources

- Thomas Koshy and Zhenguang Gao, *Sums Involving a Family of Jacobsthal Polynomial Squares*, The Fibonacci Quarterly 62 (2024), Article koshy12202023, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.tsum_gibonacciPoly_sq_sub_family` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/JacobsthalPolynomialSquareFamilySumsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/JacobsthalPolynomialSquareFamilySumsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/reciprocal-sums-of-squares-of-gibonacci-polynomi/index.html#tsum-gibonacci-poly-sq-sub-family).

## Reciprocal sums of shifted squares of Jacobsthal and Jacobsthal–Lucas polynomials (Koshy–Gao, Theorem 3.1)

**Reciprocal sums of shifted squares of Jacobsthal and Jacobsthal–Lucas polynomials
(Koshy–Gao, Theorem 3.1).** Let $J_n(x)$ and $j_n(x)$ be the Jacobsthal and Jacobsthal–Lucas
polynomials, given by $z_{n+2} = z_{n+1} + x z_n$ with initial values $J_0 = 0$, $J_1 = 1$ and
$j_0 = 2$, $j_1 = 1$. Let $x > 0$ be real, let $k$, $p$, $r$, $t$ be positive integers with
$t \le 2p$, let $w = (1 + \sqrt{4x + 1})/2$, and write $e_n = (2pn + t)k$. Then

$$
\sum_{n=0}^{\infty} \frac{(-1)^{tk} x^{e_n} J_r(x) J_{2pk}(x)}
{J_{(2pn+p+t)k}(x)^2 - (-1)^{tk} x^{e_n} J_{pk}(x)^2} =
\frac{J_{tk+r}(x)}{J_{tk}(x)} - w^r
$$

and

$$
\sum_{n=0}^{\infty} \frac{(-1)^{tk+1} (4x + 1) x^{e_n} J_r(x) J_{2pk}(x)}
{j_{(2pn+p+t)k}(x)^2 + (-1)^{tk} (4x + 1) x^{e_n} J_{pk}(x)^2} =
\frac{j_{tk+r}(x)}{j_{tk}(x)} - w^r.
$$

In the source the sums run over $n \ge 1$, with $(2pn + t - p)k$ in place of $(2pn + p + t)k$
and exponent $(2pn + t - 2p)k$ in place of $e_n$; here the summation index is shifted to start
at $n = 0$.

## Sources

- Thomas Koshy and Zhenguang Gao, *Sums Involving a Family of Jacobsthal Polynomial Squares*, The Fibonacci Quarterly 62 (2024), Article koshy12202023, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.tsum_jacobsthalPoly_sq_sub_family` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/JacobsthalPolynomialSquareFamilySumsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/JacobsthalPolynomialSquareFamilySumsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/reciprocal-sums-of-squares-of-gibonacci-polynomi/index.html#tsum-jacobsthal-poly-sq-sub-family).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reciprocal sums of squares of gibonacci polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/reciprocal-sums-of-squares-of-gibonacci-polynomi/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/reciprocal-sums-of-squares-of-gibonacci-polynomi)
