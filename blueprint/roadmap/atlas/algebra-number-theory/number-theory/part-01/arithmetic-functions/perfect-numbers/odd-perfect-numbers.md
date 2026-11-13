---
declaration: section
origin: cited
lean: MetaMathlibExt.EulerianForm, MetaMathlibExt.IsEulerPrime, MetaMathlibExt.euler_odd_perfect_form, MetaMathlibExt.prod_one_sub_inv_le_of_prefix_prod_le, MetaMathlibExt.hbcAdmissible_half_first_le, MetaMathlibExt.oddPerfect_minFac_lt, MetaMathlibExt.oddPerfect_five_le_card_primeFactors, MetaMathlibExt.finite_setOf_oddPerfect_card_primeFactors_eq
statement: formalized
---

# Odd perfect numbers

43 results, 3 proved and 40 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html).

## Eulerian form of an odd perfect number

For natural numbers $N$, $q$, $k$ and $n$, the
quadruple $(N, q, k, n)$ is in Eulerian form when $N$ is an odd perfect number, $q$ is prime,
$N = q^k n^2$, $q \equiv 1 \pmod 4$, $k \equiv 1 \pmod 4$, and $q$ and $n$ are coprime.

Formalized by `MetaMathlibExt.EulerianForm`, a definition declared in [MathlibExt/NumberTheory/EulerPrime.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EulerPrime.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#eulerian-form).

## Euler prime of an odd perfect number

A natural number $q$ is an Euler prime of a natural
number $N$ when there are natural numbers $k$ and $n$ such that $(N, q, k, n)$ is in Eulerian
form: $N$ is an odd perfect number, $q$ is prime, $N = q^k n^2$, $q \equiv 1 \pmod 4$,
$k \equiv 1 \pmod 4$, and $q$ and $n$ are coprime.

Formalized by `MetaMathlibExt.IsEulerPrime`, a definition declared in [MathlibExt/NumberTheory/EulerPrime.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EulerPrime.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#is-euler-prime).

## Euler's theorem on odd perfect numbers

Every odd perfect number $n$ can be written as
$n = q^s m^2$ with natural numbers $q$, $s$ and $m$, where $q$ is prime, $q \equiv 1 \pmod 4$,
$s \equiv 1 \pmod 4$, and $q$ and $m$ are coprime.

The statement is conditional: whether an odd perfect number exists remains open.

Formalized by `MetaMathlibExt.euler_odd_perfect_form`, a theorem declared in [MathlibExt/NumberTheory/EulerPrime.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EulerPrime.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#euler-odd-perfect-form).

## Comparison of products of $1 - 1/x$ under prefix-product domination

Let $k \ge 0$ and let
$z_1 \le \dots \le z_k$ and $y_1 \le \dots \le y_k$ be real numbers, all greater than $1$, such
that $z_1 \cdots z_l \le y_1 \cdots y_l$ for every $l$ with $0 \le l \le k$ (for $l = 0$ both sides
are the empty product). Then $\prod_{i=1}^k (1 - 1/z_i) \le \prod_{i=1}^k (1 - 1/y_i)$, with
equality if and only if $z_i = y_i$ for all $i$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 2, citing its reference [4].

Stated but not proved: `MetaMathlibExt.prod_one_sub_inv_le_of_prefix_prod_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#prod-one-sub-inv-le-of-prefix-prod-le).

## First-element bounds for HBC-admissible tuples at $1/2$

Let $k \ge 1$ and let
$y_1 < y_2 < \dots < y_k$ be positive integers with
$\prod_{i=1}^{k} (1 - 1/y_i) \le 1/2 < \prod_{i=1}^{k-1} (1 - 1/y_i)$. Then $y_1 \le k + 1$; if
every $y_i$ is odd, then $y_1 < 2(k + 3)/3$; and if every $y_i$ is prime, then $y_1 < 3k/7 + 3$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 5.

Stated but not proved: `MetaMathlibExt.hbcAdmissible_half_first_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#hbc-admissible-half-first-le).

## A linear bound on the smallest prime divisor of an odd perfect number

If $N$ is an odd
perfect number with $m$ distinct prime divisors, then the smallest prime divisor $p_1$ of $N$
satisfies $p_1 < 3m/7 + 3$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 6.

Stated but not proved: `MetaMathlibExt.oddPerfect_minFac_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-min-fac-lt).

## Sylvester's bound on the number of prime divisors of an odd perfect number

Every odd
perfect number has at least five distinct prime divisors.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (ii).

Stated but not proved: `MetaMathlibExt.oddPerfect_five_le_card_primeFactors` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-five-le-card-prime-factors).

## Dickson's finiteness theorem for odd perfect numbers

For every natural number $m$, there
are only finitely many odd perfect numbers with exactly $m$ distinct prime divisors.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (iii).

Stated but not proved: `MetaMathlibExt.finite_setOf_oddPerfect_card_primeFactors_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#finite-set-of-odd-perfect-card-prime-fac).

## Steuerwald's theorem on odd perfect numbers

If $N$ is an odd perfect number, then $N$ has
a prime divisor whose exponent in the prime factorization of $N$ is even and different from $2$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (iv).

Stated but not proved: `MetaMathlibExt.oddPerfect_exists_even_factorization_ne_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-exists-even-factorization-ne).

## McDaniel's exponent bound for odd perfect numbers below $10^{9118}$

If $N$ is an odd
perfect number with $N < 10^{9118}$, then $N$ has a prime divisor whose exponent in the prime
factorization of $N$ is at least $6$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (v).

Stated but not proved: `MetaMathlibExt.oddPerfect_exists_six_le_factorization_of_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-exists-six-le-factorization).

## Odd perfect numbers not divisible by three have at least eleven prime divisors

Every odd
perfect number that is not divisible by $3$ has at least $11$ distinct prime divisors. This is due
to Kishore (1981) and Hagis (1983).

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (vi).

Stated but not proved: `MetaMathlibExt.oddPerfect_eleven_le_card_primeFactors_of_not_three_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-eleven-le-card-prime-factors).

## Nielsen's bound on the number of prime divisors of an odd perfect number

Every odd perfect
number $N$ has at least ten distinct prime divisors, and at least twelve if $3$ does not divide $N$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (vii).

Stated but not proved: `MetaMathlibExt.oddPerfect_ten_le_card_primeFactors` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-ten-le-card-prime-factors).

## Zelinsky's bound on the smallest prime divisor of an odd perfect number

If $N$ is an odd
perfect number with $m$ distinct prime divisors, then the smallest prime divisor $p$ of $N$
satisfies $p < (m - 1)/2$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (viii).

Stated but not proved: `MetaMathlibExt.oddPerfect_minFac_lt_card_sub_one_div_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-min-fac-lt-card-sub-one-div).

## Ochem–Rao lower bound for odd perfect numbers

Every odd perfect number exceeds $10^{1500}$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (ix).

Stated but not proved: `MetaMathlibExt.ten_pow_fifteen_hundred_lt_of_oddPerfect` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#ten-pow-fifteen-hundred-lt-of-odd-perfec).

## Goto–Ohno–Iannucci bounds on the largest prime divisors of an odd perfect number

If $N$ is
an odd perfect number, then $N$ has three distinct prime divisors $p$, $q$, $r$ with
$p \ge 10^8$, $q \ge 10^4$ and $r \ge 100$. Equivalently, the largest, second largest and third
largest prime divisors of $N$ are at least $10^8$, $10^4$ and $100$ respectively.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 1 (x).

Stated but not proved: `MetaMathlibExt.oddPerfect_exists_three_large_prime_divisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-exists-three-large-prime-div).

## Product identities for calibrating numbers

Let $a$ and $d$ be positive integers and let
$k \ge 1$. Put $\alpha = (a + d)/d$, and let $n_i = 1 + \alpha^{2^{i-1}}$ for $1 \le i < k$ and
$n_k = \alpha^{2^{k-1}}$ (the calibrating numbers for $a/(a + d)$). Then
$\prod_{i=1}^{k} (1 - 1/n_i) = a/(a + d)$; for every $j$ with $1 \le j < k$,
$\prod_{i=1}^{j} n_i = (d/a)(\alpha^{2^j} - 1)$; and
$\prod_{i=1}^{k} n_i = (d/a)(\alpha^{2^k} - \alpha^{2^{k-1}})$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 3.

Stated but not proved: `MetaMathlibExt.hbcCalibrating_prod_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#hbc-calibrating-prod-identities).

## Stone's product bound for HBC-admissible tuples

Let $a$ and $d$ be coprime positive
integers, let $k \ge 1$, and let $y_1 < y_2 < \dots < y_k$ be positive integers with
$\prod_{i=1}^{k} (1 - 1/y_i) \le a/(a + d) < \prod_{i=1}^{k-1} (1 - 1/y_i)$ (the source calls such
a tuple HBC-admissible for $a/(a + d)$). Put $\alpha = (a + d)/d$, let $n_i = 1 + \alpha^{2^{i-1}}$
for $1 \le i < k$ and $n_k = \alpha^{2^{k-1}}$, and let $F_k(x) = x^{2^k} - x^{2^{k-1}}$. Then some
$\kappa$ with $1 \le \kappa \le k$ has $\prod_{i=1}^{\kappa} y_i \le \prod_{i=1}^{\kappa} n_i$.
Moreover, let $\kappa$ with $1 \le \kappa \le k$ satisfy this inequality while every $\kappa'$ with
$\kappa < \kappa' \le k$ satisfies $\prod_{i=1}^{\kappa'} n_i < \prod_{i=1}^{\kappa'} y_i$, so that
$\kappa$ is the largest such index. If $\kappa < k$, then
$a \prod_{i=1}^{k} y_i \le F_k(\alpha d^{1/2^{\kappa}})$; if $\kappa = k$, then
$a \prod_{i=1}^{k} y_i \le d \, F_k(\alpha)$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Theorem 1.

Stated but not proved: `MetaMathlibExt.hbcAdmissible_exists_prefix_le_and_prod_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#hbc-admissible-exists-prefix-le-and-prod).

## Stone's $\sqrt{d}$ product bound for HBC-admissible tuples

Let $a$ and $d$ be coprime
positive integers, let $k \ge 1$, and let $y_1 < y_2 < \dots < y_k$ be positive integers with
$\prod_{i=1}^{k} (1 - 1/y_i) \le a/(a + d) < \prod_{i=1}^{k-1} (1 - 1/y_i)$. Put
$\beta = (a + d)/\sqrt{d}$. Then $a \prod_{i=1}^{k} y_i \le \beta^{2^k} - \beta^{2^{k-1}}$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Corollary 1.

Stated but not proved: `MetaMathlibExt.hbcAdmissible_prod_le_sqrt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#hbc-admissible-prod-le-sqrt).

## Stone's $d^{3/4}$ product bound for HBC-admissible tuples

Let $a$ and $d$ be coprime
positive integers, let $k \ge 2$, and let $y_1 < y_2 < \dots < y_k$ be positive integers with
$\prod_{i=1}^{k} (1 - 1/y_i) \le a/(a + d) < \prod_{i=1}^{k-1} (1 - 1/y_i)$ and
$y_1 \ne \lfloor 1 + (a + d)/d \rfloor$. Put $\beta = (a + d)/d^{3/4}$. Then
$a \prod_{i=1}^{k} y_i \le \beta^{2^k} - \beta^{2^{k-1}}$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Corollary 2.

Stated but not proved: `MetaMathlibExt.hbcAdmissible_prod_le_of_ne_floor` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#hbc-admissible-prod-le-of-ne-floor).

## Product bound for HBC-admissible tuples at $7/10$

Let $k \ge 3$ and let
$y_1 < y_2 < \dots < y_k$ be positive integers with
$\prod_{i=1}^{k} (1 - 1/y_i) \le 7/10 < \prod_{i=1}^{k-1} (1 - 1/y_i)$. Then
$\prod_{i=1}^{k} y_i \le \frac{2}{7}\bigl(\sqrt{15}^{\,2^k} - \sqrt{15}^{\,2^{k-1}}\bigr)$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 4.

Stated but not proved: `MetaMathlibExt.hbcAdmissible_seven_tenths_prod_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#hbc-admissible-seven-tenths-prod-le).

## Product bounds for prime tuples at $1/2$ by size of the first prime

Let
$p_1 < p_2 < \dots < p_k$ be primes with
$\prod_{i=1}^{k} (1 - 1/p_i) \le 1/2 < \prod_{i=1}^{k-1} (1 - 1/p_i)$ and $p_1 \ge 5$, and let
$F_k(x) = x^{2^k} - x^{2^{k-1}}$ and $P = \prod_{i=1}^{k} p_i$. Then $P \le F_k(\sqrt{8/3^{7/8}})$.
Moreover, if $6 \le p_1 < 18$, then $P \le F_k(\sqrt{12/5^{15/16}})$; if $18 \le p_1 < 258$, then
$P \le F_k(\sqrt{512/255^{31/32}})$; and if $p_1 \ge 258$, then
$P \le F_k\bigl(\sqrt{2^{5/4} (2^{16} + 1)/2^{16}}\bigr)$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 7.

Stated but not proved: `MetaMathlibExt.hbcAdmissible_half_prime_prod_le_of_five_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#hbc-admissible-half-prime-prod-le-of-fiv).

## Product bound for prime tuples at $1/2$ starting at $5$

Let $p_1 < p_2 < \dots < p_k$ be
primes with $\prod_{i=1}^{k} (1 - 1/p_i) \le 1/2 < \prod_{i=1}^{k-1} (1 - 1/p_i)$ and $p_1 = 5$.
Put $x = \sqrt{8/3^{31/32}}$. Then $\prod_{i=1}^{k} p_i \le x^{2^k} - x^{2^{k-1}}$.

## Sources

- Andrew Stone, *Improved Upper Bounds for Odd Perfect Numbers -- Part I*, INTEGERS 24 (2024), Article A114, Lemma 8.

Stated but not proved: `MetaMathlibExt.hbcAdmissible_half_prime_prod_le_of_eq_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectHBCAdmissibleWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#hbc-admissible-half-prime-prod-le-of-eq).

## Zelinsky's upper bound on the prime reciprocal sum of an odd perfect number

Let $n$ be an
odd perfect number whose least prime factor $p_1$ satisfies $p_1 \ge 11$, and let
$T(n) = \sum_{p \mid n} 1/p$, the sum over the primes $p$ dividing $n$. Then
$T(n) < \log 2 - \frac{11}{50 p_1^2}$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Corollary 1.

Stated but not proved: `MetaMathlibExt.oddPerfect_primeReciprocalSum_lt_log_two_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-prime-reciprocal-sum-lt-log).

## Surplus of an odd perfect number with least prime factor at least 11

Let $n$ be an odd
perfect number whose least prime factor $p_1$ satisfies $p_1 \ge 11$, and let
$H(n) = \prod_{p \mid n} p/(p-1)$, the product over the primes $p$ dividing $n$. Then its surplus
$H(n) - 2$ satisfies $H(n) - 2 < \frac{25}{8 p_1 \log p_1}$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Corollary 2.

Stated but not proved: `MetaMathlibExt.oddPerfect_abundancySup_sub_two_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-abundancy-sup-sub-two-lt).

## Exponential lower bound for $1 + x + x^2$ on $(0, 1/11)$

For every real $x$ with
$0 \le x \le 1/11$, $\exp(x + 2x^2/5) \le 1 + x + x^2$, with equality if and only if $x = 0$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Lemma 3.

Stated but not proved: `MetaMathlibExt.exp_add_two_fifths_sq_le_one_add_add_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#exp-add-two-fifths-sq-le-one-add-add-sq).

## Lower bound for the prime-counting function at primes $p \ge 19$

For every prime
$p \ge 19$, the number $\pi(p)$ of primes at most $p$ satisfies $\pi(p) \ge p/\log p + 1$,
where $\log$ is the natural logarithm.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Lemma 4.

Stated but not proved: `MetaMathlibExt.div_log_add_one_le_primeCounting` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#div-log-add-one-le-prime-counting).

## Tail bound for the sum of $1/p^2$ over primes

Let $q \ge 3$ be a prime and let
$M(q) = \sum_{p \ge q} 1/p^2$ be the sum over all primes $p \ge q$. Then
$M(q) < \frac{1}{q \log q}\left(1 + \frac{2 \log \log q}{\log q}\right)$,
where $\log$ is the natural logarithm.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Lemma 6.

Stated but not proved: `MetaMathlibExt.tsum_one_div_sq_primes_ge_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#tsum-one-div-sq-primes-ge-lt).

## Bound on the tail of the prime product of $p^2/(p^2-1)$

Let $q$ be an odd prime. Then
$\sum_{p \ge q} \log \frac{p^2}{p^2-1} \le
\frac{1}{q \log q}\left(1 + \frac{2 \log \log q}{\log q}\right) + \frac{4}{q^3}$,
where the sum runs over the primes $p \ge q$. Equivalently, $\log E$ is at most this bound,
where $E = \prod_{p \ge q} \frac{p^2}{p^2-1}$ is the product over the primes $p \ge q$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Lemma 7.

Stated but not proved: `MetaMathlibExt.tsum_log_sq_div_sq_sub_one_primes_ge_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#tsum-log-sq-div-sq-sub-one-primes-ge-le).

## Upper bound for $\log(1 + 1/(x-1))$

For every integer $x \ge 2$,
$\log(1 + 1/(x-1)) \le 1/x + 25/(32x^2)$, where $\log$ is the natural logarithm.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Lemma 8.

Stated but not proved: `MetaMathlibExt.log_one_add_one_div_sub_one_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#log-one-add-one-div-sub-one-le).

## Suryanarayana's bound for $H(n)/h(n)$ with one odd exponent

For a positive integer
$n$ write $h(n) = \sigma(n)/n$ for its abundancy index, where $\sigma(n)$ is the sum of the
divisors of $n$, and $H(n) = \prod_{p \mid n} p/(p-1)$ for the product over its prime divisors.
Let $n$ be odd and let $j$ be a prime divisor of $n$ whose exponent in $n$ is odd, while the
exponent of every other prime divisor of $n$ is even. Then

$$\frac{H(n)}{h(n)} \le \frac{j^2}{j^2 - 1} \prod_{p \mid n,\ p \ne j} \frac{p^3}{p^3 - 1},$$

where $p$ runs over the prime divisors of $n$ other than $j$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Lemma 9.

Stated but not proved: `MetaMathlibExt.abundancySup_div_abundancyIndex_le_of_single_odd_exponent` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#abundancy-sup-div-abundancy-index-le-of).

## Odd perfect numbers divisible by 165 contain 5 exactly once

If $n$ is an odd perfect
number divisible by $165$, then $5$ divides $n$ exactly once: $5 \mid n$ but $25 \nmid n$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Lemma 11.

Stated but not proved: `MetaMathlibExt.oddPerfect_factorization_five_eq_one_of_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-factorization-five-eq-one-of).

## Bound on a prime that pushes $\prod p/(p-1)$ past $2$

Let $s$ be a finite set of odd
primes with $\prod_{p \in s} p/(p-1) \le 2$, and let $q$ be an odd prime with
$\left(\prod_{p \in s} p/(p-1)\right) \cdot q/(q-1) > 2$. Then
$q \le 2 \prod_{p \in s} (p - 1) - 1$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Lemma 12.

Stated but not proved: `MetaMathlibExt.le_two_mul_prod_sub_one_sub_one_of_two_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#le-two-mul-prod-sub-one-sub-one-of-two-l).

## Cohen–Hagis–Suryanarayana bounds on the prime reciprocal sum of an odd perfect number

Let $n$ be an odd perfect number and $T(n) = \sum_{p \mid n} 1/p$, the sum over the primes $p$
dividing $n$. If $\gcd(15, n) = 1$ then $T(n) \le 0.693148$; if $\gcd(15, n) = 3$ then
$T(n) \le 0.657304$; if $\gcd(15, n) = 5$ then $T(n) \le 0.678036$; and if $\gcd(15, n) = 15$
then $T(n) \le 0.673770$.

The source table also gives lower bounds, which are not stated here.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 1, Table 1.

Stated but not proved: `MetaMathlibExt.oddPerfect_primeReciprocalSum_le_of_gcd_fifteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-prime-reciprocal-sum-le-of-g).

## Suryanarayana's bounds on the prime product of an odd perfect number

Let $n$ be an odd
perfect number and $H(n) = \prod_{p \mid n} p/(p-1)$, the product over the primes $p$ dividing $n$.
If $\gcd(15, n) = 1$ then $H(n) \le 2.014754$; if $\gcd(15, n) = 3$ then $H(n) \le 2.096234$;
if $\gcd(15, n) = 5$ then $H(n) \le 2.031002$; and if $\gcd(15, n) = 15$ then
$H(n) \le 2.165439$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 2, Table 2.

Stated but not proved: `MetaMathlibExt.oddPerfect_abundancySup_le_of_gcd_fifteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-abundancy-sup-le-of-gcd-fift).

## Lower bound on the prime reciprocal sum of a primitive non-deficient number

Let $n$ be a
primitive non-deficient number with least prime factor $p_1$, let $T(n) = \sum_{p \mid n} 1/p$
and $H(n) = \prod_{p \mid n} p/(p-1)$, with the sum and product over the primes $p$ dividing $n$,
and let $S = H(n) - 2$ be the surplus of $n$. Then
$T(n) \ge \log 2 - \frac{25}{64 p_1} + \frac{S}{2} - \frac{S^2}{4}$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 3.

Stated but not proved: `MetaMathlibExt.primitiveNondeficient_primeReciprocalSum_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#primitive-nondeficient-prime-reciprocal).

## Upper bound on the prime reciprocal sum of a primitive non-deficient number with one odd exponent

**Upper bound on the prime reciprocal sum of a primitive non-deficient number with one odd
exponent.** Let $n$ be a primitive non-deficient number with least prime factor $p_1 \ge 11$,
and let $t$ be a prime factor of $n$ such that the exponent of $t$ in $n$ is odd and the exponent
of every other prime factor of $n$ is even. Suppose $2 p_1 \le t + 2$, and let
$T(n) = \sum_{p \mid n} 1/p$, the sum over the primes $p$ dividing $n$. Then
$T(n) < \log 2 - \frac{11}{50 p_1^2}$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 4.

Stated but not proved: `MetaMathlibExt.primitiveNondeficient_primeReciprocalSum_lt_of_single_odd_exponent` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#primitive-nondeficient-prime-reciprocal-2).

## Bound on the prime product of an odd perfect number via its least prime factor

Let $n$ be
an odd perfect number with least prime factor $p_1$, and let $H(n) = \prod_{p \mid n} p/(p-1)$,
the product over the primes $p$ dividing $n$. Then $H(n) \le 2 + \frac{9}{4 p_1^2}$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 5.

Stated but not proved: `MetaMathlibExt.oddPerfect_abundancySup_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-perfect-abundancy-sup-le).

## Lower bound on the prime reciprocal sum of an odd primitive non-deficient number

Let $n$
be an odd primitive non-deficient number with least prime factor $p_1$, let
$T(n) = \sum_{p \mid n} 1/p$ and $H(n) = \prod_{p \mid n} p/(p-1)$, with the sum and product over
the primes $p$ dividing $n$, and let $S = H(n) - 2$ be the surplus of $n$. Then
$T(n) \ge \log 2 - \frac{25}{32 p_1 \log p_1}
\left(1 + \frac{2 \log \log p_1}{\log p_1}\right) + \frac{S}{2} - \frac{S^2}{4}$.

The hypothesis that $n$ is odd is added: the statement as printed fails at $n = 6$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 7.

Stated but not proved: `MetaMathlibExt.odd_primitiveNondeficient_primeReciprocalSum_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#odd-primitive-nondeficient-prime-recipro).

## Bound on $H(n)$ for primitive non-deficient numbers by the least prime factor

For a
positive integer $n$ write $H(n) = \prod_{p \mid n} p/(p-1)$, the product over the prime
divisors of $n$. There is a real constant $C$ such that every primitive non-deficient number
$n$ with least prime factor $p_1$ satisfies $H(n) \le 2 + C/p_1$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 8.

Stated but not proved: `MetaMathlibExt.exists_abundancySup_le_two_add_div_minFac` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#exists-abundancy-sup-le-two-add-div-min).

## Primes congruent to $-1$ modulo $165$ are not Euler primes

For all natural numbers
$q$ and $N$ with $q \equiv -1 \pmod{165}$, $q$ is not an Euler prime of $N$. In particular, no
prime $q \equiv -1 \pmod{165}$ is the Euler prime of an odd perfect number.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 9.

Stated but not proved: `MetaMathlibExt.not_isEulerPrime_of_mod_165_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#not-is-euler-prime-of-mod-165-eq).

## No odd prime $q$ lifts $H$ of the odd part of $q + 1$ across $2$

For a positive integer
$m$ write $H(m) = \prod_{p \mid m} p/(p-1)$, the product over the prime divisors of $m$, and
$\operatorname{odd}(m)$ for the largest odd divisor of $m$. There is no odd prime $q$ with
$H(\operatorname{odd}(q+1)) < 2$ and $H(q \cdot \operatorname{odd}(q+1)) > 2$.

For $q = 2$ the conclusion fails: $H(3) = 3/2 < 2$ and $H(6) = 3 > 2$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 10.

Stated but not proved: `MetaMathlibExt.not_abundancySup_oddPart_succ_lt_two_and_two_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#not-abundancy-sup-odd-part-succ-lt-two-a).

## Fifth-power bound on the Euler prime of an odd perfect number

If $(n, q, e, m)$ is in
Eulerian form, that is, $n$ is an odd perfect number, $q$ is a prime coprime to $m$,
$n = q^e m^2$ and $q \equiv e \equiv 1 \pmod 4$, then $e = 1$ or $q^5 < 2m^2$, that is,
$q < 2^{1/5} m^{2/5}$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 11.

Stated but not proved: `MetaMathlibExt.eulerianForm_exponent_eq_one_or_pow_five_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#eulerian-form-exponent-eq-one-or-pow-fiv).

## Refined fifth-power bound on the Euler prime of an odd perfect number

If $(n, q, e, m)$
is in Eulerian form, that is, $n$ is an odd perfect number, $q$ is a prime coprime to $m$,
$n = q^e m^2$ and $q \equiv e \equiv 1 \pmod 4$, then $e = 1$ or
$3^2 \cdot 5^2 \cdot 11^2 \cdot 13^2 \cdot q^5 < 2m^2$, that is,
$q < \left(2/(3^2 \cdot 5^2 \cdot 11^2 \cdot 13^2)\right)^{1/5} m^{2/5}$.

## Sources

- Joshua Zelinsky, *The Sum of the Reciprocals of the Prime Divisors of an Odd Perfect or Odd Primitive Non-deficient Number*, INTEGERS 25 (2025), Article A59, Proposition 12.

Stated but not proved: `MetaMathlibExt.eulerianForm_exponent_eq_one_or_mul_pow_five_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/OddPerfectPrimeReciprocalSumWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html#eulerian-form-exponent-eq-one-or-mul-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Odd perfect numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/odd-perfect-numbers)
