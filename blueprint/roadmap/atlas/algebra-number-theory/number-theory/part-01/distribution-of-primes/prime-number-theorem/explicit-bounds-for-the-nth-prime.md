---
declaration: section
origin: cited
lean: MetaMathlibExt.axler_nth_prime_lower_bound, MetaMathlibExt.axler_nth_prime_upper_bound, MetaMathlibExt.mandl_prime_sum_inequality, MetaMathlibExt.primeCounting_gt_div_log_of_seventeen_le, MetaMathlibExt.nthPrime_lt_mul_log_nthPrime, MetaMathlibExt.primeCounting_lt_div_log_sub_eleven_tenths, MetaMathlibExt.nthPrime_lt_mul_log_nthPrime_sub_one, MetaMathlibExt.primeCounting_gt_div_log_sub_one_sub_inv_log
statement: formalized
---

# Explicit bounds for the nth prime

20 results, 20 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html).

## Axler's lower bound for the $n$th prime

For every integer $n \ge 2$, the $n$th prime
$p_n$ (so that $p_1 = 2$) satisfies
$p_n > n \left(\log n + \log\log n - 1 + \frac{\log\log n - 2}{\log n} -
\frac{(\log\log n)^2 - 6 \log\log n + 11.321}{2 \log^2 n}\right)$.

## Sources

- Christian Axler, "New Estimates for the nth Prime Number," Journal of Integer Sequences 22 (2019), Article 19.4.2, Theorem `thm104`, equation (1.14), lines 190--196 of https://cs.uwaterloo.ca/journals/JIS/VOL22/Axler/axler17.tex.

Stated but not proved: `MetaMathlibExt.axler_nth_prime_lower_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerNthPrimeLowerBoundWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerNthPrimeLowerBoundWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#axler-nth-prime-lower-bound).

## Axler's upper bound for the $n$th prime

For every integer $n \ge 46254381$, the $n$th
prime $p_n$ (so that $p_1 = 2$) satisfies
$p_n < n \left(\log n + \log\log n - 1 + \frac{\log\log n - 2}{\log n} -
\frac{(\log\log n)^2 - 6 \log\log n + 10.667}{2 \log^2 n}\right)$.

## Sources

- Christian Axler, "New Estimates for the nth Prime Number," Journal of Integer Sequences 22 (2019), Article 19.4.2, Theorem `thm101`, equation (1.12), lines 160–166 of https://cs.uwaterloo.ca/journals/JIS/VOL22/Axler/axler17.tex. Context at lines 148–158 distinguishes this refinement from the weaker earlier Dusart bound.

Stated but not proved: `MetaMathlibExt.axler_nth_prime_upper_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/AxlerNthPrimeUpperBoundWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/AxlerNthPrimeUpperBoundWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#axler-nth-prime-upper-bound).

## Mandl's inequality for the sum of the first $n$ primes

Let $p_k$ denote the $k$-th
prime, so that $p_1 = 2$. For every natural number $n \ge 9$, twice the sum of the first $n$
primes is at most $n$ times the $n$-th prime: $2(p_1 + \cdots + p_n) \le n \, p_n$.

Dusart proved the inequality for every $n \ge 9$, as quoted by Axler.

## Sources

- Christian Axler, "On a Sequence Involving Prime Numbers," Journal of Integer Sequences 18 (2015), source equation (101), lines 89-107, https://cs.uwaterloo.ca/journals/JIS/VOL18/Axler/axler6.tex.

Stated but not proved: `MetaMathlibExt.mandl_prime_sum_inequality` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlPrimeSumWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlPrimeSumWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#mandl-prime-sum-inequality).

## The Rosser–Schoenfeld lower bound $x / \log x$ for the prime-counting function

For every
real number $x \ge 17$, the number $\pi(x)$ of primes at most $x$ satisfies
$x / \log x < \pi(x)$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 2.

Stated but not proved: `MetaMathlibExt.primeCounting_gt_div_log_of_seventeen_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#prime-counting-gt-div-log-of-seventeen-l).

## For $n \ge 7$, the $n$th prime is less than $n$ times its logarithm

For every integer
$n \ge 7$, the $n$th prime $p_n$ (counting from $p_1 = 2$) satisfies $p_n < n \log p_n$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 2, inequality (2).

Stated but not proved: `MetaMathlibExt.nthPrime_lt_mul_log_nthPrime` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#nth-prime-lt-mul-log-nth-prime).

## Dusart's upper bound $x / (\log x - 1.1)$ for the prime-counting function

For every
real number $x \ge 60184$, the number $\pi(x)$ of primes at most $x$ satisfies
$\pi(x) < x / (\log x - 1.1)$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 3.

Stated but not proved: `MetaMathlibExt.primeCounting_lt_div_log_sub_eleven_tenths` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#prime-counting-lt-div-log-sub-eleven-ten).

## An upper bound for the $n$-th prime in terms of its logarithm

Let $p_n$ denote the
$n$-th prime, so that $p_1 = 2$. For every integer $n \ge 711$, $p_n < n(\log p_n - 1)$.

Here $711 = \pi(5393)$, where $\pi(x)$ denotes the number of primes at most $x$. The paper's
companion inequality (3) is not included: it fails at $n = 6076$, where $p_{6076} = 60169$ and
$6076(\log 60169 - 1.1) \approx 60182.2$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 3, inequality (4).

Stated but not proved: `MetaMathlibExt.nthPrime_lt_mul_log_nthPrime_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#nth-prime-lt-mul-log-nth-prime-sub-one).

## Lower bound $x / (\log x - 1 - 1 / \log x)$ for the prime-counting function

For every
real number $x \ge 468049$, the number $\pi(x)$ of primes at most $x$ satisfies
$\pi(x) > x / (\log x - 1 - 1 / \log x)$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 4.

Stated but not proved: `MetaMathlibExt.primeCounting_gt_div_log_sub_one_sub_inv_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#prime-counting-gt-div-log-sub-one-sub-in).

## A second-order upper bound for the $n$-th prime in terms of its logarithm

Let $p_n$
denote the $n$-th prime, so that $p_1 = 2$. For every integer $n \ge 39071$,

$$p_n < n\left(\log p_n - 1 - \frac{1}{\log p_n}\right).$$

Here $39071 = \pi(468049)$, where $\pi(x)$ denotes the number of primes at most $x$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 4, inequality (5).

Stated but not proved: `MetaMathlibExt.nthPrime_lt_mul_log_nthPrime_sub_one_sub_inv_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#nth-prime-lt-mul-log-nth-prime-sub-one-s).

## Lower bound for $\log n$ in terms of the logarithm of the $n$-th prime

Let $p_n$ denote
the $n$-th prime, so that $p_1 = 2$. For every integer $n \ge 234057667276344608$,
$\log n \ge 0.914 \log p_n$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 6, inequality (15).

Stated but not proved: `MetaMathlibExt.mul_log_nthPrime_le_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#mul-log-nth-prime-le-log).

## An explicit inequality between $n$ and the $n$th prime

For every integer $n \ge 1$, the
$n$th prime $p_n$ (counting from $p_1 = 2$) satisfies

$$118.676119576 \, n^2 (\log p_n)^3 + 709.7856 \, n \, p_n (\log p_n)^2
< 937.5 \, p_n^2 \log p_n + 5674.5 \, p_n^2.$$

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Proposition 1.

Stated but not proved: `MetaMathlibExt.nthPrime_sq_log_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#nth-prime-sq-log-bound).

## An auxiliary inequality in $\log n$ and $\log\log n$

For every integer $n \ge 2$, with
$L = \log n$,

$$\frac{4.151332(\log L - 2)}{L} + \frac{3.151332(\log L - 1)}{L} +
\frac{3.151332(\log L - 2)}{L^2} \le 1.$$

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Proposition 3, inequality (25).

Stated but not proved: `MetaMathlibExt.loglog_ratio_sum_le_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#loglog-ratio-sum-le-one).

## Lower bounds for the $n$-th prime in terms of its logarithm

Let $p_n$ denote the $n$-th
prime, so that $p_1 = 2$, and put $L = \log p_n$. Then
$p_n > n\left(L - 1 - \frac{1.109}{L}\right)$ for every integer $n \ge 2621506158680$,
$p_n > n\left(L - 1 - \frac{1}{L} - \frac{3.48}{L^2}\right)$ for every integer
$n \ge 4605081012945$,
$p_n > n\left(L - 1 - \frac{1}{L} - \frac{3.024334}{L^2} - \frac{14.893}{L^3}\right)$ for every
integer $n \ge 4514634967572$, and
$p_n > n\left(L - 1 - \frac{1}{L} - \frac{3.024334}{L^2} - \frac{12.975666}{L^3} -
\frac{79.962}{L^4}\right)$ for every integer $n \ge 8$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Corollary 1.

Stated but not proved: `MetaMathlibExt.nthPrime_gt_mul_log_sub_corollary_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#nth-prime-gt-mul-log-sub-corollary-one).

## Zhang–Xiong upper bounds for the $n$th prime

Let $p_n$ be the $n$th prime (counting from
$p_1 = 2$) and $L = \log p_n$. Set $c_2 = 2.975666$, $c_3 = 13.024334$, $c_4 = 70.951332$,
$c_5 = 460.634397856444$ and $c_6 = 3444.031844143556$, and set $N_2 = 3278841$,
$N_3 = 355193892$, $N_4 = 6226419706$, $N_5 = 38900733192$ and $N_6 = 64497259289$.
Then for each $k \in \{2, 3, 4, 5, 6\}$ and every integer $n \ge N_k$,

$$
p_n < n \left(L - 1 - \frac{1}{L} - \sum_{j=2}^{k} \frac{c_j}{L^j}\right).
$$

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Corollary 2.

Stated but not proved: `MetaMathlibExt.nthPrime_lt_mul_log_sub_corollary_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#nth-prime-lt-mul-log-sub-corollary-two).

## Lower bound for the logarithm of the $n$-th prime

Let $p_n$ denote the $n$-th prime, so
that $p_1 = 2$. For every integer $n \ge 3$,

$$\log p_n \ge \log n + \log\log n + \log\left(1 + \frac{\log\log n - 1}{\log n}\right).$$

The paper states this for all positive integers $n$; the right side is undefined at $n = 1$
(where $\log\log 1$ appears) and at $n = 2$ (where the last logarithm's argument is about
$-0.9715$), so $n \ge 3$ is assumed.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 8, inequality (17).

Stated but not proved: `MetaMathlibExt.log_nthPrime_ge_log_add_loglog` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#log-nth-prime-ge-log-add-loglog).

## Bounds for $n$ times the $n$-th prime minus the sum of the first $n$ primes

Let $p_k$
denote the $k$-th prime, so that $p_1 = 2$, and for $n \ge 1$ put $L = \log p_n$ and
$S(n) = n p_n - \sum_{k=1}^{n} p_k$. For every integer $n \ge 440200309$,

$$S(n) \ge p_n^2\left(\frac{1}{2L} + \frac{3}{4L^2} + \frac{7}{4L^3} + \frac{44.4}{8L^4} +
\frac{92.1}{4L^5} + \frac{937.5}{8L^6} + \frac{5674.5}{8L^7} + \frac{79789.5}{16L^8}\right),$$

and for every integer $n \ge 1$,

$$S(n) \le p_n^2\left(\frac{1}{2L} + \frac{3}{4L^2} + \frac{7}{4L^3} + \frac{45.6}{8L^4} +
\frac{93.9}{4L^5} + \frac{952.5}{8L^6} + \frac{5755.5}{8L^7} + \frac{116371}{16L^8}\right).$$

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Lemma 9.

Stated but not proved: `MetaMathlibExt.mul_nthPrime_sub_sum_primes_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#mul-nth-prime-sub-sum-primes-bounds).

## Explicit lower bound in Mandl's inequality

Let $p_k$ denote the $k$-th prime, so that
$p_1 = 2$. For every integer $n \ge 4605081012945$, put $\ell = \log n$, $L = \log p_n$,
$M(n) = \frac{n p_n}{2} - \sum_{k=1}^{n} p_k$ and

$$\omega(n) = \frac{3.151332\,\ell^2}{4L^2} + \frac{\ell^2}{4L} + \frac{16.7\,\ell^2}{4L^3} -
\frac{\ell}{4} + \frac{\log \ell}{4}.$$

Then

$$M(n) > \frac{n^2}{4} + \frac{n^2}{4\ell} - \frac{n^2 \log \ell}{4\ell^2} +
\frac{\omega(n)\, n^2}{\ell^2}.$$

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Proposition 2.

Stated but not proved: `MetaMathlibExt.mandl_sum_gt_omega_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#mandl-sum-gt-omega-bound).

## Explicit upper bound in Mandl's inequality

Let $p_k$ denote the $k$-th prime, so that
$p_1 = 2$. For every integer $n \ge 64497259289$, put $\ell = \log n$, $L = \log p_n$,
$M(n) = \frac{n p_n}{2} - \sum_{k=1}^{n} p_k$,

$$\tau = 34.6L^3 + 205.592008L^2 + 1420.426661948448L + 28890.293784512888$$

and

$$\Omega(n) = \frac{\ell^2}{4L} + \frac{3.848668\,\ell^2}{4L^2} - \frac{\ell}{4} +
\frac{\log \ell}{4} + \frac{\tau\,\ell^2}{8L^6}.$$

Then

$$M(n) < \frac{n^2}{4} + \frac{n^2}{4\ell} - \frac{n^2 \log \ell}{4\ell^2} +
\frac{\Omega(n)\, n^2}{\ell^2}.$$

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Proposition 4.

Stated but not proved: `MetaMathlibExt.mandl_sum_lt_Omega_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#mandl-sum-lt-omega-bound).

## Zhang–Xiong refinement of Mandl's inequality

Let $p_k$ denote the $k$-th prime, so that
$p_1 = 2$, and let $M(n) = \frac{n p_n}{2} - \sum_{k=1}^{n} p_k$. For real $\eta$ let

$$B_\eta(n) = \frac{n^2}{4}\left(1 + \frac{1}{\log n} -
\frac{\log\log n - \eta}{(\log n)^2}\right).$$

With $\alpha = 3.151332$ and $\beta = 4.168668$, we have $B_\alpha(n) < M(n)$ for every integer
$n \ge 234057667276344608$, and $M(n) < B_\beta(n)$ for every integer $n \ge 64497259289$.

## Sources

- Qianxi Zhang and Xinhua Xiong, *New Refinements of Mandl's Inequality*, INTEGERS 25 (2025), Article A58, Theorem 1.

Stated but not proved: `MetaMathlibExt.mandl_sum_between_B_alpha_B_beta` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/MandlRefinementsWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#mandl-sum-between-b-alpha-b-beta).

## Rosser's lower bound for the $n$th prime

For every positive integer $n$, the $n$th prime
$p_n$ (counting from $p_1 = 2$) satisfies $p_n > n \log n$.

For $n = 1$ the bound reads $2 > 0$.

## Sources

- Christian Axler, "New Estimates for the nth Prime Number", Journal of Integer Sequences 22 (2019), Article 19.4.2, equation (1.3), line 115, with Rosser's theorem stated at lines 115–120, attributed there to Rosser, <https://cs.uwaterloo.ca/journals/JIS/VOL22/Axler/axler17.tex>.

Stated but not proved: `MetaMathlibExt.rosser_nthPrime_lower_bound_zeroBased` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/RosserNthPrimeWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/RosserNthPrimeWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html#rosser-nth-prime-lower-bound-zero-based).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Explicit bounds for the nth prime](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-bounds-for-the-nth-prime)
