---
declaration: section
origin: cited
lean: MetaMathlibExt.trinomialNegPowSeries, MetaMathlibExt.constantCoeff_trinomialNegPowSeries, MetaMathlibExt.trinomialNegPowSeries_neg_one, MetaMathlibExt.kampeDeFerietHermite, MetaMathlibExt.kampeDeFerietHermite_zero, MetaMathlibExt.kampeDeFerietHermite_two_two, MetaMathlibExt.coeff_hermiteShift_mul_trinomialNegPowSeries, MetaMathlibExt.coeff_nietoHermiteSeries_mul_trinomialNegPowSeries
statement: formalized
---

# Catalan-type polynomials

11 results, 6 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html).

## Negative real power of a trinomial as a power series

For real numbers $\lambda$, $c$,
$\alpha$, $\beta$ and a natural number $m$, this is the formal power series in $t$ with real
coefficients

$$c^{-\lambda} \sum_{n \ge 0} \binom{-\lambda}{n} u^n, \qquad u = \frac{-\alpha t + \beta t^m}{c},$$

that is, the real power $c^{-\lambda}$ times the binomial series
$(1 + t)^{-\lambda} = \sum_{n \ge 0} \binom{-\lambda}{n} t^n$ with $u$ substituted for $t$ (for
$c = 0$ the division is read as $0$, so $u = 0$). The substitution is meaningful when $u$ has
zero constant term, which holds for $m \ge 1$; for $c > 0$ and $m \ge 1$ the series is the
expansion of $(c - \alpha t + \beta t^m)^{-\lambda}$ in powers of $t$.

For $c > 0$ and $m \ge 1$ this is the denominator factor of every generating function in Pathan
and Usman's paper; Section 2 takes $c = 1$, $\alpha = m$ and $\beta = x$.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Equations (6), (12) and (15).

Formalized by `MetaMathlibExt.trinomialNegPowSeries`, a definition declared in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#trinomial-neg-pow-series).

## Constant term of the trinomial series

For all real numbers $\lambda, c, \alpha, \beta$
and every natural number $m \ne 0$, the negative real power of the trinomial
$c - \alpha t + \beta t^m$ with exponent $\lambda$ as a power series in $t$, that is, the real
power $c^{-\lambda}$ times the binomial series $(1 + u)^{-\lambda}$ with
$u = (-\alpha t + \beta t^m)/c$ substituted (where $u = 0$ when $c = 0$), has constant term
$c^{-\lambda}$.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Equation (6).

Formalized by `MetaMathlibExt.constantCoeff_trinomialNegPowSeries`, a theorem declared in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#constant-coeff-trinomial-neg-pow-series).

## The trinomial series at exponent one

For all real numbers $\alpha, \beta$ and every
natural number $m \ne 0$, the formal expansion of $(1 - \alpha t + \beta t^m)^{-\lambda}$ in
powers of $t$ at $\lambda = -1$ is the polynomial $1 - \alpha t + \beta t^m$ itself.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Equation (6).

Formalized by `MetaMathlibExt.trinomialNegPowSeries_neg_one`, a theorem declared in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#trinomial-neg-pow-series-neg-one).

## Kampé de Fériet polynomials

For natural numbers $m, n$ and elements $x, y$ of a
commutative $\mathbb{R}$-algebra, the Kampé de Fériet (two-variable Hermite) polynomial is

$$H^m_n(x, y) = \sum_{r=0}^{q} \frac{n!}{r!\,(n - m r)!}\, y^r x^{n - m r},$$

where $q = \lfloor n / m \rfloor$, read as $q = 0$ when $m = 0$. The paper writes $H_n(x, y)$
for $H^2_n(x, y)$; taking values in an algebra lets $H_k(x + 2yt, y)$ be formed as a formal
power series in $t$.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Equation (2).

Formalized by `MetaMathlibExt.kampeDeFerietHermite`, a definition declared in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#kampe-de-feriet-hermite).

## The zeroth Kampé de Fériet polynomial

For every natural number $m$ and all elements
$x, y$ of a commutative $\mathbb{R}$-algebra, $H^m_0(x, y) = 1$.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Equation (2).

Formalized by `MetaMathlibExt.kampeDeFerietHermite_zero`, a theorem declared in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#kampe-de-feriet-hermite-zero).

## The second Kampé de Fériet polynomial

For all real numbers $x$ and $y$,
$H^2_2(x, y) = x^2 + 2y$.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Equation (2).

Formalized by `MetaMathlibExt.kampeDeFerietHermite_two_two`, a theorem declared in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#kampe-de-feriet-hermite-two-two).

## Hermite-shifted Catalan-type polynomials as convolutions

Write $H_n(x, y) = H^2_n(x, y)$
for the Kampé de Fériet polynomials. For a natural number $m$ and real numbers $\lambda, z$,
write $(1 - m t + z t^m)^{-\lambda}$ and $(1 - m z t + t^m)^{-\lambda}$ for the negative real
powers of the trinomials $1 - m t + z t^m$ and $1 - m z t + t^m$ with exponent $\lambda$ as
power series in $t$ (for $m \ge 1$ these are their expansions in powers of $t$), and let
$P^\lambda_{r,m}(z)$ and $h^\lambda_{r,m}(z)$ be their coefficients of $t^r$. For all natural
numbers $k, m, n$ and real numbers $\lambda, x, y, z$, as formal power series in $t$ (with
$e^{xt + yt^2}$ the exponential series and $H_k(x + 2yt, y)$ evaluated in power series), the
coefficient of $t^n$ in $e^{xt + yt^2} H_k(x + 2yt, y) (1 - m t + z t^m)^{-\lambda}$ is
$\sum_{r=0}^{n} H_{n-r+k}(x, y) P^\lambda_{r,m}(z) / (n - r)!$, and the coefficient of $t^n$
in $e^{xt + yt^2} H_k(x + 2yt, y) (1 - m z t + t^m)^{-\lambda}$ is
$\sum_{r=0}^{n} H_{n-r+k}(x, y) h^\lambda_{r,m}(z) / (n - r)!$.

These coefficients are the paper's $H^{k;\lambda}_{n,m}(x, y, z)$ and
$h^{k;\lambda}_{n,m}(x, y, z)$ (Definition 3, Equations (8) and (9)).

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Theorem 2.

Stated but not proved: `MetaMathlibExt.coeff_hermiteShift_mul_trinomialNegPowSeries` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#coeff-hermite-shift-mul-trinomial-neg-po).

## Nieto–Hermite Catalan-type polynomials as convolutions

Let $j, k, m, r$ be natural
numbers with $k \le r$ and let $\lambda, x, y$ be real numbers. Let $E(t) = e^{2yt - t^2}$ be the
exponential series, so that its coefficient of $t^n$ is $H_n(y) / n!$ with $H_n$ the Hermite
polynomials, and let $F(t)$ be the power series whose coefficient of $t^n$ is $H_n(y) / n!$ when
$n \ge k$ and $j \mid n - k$, and $0$ otherwise (for $j \ge 1$ this is the series
$F(j, k, y, t) = \sum_n H_{jn+k}(y) t^{jn+k} / (jn + k)!$ of Equation (1)). Write
$(1 - m t + x t^m)^{-\lambda}$ and $(1 - m x t + t^m)^{-\lambda}$ for the negative real powers
of the trinomials $1 - m t + x t^m$ and $1 - m x t + t^m$ with exponent $\lambda$ as power
series in $t$ (for $m \ge 1$ these are their expansions in powers of $t$), let
$P^\lambda_{s,m}(x)$ and $h^\lambda_{s,m}(x)$ be their coefficients of $t^s$, and let
$q = \lfloor (r - k) / j \rfloor$, read as $q = 0$ when $j = 0$. Then the coefficient of
$t^r$ in $F(t) (1 - m t + x t^m)^{-\lambda}$ is
$\sum_{n=0}^{q} H_{jn+k}(y) P^\lambda_{r-jn-k,m}(x) / (jn + k)!$, and the coefficient of $t^r$
in $F(t) (1 - m x t + t^m)^{-\lambda}$ is the same sum with $h^\lambda_{r-jn-k,m}(x)$ in place
of $P^\lambda_{r-jn-k,m}(x)$.

These are the paper's $F^{j.k;\lambda}_{r,m}(x, y)$ and $f^{j.k;\lambda}_{r,m}(x, y)$
(Equations (10) and (11)). The paper takes $j, m \ge 1$; for $r < k$ its sum is empty.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Theorem 3.

Stated but not proved: `MetaMathlibExt.coeff_nietoHermiteSeries_mul_trinomialNegPowSeries` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#coeff-nieto-hermite-series-mul-trinomial).

## Splitting the numerator of a unified Catalan-type generating function

Let
$j, k, m, d, n$ be natural numbers, let $a, b, c, \lambda, x, y$ be real numbers and let $A$ be
a polynomial with integer coefficients. Let $K(t)$ be the negative real power of the trinomial
$c - a x t + b (2x - 1)^d t^m$ with exponent $\lambda$ as a power series in $t$ (for $c > 0$ and
$m \ge 1$ this is the expansion of $(c - a x t + b (2x - 1)^d t^m)^{-\lambda}$ in powers of $t$),
and let $S(t) = \sum_i y^i t^i / i!$, the sum running over the natural numbers $i \ge k$ with
$j \mid i - k$ (for $j \ge 1$ this is the pseudo-Bessel function $S(j, k, yt)$ of Equation (5)).
Then the coefficient of $t^n$ in $(S(t) + A(x)\, t)\, K(t)$ equals the coefficient of $t^n$ in
$S(t) K(t)$, plus the coefficient of $t^n$ in $(1 + A(x)\, t)\, K(t)$, minus the coefficient of
$t^n$ in $K(t)$.

In the paper's notation this is
$P^{j.k;\lambda,A}_{n,m}(x, y) = P^{j.k;\lambda,0}_{n,m}(x, y) + P^{1.0;\lambda,A}_{n,m}(x) -
P^{1.0;\lambda,0}_{n,m}(x)$; the kernel is the paper's for $c > 0$.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Theorem 6.

Stated but not proved: `MetaMathlibExt.coeff_catalanTypeKernel_decomposition` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#coeff-catalan-type-kernel-decomposition).

## Determinant of the lower-triangular Catalan-type matrix

Let $m, N$ be natural numbers,
let $\lambda, x$ be real numbers, let $A$ be a polynomial with integer coefficients, and let
$P_n$ be the coefficient of $t^n$ in $(1 + A(x)\, t)(1 - m t + x t^m)^{-\lambda}$, where
$(1 - m t + x t^m)^{-\lambda}$ denotes the negative real power of the trinomial
$1 - m t + x t^m$ with exponent $\lambda$ as a power series in $t$ (for $m \ge 1$, its expansion
in powers of $t$). Then the $(N + 1) \times (N + 1)$ matrix whose $(i, j)$ entry, for
$0 \le i, j \le N$, is $P_{i-j}$ when $j \le i$ and $0$ otherwise has determinant $P_0^{N+1}$.

In the paper's notation $P_n = P^{\lambda,A}_{n,m}(x)$ (Definition 6 at $y = 0$) and the matrix
is $P_N^{(m,\lambda,A)}(x)$ of Equation (18). The paper's proviso $P_0 \ne 0$ is dropped.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Theorem 7.

Stated but not proved: `MetaMathlibExt.det_catalanTypeLowerTriangular` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#det-catalan-type-lower-triangular).

## Hankel determinants of recurrent Catalan-type sequences vanish

Let $m, N, r$ be natural
numbers with $r \le N$, let $\lambda, x$ be real numbers, let $A$ be a polynomial with integer
coefficients, and let $P_n$ be the coefficient of $t^n$ in
$(1 + A(x)\, t)(1 - m t + x t^m)^{-\lambda}$, where $(1 - m t + x t^m)^{-\lambda}$ denotes the
negative real power of the trinomial $1 - m t + x t^m$ with exponent $\lambda$ as a power series
in $t$ (for $m \ge 1$, its expansion in powers of $t$). Suppose real numbers $c_0, \dots, c_r$,
not all zero, satisfy $\sum_{k=0}^{r} c_k P_{n-k} = 0$ for every $n \ge r$. Then the
$(N + 1) \times (N + 1)$ Hankel matrix with $(i, j)$ entry $P_{i+j}$ for $0 \le i, j \le N$ has
determinant $0$.

In the paper's notation $P_n = P^{\lambda,A}_{n,m}(x)$, the recurrence is Equation (22) and the
Hankel matrix is $H_N^{(m,\lambda,A)}(x)$ of Equation (20). The paper's assumption $1 \le r$ is
dropped.

## Sources

- M. A. Pathan and T. Usman, *Unified Catalan-Type Polynomials with Matrix Formulations and Applications*, INTEGERS 26 (2026), Article A105, Theorem 8.

Stated but not proved: `MetaMathlibExt.det_catalanTypeHankel_eq_zero` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/UnifiedCatalanTypePolynomialsWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html#det-catalan-type-hankel-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Catalan-type polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/orthogonal-polynomials/catalan-type-polynomials)
