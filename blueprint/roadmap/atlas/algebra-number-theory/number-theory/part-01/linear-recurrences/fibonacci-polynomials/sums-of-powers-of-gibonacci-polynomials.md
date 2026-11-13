---
declaration: section
origin: cited
lean: MetaMathlibExt.gibonacciPoly_mul_sub_sq, MetaMathlibExt.tsum_inv_pow_gibonacciPoly_sub_odd, MetaMathlibExt.tsum_inv_pow_gibonacciPoly_sub_even, MetaMathlibExt.tsum_inv_pow_gibonacciPoly_succ_sub_odd, MetaMathlibExt.tsum_inv_pow_gibonacciPoly_succ_sub_even, MetaMathlibExt.fibPoly_pow_even_sub, MetaMathlibExt.lucasPoly_pow_even_sub, MetaMathlibExt.fibPoly_pow_odd_sub
statement: formalized
---

# Sums of powers of gibonacci polynomials

29 results, 29 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html).

## Catalan-type identities for Fibonacci and Lucas polynomials

Let $f_i$ and $\ell_i$ be
the Fibonacci and Lucas polynomials in $\mathbb{Z}[x]$, defined by $f_0 = 0$, $f_1 = 1$,
$\ell_0 = 2$, $\ell_1 = x$ and $g_{i+2} = x g_{i+1} + g_i$ for $g = f, \ell$. For all natural
numbers $k \le n$,

$$
f_{n+k} f_{n-k} - f_n^2 = (-1)^{n+k+1} f_k^2
\quad\text{and}\quad
\ell_{n+k} \ell_{n-k} - \ell_n^2 = (-1)^{n+k} (x^2 + 4) f_k^2
$$

in $\mathbb{Z}[x]$.

The source quotes this lemma from Koshy.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.gibonacciPoly_mul_sub_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#gibonacci-poly-mul-sub-sq).

## Telescoping inverse-power series of gibonacci polynomials at odd indices, odd shift

Let $x > 0$ be real, and let $g_n$ denote either the Fibonacci polynomials, given by $g_0 = 0$ and
$g_1 = 1$, or the Lucas polynomials, given by $g_0 = 2$ and $g_1 = x$, both satisfying
$g_{n+2} = x g_{n+1} + g_n$ and evaluated at $x$. Let $k$ be an odd natural number and
$\lambda$ a positive integer. Then

$$\sum_{n=0}^{\infty} \left(\frac{1}{g_{2n+1}^{\lambda}} - \frac{1}{g_{2n+1+2k}^{\lambda}}\right) =
\sum_{r=1}^{k} \frac{1}{g_{2r-1}^{\lambda}}.$$

The source quotes this lemma from Koshy as the sum over $n \ge (k + 1)/2$ of
$1/g_{2n-k}^{\lambda} - 1/g_{2n+k}^{\lambda}$; here the summation index is shifted to start at $0$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.tsum_inv_pow_gibonacciPoly_sub_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-inv-pow-gibonacci-poly-sub-odd).

## Telescoping inverse-power series of gibonacci polynomials at even indices, even shift

Let $x > 0$ be real, and let $g_n$ denote either the Fibonacci polynomials, given by $g_0 = 0$ and
$g_1 = 1$, or the Lucas polynomials, given by $g_0 = 2$ and $g_1 = x$, both satisfying
$g_{n+2} = x g_{n+1} + g_n$ and evaluated at $x$. Let $k$ be an even natural number and
$\lambda$ a positive integer. Then

$$\sum_{n=0}^{\infty} \left(\frac{1}{g_{2n+2}^{\lambda}} - \frac{1}{g_{2n+2+2k}^{\lambda}}\right) =
\sum_{r=1}^{k} \frac{1}{g_{2r}^{\lambda}}.$$

The source quotes this lemma from Koshy as the sum over $n \ge k/2 + 1$ of
$1/g_{2n-k}^{\lambda} - 1/g_{2n+k}^{\lambda}$; here the summation index is shifted to start at $0$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 2.3.

Stated but not proved: `MetaMathlibExt.tsum_inv_pow_gibonacciPoly_sub_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-inv-pow-gibonacci-poly-sub-even).

## Telescoping inverse-power series of gibonacci polynomials at even indices, odd shift

Let $x > 0$ be real, and let $g_n$ denote either the Fibonacci polynomials, given by $g_0 = 0$ and
$g_1 = 1$, or the Lucas polynomials, given by $g_0 = 2$ and $g_1 = x$, both satisfying
$g_{n+2} = x g_{n+1} + g_n$ and evaluated at $x$. Let $k$ be an odd natural number and
$\lambda$ a positive integer. Then

$$\sum_{n=0}^{\infty} \left(\frac{1}{g_{2n+2}^{\lambda}} - \frac{1}{g_{2n+2+2k}^{\lambda}}\right) =
\sum_{r=1}^{k} \frac{1}{g_{2r}^{\lambda}}.$$

The source quotes this lemma from Koshy as the sum over $n \ge (k + 1)/2$ of
$1/g_{2n+1-k}^{\lambda} - 1/g_{2n+1+k}^{\lambda}$; here the summation index is shifted to start
at $0$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 2.4.

Stated but not proved: `MetaMathlibExt.tsum_inv_pow_gibonacciPoly_succ_sub_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-inv-pow-gibonacci-poly-succ-sub-odd).

## Telescoping inverse-power series of gibonacci polynomials at odd indices, even shift

Let $x > 0$ be real, and let $g_n$ denote either the Fibonacci polynomials, given by $g_0 = 0$ and
$g_1 = 1$, or the Lucas polynomials, given by $g_0 = 2$ and $g_1 = x$, both satisfying
$g_{n+2} = x g_{n+1} + g_n$ and evaluated at $x$. Let $k$ be an even natural number and
$\lambda$ a positive integer. Then

$$\sum_{n=0}^{\infty} \left(\frac{1}{g_{2n+1}^{\lambda}} - \frac{1}{g_{2n+1+2k}^{\lambda}}\right) =
\sum_{r=1}^{k} \frac{1}{g_{2r-1}^{\lambda}}.$$

The source quotes this lemma from Koshy as the sum over $n \ge k/2$ of
$1/g_{2n+1-k}^{\lambda} - 1/g_{2n+1+k}^{\lambda}$; here the summation index is shifted to start
at $0$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 2.5.

Stated but not proved: `MetaMathlibExt.tsum_inv_pow_gibonacciPoly_succ_sub_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-inv-pow-gibonacci-poly-succ-sub-eve).

## Even powers of Fibonacci polynomials at $n \pm k$

Let $f_i \in \mathbb{Z}[x]$ be the
Fibonacci polynomials, defined by $f_0 = 0$, $f_1 = 1$ and $f_{i+2} = x f_{i+1} + f_i$. For all
natural numbers $k \le n$ and every natural number $m$,

$$
(x^2 + 4)^{m-1} \bigl(f_{n+k}^{2m} - f_{n-k}^{2m}\bigr) =
\sum_{j=0}^{m-1} \binom{2m}{j} (-1)^{(n+k+1)j} f_{2k(m-j)} f_{2n(m-j)}
$$

in $\mathbb{Z}[x]$, where for $m = 0$ the exponent $m - 1$ is read as $0$ (both sides are then
$0$).

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 3.1.

Stated but not proved: `MetaMathlibExt.fibPoly_pow_even_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#fib-poly-pow-even-sub).

## Even powers of Lucas polynomials at $n \pm k$

Let $f_i$ and $\ell_i$ be the
Fibonacci and Lucas polynomials in $\mathbb{Z}[x]$, defined by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$,
$\ell_1 = x$ and $g_{i+2} = x g_{i+1} + g_i$ for $g = f, \ell$. For all natural numbers
$k \le n$ and every natural number $m$,

$$
\ell_{n+k}^{2m} - \ell_{n-k}^{2m} =
(x^2 + 4) \sum_{j=0}^{m-1} \binom{2m}{j} (-1)^{(n+k)j} f_{2k(m-j)} f_{2n(m-j)}
$$

in $\mathbb{Z}[x]$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 3.2.

Stated but not proved: `MetaMathlibExt.lucasPoly_pow_even_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#lucas-poly-pow-even-sub).

## Odd powers of Fibonacci polynomials at $n \pm k$

Let $f_i$ and $\ell_i$ be the
Fibonacci and Lucas polynomials in $\mathbb{Z}[x]$, defined by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$,
$\ell_1 = x$ and $g_{i+2} = x g_{i+1} + g_i$ for $g = f, \ell$. Let $k \le n$ and $m$ be natural
numbers. In $\mathbb{Z}[x]$, if $k$ is odd then

$$
(x^2 + 4)^m \bigl(f_{n+k}^{2m+1} - f_{n-k}^{2m+1}\bigr) =
\sum_{j=0}^{m} \binom{2m+1}{j} (-1)^{nj} f_{n(2m+1-2j)} \ell_{k(2m+1-2j)},
$$

and if $k$ is even then

$$
(x^2 + 4)^m \bigl(f_{n+k}^{2m+1} - f_{n-k}^{2m+1}\bigr) =
\sum_{j=0}^{m} \binom{2m+1}{j} (-1)^{(n+1)j} \ell_{n(2m+1-2j)} f_{k(2m+1-2j)}.
$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 4.1.

Stated but not proved: `MetaMathlibExt.fibPoly_pow_odd_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#fib-poly-pow-odd-sub).

## Odd powers of Lucas polynomials at $n \pm k$

Let $f_i$ and $\ell_i$ be the
Fibonacci and Lucas polynomials in $\mathbb{Z}[x]$, defined by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$,
$\ell_1 = x$ and $g_{i+2} = x g_{i+1} + g_i$ for $g = f, \ell$. Let $k \le n$ and $m$ be natural
numbers. In $\mathbb{Z}[x]$, if $k$ is odd then

$$
\ell_{n+k}^{2m+1} - \ell_{n-k}^{2m+1} =
\sum_{j=0}^{m} \binom{2m+1}{j} (-1)^{(n+1)j} \ell_{n(2m+1-2j)} \ell_{k(2m+1-2j)},
$$

and if $k$ is even then

$$
\ell_{n+k}^{2m+1} - \ell_{n-k}^{2m+1} =
(x^2 + 4) \sum_{j=0}^{m} \binom{2m+1}{j} (-1)^{nj} f_{n(2m+1-2j)} f_{k(2m+1-2j)}.
$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Lemma 4.2.

Stated but not proved: `MetaMathlibExt.lucasPoly_pow_odd_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#lucas-poly-pow-odd-sub).

## Cubic-denominator series for even-index Fibonacci polynomials

Let $f_i$ and $\ell_i$ be the
Fibonacci and Lucas polynomials, defined by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$, $\ell_1 = x$ and
$g_{i+2} = x g_{i+1} + g_i$ for $g = f, \ell$. For every real $x > 0$,

$$
\sum_{n \ge 1} \frac{(x^3 + 3x) f_{6n}(x) + 3x f_{2n}(x)}{(f_{2n}(x)^2 + 1)^3} = x^2 + 4
$$

and

$$
\sum_{n \ge 2} \frac{x(x^4 + 4x^2 + 3) \ell_{6n}(x) - 3x \ell_{2n}(x)}{(f_{2n}(x)^2 - x^2)^3} =
\frac{(x^2 + 4)\bigl((x^2 + 2)^3 + 1\bigr)}{x^3 (x^2 + 2)^3}.
$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Corollary 4.3.

Stated but not proved: `MetaMathlibExt.tsum_fibPoly_cube_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-poly-cube-even-index).

## Cubic series over even-indexed Lucas polynomials

Let $x > 0$ be real, and let $f_n$ and
$\ell_n$ denote the Fibonacci and Lucas polynomials evaluated at $x$, given by $f_0 = 0$,
$f_1 = 1$, $\ell_0 = 2$, $\ell_1 = x$ and the recurrence $z_{n+2} = x z_{n+1} + z_n$ for both. Then

$$\sum_{n=1}^{\infty} \frac{(x^3 + 3x) \ell_{6n} - 3x \ell_{2n}}
{\left(\ell_{2n}^2 - (x^2 + 4)\right)^3} = \frac{1}{x^3}$$

and

$$\sum_{n=2}^{\infty} \frac{x(x^4 + 4x^2 + 3) f_{6n} + 3x f_{2n}}
{\left(\ell_{2n}^2 + (x^2 + 4) x^2\right)^3} =
\frac{1}{x^2 + 4} \left(\frac{1}{(x^2 + 2)^3} + \frac{1}{(x^4 + 4x^2 + 2)^3}\right).$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Corollary 4.5.

Stated but not proved: `MetaMathlibExt.tsum_lucasPoly_cube_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-lucas-poly-cube-even-index).

## Cubic-denominator series for odd-index Fibonacci polynomials

Let $f_i$ and $\ell_i$ be the
Fibonacci and Lucas polynomials, defined by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$, $\ell_1 = x$ and
$g_{i+2} = x g_{i+1} + g_i$ for $g = f, \ell$. For every real $x > 0$,

$$
\sum_{n \ge 1} \frac{(x^3 + 3x) f_{6n+3}(x) - 3x f_{2n+1}(x)}{(f_{2n+1}(x)^2 - 1)^3} =
\frac{x^2 + 4}{x^3}
$$

and

$$
\sum_{n \ge 1} \frac{x(x^4 + 4x^2 + 3) \ell_{6n+3}(x) + 3x \ell_{2n+1}(x)}
{(f_{2n+1}(x)^2 + x^2)^3} =
\frac{(x^2 + 4)\bigl((x^2 + 1)^3 + 1\bigr)}{(x^2 + 1)^3}.
$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Corollary 4.7.

Stated but not proved: `MetaMathlibExt.tsum_fibPoly_cube_odd_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-poly-cube-odd-index).

## Cubic sums with odd-index Lucas polynomial denominators

Let $f_n$ and $\ell_n$ denote the
Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$, $\ell_1 = x$ and
$g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, \ell\}$, evaluated at a real number $x > 0$. Then

$$\sum_{n \ge 1} \frac{(x^3 + 3x) \ell_{6n+3} + 3x \ell_{2n+1}}{(\ell_{2n+1}^2 + x^2 + 4)^3}
= \frac{1}{(x^2 + 2)^3}$$

and

$$\sum_{n \ge 1} \frac{x (x^4 + 4x^2 + 3) f_{6n+3} - 3x f_{2n+1}}{(\ell_{2n+1}^2 - x^2 (x^2 + 4))^3}
= \frac{(x^2 + 3)^3 + 1}{x^3 (x^2 + 4) (x^2 + 3)^3}.$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Corollary 4.9.

Stated but not proved: `MetaMathlibExt.tsum_lucasPoly_cube_odd_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-lucas-poly-cube-odd-index).

## Cubic-denominator series for even-index Fibonacci numbers

Let $F_n$ be the Fibonacci
numbers ($F_0 = 0$, $F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$) and $L_n$ the Lucas numbers. Then, as
series of real numbers,

$$
\sum_{n \ge 1} \frac{4F_{6n} + 3F_{2n}}{(F_{2n}^2 + 1)^3} = 5
\quad\text{and}\quad
\sum_{n \ge 2} \frac{8L_{6n} - 3L_{2n}}{(F_{2n}^2 - 1)^3} = \frac{140}{27}.
$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Corollary 4.4.

Stated but not proved: `MetaMathlibExt.tsum_fib_cube_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-cube-even-index).

## Cubic series over even-indexed Lucas numbers

Let $F_n$ and $L_n$ denote the Fibonacci and
Lucas numbers, given by $F_0 = 0$, $F_1 = 1$, $L_0 = 2$, $L_1 = 1$ and the recurrence
$z_{n+2} = z_{n+1} + z_n$ for both. Then

$$\sum_{n=1}^{\infty} \frac{4L_{6n} - 3L_{2n}}{(L_{2n}^2 - 5)^3} = 1$$

and

$$\sum_{n=2}^{\infty} \frac{8F_{6n} + 3F_{2n}}{(L_{2n}^2 + 5)^3} = \frac{74}{9261}.$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Corollary 4.6.

Stated but not proved: `MetaMathlibExt.tsum_lucas_cube_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-lucas-cube-even-index).

## Cubic-denominator series for odd-index Fibonacci numbers

Let $F_n$ be the Fibonacci
numbers ($F_0 = 0$, $F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$) and $L_n$ the Lucas numbers. Then, as
series of real numbers,

$$
\sum_{n \ge 1} \frac{4F_{6n+3} - 3F_{2n+1}}{(F_{2n+1}^2 - 1)^3} = 5
\quad\text{and}\quad
\sum_{n \ge 1} \frac{8L_{6n+3} + 3L_{2n+1}}{(F_{2n+1}^2 + 1)^3} = \frac{45}{8}.
$$

These are the case $x = 1$ of Corollary 4.7. The extracted record of the source prints the lower
limit of the second series as $n = 2$; with that limit the sum would be
$45/8 - 124/25 = 133/200$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Corollary 4.8.

Stated but not proved: `MetaMathlibExt.tsum_fib_cube_odd_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-cube-odd-index).

## Cubic series over odd-indexed Lucas numbers

Let $F_n$ and $L_n$ denote the Fibonacci and
Lucas numbers, given by $F_0 = 0$, $F_1 = 1$, $L_0 = 2$, $L_1 = 1$ and the recurrence
$z_{n+2} = z_{n+1} + z_n$ for both. Then

$$\sum_{n=1}^{\infty} \frac{4L_{6n+3} + 3L_{2n+1}}{(L_{2n+1}^2 + 5)^3} = \frac{1}{27}$$

and

$$\sum_{n=1}^{\infty} \frac{8F_{6n+3} - 3F_{2n+1}}{(L_{2n+1}^2 - 5)^3} = \frac{13}{64}.$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Corollary 4.10.

Stated but not proved: `MetaMathlibExt.tsum_lucas_cube_odd_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-lucas-cube-odd-index).

## Series of even powers of Fibonacci polynomials at even indices

Let $f_i$ be the
Fibonacci polynomials, defined by $f_0 = 0$, $f_1 = 1$ and $f_{i+2} = x f_{i+1} + f_i$. Let
$x > 0$ be real and let $k$ and $m$ be positive integers. If $k$ is odd, put $L = (k + 1)/2$ and
$s_r = 2r - 1$; if $k$ is even, put $L = k/2 + 1$ and $s_r = 2r$. Then

$$
\sum_{n \ge L} \frac{\sum_{j=0}^{m-1} \binom{2m}{j} (-1)^{(k+1)j} f_{2k(m-j)}(x)
f_{4n(m-j)}(x)}{\bigl(f_{2n}(x)^2 - (-1)^k f_k(x)^2\bigr)^{2m}} =
(x^2 + 4)^{m-1} \sum_{r=1}^{k} \frac{1}{f_{s_r}(x)^{2m}}.
$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.tsum_fibPoly_even_pow_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-poly-even-pow-even-index).

## Even-power sums with even-index Lucas polynomial denominators

Let $f_n$ and $\ell_n$
denote the Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$,
$\ell_1 = x$ and $g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, \ell\}$, evaluated at a real number
$x > 0$, and let $k$ and $m$ be positive integers. Put $L = (k + 1)/2$ and $s_r = 2r - 1$ if $k$
is odd, and $L = k/2 + 1$ and $s_r = 2r$ if $k$ is even. Then

$$\sum_{n \ge L} \frac{\sum_{j=0}^{m-1} \binom{2m}{j} (-1)^{kj} f_{2k(m-j)} f_{4n(m-j)}}
{\left(\ell_{2n}^2 + (-1)^k (x^2 + 4) f_k^2\right)^{2m}}
= \frac{1}{x^2 + 4} \sum_{r=1}^{k} \frac{1}{\ell_{s_r}^{2m}}.$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Theorem 1.2.

Stated but not proved: `MetaMathlibExt.tsum_lucasPoly_even_pow_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-lucas-poly-even-pow-even-index).

## Even-power series over odd-indexed Fibonacci polynomials

Let $x > 0$ be real, let $f_n$
denote the Fibonacci polynomials evaluated at $x$, given by $f_0 = 0$, $f_1 = 1$ and
$f_{n+2} = x f_{n+1} + f_n$, and let $k$ and $m$ be positive integers. Put $M = (k + 1)/2$ and
$t_r = 2r$ if $k$ is odd, and $M = k/2$ and $t_r = 2r - 1$ if $k$ is even. Then

$$\sum_{n=0}^{\infty} \frac{\sum_{j=0}^{m-1} \binom{2m}{j} (-1)^{kj} f_{2k(m-j)}
f_{(4(n+M)+2)(m-j)}}{\left(f_{2(n+M)+1}^2 + (-1)^k f_k^2\right)^{2m}} =
(x^2 + 4)^{m-1} \sum_{r=1}^{k} \frac{1}{f_{t_r}^{2m}}.$$

This is the source's sum over $n \ge M$ with the summation index shifted to start at $0$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Theorem 1.3.

Stated but not proved: `MetaMathlibExt.tsum_fibPoly_even_pow_odd_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-poly-even-pow-odd-index).

## Even-power sums with odd-index Lucas polynomial denominators

Let $f_n$ and $\ell_n$
denote the Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$,
$\ell_1 = x$ and $g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, \ell\}$, evaluated at a real number
$x > 0$, and let $k$ and $m$ be positive integers. Put $M = (k + 1)/2$ and $t_r = 2r$ if $k$ is
odd, and $M = k/2$ and $t_r = 2r - 1$ if $k$ is even. Then

$$\sum_{n \ge M} \frac{\sum_{j=0}^{m-1} \binom{2m}{j} (-1)^{(k+1)j} f_{2k(m-j)} f_{(4n+2)(m-j)}}
{\left(\ell_{2n+1}^2 - (-1)^k (x^2 + 4) f_k^2\right)^{2m}}
= \frac{1}{x^2 + 4} \sum_{r=1}^{k} \frac{1}{\ell_{t_r}^{2m}}.$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Theorem 1.4.

Stated but not proved: `MetaMathlibExt.tsum_lucasPoly_even_pow_odd_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-lucas-poly-even-pow-odd-index).

## Odd-power series over even-indexed Fibonacci polynomials

Let $x > 0$ be real, let $f_n$
and $\ell_n$ denote the Fibonacci and Lucas polynomials evaluated at $x$, given by $f_0 = 0$,
$f_1 = 1$, $\ell_0 = 2$, $\ell_1 = x$ and the recurrence $z_{n+2} = x z_{n+1} + z_n$ for both, and
let $k$ be a positive integer and $m$ a natural number. Put $L = (k + 1)/2$ if $k$ is odd and
$L = k/2 + 1$ if $k$ is even. If $k$ is odd, then

$$\sum_{n=0}^{\infty} \frac{\sum_{j=0}^{m} \binom{2m+1}{j} f_{2(n+L)(2m+1-2j)}
\ell_{k(2m+1-2j)}}{\left(f_{2(n+L)}^2 + f_k^2\right)^{2m+1}} =
(x^2 + 4)^m \sum_{r=1}^{k} \frac{1}{f_{2r-1}^{2m+1}},$$

and if $k$ is even, then

$$\sum_{n=0}^{\infty} \frac{\sum_{j=0}^{m} \binom{2m+1}{j} (-1)^j \ell_{2(n+L)(2m+1-2j)}
f_{k(2m+1-2j)}}{\left(f_{2(n+L)}^2 - f_k^2\right)^{2m+1}} =
(x^2 + 4)^m \sum_{r=1}^{k} \frac{1}{f_{2r}^{2m+1}}.$$

These are the source's sums over $n \ge L$ with the summation index shifted to start at $0$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Theorem 1.5.

Stated but not proved: `MetaMathlibExt.tsum_fibPoly_odd_pow_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-poly-odd-pow-even-index).

## Odd-power sums with even-index Lucas polynomial denominators

Let $f_n$ and $\ell_n$
denote the Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$,
$\ell_1 = x$ and $g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, \ell\}$, evaluated at a real number
$x > 0$, let $k$ be a positive integer and $m$ a natural number, and put $L = (k + 1)/2$ if $k$ is
odd and $L = k/2 + 1$ if $k$ is even. If $k$ is odd, then

$$\sum_{n \ge L} \frac{\sum_{j=0}^{m} (-1)^j \binom{2m+1}{j} \ell_{2n(2m+1-2j)} \ell_{k(2m+1-2j)}}
{\left(\ell_{2n}^2 - (x^2 + 4) f_k^2\right)^{2m+1}}
= \sum_{r=1}^{k} \frac{1}{\ell_{2r-1}^{2m+1}},$$

and if $k$ is even, then

$$\sum_{n \ge L} \frac{\sum_{j=0}^{m} \binom{2m+1}{j} f_{2n(2m+1-2j)} f_{k(2m+1-2j)}}
{\left(\ell_{2n}^2 + (x^2 + 4) f_k^2\right)^{2m+1}}
= \frac{1}{x^2 + 4} \sum_{r=1}^{k} \frac{1}{\ell_{2r}^{2m+1}}.$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Theorem 1.6.

Stated but not proved: `MetaMathlibExt.tsum_lucasPoly_odd_pow_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-lucas-poly-odd-pow-even-index).

## Odd-power series over odd-indexed Fibonacci polynomials

Let $x > 0$ be real, let $f_n$
and $\ell_n$ denote the Fibonacci and Lucas polynomials evaluated at $x$, given by $f_0 = 0$,
$f_1 = 1$, $\ell_0 = 2$, $\ell_1 = x$ and the recurrence $z_{n+2} = x z_{n+1} + z_n$ for both, and
let $k$ be a positive integer and $m$ a natural number. Put $M = (k + 1)/2$ if $k$ is odd and
$M = k/2$ if $k$ is even. If $k$ is odd, then

$$\sum_{n=0}^{\infty} \frac{\sum_{j=0}^{m} \binom{2m+1}{j} (-1)^j f_{(2(n+M)+1)(2m+1-2j)}
\ell_{k(2m+1-2j)}}{\left(f_{2(n+M)+1}^2 - f_k^2\right)^{2m+1}} =
(x^2 + 4)^m \sum_{r=1}^{k} \frac{1}{f_{2r}^{2m+1}},$$

and if $k$ is even, then

$$\sum_{n=0}^{\infty} \frac{\sum_{j=0}^{m} \binom{2m+1}{j} \ell_{(2(n+M)+1)(2m+1-2j)}
f_{k(2m+1-2j)}}{\left(f_{2(n+M)+1}^2 + f_k^2\right)^{2m+1}} =
(x^2 + 4)^m \sum_{r=1}^{k} \frac{1}{f_{2r-1}^{2m+1}}.$$

These are the source's sums over $n \ge M$ with the summation index shifted to start at $0$.

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Theorem 1.7.

Stated but not proved: `MetaMathlibExt.tsum_fibPoly_odd_pow_odd_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-poly-odd-pow-odd-index).

## Odd-power sums with odd-index Lucas polynomial denominators

Let $f_n$ and $\ell_n$
denote the Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $\ell_0 = 2$,
$\ell_1 = x$ and $g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, \ell\}$, evaluated at a real number
$x > 0$, let $k$ be a positive integer and $m$ a natural number, and put $M = (k + 1)/2$ if $k$ is
odd and $M = k/2$ if $k$ is even. If $k$ is odd, then

$$\sum_{n \ge M} \frac{\sum_{j=0}^{m} \binom{2m+1}{j} \ell_{(2n+1)(2m+1-2j)} \ell_{k(2m+1-2j)}}
{\left(\ell_{2n+1}^2 + (x^2 + 4) f_k^2\right)^{2m+1}}
= \sum_{r=1}^{k} \frac{1}{\ell_{2r}^{2m+1}},$$

and if $k$ is even, then

$$\sum_{n \ge M} \frac{\sum_{j=0}^{m} (-1)^j \binom{2m+1}{j} f_{(2n+1)(2m+1-2j)} f_{k(2m+1-2j)}}
{\left(\ell_{2n+1}^2 - (x^2 + 4) f_k^2\right)^{2m+1}}
= \frac{1}{x^2 + 4} \sum_{r=1}^{k} \frac{1}{\ell_{2r-1}^{2m+1}}.$$

## Sources

- Yinqi Lin and Bo Zhou, *Infinite Sums Involving Powers of Gibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article linzhou02172024, Theorem 1.8.

Stated but not proved: `MetaMathlibExt.tsum_lucasPoly_odd_pow_odd_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialPowerSumsWanted.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-lucas-poly-odd-pow-odd-index).

## Telescoping sum of powers of gibonacci polynomial ratios

Let $f_n$ and $l_n$ denote the
Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $l_0 = 2$, $l_1 = x$ and
$g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, l\}$, evaluated at a real number $x > 0$, and let
$\alpha = (x + \sqrt{x^2 + 4})/2$. Then for $g \in \{f, l\}$, every positive integer $k$ and all
natural numbers $r$ and $\lambda$,

$$\sum_{n \ge 0} \left(\frac{g_{(2n+1)k+r}^\lambda}{g_{(2n+1)k}^\lambda} -
\frac{g_{(2n+3)k+r}^\lambda}{g_{(2n+3)k}^\lambda}\right)
= \frac{g_{k+r}^\lambda}{g_k^\lambda} - \alpha^{r\lambda}.$$

## Sources

- Thomas Koshy, *More Sums Involving Gibonacci Polynomial Squares Revisited*, The Fibonacci Quarterly 62 (2024), Article koshy07202023, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.tsum_gibonacciPoly_pow_ratio_telescope` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialSquareSumsRevisitedWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialSquareSumsRevisitedWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-gibonacci-poly-pow-ratio-telescope).

## Telescoping sum of powers of inverse gibonacci polynomial ratios

Let $f_n$ and $l_n$
denote the Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $l_0 = 2$, $l_1 = x$
and $g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, l\}$, evaluated at a real number $x > 0$, and
let $\beta = (x - \sqrt{x^2 + 4})/2$. Then for $g \in \{f, l\}$, every positive integer $k$ and
all natural numbers $r$ and $\lambda$,

$$\sum_{n \ge 0} \left(\frac{g_{(2n+1)k}^\lambda}{g_{(2n+1)k+r}^\lambda} -
\frac{g_{(2n+3)k}^\lambda}{g_{(2n+3)k+r}^\lambda}\right)
= \frac{g_k^\lambda}{g_{k+r}^\lambda} - (-\beta)^{r\lambda}.$$

## Sources

- Thomas Koshy, *More Sums Involving Gibonacci Polynomial Squares Revisited*, The Fibonacci Quarterly 62 (2024), Article koshy07202023, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.tsum_gibonacciPoly_pow_inv_ratio_telescope` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialSquareSumsRevisitedWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialSquareSumsRevisitedWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-gibonacci-poly-pow-inv-ratio-telesc).

## Gibonacci polynomial square sums at even multiples of the index

Let $f_n$ and $l_n$
denote the Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $l_0 = 2$, $l_1 = x$
and $g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, l\}$, evaluated at a real number $x > 0$, and
let $\alpha = (x + \sqrt{x^2 + 4})/2$. Let $g$ be $f$ with $(\mu, \nu) = (1, -1)$, or $l$ with
$(\mu, \nu) = (x^2 + 4, 1)$. Then for every positive integer $k$ and every natural number $r$,

$$\sum_{n \ge 1} \frac{(-1)^{k+1} \mu \nu f_r f_{2k}}{g_{2nk}^2 + (-1)^k \mu \nu f_k^2}
= \frac{g_{k+r}}{g_k} - \alpha^r.$$

The extracted statement of this theorem prints the numerator with $(-1)^k$ in place of
$(-1)^{k+1}$, which negates the left side and makes the identity false (for $x = 1$, $g = f$ and
$k = r = 1$ that left side is $(\sqrt{5} - 1)/2$ while the right side is $(1 - \sqrt{5})/2$); the
paper's proof and its corollaries use the sign stated here.

## Sources

- Thomas Koshy, *More Sums Involving Gibonacci Polynomial Squares Revisited*, The Fibonacci Quarterly 62 (2024), Article koshy07202023, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.tsum_fib_mul_div_gibonacciPoly_sq_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialSquareSumsRevisitedWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialSquareSumsRevisitedWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-mul-div-gibonacci-poly-sq-add).

## Gibonacci polynomial square sums at shifted even multiples of the index

Let $f_n$ and
$l_n$ denote the Fibonacci and Lucas polynomials, given by $f_0 = 0$, $f_1 = 1$, $l_0 = 2$,
$l_1 = x$ and $g_{n+2} = x g_{n+1} + g_n$ for $g \in \{f, l\}$, evaluated at a real number
$x > 0$, and let $\beta = (x - \sqrt{x^2 + 4})/2$. Let $g$ be $f$ with $(\mu, \nu) = (1, -1)$, or
$l$ with $(\mu, \nu) = (x^2 + 4, 1)$. Then for every positive integer $k$ and every natural
number $r$,

$$\sum_{n \ge 1} \frac{(-1)^k \mu \nu f_r f_{2k}}{g_{2nk+r}^2 + (-1)^{r+k} \mu \nu f_k^2}
= \frac{g_k}{g_{k+r}} - (-\beta)^r.$$

## Sources

- Thomas Koshy, *More Sums Involving Gibonacci Polynomial Squares Revisited*, The Fibonacci Quarterly 62 (2024), Article koshy07202023, Theorem 3.2.

Stated but not proved: `MetaMathlibExt.tsum_fib_mul_div_gibonacciPoly_shift_sq_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/GibonacciPolynomialSquareSumsRevisitedWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GibonacciPolynomialSquareSumsRevisitedWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html#tsum-fib-mul-div-gibonacci-poly-shift-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of powers of gibonacci polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/sums-of-powers-of-gibonacci-polynomials)
