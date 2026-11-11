---
declaration: section
origin: cited
lean: MetaMathlibExt.primeCounting_lt_div_log_sub_six_terms, MetaMathlibExt.div_log_sub_six_terms_lt_primeCounting, MetaMathlibExt.div_log_sub_three_terms_lt_primeCounting, MetaMathlibExt.primeCounting_lt_div_log_sub_four_terms, MetaMathlibExt.primeCounting_lt_eight_term_series, MetaMathlibExt.four_term_series_lt_primeCounting, MetaMathlibExt.exists_prime_mem_Ioc_mul_one_add_div_log_pow, MetaMathlibExt.primeCounting_lt_div_log_sub_table_two
statement: formalized
---

# Explicit bounds for the prime-counting function

35 results, 35 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html).

## Axler's six-term upper bound for the prime-counting function

Let $\pi(x)$ denote the
number of primes $p \le x$ and $\log$ the natural logarithm. For every real $x \ge 48$,

$$
\pi(x) < \frac{x}{\log x - 1 - \frac{1}{\log x} - \frac{3.024334}{\log^2 x} -
\frac{12.975666}{\log^3 x} - \frac{71.048668}{\log^4 x} - \frac{461.364417856444}{\log^5 x} -
\frac{4331.1}{\log^6 x}}.
$$

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Theorem 2.

Stated but not proved: `MetaMathlibExt.primeCounting_lt_div_log_sub_six_terms` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-counting-lt-div-log-sub-six-terms).

## Axler's six-term lower bound for the prime-counting function

For every real
$x \ge 1751189194177$ (the prime $p_{64497259289}$),

$$
\pi(x) > \frac{x}{\log x - 1 - \frac{1}{\log x} - \frac{2.975666}{\log^2 x} -
\frac{13.024334}{\log^3 x} - \frac{70.951332}{\log^4 x} - \frac{b_5}{\log^5 x} -
\frac{b_6}{\log^6 x}},
$$

where $b_5 = 460.634397856444$, $b_6 = 3444.031844143556$ and $\pi(x)$ is the number of primes
$p \le x$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Theorem 3.

Stated but not proved: `MetaMathlibExt.div_log_sub_six_terms_lt_primeCounting` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#div-log-sub-six-terms-lt-prime-counting).

## Axler's unconditional three-term lower bound for the prime-counting function

Let
$\pi(x)$ denote the number of primes $p \le x$ and $\log$ the natural logarithm. For every real
$x \ge 65405887$,

$$
\pi(x) > \frac{x}{\log x - 1 - \frac{1}{\log x} - \frac{3}{\log^2 x}}.
$$

This is the paper's inequality (14). Before, it was known on the interval
$[65405887, 2.7358 \cdot 10^{40}]$, for $x \ge 4.8447 \cdot 10^{19377}$, and for all
$x \ge 65405887$ under the Riemann hypothesis.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Theorem 4, inequality (14).

Stated but not proved: `MetaMathlibExt.div_log_sub_three_terms_lt_primeCounting` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#div-log-sub-three-terms-lt-prime-countin).

## Axler's upper bound for the prime-counting function above 29.53

Let $\pi(x)$ denote the
number of primes $p \le x$ and $\log$ the natural logarithm. For every real $x \ge 29.53$,

$$
\pi(x) < \frac{x}{\log x - 1 - \frac{1}{\log x} - \frac{3}{\log^2 x} - \frac{70.935}{\log^3 x}}.
$$

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Proposition 4.

Stated but not proved: `MetaMathlibExt.primeCounting_lt_div_log_sub_four_terms` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-counting-lt-div-log-sub-four-terms).

## Eight-term upper bound for the prime-counting function

For every real $x > 1$, the
number $\pi(x)$ of primes $p \le x$ satisfies
$\pi(x) < \frac{x}{\log x} + \frac{x}{\log^2 x} + \frac{2x}{\log^3 x} +
\frac{6.024334\,x}{\log^4 x} + \frac{24.024334\,x}{\log^5 x} + \frac{120.12167\,x}{\log^6 x} +
\frac{720.73002\,x}{\log^7 x} + \frac{6098\,x}{\log^8 x}$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Proposition 5.

Stated but not proved: `MetaMathlibExt.primeCounting_lt_eight_term_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-counting-lt-eight-term-series).

## Axler's four-term series lower bound for the prime-counting function

Let $\pi(x)$ denote
the number of primes $p \le x$ and $\log$ the natural logarithm. For every real $x \ge 10384261$,

$$
\pi(x) > \frac{x}{\log x} + \frac{x}{\log^2 x} + \frac{2x}{\log^3 x} + \frac{6x}{\log^4 x}.
$$

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Corollary 6.

Stated but not proved: `MetaMathlibExt.four_term_series_lt_primeCounting` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#four-term-series-lt-prime-counting).

## Axler's primes in short intervals

Let $\log$ denote the natural logarithm, and put
$a = 1/(1.42969 \cdot 10^{12} - 1)$ and $b = 1/(1.59753 \cdot 10^{12} - 1)$. For every real
$x \ge 952527672606693$ there is a prime $p$ with $x < p \le x\,(1 + 43a/\log x)$. Moreover, for
each of the pairs $(n, X_n)$ equal to $(2, 684943746324434)$, $(3, 543684371469081)$,
$(4, 336149866771577)$ and $(5, 246782656239427)$, and every real $x \ge X_n$, there is a prime
$p$ with $x < p \le x\,(1 + 46^n b/\log^n x)$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Theorem 1 and Table 1.

Stated but not proved: `MetaMathlibExt.exists_prime_mem_Ioc_mul_one_add_div_log_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#exists-prime-mem-ioc-mul-one-add-div-log).

## Axler's Table 2 upper bounds for the prime-counting function

Let $\pi(x)$ denote the
number of primes $p \le x$ and $\log$ the natural logarithm. For each of the three rows
$(a_0, a_1, a_2, x_0)$ equal to $(1.0343, 0, 0, 106640139304611)$, $(1, 1.109, 0, 81250795096339)$
and $(1, 1, 3.48, 145413088724077)$, every real $x \ge x_0$ satisfies

$$
\pi(x) < \frac{x}{\log x - a_0 - \frac{a_1}{\log x} - \frac{a_2}{\log^2 x}}.
$$

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Corollary 1 and Table 2.

Stated but not proved: `MetaMathlibExt.primeCounting_lt_div_log_sub_table_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-counting-lt-div-log-sub-table-two).

## Axler's Table 3 upper bounds for the prime-counting function

Let $\pi(x)$ denote the
number of primes $p \le x$ and $\log$ the natural logarithm. For each of the three rows
$(a_3, a_4, a_5, x_0)$ equal to $(14.893, 0, 0, 142464507937911)$, $(12.975666, 79.962, 0, 22)$
and $(12.975666, 71.048668, 533.594, 32)$, every real $x \ge x_0$ satisfies

$$
\pi(x) < \frac{x}{\log x - 1 - \frac{1}{\log x} - \frac{3.024334}{\log^2 x} -
\frac{a_3}{\log^3 x} - \frac{a_4}{\log^4 x} - \frac{a_5}{\log^5 x}}.
$$

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Corollary 2 and Table 3.

Stated but not proved: `MetaMathlibExt.primeCounting_lt_div_log_sub_table_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-counting-lt-div-log-sub-table-thre).

## Three-term upper bounds for the prime-counting function (Table 4)

Let $\pi(x)$ be the
number of primes $p \le x$. For each of the twelve pairs $(\varepsilon, x_0)$ listed below and
every real $x \ge x_0$,
$\pi(x) < \frac{x}{\log x} + \frac{x}{\log^2 x} + \frac{(2 + \varepsilon)\,x}{\log^3 x}$.
The pairs are $(0.21, 160930932942272)$, $(0.215, 83016503500865)$,
$(0.22, 43999690220699)$, $(0.225, 23824649646672)$, $(0.23, 13279102022111)$,
$(0.24, 4511700549332)$, $(0.25, 1615202653795)$, $(0.26, 643809266445)$,
$(0.2651, 406742886708)$, $(0.27, 265248130170)$, $(0.28, 117997473286)$ and
$(0.29, 57720805589)$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Corollary 3 and Table 4.

Stated but not proved: `MetaMathlibExt.primeCounting_lt_three_term_series_table_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-counting-lt-three-term-series-tabl).

## Axler's Table 5 lower bounds for the prime-counting function

Let $\pi(x)$ denote the
number of primes $p \le x$ and $\log$ the natural logarithm. For each of the four rows
$(a_3, a_4, a_5, x_0)$ equal to $(13.024334, 70.951332, 460.634397856444, 1035745443241)$,
$(13.024334, 70.951332, 0, 153887581621)$, $(13.024334, 0, 0, 7713187213)$ and
$(0, 0, 0, 54941209)$, every real $x \ge x_0$ satisfies

$$
\pi(x) > \frac{x}{\log x - 1 - \frac{1}{\log x} - \frac{2.975666}{\log^2 x} -
\frac{a_3}{\log^3 x} - \frac{a_4}{\log^4 x} - \frac{a_5}{\log^5 x}}.
$$

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Corollary 4 and Table 5.

Stated but not proved: `MetaMathlibExt.div_log_sub_table_five_lt_primeCounting` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#div-log-sub-table-five-lt-prime-counting).

## Axler's Table 6 lower bounds for the prime-counting function

Let $\pi(x)$ denote the
number of primes $p \le x$ and $\log$ the natural logarithm. For each of the five rows
$(b_5, b_6, b_7, b_8, x_0)$ equal to
$(23.975666, 119.87833, 719.26998, 5034.88986, 1681111802141)$,
$(23.975666, 119.87833, 719.26998, 0, 721733241667)$,
$(23.975666, 119.87833, 0, 0, 110838719141)$, $(23.975666, 0, 0, 0, 1331691853)$ and
$(0, 0, 0, 0, 10383799)$, every real $x \ge x_0$ satisfies

$$
\pi(x) > \frac{x}{\log x} + \frac{x}{\log^2 x} + \frac{2x}{\log^3 x} +
\frac{5.975666\,x}{\log^4 x} + \frac{b_5 x}{\log^5 x} + \frac{b_6 x}{\log^6 x} +
\frac{b_7 x}{\log^7 x} + \frac{b_8 x}{\log^8 x}.
$$

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Corollary 5 and Table 6.

Stated but not proved: `MetaMathlibExt.eight_term_series_table_six_lt_primeCounting` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#eight-term-series-table-six-lt-prime-cou).

## Axler's cubic-logarithm bound for Chebyshev's theta function

For every real
$x \ge 1757126630797$ (the prime $p_{64707865143}$),

$$
|\vartheta(x) - x| < \frac{0.024334\, x}{\log^3 x},
$$

where $\vartheta(x) = \sum_{p \le x} \log p$ is Chebyshev's function, the sum over the primes
$p \le x$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Proposition 1, inequality (6).

Stated but not proved: `MetaMathlibExt.abs_theta_sub_lt_div_log_cube` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#abs-theta-sub-lt-div-log-cube).

## Axler's four bounds for Chebyshev's theta function

Let
$\vartheta(x) = \sum_{p \le x} \log p$ be Chebyshev's function, the sum over the primes
$p \le x$. Then for real $x$ we have
$|\vartheta(x) - x| < 0.043\, x / \log^3 x$ for $x \ge e^{40}$,
$|\vartheta(x) - x| < 0.15\, x / \log^3 x$ for $e^{35} \le x < e^{5000}$,
$|\vartheta(x) - x| < 99.07\, x / \log^4 x$ for $x \ge e^{25}$, and
$|\vartheta(x) - x| < 100\, x / \log^4 x$ for $x \ge 70111$.

These bounds are re-established after the correction of Faber and Kadiri's bounds.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Proposition 3, inequalities (25)-(28).

Stated but not proved: `MetaMathlibExt.abs_theta_sub_lt_axler_four_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#abs-theta-sub-lt-axler-four-bounds).

## Axler's explicit Mertens second theorem

For every real $x \ge 1757126630797$,

$$
\Big|\sum_{p \le x} \frac{1}{p} - \log\log x - B\Big| \le
\frac{0.024334}{3 \log^3 x} \Big(1 + \frac{15}{4 \log x}\Big),
$$

where the sum runs over the primes $p \le x$ and $B$ is the Meissel–Mertens constant, the limit
of $\sum_{p \le n} 1/p - \log\log n$ as the integer $n$ tends to infinity. It equals
$\gamma + \sum_p (\log(1 - 1/p) + 1/p)$, with $\gamma$ Euler's constant.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Theorem 5, inequality (17).

Stated but not proved: `MetaMathlibExt.abs_sum_inv_prime_sub_log_log_sub_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#abs-sum-inv-prime-sub-log-log-sub-le).

## Axler's explicit Mertens first theorem

For every real $x \ge 1757126630797$,

$$
\Big|\sum_{p \le x} \frac{\log p}{p} - \log x - E\Big| \le
\frac{0.024334}{2 \log^2 x} \Big(1 + \frac{2}{\log x}\Big),
$$

where the sum runs over the primes $p \le x$ and $E$ is Mertens' constant, the limit of
$\sum_{p \le n} \log p / p - \log n$ as the integer $n$ tends to infinity. It equals
$-\gamma - \sum_p \log p / (p(p-1)) = -1.3325\ldots$, with $\gamma$ Euler's constant.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Theorem 6.

Stated but not proved: `MetaMathlibExt.abs_sum_log_div_prime_sub_log_sub_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#abs-sum-log-div-prime-sub-log-sub-le).

## Explicit Mertens third theorem

Let $\gamma$ be the Euler–Mascheroni constant and
$f(x) = \frac{0.024334}{3 \log^3 x} \left(1 + \frac{15}{4 \log x}\right)$. For every real
$x \ge 1757126630797$, the product over the primes $p \le x$ satisfies
$\frac{e^{-\gamma}}{\log x} \exp(-f(x)) < \prod_{p \le x} \left(1 - \frac{1}{p}\right) <
\frac{e^{-\gamma}}{\log x} \exp\left(f(x) + \frac{1.02}{(x - 1) \log x}\right)$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Proposition 7.

Stated but not proved: `MetaMathlibExt.prod_one_sub_inv_prime_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prod-one-sub-inv-prime-bounds).

## Explicit bounds for $\prod_{p \le x} (1 + 1/p)$

Let $\gamma$ be the Euler–Mascheroni
constant and $f(x) = \frac{0.024334}{3 \log^3 x} \left(1 + \frac{15}{4 \log x}\right)$. For every
real $x \ge 1757126630797$, the product over the primes $p \le x$ satisfies
$\frac{6 e^{\gamma}}{\pi^2} \exp\left(-f(x) - \frac{1.02}{(x - 1) \log x}\right) \log x <
\prod_{p \le x} \left(1 + \frac{1}{p}\right) <
\frac{6 e^{\gamma}}{\pi^2} \left(1 + \frac{1}{x}\right) \exp(f(x)) \log x$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Corollary 7.

Stated but not proved: `MetaMathlibExt.prod_one_add_inv_prime_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prod-one-add-inv-prime-bounds).

## Converting a lower bound for $\pi(x)$ into a truncated series

Let $\pi(x)$ be the number
of primes $p \le x$. Let $n \ge 1$ be an integer, let $a_0, \dots, a_n$ be reals with $a_0 > 0$
and $a_1, \dots, a_n < 0$, and let $x_0 > 0$. Suppose that for every real $x \ge x_0$ the
denominator $D(x) = a_0 \log x + \sum_{i=1}^{n} a_i / \log^{i-1} x$ is positive and
$\pi(x) > x / D(x)$. Let $b_0 = 1/a_0$ and $b_k = -\frac{1}{a_0} \sum_{i=1}^{k} a_i b_{k-i}$ for
$1 \le k \le n$. Then for every real $x \ge x_0$,
$\pi(x) > \sum_{k=0}^{n} \frac{b_k x}{\log^{k+1} x}$.

The recursion uses $b_{k-i}$, the index of the paper's proof: it turns the first row of Table 5
into the Table 6 coefficients $1, 1, 2, 5.975666, 23.975666, \dots$. The source record of the
statement prints $b_{k-1}$ instead, which would give $b_3 = 9.951332$ there.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Proposition 6.

Stated but not proved: `MetaMathlibExt.series_lt_primeCounting_of_lt_primeCounting` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#series-lt-prime-counting-of-lt-prime-cou).

## Prime counting between the auxiliary functions $J$

Let $\pi(x)$ be the number of primes
$p \le x$ and $\vartheta(x) = \sum_{p \le x} \log p$ Chebyshev's function. Let $k \ge 1$ be an
integer and let $\eta > 0$ and $x_1 > 1$ be reals with $|\vartheta(y) - y| < \eta y / \log^k y$
for every real $y \ge x_1$. For reals $e$ and $x \ge x_1$ set
$J_e(x) = \pi(x_1) - \frac{\vartheta(x_1)}{\log x_1} + \frac{x}{\log x} +
\frac{e\,x}{\log^{k+1} x} + \int_{x_1}^{x} \left(\frac{1}{\log^2 t} +
\frac{e}{\log^{k+2} t}\right) dt$.
Then $J_{-\eta}(x) \le \pi(x) \le J_{\eta}(x)$ for every real $x \ge x_1$.

The inequalities are non-strict, as the paper prints them.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Lemma 1.

Stated but not proved: `MetaMathlibExt.primeCounting_mem_Icc_auxJ` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-counting-mem-icc-aux-j).

## Büthe's bound of the prime-counting function by the logarithmic integral

Let $\pi(x)$
denote the number of primes $p \le x$, and let $\operatorname{li}(x)$ be the logarithmic integral,
the principal value $\mathrm{PV}\int_0^x \frac{dt}{\log t}$. For every real $x$ with
$2 \le x \le 10^{19}$, $\pi(x) \le \operatorname{li}(x)$.

The paper prints the non-strict form; Büthe's original bound is strict.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Lemma 2 (Büthe).

Stated but not proved: `MetaMathlibExt.primeCounting_le_logarithmicIntegral` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-counting-le-logarithmic-integral).

## Johnston's range for Schoenfeld's inequality

For every real $x$ with
$2657 \le x \le 1.101 \cdot 10^{26}$,

$$
|\pi(x) - \operatorname{li}(x)| < \frac{\sqrt{x} \log x}{8\pi},
$$

where $\pi(x)$ is the number of primes $p \le x$ and $\operatorname{li}$ is the logarithmic
integral.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Lemma 3 (Johnston).

Stated but not proved: `MetaMathlibExt.abs_primeCounting_sub_logarithmicIntegral_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#abs-prime-counting-sub-logarithmic-integ).

## Tails of prime power sums from a Chebyshev bound

Let $k \ge 1$ be an integer and let
$\eta > 0$ and $x_0 > 1$ be reals such that $|\vartheta(y) - y| < \eta y / \log^k y$ for every
real $y \ge x_0$, where $\vartheta(y) = \sum_{p \le y} \log p$ is Chebyshev's function. Then
for every integer $n \ge 2$ and every real $x \ge x_0$,

$$
\Big|\operatorname{li}(x^{1-n}) + \sum_{p > x} \frac{1}{p^n}\Big| <
\frac{\eta}{x^{n-1} \log^{k+1} x} \Big(1 + \frac{n}{n-1}\Big),
$$

where $\operatorname{li}$ is the logarithmic integral and the sums run over primes $p$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Lemma 6.

Stated but not proved: `MetaMathlibExt.abs_logarithmicIntegral_add_tsum_inv_prime_pow_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#abs-logarithmic-integral-add-tsum-inv-pr).

## The Mertens remainder from a Chebyshev bound

Let $k \ge 1$ be an integer and let
$\eta > 0$ and $x_0 > 1$ be reals such that $|\vartheta(y) - y| < \eta y / \log^k y$ for every
real $y \ge x_0$, where $\vartheta(y) = \sum_{p \le y} \log p$ is Chebyshev's function. For
real $x$ let $S(x) = \sum_{p > x} \big(\log(1 - 1/p) + 1/p\big)$, the sum over the primes
$p > x$. Then for every real $x \ge x_0$,

$$
\Big|S(x) - \sum_{m \ge 1} \frac{\operatorname{li}(x^{-m})}{m+1}\Big| <
\frac{\eta}{\log^{k+1} x} \Big((x+1) \log\frac{x}{x-1} - 1\Big),
$$

where $\operatorname{li}$ is the logarithmic integral.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Proposition 8; `S(x)` as in the paper's equation (6.5).

Stated but not proved: `MetaMathlibExt.abs_mertensRemainder_sub_tsum_logarithmicIntegral_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#abs-mertens-remainder-sub-tsum-logarithm).

## Tails of prime power sums under the Riemann hypothesis

Assume the Riemann
hypothesis. Then for every integer $n \ge 2$ and every real $x \ge 599$,

$$
\Big|\operatorname{li}(x^{1-n}) + \sum_{p > x} \frac{1}{p^n}\Big| <
\frac{1}{8\pi x^{n - 1/2}} \Big(1 + \frac{2n}{2n-1}\Big) \Big(\log x + \frac{2}{2n-1}\Big),
$$

where $\operatorname{li}$ is the logarithmic integral and the sum runs over the primes $p > x$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Proposition 9.

Stated but not proved: `MetaMathlibExt.abs_logarithmicIntegral_add_tsum_inv_prime_pow_lt_of_RH` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#abs-logarithmic-integral-add-tsum-inv-pr-2).

## The last branch of Axler's error factor is nonincreasing

Let $R = 5.5666305$ and for
real $y \ge e^{673}$ let

$$
a(y) = \log^6 y \cdot 121.0961 \Big(\frac{\log y}{R}\Big)^{3/2}
\exp\Big(-2\sqrt{\frac{\log y}{R}}\Big).
$$

Then $a(x) \le a(x_1)$ for all reals $x_1$ and $x$ with $e^{673} \le x_1 \le x$.

This is the paper's function $a$ on $y \ge e^{673}$. The paper prints the statement as
$a_n(x) \le a_n(x_1)$; its proof ($a'(x) < 0$ for $x \ge e^{673}$) and the later use
$a(t) \le a(x_1)$ show that $a_n$ is a typo for $a$.

## Sources

- Christian Axler, *Effective Estimates for Some Functions Defined over Primes*, INTEGERS 24 (2024), Article A34, Lemma 5, with the function `a` defined at the start of Section 6.

Stated but not proved: `MetaMathlibExt.axlerThetaErrorFactor_tail_antitone` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerEffectivePrimeEstimatesWanted.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#axler-theta-error-factor-tail-antitone).

## Dusart's primes in short intervals

For every real number $x \ge 396738$ there is a
prime $p$ with $x < p \le x \bigl(1 + \frac{1}{25 (\log x)^2}\bigr)$, where $\log$ is the natural
logarithm.

## Sources

- Pierre Dusart, arXiv:1002.0442v1, Proposition at source lines 549--552; stable ID `lead:dusart-2010-prime-interval:aee139bd68`.

Stated but not proved: `dusart_2010_prime_interval_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/Dusart2010.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/Dusart2010.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#dusart-2010-prime-interval-bound).

## Dusart's upper bound for $\pi(x)$ for all $x > 1$

Let $\pi(x)$ be the number of primes
$p \le x$ and $\log$ the natural logarithm. For every real number $x > 1$,
$\pi(x) \le \frac{x}{\log x} \bigl(1 + \frac{1.2762}{\log x}\bigr)$.

## Sources

- Pierre Dusart, "Explicit estimates of some functions over primes," *The Ramanujan Journal* 45 (2018), 227-251, Corollary 5.2(d).

Stated but not proved: `dusart_pi_upper` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/Dusart2010.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/Dusart2010.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#dusart-pi-upper).

## Dusart's lower bound for $\pi(x)$ for $x \ge 599$

Let $\pi(x)$ be the number of primes
$p \le x$ and $\log$ the natural logarithm. For every real number $x \ge 599$,
$\frac{x}{\log x} \bigl(1 + \frac{1}{\log x}\bigr) \le \pi(x)$.

## Sources

- Pierre Dusart, "Explicit estimates of some functions over primes," *The Ramanujan Journal* 45 (2018), 227-251, Corollary 5.2(c).

Stated but not proved: `dusart_pi_lower` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/Dusart2010.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/Dusart2010.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#dusart-pi-lower).

## Dusart's asymptotic expansion of $\pi(x)$ with explicit error

Let $\pi(x)$ be the number
of primes $p \le x$ and $\log$ the natural logarithm. For every real number $x \ge 4 \cdot 10^9$
there is a real number $E$ with $|E| \le \frac{7.32}{(\log x)^3}$ such that

$$\pi(x) = \frac{x}{\log x} \Bigl(1 + \frac{1}{\log x} + \frac{2}{(\log x)^2} + E\Bigr).$$

## Sources

- Pierre Dusart, *Explicit estimates of some functions over primes*, Ramanujan J. 45(1) (2018), 227–251, <https://doi.org/10.1007/s11139-016-9839-4>, Theorem 5.1.

Stated but not proved: `MetaMathlibExt.dusart_pi_asymptotic_expansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/DusartPiAsymptoticExpansionWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartPiAsymptoticExpansionWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#dusart-pi-asymptotic-expansion).

## Dusart's second-order lower bound for $\pi(x)$

Let $\pi(x)$ be the number of primes
$p \le x$ and let $\log$ be the natural logarithm. For every real number $x \ge 88789$,

$$\pi(x) \ge \frac{x}{\log x}\left(1 + \frac{1}{\log x} + \frac{2}{(\log x)^2}\right).$$

## Sources

- Pierre Dusart, *Explicit estimates of some functions over primes*, Ramanujan J. 45(1) (2018), 227–251, <https://doi.org/10.1007/s11139-016-9839-4>, Corollary 5.2(e).

Stated but not proved: `MetaMathlibExt.dusart_pi_lower_second_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/DusartPiLowerSecondOrderWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartPiLowerSecondOrderWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#dusart-pi-lower-second-order).

## Dusart's shifted-logarithm lower bound for $\pi(x)$

Let $\pi(x)$ be the number of primes
$p \le x$ and let $\log$ be the natural logarithm. For every real number $x \ge 5393$,
$\pi(x) \ge \frac{x}{\log x - 1}$.

## Sources

- Pierre Dusart, *Explicit estimates of some functions over primes*, Ramanujan J. 45(1) (2018), 227–251, <https://doi.org/10.1007/s11139-016-9839-4>, Corollary 5.3(a).

Stated but not proved: `MetaMathlibExt.dusart_pi_lower_shifted_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/DusartPiLowerShiftedLogWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartPiLowerShiftedLogWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#dusart-pi-lower-shifted-log).

## Dusart's second-order upper bound for $\pi(x)$

Let $\pi(x)$ be the number of primes
$p \le x$ and let $\log$ be the natural logarithm. For every real number $x > 1$,

$$\pi(x) \le \frac{x}{\log x}\left(1 + \frac{1}{\log x} + \frac{2.53816}{(\log x)^2}\right).$$

## Sources

- Pierre Dusart, *Explicit estimates of some functions over primes*, Ramanujan J. 45(1) (2018), 227–251, <https://doi.org/10.1007/s11139-016-9839-4>, Corollary 5.2(f).

Stated but not proved: `MetaMathlibExt.dusart_pi_upper_second_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/DusartPiUpperSecondOrderWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartPiUpperSecondOrderWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#dusart-pi-upper-second-order).

## Dusart's shifted-logarithm upper bound for $\pi(x)$

Let $\pi(x)$ be the number of primes
$p \le x$ and let $\log$ be the natural logarithm. For every real number $x > e^{1.112}$,
$\pi(x) \le \frac{x}{\log x - 1.112}$.

## Sources

- Pierre Dusart, *Explicit estimates of some functions over primes*, Ramanujan J. 45(1) (2018), 227–251, <https://doi.org/10.1007/s11139-016-9839-4>, Corollary 5.3(b).

Stated but not proved: `MetaMathlibExt.dusart_pi_upper_shifted_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/DusartPiUpperShiftedLogWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartPiUpperShiftedLogWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#dusart-pi-upper-shifted-log).

## Counting primes with prime subscripts

Let $\pi(x)$ be the number of primes at most $x$,
and let $\operatorname{Li}(x) = \int_2^x dt / \log t$. Then $\pi(\pi(x)) \sim x / (\log x)^2$ as
the real number $x$ tends to infinity, and there is a constant $A > 0$ such that, as $x \to \infty$,

$$
\pi(\pi(x)) - \operatorname{Li}(\operatorname{Li}(x)) =
O\left(x \exp\left(-A (\log x)^{3/5} (\log \log x)^{-1/5}\right)\right).
$$

## Sources

- Kevin A. Broughan and A. Ross Barnett, "On the Subsequence of Primes Having Prime Subscripts," Journal of Integer Sequences 12 (2009), Article 09.2.3, Theorem, lines 225–234, <https://cs.uwaterloo.ca/journals/JIS/VOL12/Broughan/broughan16.tex>.

Stated but not proved: `MetaMathlibExt.prime_prime_counting_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/PrimePrimeCountingWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/PrimePrimeCountingWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html#prime-prime-counting-asymptotic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Explicit bounds for the prime-counting function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-prime-counting-function)
