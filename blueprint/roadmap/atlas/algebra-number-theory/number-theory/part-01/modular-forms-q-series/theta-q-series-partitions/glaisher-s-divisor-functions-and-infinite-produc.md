---
declaration: section
origin: cited
lean: MetaMathlibExt.series_divisor_add_of_mul, MetaMathlibExt.series_divisor_calculus, MetaMathlibExt.series_divisor_pow_recursion, MetaMathlibExt.glaisher_divisors_series_divisor_recurrences, MetaMathlibExt.glaisher_partition_recurrences, MetaMathlibExt.sum_squares_triangular_power_recurrences, MetaMathlibExt.glaisher_theta_divisor_recursions, MetaMathlibExt.power_coeff_convolution_zpow
statement: formalized
---

# Glaisher's divisor functions and infinite products

16 results, 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html).

## Series-divisors add under multiplication

Let $R$ be a commutative ring and let $A$, $B$
be formal power series over $R$ with coefficients $a(n)$, $b(n)$. Suppose $s_A, s_B$ are maps
$\mathbb{N} \to R$ with $n\,a(n) = \sum_{i=1}^{n} s_A(i)\,a(n-i)$ and
$n\,b(n) = \sum_{i=1}^{n} s_B(i)\,b(n-i)$ for every $n \ge 0$ (that is, $s_A$ and $s_B$ are
series-divisors of $A$ and $B$). Then, writing $c(n)$ for the coefficients of $AB$,
$n\,c(n) = \sum_{i=1}^{n} \bigl(s_A(i) + s_B(i)\bigr)\,c(n-i)$ for every $n \ge 0$, so $s_A + s_B$
is a series-divisor of $AB$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Lemma 2 (`jis-2024-24.1.6-lem-2`).

Stated but not proved: `MetaMathlibExt.series_divisor_add_of_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#series-divisor-add-of-mul).

## Calculus of series-divisors

Let $R$ be a commutative ring, let $A$ be a formal power
series over $R$, write $[q^k]F$ for the coefficient of $q^k$ in a power series $F$, and let
$s : \mathbb{N} \to R$ satisfy $n\,[q^n]A = \sum_{i=1}^{n} s(i)\,[q^{n-i}]A$ for every $n \ge 0$
(that is, $s$ is a series-divisor of $A$). Then the following hold for every $n \ge 0$:
(a) for every power series $B$ over $R$ with $AB = 1$,
$n\,[q^n]B = \sum_{i=1}^{n} \bigl(-s(i)\bigr)\,[q^{n-i}]B$;
(b) $n\,[q^n]A(-q) = \sum_{i=1}^{n} (-1)^i s(i)\,[q^{n-i}]A(-q)$;
(c) for every integer $m \ge 1$, $n\,[q^n]A(q^m) = \sum_{i=1}^{n} t_m(i)\,[q^{n-i}]A(q^m)$,
where $t_m(i) = m\,s(i/m)$ if $m \mid i$ and $t_m(i) = 0$ otherwise;
(d) for every integer $m \ge 0$, $n\,[q^n]A^m = \sum_{i=1}^{n} m\,s(i)\,[q^{n-i}]A^m$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Proposition 3 (`jis-2024-24.1.6-prop-3`).

Stated but not proved: `MetaMathlibExt.series_divisor_calculus` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#series-divisor-calculus).

## Coefficient recursion for powers of a power series

Let $R$ be a commutative ring, let
$A$ be a formal power series over $R$ with coefficients $a(k)$, and let $s : \mathbb{N} \to R$
satisfy $k\,a(k) = \sum_{i=1}^{k} s(i)\,a(k-i)$ for every $k \ge 0$ (that is, $s$ is a
series-divisor of $A$). For natural numbers $m$ and $k$, write $a_m(k)$ for the coefficient of
$q^k$ in $A^m$. Then for all natural numbers $m$ and $n$,
$n\,a_m(n) = m \sum_{j=1}^{n} s(j)\,a_m(n-j)$.

## Sources

- in Corollary 4 the printed summand `σ^A(i)` is read as `σ^A(j)` (the summation index).
- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Corollary 4 (`jis-2024-24.1.6-cor-4`).

Stated but not proved: `MetaMathlibExt.series_divisor_pow_recursion` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#series-divisor-pow-recursion).

## Glaisher's divisor functions as series-divisors

Let $n$ be a natural number. For a
positive integer $m$, write $\sigma(m)$ for the sum of the divisors of $m$, $d_B(m)$ and
$d_C(m)$ for the sums of the odd and of the even divisors of $m$, $d_D(m)$ and $d_E(m)$ for the
sums of the divisors $d$ of $m$ with $m/d$ odd and with $m/d$ even,
$d_F(m) = \sum_{d \mid m} (-1)^{d-1} d$ and $d_G(m) = \sum_{d \mid m} (-1)^{m/d-1} d$, and set all
of these to $0$ at $m = 0$. Let $p(m)$, $p_o(m)$, $p_e(m)$ and $p_d(m)$ be the numbers of
partitions of $m$, of partitions of $m$ into odd parts, into even parts and into distinct parts,
let $\bar p(m)$ be the number of overpartitions of $m$, let $r(m)$ be the number of integers $k$
with $k^2 = m$, and let $t(m)$ be the number of natural numbers $k$ with $k(k+1)/2 = m$. Then
$d_C(n) = 2 d_E(n)$, and, with every sum running over $1 \le i \le n$,
$n\,p(n) = \sum_i \sigma(i)\,p(n-i)$, $n\,p_o(n) = \sum_i d_B(i)\,p_o(n-i)$,
$n\,p_e(n) = \sum_i d_C(i)\,p_e(n-i)$, $n\,\bar p(n) = \sum_i 2 d_D(i)\,\bar p(n-i)$,
$n\,r(n) = \sum_i (-1)^{i+1} 2 d_D(i)\,r(n-i)$, $n\,t(n) = \sum_i d_F(i)\,t(n-i)$ and
$n\,p_d(n) = \sum_i d_G(i)\,p_d(n-i)$.

In the language of the source, these recurrences say that $\sigma$, $d_B$, $d_C$, $2 d_D$,
$i \mapsto (-1)^{i+1} 2 d_D(i)$, $d_F$ and $d_G$ are the series-divisors of the generating
functions of $p$, $p_o$, $p_e$, $\bar p$, $\varphi(q) = \sum_{k \in \mathbb{Z}} q^{k^2}$,
$\psi(q) = \sum_{k \ge 0} q^{k(k+1)/2}$ and $p_d$ respectively.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 9 (`jis-2024-24.1.6-thm-9`).

Stated but not proved: `MetaMathlibExt.glaisher_divisors_series_divisor_recurrences` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#glaisher-divisors-series-divisor-recurre).

## Recurrences for partitions into even or distinct parts and for overpartitions

Let $n$
be a natural number. Let $p_e(m)$, $p_o(m)$ and $p_d(m)$ be the numbers of partitions of $m$
into even parts, into odd parts and into distinct parts, and let $\bar p(m)$ be the number of
overpartitions of $m$. For a positive integer $m$, write $\sigma(m)$ for the sum of the divisors
of $m$, $\sigma(m/2)$ for $\sigma$ evaluated at $m/2$ when $m$ is even and for $0$ when $m$ is
odd, $d_B(m)$ and $d_C(m)$ for the sums of the odd and of the even divisors of $m$, $d_D(m)$ for
the sum of the divisors $d$ of $m$ with $m/d$ odd, and $d_G(m) = \sum_{d \mid m} (-1)^{m/d-1} d$.
Then, with every sum running over $1 \le i \le n$,
$n\,p_e(n) = \sum_i d_C(i)\,p_e(n-i) = 2\sum_i \sigma(i/2)\,p_e(n-i)$,
$n\,p_d(n) = \sum_i d_B(i)\,p_o(n-i) = \sum_i d_G(i)\,p_d(n-i) =
\sum_i (\sigma(i) - 2\sigma(i/2))\,p_d(n-i)$, and
$n\,\bar p(n) = 2\sum_i d_D(i)\,\bar p(n-i) = 2\sum_i (\sigma(i) - \sigma(i/2))\,\bar p(n-i)$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 10 (`jis-2024-24.1.6-thm-10`).

Stated but not proved: `MetaMathlibExt.glaisher_partition_recurrences` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#glaisher-partition-recurrences).

## Recurrences for sums of squares and sums of triangular numbers

Let $m \ge 1$ be an
integer. For $n \ge 0$, let $r_m(n)$ be the number of $x \in \mathbb{Z}^m$ with
$x_1^2 + \dots + x_m^2 = n$, and let $t_m(n)$ be the number of $x \in \mathbb{Z}_{\ge 0}^m$ with
$\sum_{i=1}^{m} x_i(x_i+1)/2 = n$. Let $\sigma$ be the sum-of-divisors function, and set
$\sigma(j/2) = 0$ when $j$ is odd. Then for every $n \ge 0$,

$$n\,r_m(n) = m \sum_{j=1}^{n} 2(-1)^{j+1}\bigl(\sigma(j) - \sigma(j/2)\bigr)\,r_m(n-j)$$

and

$$n\,t_m(n) = m \sum_{j=1}^{n} \bigl(\sigma(j) - 4\sigma(j/2)\bigr)\,t_m(n-j).$$

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 11 (`jis-2024-24.1.6-thm-11`).

Stated but not proved: `MetaMathlibExt.sum_squares_triangular_power_recurrences` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#sum-squares-triangular-power-recurrences).

## Six recursions for Glaisher's divisor functions from the theta functions

Let $n \ge 1$
be a natural number. Write $\sigma(m)$ for the sum of the positive divisors of $m$, $d_D(m)$ for
the sum of the divisors $d$ of $m$ with $m/d$ odd, $d_F(m) = \sum_{d \mid m} (-1)^{d-1} d$,
$\bar\sigma_3(m) = \sum_{d \mid m,\ m/d \text{ odd}} d^3$,
$\tilde\sigma_3(m) = \sum_{d \mid m} (-1)^{d-1} d^3$ and $S(m) = \sigma(m) - 4\sigma(m/4)$, where
$\sigma(m/4) = 0$ unless $4 \mid m$; all of these are $0$ at every integer $m \le 0$. Then
$d_D(n) + 2\sum_{j=1}^{n} (-1)^j d_D(n-j^2)$ is $(-1)^{n-1} n$ if $n$ is a perfect square and
$0$ otherwise; $\sum_{j=0}^{n} d_F(n-j(j+1)/2)$ is $n$ if $n = k(k+1)/2$ for some natural number
$k$ and $0$ otherwise; $8\sum_{j=1}^{n-1} (-1)^{j+1} d_D(j)\,S(n-j) = n\,S(n) + (-1)^n d_D(n)$;
$4\sum_{j=1}^{n} d_F(j)\,\sigma(2n+1-2j) = n\,\sigma(2n+1)$;
$16\sum_{j=1}^{n-1} d_D(j)\,\tilde\sigma_3(n-j) = d_D(n) - n\,\tilde\sigma_3(n)$; and
$8\sum_{j=1}^{n} d_F(j)\,\bar\sigma_3(n+1-j) = n\,\bar\sigma_3(n+1)$.

These recursions come from the theta functions $\varphi(q) = \sum_{k \in \mathbb{Z}} q^{k^2}$ and
$\psi(q) = \sum_{k \ge 0} q^{k(k+1)/2}$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 14 (`jis-2024-24.1.6-thm-14`).

Stated but not proved: `MetaMathlibExt.glaisher_theta_divisor_recursions` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#glaisher-theta-divisor-recursions).

## Power recursion lemma for nonzero integer exponents

Let $K$ be a field of characteristic
zero, let $A$ be an invertible formal power series in $K[[X]]$, and let $u$ and $v$ be nonzero
integers. Write $a_u(k)$ and $a_v(k)$ for the coefficients of $X^k$ in $A^u$ and $A^v$. Then for
every natural number $n$,

$$\sum_{k=0}^{n} \left(n - \left(\frac{u}{v} + 1\right) k\right) a_u(n-k)\, a_v(k) = 0.$$

Invertibility of $A$ is assumed so that the negative powers $A^u$, $A^v$ make sense.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Lemma 17 (`jis-2024-24.1.6-lem-17`).

Stated but not proved: `MetaMathlibExt.power_coeff_convolution_zpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#power-coeff-convolution-zpow).

## Power recursion lemma for positive exponents

Let $K$ be a field of characteristic zero,
let $A \in K[[X]]$ be a formal power series, and let $u$ and $v$ be positive integers. Write
$a_u(k)$ and $a_v(k)$ for the coefficients of $X^k$ in $A^u$ and $A^v$. Then for every natural
number $n$,

$$\sum_{k=0}^{n} \left(n - \left(\frac{u}{v} + 1\right) k\right) a_u(n-k)\, a_v(k) = 0.$$

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Lemma 17 (`jis-2024-24.1.6-lem-17`).

Stated but not proved: `MetaMathlibExt.power_coeff_convolution_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#power-coeff-convolution-pow).

## Six divisor-function identities from the power recursion lemma

Let $n \ge 1$ be a
natural number. Write $\sigma(m)$ for the sum of the positive divisors of $m$,
$\bar\sigma_3(m) = \sum_{d \mid m,\ m/d \text{ odd}} d^3$,
$\tilde\sigma_3(m) = \sum_{d \mid m} (-1)^{d-1} d^3$ and $S(m) = \sigma(m) - 4\sigma(m/4)$, where
$\sigma(m/4) = 0$ unless $4 \mid m$; all of these are $0$ at every integer $m \le 0$. Then
$2n\,\sigma(2n+1) = \sum_{j=1}^{n} (5j(j+1) - 2n)\,\sigma(2n+1-j(j+1))$; the number
$n\,S(n) - 2\sum_{j=1}^{n} (5j^2 - n)\,S(n-j^2)$ is $n$ if $n$ is a perfect square and $0$
otherwise;
$n\,\bar\sigma_3(n+1) = \sum_{j=1}^{n+1} (9j(j+1)/2 - n)\,\bar\sigma_3(n+1-j(j+1)/2)$; the
number $n\,\tilde\sigma_3(n) - 2\sum_{j=1}^{n} (-1)^j (9j^2 - n)\,\tilde\sigma_3(n-j^2)$ is
$(-1)^{n-1} n$ if $n$ is a perfect square and $0$ otherwise;
$\sum_{j=0}^{n+1} (3j - n)\,\sigma(2j+1)\,\bar\sigma_3(n+1-j) = 0$; and
$n\,(\tilde\sigma_3(n) + (-1)^n S(n)) =
8\sum_{j=1}^{n-1} (3j - n)(-1)^j S(j)\,\tilde\sigma_3(n-j)$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 19 (`jis-2024-24.1.6-thm-19`).

Stated but not proved: `MetaMathlibExt.glaisher_power_recursion_divisor_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#glaisher-power-recursion-divisor-identit).

## Glaisher's congruences for divisor sums over squares and triangular numbers

Let
$n \ge 1$ be a natural number. Write $\sigma(m)$ for the sum of the positive divisors of $m$
and $\bar\sigma_3(m) = \sum_{d \mid m,\ m/d \text{ odd}} d^3$, and set
$\sigma(m) = \bar\sigma_3(m) = 0$ for every integer $m \le 0$. Then the following hold. If
$5 \nmid n$, then $\sum_{j=0}^{n} \sigma(2n+1-j(j+1)) \equiv 0 \pmod 5$. The sum
$\sum_{j=0}^{n} \sigma(n-j(j+1)/2)$ is congruent modulo $4$ to $n$ if $n = k(k+1)/2$ for some
natural number $k$, and to $0$ otherwise. If $5 \nmid n$ and $n \equiv 2$ or $3 \pmod 4$, then
$\sigma(n) + 2\sum_{j=1}^{n} \sigma(n-j^2) \equiv 0 \pmod 5$. If $n$ is coprime to $3$, then
$\sum_{j=0}^{n+1} \bar\sigma_3(n+1-j(j+1)/2) \equiv 0 \pmod 9$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 20 (`jis-2024-24.1.6-thm-20`).

Stated but not proved: `MetaMathlibExt.glaisher_divisor_sum_congruences` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#glaisher-divisor-sum-congruences).

## A congruence modulo 5 for divisor sums over triangular shifts

Let $\sigma$ be the
sum-of-divisors function, with $\sigma(r) = 0$ for $r \le 0$. For every integer $n \ge 1$, the sum
$\sum_{j=0}^{n} \sigma\bigl(2n + 1 - j(j+1)\bigr)$ is congruent to $1$ modulo $5$ if
$n = 5k(k+1)/2$ for some integer $k \ge 0$, and to $0$ modulo $5$ otherwise.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 23 (`jis-2024-24.1.6-thm-23`).

Stated but not proved: `MetaMathlibExt.sigma_triangular_shift_sum_mod_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#sigma-triangular-shift-sum-mod-five).

## Convolution identities for the series-divisor of an invertible series

Let $R$ be a
commutative ring and let $A$, $B$ be formal power series over $R$ with coefficients $a(k)$,
$b(k)$ and $AB = 1$. Let $s : \mathbb{N} \to R$ satisfy $s(0) = 0$ and
$k\,a(k) = \sum_{i=1}^{k} s(i)\,a(k-i)$ for every $k \ge 0$ (that is, $s$ is a series-divisor
of $A$). Then for every $n \ge 0$,

$$s(n) = \sum_{i=0}^{n} (n-i)\,a(n-i)\,b(i)$$

and

$$\sum_{i=1}^{n} s(n-i)\,s(i) = -\sum_{i=1}^{n} i\,(n-i)\,a(n-i)\,b(i).$$

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Lemma 25 (`jis-2024-24.1.6-lem-25`).

Stated but not proved: `MetaMathlibExt.series_divisor_inverse_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#series-divisor-inverse-convolution).

## Overpartition formulas for a divisor sum with odd cofactors

Let $n$ be a natural number.
Write $\sigma(m)$ for the sum of the positive divisors of $m$, $\sigma(m/2)$ for $\sigma$
evaluated at $m/2$ when $m$ is even and for $0$ when $m$ is odd, and $d_D(m)$ for the sum of the
divisors $d$ of $m$ with $m/d$ odd, with $\sigma(0) = d_D(0) = 0$; let $\bar p(m)$ be the number
of overpartitions of $m$. Then $2 d_D(n) = 2(\sigma(n) - \sigma(n/2)) = n\,\bar p(n) +
2\sum_{i \ge 1,\ i^2 \le n} (-1)^i (n - i^2)\,\bar p(n - i^2)$ and
$2\sum_{i=1}^{n} d_D(n-i)\,d_D(i) =
\sum_{i \ge 1,\ i^2 \le n} (-1)^{i+1} i^2 (n - i^2)\,\bar p(n - i^2)$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 26 (`jis-2024-24.1.6-thm-26`).

Stated but not proved: `MetaMathlibExt.overpartition_glaisher_dD_formulas` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#overpartition-glaisher-d-d-formulas).

## Ramanujan's congruence modulo $5$ and a convolution of divisor sums

Let $p(k)$ be the
number of partitions of $k$ and $\sigma(k)$ the sum of the positive divisors of $k$. Then
$p(5m+4) \equiv 0 \pmod 5$ for every natural number $m$ if and only if
$\sum_{i=1}^{5m} \sigma(i)\,\sigma(5m+1-i) \equiv 0 \pmod 5$ for every natural number $m$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 28 (`jis-2024-24.1.6-thm-28`).

Stated but not proved: `MetaMathlibExt.partition_mod_five_iff_sigma_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#partition-mod-five-iff-sigma-convolution).

## Overpartitions modulo $8$ and a convolution of divisor sums

Let $\bar p(k)$ be the
number of overpartitions of $k$, and let $d_D(k)$ be the sum of the divisors $d$ of $k$ for which
$k/d$ is odd. Then $\bar p(4m+3) \equiv 0 \pmod 8$ for every natural number $m$ if and only if
$\sum_{i=1}^{4m-1} d_D(i)\,d_D(4m-i) \equiv 0 \pmod 4$ for every natural number $m$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, *Glaisher's Divisors and Infinite Products*, Journal of Integer Sequences 27 (2024), Article 24.1.6, Theorem 30 (`jis-2024-24.1.6-thm-30`).

Stated but not proved: `MetaMathlibExt.overpartition_mod_eight_iff_dD_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GlaisherDivisorsInfiniteProductsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html#overpartition-mod-eight-iff-d-d-convolut).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Glaisher's divisor functions and infinite products](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/glaisher-s-divisor-functions-and-infinite-produc)
