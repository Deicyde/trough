---
declaration: section
origin: cited
lean: MetaMathlibExt.dirichlet_series_gcd_sum, MetaMathlibExt.gcd_sum_eq_totient_sum, MetaMathlibExt.gcdSumMean, MetaMathlibExt.gcdSumMean_one, MetaMathlibExt.gcdSumMean_two, MetaMathlibExt.gcdSumMean_eq_sum_totient_div, MetaMathlibExt.sum_gcdSumMean_sq_asymptotic, MetaMathlibExt.sum_gcdSumMean_cube_asymptotic
statement: formalized
---

# Pillai's gcd-sum function

19 results, 6 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html).

## Dirichlet series of the gcd-sum function

For $n \ge 1$ let
$g(n) = \sum_{i=1}^{n} \gcd(n, i)$. For every complex number $s$ with $\operatorname{Re} s > 2$,
the series $\sum_{n \ge 1} g(n)/n^s$ sums to $\zeta(s-1)^2/\zeta(s)$, where $\zeta$ is the
Riemann zeta function.

The function $g$ is the Dirichlet convolution of the identity function with Euler's totient
function $\varphi$, which gives the factorization $\zeta(s-1) \cdot (\zeta(s-1)/\zeta(s))$.

## Sources

- Kevin A. Broughan, "The gcd-sum function," Journal of Integer Sequences 4 (2001), Article 01.2.2, Theorem (unlabeled), equations (labels 12, 8), lines 336–349, https://cs.uwaterloo.ca/journals/JIS/VOL4/BROUGHAN/gcdsum.tex

Formalized by `MetaMathlibExt.dirichlet_series_gcd_sum`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/GcdSumDirichlet.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/GcdSumDirichlet.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#dirichlet-series-gcd-sum).

## The gcd-sum as a divisor sum of totients

For every positive integer $n$,
$\sum_{j=1}^{n} \gcd(j, n) = n \sum_{d \mid n} \varphi(d)/d$, where $\varphi$ is Euler's totient
function and $d$ runs over the positive divisors of $n$.

Grouping the terms with $\gcd(j, n) = e$, of which there are $\varphi(n/e)$, shows that the sum
equals $\sum_{e \mid n} e \, \varphi(n/e)$.

## Sources

- Kevin A. Broughan, "The Gcd-Sum Function," Journal of Integer Sequences 4 (2001), Article 01.2.2, Theorem 2.3, lines 220–226, https://cs.uwaterloo.ca/journals/JIS/VOL4/BROUGHAN/gcdsum.tex

Formalized by `MetaMathlibExt.gcd_sum_eq_totient_sum`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/GcdSumTotient.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/GcdSumTotient.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#gcd-sum-eq-totient-sum).

## The mean gcd-sum function

For a natural number $n$, let $P(n) = \sum_{j=1}^{n} \gcd(j, n)$
be Pillai's gcd-sum function. The mean gcd-sum function is the real-valued function given by
$A(n) = P(n)/n$ for $n \ge 1$ and $A(0) = 0$.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Section 1 (definition of `A(n)`).

Formalized by `MetaMathlibExt.gcdSumMean`, a definition declared in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#gcd-sum-mean).

## The mean gcd-sum function at $1$

The mean gcd-sum function $A$ satisfies $A(1) = 1$.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Section 1 (definition of `A(n)`).

Formalized by `MetaMathlibExt.gcdSumMean_one`, a theorem declared in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#gcd-sum-mean-one).

## The mean gcd-sum function at $2$

The mean gcd-sum function $A$ satisfies $A(2) = 3/2$,
since $A(2) = P(2)/2$, where $P(n) = \sum_{j=1}^{n} \gcd(j, n)$ is Pillai's gcd-sum function
and $P(2) = \gcd(1, 2) + \gcd(2, 2) = 3$.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Section 1 (definition of `A(n)`).

Formalized by `MetaMathlibExt.gcdSumMean_two`, a theorem declared in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#gcd-sum-mean-two).

## Divisor-sum formula for the mean gcd-sum function

For every natural number $n \ge 1$,
the mean gcd-sum function $A$ satisfies $A(n) = \sum_{d \mid n} \varphi(d)/d$, where $\varphi$ is
Euler's totient function and the sum runs over the positive divisors $d$ of $n$.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Section 1 (Pillai's identity).

Formalized by `MetaMathlibExt.gcdSumMean_eq_sum_totient_div`, a theorem declared in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#gcd-sum-mean-eq-sum-totient-div).

## Asymptotic formula for the second moment of the mean gcd-sum function

For $n \ge 1$ let
$A(n) = \frac{1}{n} \sum_{j=1}^{n} \gcd(j, n)$ be the mean gcd-sum function. There are a real
polynomial $P$ and a real constant $C$ such that, as $x \to \infty$,

$$\sum_{1 \le n \le x} A(n)^2 = x P(\log x) +
O\left(x^{1/2} \exp\left(C (\log \log x)^2\right)\right).$$

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Theorem 1.

Stated but not proved: `MetaMathlibExt.sum_gcdSumMean_sq_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#sum-gcd-sum-mean-sq-asymptotic).

## Asymptotic formula for the third moment of the mean gcd-sum function

For $n \ge 1$ let
$A(n) = \frac{1}{n} \sum_{j=1}^{n} \gcd(j, n)$ be the mean gcd-sum function. There are a real
polynomial $P$ and a real constant $C$ such that, as $x \to \infty$,

$$\sum_{1 \le n \le x} A(n)^3 = x P(\log x) +
O\left(x^{5/8} \exp\left(C (\log \log x)^2\right)\right).$$

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Theorem 2.

Stated but not proved: `MetaMathlibExt.sum_gcdSumMean_cube_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#sum-gcd-sum-mean-cube-asymptotic).

## Asymptotic formula for the fourth moment of the mean gcd-sum function

For $n \ge 1$ let
$A(n) = \frac{1}{n} \sum_{j=1}^{n} \gcd(j, n)$ be the mean gcd-sum function. There is a real
polynomial $P$ such that for every $\varepsilon > 0$, as $x \to \infty$,

$$\sum_{1 \le n \le x} A(n)^4 = x P(\log x) + O_\varepsilon\left(x^{157/199 + \varepsilon}\right).$$

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Theorem 3.

Stated but not proved: `MetaMathlibExt.sum_gcdSumMean_pow_four_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#sum-gcd-sum-mean-pow-four-asymptotic).

## Asymptotic formula for the higher moments of the mean gcd-sum function

For $n \ge 1$ let
$A(n) = \frac{1}{n} \sum_{j=1}^{n} \gcd(j, n)$ be the mean gcd-sum function, and let $k \ge 5$ be
an integer. There is a real polynomial $P$ such that for every $\varepsilon > 0$, as
$x \to \infty$,

$$\sum_{1 \le n \le x} A(n)^k = x P(\log x) +
O_{k,\varepsilon}\left(x^{1 + 2\varepsilon - 42/(13 \cdot 2^k - 9)}\right).$$

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Theorem 4.

Stated but not proved: `MetaMathlibExt.sum_gcdSumMean_pow_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#sum-gcd-sum-mean-pow-asymptotic).

## Factorization of the Dirichlet series of powers of the mean gcd-sum function

Let $k$ be a
natural number and let $A$ be the mean gcd-sum function. There are functions
$g, h \colon \mathbb{N} \to \mathbb{C}$ such that the Dirichlet series
$G_k(s) = \sum_{n \ge 1} g(n) n^{-s}$ converges absolutely for every complex $s$ with
$\operatorname{Re} s > 1/2$, the Dirichlet series $\tilde G_{k,2}(s) = \sum_{n \ge 1} h(n) n^{-s}$
converges absolutely for every complex $s$ with $\operatorname{Re} s > 1/3$, and for every complex
$s$ with $\operatorname{Re} s > 1$,

$$\sum_{n \ge 1} A(n)^k n^{-s} = \zeta(s)^{2^k} G_k(s)$$

and

$$G_k(s) \, \zeta(2s)^{4^k - 3^k - \binom{2^k}{2}} = \tilde G_{k,2}(s).$$

The exponent $4^k - 3^k - \binom{2^k}{2}$ is a nonnegative integer, since
$3^k + \binom{2^k}{2} \le 4^k$. The paper also gives an explicit Euler product for
$\tilde G_{k,2}$, which is not stated here.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Lemma 8.

Stated but not proved: `MetaMathlibExt.LSeries_gcdSumMean_pow_eq_riemannZeta_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#lseries-gcd-sum-mean-pow-eq-riemann-zeta).

## An alternating binomial sum vanishes

Let $k$ and $m$ be natural numbers with $k \ge 2$
and $m \ge 2^k - 1$. Then, computed in the integers,

$$\sum_{r=0}^{\min(2^k,\, m+1)} (-1)^r \binom{2^k}{r} (m + 1 - r)^k = 0.$$

Since $m + 1 \ge 2^k$, the upper limit of the sum is $2^k$.

This sum is the exponent $\ell_m$ of the paper: the coefficient of $p^{-ms}$ in
$(1 - p^{-s})^{2^k} \sum_{a \ge 0} (a + 1)^k p^{-as}$, which is why it stops at $r = m + 1$. The
paper prints the sum up to $r = 2^k$ for every $m$; that sum vanishes for every $m$, being a
$2^k$-th difference of a polynomial of degree $k$, which contradicts the paper's own
$\ell_2 = 3^k - 4^k + \binom{2^k}{2}$: for $k = m = 2$ the truncated sum is $-1$. So with the
truncation the hypothesis $m \ge 2^k - 1$ is needed. The paper's hypothesis $k \ge 2$ is kept: for
$k = 0$ the term $r = m + 1$ contributes $0^0 = 1$ rather than the coefficient of a negative
index, so the truncated sum is no longer the coefficient read off from the paper's Euler product.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Theorem 5.

Stated but not proved: `MetaMathlibExt.alternating_choose_two_pow_mul_pow_eq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#alternating-choose-two-pow-mul-pow-eq-ze).

## Dirichlet series of the square of the mean gcd-sum function

Let $A$ be the mean gcd-sum
function. There is a function $h \colon \mathbb{N} \to \mathbb{C}$ such that the Dirichlet series
$\tilde G_{2,2}(s) = \sum_{n \ge 1} h(n) n^{-s}$ converges absolutely for every complex $s$ with
$\operatorname{Re} s > 0$, and for every complex $s$ with $\operatorname{Re} s > 1$,

$$\sum_{n \ge 1} A(n)^2 n^{-s} = \frac{\zeta(s)^4}{\zeta(2s)} \, \tilde G_{2,2}(s).$$

This is the case $k = 2$ of the paper's Theorem 5, which gives the absolute convergence of
$\tilde G_{2,2}(s)$ in every half-plane $\operatorname{Re} s > 1/N$ with $N \ge 1$, that is, for
$\operatorname{Re} s > 0$.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Theorem 5.

Stated but not proved: `MetaMathlibExt.LSeries_gcdSumMean_sq_eq_riemannZeta_pow_four_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#lseries-gcd-sum-mean-sq-eq-riemann-zeta).

## Ivić's eighth-moment bound on the line $\operatorname{Re} s = 5/8$

There are real
constants $C$ and $T_0$ such that for every real $T \ge T_0$,

$$\int_{T/2}^{T} |\zeta(5/8 + it)|^8 \, dt \le C T (\log T)^{38}.$$

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Lemma 2.

Stated but not proved: `MetaMathlibExt.riemannZeta_eighth_moment_five_eighths_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#riemann-zeta-eighth-moment-five-eighths).

## Lemma 3

**Lemma 3** (quoted twelfth-moment asymptotic). For fixed `5/7 < σ < 1` and every `ε > 0`,
`∫_1^T |ζ(σ + i t)|^{12} dt = T ∑_{n ≥ 1} d_6(n)^2 n^{-2σ} + O(T^{(9 - 7σ)/4 + ε})`, where
`d_6 = ζ^{*6}` is the six-fold divisor function. The printed side condition `|t| ≥ 1` is implied
by the integration range and omitted.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Lemma 3.

Stated but not proved: `MetaMathlibExt.riemannZeta_twelfth_moment_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#riemann-zeta-twelfth-moment-asymptotic).

## A weighted fourth-moment bound for $\zeta$ on the critical line

There are real constants
$C$ and $T_0$ such that for every real $T \ge T_0$,

$$\int_{10}^{T} \frac{|\zeta(1/2 + it)|^4}{|\zeta(1 + 2it)|} \, dt \le C T (\log T)^5.$$

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Lemma 5.

Stated but not proved: `MetaMathlibExt.riemannZeta_fourth_moment_div_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#riemann-zeta-fourth-moment-div-le).

## Ramachandra–Sankaranarayanan bound for $\zeta$ at a well-chosen height

Let $\zeta$ be the
Riemann zeta function. There are real constants $C$ and $U_0$ such that for every real
$U \ge U_0$ there is a real number $T$ with $U < T < 2U$ such that for every real $\sigma \ge 1/2$,

$$
|\zeta(\sigma + iT)| \le \exp\bigl(C (\log \log U)^2\bigr) \quad \text{and} \quad
|\zeta(\sigma - iT)| \le \exp\bigl(C (\log \log U)^2\bigr).
$$

The source adds that this bound is $\ll U^{\varepsilon}$ for every $\varepsilon > 0$; that
consequence is not part of this statement.

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Lemma 7.

Stated but not proved: `MetaMathlibExt.exists_riemannZeta_norm_le_exp_loglog_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMomentsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMomentsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#exists-riemann-zeta-norm-le-exp-loglog-s).

## Mean square of the error term for gcd-sum moments under RH

Let
$A(n) = \frac{1}{n} \sum_{m=1}^{n} \gcd(m, n)$ be the mean gcd-sum function. Assume the Riemann
Hypothesis and let $k \ge 2$ be an integer. Then there is a real polynomial $P$ with the following
property. Write $E(u) = \sum_{1 \le n \le u} A(n)^k - u P(\log u)$ for real $u$. For every real
$\eta$ with $\frac{1}{2^k}\left(4^k - 3^k - \binom{2^k}{2}\right) + \frac{1}{2^{k+1}} + 1 \le \eta$
there are real constants $C$ and $T_0$ such that for all real $T \ge T_0$,

$$\int_1^T E(u)^2 \, du \le C \, T^{2 - 1/2^k} \exp\left(\frac{2 \eta \log T}{\log \log T}\right).$$

## Sources

- Isao Kiuchi and Yuki Tsuruta, *Mean Square Estimates for GCD-Sum Functions*, INTEGERS 25 (2025), Article A53, Theorem 1.

Stated but not proved: `MetaMathlibExt.gcdSumMean_pow_error_sq_integral_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMeanSquareWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMeanSquareWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#gcd-sum-mean-pow-error-sq-integral-le).

## Integral of the error term for gcd-sum moments under RH

Let
$A(n) = \frac{1}{n} \sum_{m=1}^{n} \gcd(m, n)$ be the mean gcd-sum function. Assume the Riemann
Hypothesis and let $k \ge 2$ be an integer. Then there is a real polynomial $P$ with the following
property. Write $E(u) = \sum_{1 \le n \le u} A(n)^k - u P(\log u)$ for real $u$. For every real
$\eta$ with $\frac{1}{2^k}\left(4^k - 3^k - \binom{2^k}{2}\right) + \frac{1}{2^{k+1}} + 1 \le \eta$
there are real constants $C$ and $T_0$ such that for all real $T \ge T_0$,

$$\left|\int_1^T E(u) \, du\right| \le C \, T^{3/2 - 1/2^{k+1}}
\exp\left(\frac{\eta \log T}{\log \log T}\right).$$

## Sources

- Isao Kiuchi and Yuki Tsuruta, *Mean Square Estimates for GCD-Sum Functions*, INTEGERS 25 (2025), Article A53, Corollary 1.

Stated but not proved: `MetaMathlibExt.gcdSumMean_pow_error_integral_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdSumMeanSquareWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdSumMeanSquareWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html#gcd-sum-mean-pow-error-integral-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pillai's gcd-sum function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/pillai-s-gcd-sum-function)
