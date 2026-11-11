---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSZumkeller, MetaMathlibExt.IsUnitarySZumkeller, MetaMathlibExt.isSZumkeller_sixty, MetaMathlibExt.not_isSZumkeller_six, MetaMathlibExt.isUnitarySZumkeller_sixty, MetaMathlibExt.not_isUnitarySZumkeller_six, MetaMathlibExt.sigma_one_prod_formulas, MetaMathlibExt.sigma_two_prod_formulas
statement: formalized
---

# Zumkeller numbers

37 results, 9 proved and 28 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html).

## s-Zumkeller numbers

A natural number $n$ is s-Zumkeller if its proper divisors can be
split into two disjoint nonempty sets whose elements have equal sums of squares. Each of the two
sums is then $(\sigma_2(n) - n^2)/2$, where $\sigma_2(n)$ is the sum of the squares of the
positive divisors of $n$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Definition 1.

Formalized by `MetaMathlibExt.IsSZumkeller`, a definition declared in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-szumkeller).

## Unitary s-Zumkeller numbers

A natural number $n$ is a unitary s-Zumkeller number when
its proper unitary divisors (the unitary divisors of $n$ other than $n$) split into two nonempty
disjoint sets $A$ and $B$ with equal sums of squares, $\sum_{d \in A} d^2 = \sum_{d \in B} d^2$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Definition 2.

Formalized by `MetaMathlibExt.IsUnitarySZumkeller`, a definition declared in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-unitary-szumkeller).

## $60$ is s-Zumkeller

The number $60$ is s-Zumkeller: the squares of its proper divisors
$1, 2, 5, 30$ sum to $1^2 + 2^2 + 5^2 + 30^2 = 930$, which is half of the sum of the squares of
all proper divisors of $60$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Example 1.

Formalized by `MetaMathlibExt.isSZumkeller_sixty`, a theorem declared in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-szumkeller-sixty).

## The number 6 is not s-Zumkeller

The number $6$ is not an s-Zumkeller number: the squares of
its proper divisors sum to $1^2 + 2^2 + 3^2 = 14$, and they admit no split into two parts with
equal sums.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Section 1.

Formalized by `MetaMathlibExt.not_isSZumkeller_six`, a theorem declared in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#not-is-szumkeller-six).

## The number 60 is unitary s-Zumkeller

The number $60$ is a unitary s-Zumkeller number: its
proper unitary divisors are $1, 3, 4, 5, 12, 15, 20$, and $20^2 + 3^2 + 1^2 = 410$ is half the sum
of their squares.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Example 2.

Formalized by `MetaMathlibExt.isUnitarySZumkeller_sixty`, a theorem declared in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-unitary-szumkeller-sixty).

## The number 6 is not unitary s-Zumkeller

The number $6$ is not a unitary s-Zumkeller
number.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Section 1.

Formalized by `MetaMathlibExt.not_isUnitarySZumkeller_six`, a theorem declared in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#not-is-unitary-szumkeller-six).

## Product formulas for the sum of divisors

Let $n \ne 0$ be a natural number, let
$\sigma(n)$ be the sum of the divisors of $n$, and for each prime $p$ dividing $n$ let $k_p$ be
the exponent of $p$ in $n$. Then, with products over the primes $p$ dividing $n$,

$$\sigma(n) = \prod_{p \mid n} \frac{p^{k_p + 1} - 1}{p - 1}$$

and

$$\frac{\sigma(n)}{n} = \prod_{p \mid n} \frac{p^{k_p + 1} - 1}{p^{k_p} (p - 1)}.$$

If moreover $n > 1$, then $\sigma(n)/n < \prod_{p \mid n} p/(p - 1)$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Lemma 1(i) (quoting Peng and Bhaskara Rao).

Stated but not proved: `MetaMathlibExt.sigma_one_prod_formulas` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#sigma-one-prod-formulas).

## Product formulas for the sum of squared divisors

Let $n \ne 0$ be a natural number,
let $\sigma_2(n)$ be the sum of the squares of the divisors of $n$, and for each prime $p$
dividing $n$ let $k_p$ be the exponent of $p$ in $n$. Then, with products over the primes $p$
dividing $n$,

$$\sigma_2(n) = \prod_{p \mid n} \frac{p^{2(k_p + 1)} - 1}{p^2 - 1}$$

and

$$\frac{\sigma_2(n)}{n^2} = \prod_{p \mid n} \frac{p^{2(k_p + 1)} - 1}{p^{2k_p} (p^2 - 1)}.$$

If moreover $n > 1$, then $\sigma_2(n)/n^2 < \prod_{p \mid n} p^2/(p^2 - 1)$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Lemma 1(ii) (quoting Peng and Bhaskara Rao).

Stated but not proved: `MetaMathlibExt.sigma_two_prod_formulas` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#sigma-two-prod-formulas).

## Number of unitary divisors

A positive integer $n$ with $m$ distinct prime factors has
exactly $2^m$ unitary divisors.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Lemma 2 (quoting Bege).

Stated but not proved: `MetaMathlibExt.card_unitaryDivisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#card-unitary-divisors).

## Sum of squares of unitary divisors

For every positive integer $n$, the sum of the
squares of the unitary divisors of $n$ equals $\prod_{p} \left(1 + p^{2k_p}\right)$, where $p$
ranges over the distinct prime factors of $n$ and $k_p$ is the exponent of $p$ in $n$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Lemma 3(i) (quoting Subbarao and Warren).

Stated but not proved: `MetaMathlibExt.sum_sq_unitaryDivisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#sum-sq-unitary-divisors).

## Properties of even s-Zumkeller numbers

Let $n$ be an even s-Zumkeller number and let
$\sigma_2(n)$ be the sum of the squares of the positive divisors of $n$. Then $\sigma_2(n)$ is
even, some odd prime $p$ divides $n$ with an odd exponent in the prime factorization of $n$, and
$3n^2 \le 2\sigma_2(n)$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 1.

Stated but not proved: `MetaMathlibExt.isSZumkeller_even_props` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-szumkeller-even-props).

## Criterion for even s-Zumkeller numbers

Let $n$ be an even positive integer and let
$\sigma_2(n)$ be the sum of the squares of the positive divisors of $n$. Then $n$ is s-Zumkeller
if and only if there is a (possibly empty) set $S$ of proper divisors of $n$, not containing
$n/2$, such that $4 \sum_{d \in S} d^2 = 2\sigma_2(n) - 3n^2$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 2.

Stated but not proved: `MetaMathlibExt.isSZumkeller_iff_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-szumkeller-iff-of-even).

## Even s-Zumkeller numbers have at least twelve divisors

If $n$ is an even s-Zumkeller
number, then $n$ has at least $12$ positive divisors.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 3.

Stated but not proved: `MetaMathlibExt.twelve_le_card_divisors_of_isSZumkeller` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#twelve-le-card-divisors-of-is-szumkeller).

## Even s-Zumkeller numbers are divisible by 3

If $n$ is an even s-Zumkeller number, then
$3$ divides $n$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 4.

Stated but not proved: `MetaMathlibExt.three_dvd_of_isSZumkeller` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#three-dvd-of-is-szumkeller).

## Even s-Zumkeller numbers are divisible by 6

Every even s-Zumkeller number is divisible
by $6$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Corollary 1.

Stated but not proved: `MetaMathlibExt.six_dvd_of_isSZumkeller` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#six-dvd-of-is-szumkeller).

## A prime-factor product bound for s-Zumkeller numbers

Let $n$ be an s-Zumkeller number
and let $p_1$ be its least prime factor. Then

$$\frac{2}{p_1^2} + 1 < \prod_{p} \frac{p^2}{p^2 - 1},$$

where the product ranges over the distinct prime factors $p$ of $n$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 5.

Stated but not proved: `MetaMathlibExt.two_div_minFac_sq_add_one_lt_prod` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#two-div-min-fac-sq-add-one-lt-prod).

## Even s-Zumkeller numbers have at least three prime factors

If $n$ is an even
s-Zumkeller number, then $n$ has at least $3$ distinct prime factors.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 6(i).

Stated but not proved: `MetaMathlibExt.three_le_card_primeFactors_of_isSZumkeller_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#three-le-card-prime-factors-of-is-szumke).

## Odd s-Zumkeller numbers divisible by $3$ have at least eight prime factors

Every odd
s-Zumkeller number divisible by $3$ has at least $8$ distinct prime factors.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 6(ii).

Stated but not proved: `MetaMathlibExt.eight_le_card_primeFactors_of_isSZumkeller_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#eight-le-card-prime-factors-of-is-szumke).

## Odd s-Zumkeller numbers are perfect squares

Every odd s-Zumkeller number is a perfect
square.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 7.

Stated but not proved: `MetaMathlibExt.isSquare_of_isSZumkeller_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-square-of-is-szumkeller-odd).

## Lower bound for odd s-Zumkeller numbers divisible by 3

Every odd s-Zumkeller number $n$
divisible by $3$ satisfies
$n \ge 12442607161209225 = (3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot 19 \cdot 23)^2$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 8.

Stated but not proved: `MetaMathlibExt.le_of_isSZumkeller_odd_three_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#le-of-is-szumkeller-odd-three-dvd).

## Harmonic mean of squared divisors of even s-Zumkeller numbers

Let $n$ be an even
s-Zumkeller number and let $\tau(n)$ be the number of positive divisors of $n$. Then
$\tau(n) / \sum_{d \mid n} d^{-2} \le 2\tau(n)/3$, where the sum runs over the positive divisors
$d$ of $n$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 9.

Stated but not proved: `MetaMathlibExt.harmonicMeanSq_le_of_isSZumkeller` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#harmonic-mean-sq-le-of-is-szumkeller).

## Harmonic mean of squared divisors of s-Zumkeller numbers $2^\alpha(2^{\alpha+1}-1)$

Let
$\alpha \ge 1$ be an integer, let $n = 2^\alpha (2^{\alpha+1} - 1)$ and let $\tau(n)$ be the
number of positive divisors of $n$. If $n$ is s-Zumkeller, then
$\tau(n) / \sum_{d \mid n} d^{-2} < 2^{2\alpha+3}/3$, where the sum runs over the positive
divisors $d$ of $n$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 10.

Stated but not proved: `MetaMathlibExt.harmonicMeanSq_lt_of_isSZumkeller_mersenne` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#harmonic-mean-sq-lt-of-is-szumkeller-mer).

## Lower bounds for unitary s-Zumkeller numbers

Let $n$ be a unitary s-Zumkeller
number, let $q$ be the least unitary divisor of $n$ greater than $1$, and for each prime $p$
dividing $n$ let $k_p$ be the exponent of $p$ in $n$. Then, with both sums over all unitary
divisors $d$ of $n$ (including $n$ itself), $n^2 (2/q^2 + 1) \le \sum_d d^2$ and
$2/q^2 + 1 \le \sum_d 1/d^2$. Moreover $2/q^2 + 1 \le \prod_{p \mid n} (1 + p^{2k_p})/p^{2k_p}$,
the product running over the primes $p$ dividing $n$.

The number $q$ is the smallest of the prime powers $p^{k_p}$.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 11.

Stated but not proved: `MetaMathlibExt.isUnitarySZumkeller_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-unitary-szumkeller-bounds).

## Unitary divisor counts of unitary s-Zumkeller numbers

Let $n$ be a unitary s-Zumkeller
number and let $q$ be the least unitary divisor of $n$ greater than $1$. If $q = 2$, then $n$ has
more than $2^6$ unitary divisors; if $q = 3$ or $q = 4$, then $n$ has more than $2^2$ unitary
divisors.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 12.

Stated but not proved: `MetaMathlibExt.card_unitaryDivisors_of_isUnitarySZumkeller` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#card-unitary-divisors-of-is-unitary-szum).

## No odd unitary s-Zumkeller numbers

There is no odd unitary s-Zumkeller number.

## Sources

- Jayanta Kalita and Helen K. Saikia, *A Study on Generalized Zumkeller Numbers*, INTEGERS 24 (2024), Article A95, Proposition 13.

Stated but not proved: `MetaMathlibExt.not_isUnitarySZumkeller_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/SZumkellerWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SZumkellerWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#not-is-unitary-szumkeller-of-odd).

## Product of the divisors

For a natural number $n$, $T(n)$ is the product of all positive
divisors of $n$. For $n = 0$ the set of divisors is taken to be empty, so $T(0) = 1$.

Formalized by `MathlibExt.NumberTheory.SuperMZumkellerWanted.divisorProd`, a definition declared in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#divisor-prod).

## Super-m-Zumkeller numbers

For a natural number $n$, let $T(n)$ be the product of the
positive divisors of $n$ (for $n = 0$ the divisor set is taken to be empty, so $T(0) = 1$).
Then $n$ is *super-m-Zumkeller* if there is a set $A$ of positive divisors of $T(n)$ such that
the product of the elements of $A$ equals the product of the positive divisors of $T(n)$ that
are not in $A$; that is, the divisors of $T(n)$ split into two complementary sets, one of which
may be empty, with equal products.

Formalized by `MathlibExt.NumberTheory.SuperMZumkellerWanted.IsSuperMZumkeller`, a definition declared in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-super-mzumkeller).

## $k$-m-perfect numbers

For natural numbers $k$ and $n$, $n$ is $k$-m-perfect if
$T(n) = n^k$, where $T(n)$ is the product of the divisors of $n$.

Formalized by `MathlibExt.NumberTheory.SuperMZumkellerWanted.IsKMPerfect`, a definition declared in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-kmperfect).

## Square of the product of the divisors

For every positive integer $n$, let $T(n)$ be the
product of the positive divisors of $n$ and $\tau(n)$ their number. Then $T(n)^2 = n^{\tau(n)}$.

The paper writes this as $T(n) = n^{\tau(n)/2}$.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.divisorProd_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#divisor-prod-sq).

## Super-m-Zumkeller numbers $n \ge 2$ have at least three divisors

If a natural number
$n \ge 2$ is super-m-Zumkeller, then the number $\tau(n)$ of positive divisors of $n$ satisfies
$\tau(n) \ge 3$.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.three_le_card_divisors_of_isSuperMZumkeller` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#three-le-card-divisors-of-is-super-mzumk).

## Criterion for super-m-Zumkeller numbers

Let $n \ge 2$ be an integer, let $\tau(n)$ be the
number of positive divisors of $n$ and $T(n)$ their product. Then $n$ is super-m-Zumkeller if and
only if $8$ divides $\alpha \cdot \tau(n) \cdot \tau(T(n))$ for every prime $p$ dividing $n$,
where $\alpha$ is the exponent of $p$ in $n$.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.isSuperMZumkeller_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-super-mzumkeller-iff).

## Super-m-Zumkeller prime powers

Let $p$ be a prime and $\alpha \ge 1$ an integer. Then
$p^\alpha$ is super-m-Zumkeller if and only if
$\alpha \equiv 0, 2, 5, 7, 8, 10, 13$ or $15 \pmod{16}$.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.isSuperMZumkeller_prime_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-super-mzumkeller-prime-pow-iff).

## Products of at least three distinct primes are super-m-Zumkeller

For every finite set
$S$ of at least three primes, the product $\prod_{p \in S} p$ is super-m-Zumkeller.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.isSuperMZumkeller_prod_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-super-mzumkeller-prod-primes).

## Odd powers of $2$ times two distinct odd primes are super-m-Zumkeller

Let $k$ be an odd
natural number and let $p$ and $q$ be distinct odd primes. Then $2^k p q$ is super-m-Zumkeller.

The primes are required to be odd because the paper's proof uses that this number has
$(k+1) \cdot 2^2$ divisors.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.isSuperMZumkeller_two_pow_mul_two_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-super-mzumkeller-two-pow-mul-two-prim).

## Powers of $2$ times at least three distinct odd primes are super-m-Zumkeller

Let $k$ be
a natural number and $S$ a finite set of at least three odd primes. Then $2^k \prod_{p \in S} p$
is super-m-Zumkeller.

The primes are required to be odd because the paper's proof uses that this number has
$(k+1)2^r$ divisors, where $r$ is the number of primes in $S$.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.isSuperMZumkeller_two_pow_mul_prod_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-super-mzumkeller-two-pow-mul-prod-pri).

## $k$-m-perfect numbers with $k$ a positive multiple of $4$ are super-m-Zumkeller

Let
$k \ge 2$ be a natural number with $k \equiv 0 \pmod 4$. Then every natural number that is
$k$-m-perfect is super-m-Zumkeller.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Theorem 6.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.isSuperMZumkeller_of_isKMPerfect` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-super-mzumkeller-of-is-kmperfect).

## $4$ is super-m-Zumkeller but not $k$-m-perfect for $k \ge 2$

The number $4$ is
super-m-Zumkeller, and for no natural number $k \ge 2$ is $4$ a $k$-m-perfect number. This is the
paper's counterexample to the converse of Theorem 6.

## Sources

- Harish Patodia, "Super m-Zumkeller Numbers", Theorem 6.

Stated but not proved: `MathlibExt.NumberTheory.SuperMZumkellerWanted.isSuperMZumkeller_four_not_kmPerfect` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperMZumkellerWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperMZumkellerWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html#is-super-mzumkeller-four-not-km-perfect).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zumkeller numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/zumkeller-numbers)
