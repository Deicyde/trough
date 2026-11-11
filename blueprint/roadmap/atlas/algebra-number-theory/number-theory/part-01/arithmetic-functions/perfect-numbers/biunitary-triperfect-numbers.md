---
declaration: section
origin: cited
lean: MetaMathlibExt.sigmaBiunitary_eq_three_mul_iff_of_twentySeven_dvd, MetaMathlibExt.odd_sigmaBiunitary_iff, MetaMathlibExt.two_pow_card_primeFactors_dvd_sigmaBiunitary_of_odd, MetaMathlibExt.two_pow_card_primeFactors_sub_one_dvd_sigmaBiunitary_of_even, MetaMathlibExt.sigmaBiunitary_prime_pow_div_ge, MetaMathlibExt.sigmaBiunitary_prime_pow_div_ge_of_two_mul_sub_one_le, MetaMathlibExt.primitivePrimeDivisor_pow_sub_one_mod_eq_one, MetaMathlibExt.exists_primitivePrimeDivisor_pow_add_one
statement: formalized
---

# Biunitary triperfect numbers

21 results, 21 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html).

## The only biunitary triperfect number divisible by $27$ is $2160$

For every positive
integer $N$ divisible by $27$, $\sigma^{**}(N) = 3N$ if and only if $N = 2160$, where
$\sigma^{**}$ is the biunitary divisor sum.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Theorem 1 (`jis-2025-25.4.5-thm-1`).

Stated but not proved: `MetaMathlibExt.sigmaBiunitary_eq_three_mul_iff_of_twentySeven_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#sigma-biunitary-eq-three-mul-iff-of-twen).

## Parity of the biunitary divisor sum

For every positive integer $n$, the biunitary divisor
sum $\sigma^{**}(n)$ is odd if and only if $n = 2^k$ for some natural number $k$ (so $n = 1$ is
included).

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 2 (`jis-2025-25.4.5-lem-2`).

Stated but not proved: `MetaMathlibExt.odd_sigmaBiunitary_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#odd-sigma-biunitary-iff).

## Powers of two dividing the biunitary divisor sum of an odd number

For every odd natural
number $n$, $2^{\omega(n)}$ divides $\sigma^{**}(n)$, where $\omega(n)$ is the number of distinct
prime factors of $n$ and $\sigma^{**}$ is the biunitary divisor sum.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 2 (`jis-2025-25.4.5-lem-2`).

Stated but not proved: `MetaMathlibExt.two_pow_card_primeFactors_dvd_sigmaBiunitary_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#two-pow-card-prime-factors-dvd-sigma-biu).

## Divisibility of the biunitary divisor sum of an even number by a power of two

For every
positive even natural number $n$, writing $\omega(n)$ for the number of distinct prime factors of
$n$, the power $2^{\omega(n) - 1}$ divides the biunitary divisor sum $\sigma^{**}(n)$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 2 (`jis-2025-25.4.5-lem-2`).

Stated but not proved: `MetaMathlibExt.two_pow_card_primeFactors_sub_one_dvd_sigmaBiunitary_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#two-pow-card-prime-factors-sub-one-dvd-s).

## Lower bounds for the biunitary divisor sum of a prime power

Let $p$ be a prime and
$e \ge 1$, and write $\sigma^{**}$ for the biunitary divisor sum. Then, in $\mathbb{Q}$,
$\sigma^{**}(p^e)/p^e \ge 1 + 1/p^2$; if moreover $e \ne 2$, then
$\sigma^{**}(p^e)/p^e \ge 1 + 1/p$; and if $e \ge 3$, then
$\sigma^{**}(p^e)/p^e \ge (1 + 1/p)(1 + 1/p^3)$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 3 (`jis-2025-25.4.5-lem-3`).

Stated but not proved: `MetaMathlibExt.sigmaBiunitary_prime_pow_div_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#sigma-biunitary-prime-pow-div-ge).

## Comparison bounds for the biunitary divisor sum of a prime power

Let $p$ be a prime and
let $m \ge 1$ and $e \ge 2m - 1$ be natural numbers, and write $\sigma^{**}$ for the biunitary
divisor sum. Then, in $\mathbb{Q}$,
$\sigma^{**}(p^e)/p^e \ge \sigma^{**}(p^{2m})/p^{2m}$, and if moreover $e \ne 2m$, then
$\sigma^{**}(p^e)/p^e \ge \sum_{i=0}^{m} 1/p^i$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 3 (`jis-2025-25.4.5-lem-3`).

Stated but not proved: `MetaMathlibExt.sigmaBiunitary_prime_pow_div_ge_of_two_mul_sub_one_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#sigma-biunitary-prime-pow-div-ge-of-two).

## Primitive prime divisors of $a^n - 1$ are $1$ modulo $n$

Let $a \ge 2$ and $n \ge 2$ be
natural numbers, and let $p$ be a primitive prime divisor of the integer sequence $m \mapsto
a^m - 1$ at index $n$, that is, a prime that divides $a^n - 1$ and divides no $a^m - 1$ with
$1 \le m < n$. Then $p \equiv 1 \pmod n$.

This is the congruence half of Bang's theorem. Its existence half (such a $p$ exists unless
$(a, n) = (2, 6)$, or $n = 2$ and $a + 1$ is a power of $2$) is the case $b = 1$ of the
Bang–Zsigmondy theorem.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 4 (`jis-2025-25.4.5-lem-4`), quoting Bang.

Stated but not proved: `MetaMathlibExt.primitivePrimeDivisor_pow_sub_one_mod_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#primitive-prime-divisor-pow-sub-one-mod).

## Primitive prime factors of $a^n + 1$

Let $a \ge 2$ and $n \ge 1$ be integers with
$(a, n) \ne (2, 3)$, and if $n = 1$ suppose that $a + 1$ is not a power of $2$. Then $a^n + 1$
has a primitive prime factor $p$, that is, a prime $p$ that divides $a^n + 1$ but divides no
$a^m + 1$ with $1 \le m < n$, such that $p \equiv 1 \pmod{2n}$.

The second exception is not in the printed statement: for $a = 3$, $n = 1$ the only prime factor
of $3 + 1 = 4$ is $2 \not\equiv 1 \pmod 2$; the paper's proof applies Lemma 2.3 to
$a^{2n} - 1$, whose exceptions include exactly this case.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 5 (`jis-2025-25.4.5-lem-5`).

Stated but not proved: `MetaMathlibExt.exists_primitivePrimeDivisor_pow_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#exists-primitive-prime-divisor-pow-add-o).

## Prime factors of the biunitary divisor sum of a power of $3$

Let $f$, $t$ and $\eta$ be
natural numbers with $\eta \in \{0, 1\}$ and $f = 2t - 1 - \eta$, suppose $f \ge 5$, and write
$\sigma^{**}$ for the biunitary divisor sum. Then at least one of the following holds:
(A) $\eta = 0$ and $\sigma^{**}(3^f)$ has a prime factor $p$ with $5 < p \le (3^t - 1)/2$;
(B) $5 \mid \sigma^{**}(3^f)$, and $f \equiv 2 \pmod 4$ or $f \in \{7, 8\}$;
(C) $\sigma^{**}(3^f)$ has a prime factor $p$ with $p > 5$ and $p^2 \le (3^{t - \eta} - 1)/2$;
(D) $4 \mid t$, $\eta = 1$, and $(3^{t-1} - 1)/2$ is prime.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 6 (`jis-2025-25.4.5-lem-6`).

Stated but not proved: `MetaMathlibExt.sigmaBiunitary_three_pow_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#sigma-biunitary-three-pow-cases).

## Prime factors of the biunitary divisor sum of a power of $2$

Let $e$, $s$ and $\delta$
be natural numbers with $\delta \in \{0, 1\}$ and $e = 2s - 1 - \delta$, suppose $e \ge 6$ and
$e \notin \{8, 12\}$, and write $\sigma^{**}$ for the biunitary divisor sum. Then at least one of
the following holds:
(a) $\delta = 0$ and $\sigma^{**}(2^e)$ has two distinct prime factors $q_1, q_2$ with
$5 < q_i \le 2^s - 1$ for $i = 1, 2$;
(b) $5 \mid \sigma^{**}(2^e)$;
(c) $\sigma^{**}(2^e)$ has two distinct prime factors $q_1, q_2$ such that each $q_i$ equals
$2^{s-1} - 1$ or $2^s + 1$ or satisfies $5 < q_i$ and $q_i^2 \le 2^s - 3$, and if some $q_i$
equals $2^{s-1} - 1$ or $2^s + 1$, then $4 \mid s$ and $\delta = 1$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 7 (`jis-2025-25.4.5-lem-7`).

Stated but not proved: `MetaMathlibExt.sigmaBiunitary_two_pow_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#sigma-biunitary-two-pow-cases).

## Prime factors at least $5$ of biunitary divisor sums of prime powers

For every prime $p$
and every integer $g \ge 2$ with $(p, g) \ne (2, 4)$, the biunitary divisor sum $\sigma^{**}(p^g)$
has a prime factor $q \ge 5$.

The excluded case is a genuine exception: $\sigma^{**}(2^4) = 1 + 2 + 8 + 16 = 27 = 3^3$. It is
not in the printed statement; the paper's proof applies Lemma 2.4 to $p^u + 1$ with
$g = 2u - 1 - \varepsilon$, and $(p, u) = (2, 3)$ is that lemma's exception.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 8 (I) (`jis-2025-25.4.5-lem-8`).

Stated but not proved: `MetaMathlibExt.exists_prime_ge_five_dvd_sigmaBiunitary_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#exists-prime-ge-five-dvd-sigma-biunitary).

## Prime factors at least $7$ of biunitary divisor sums of odd prime powers

For every odd
prime $p$ and every integer $g \ge 4$, the biunitary divisor sum $\sigma^{**}(p^g)$ has a prime
factor $q \ge 7$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 8 (II) (`jis-2025-25.4.5-lem-8`).

Stated but not proved: `MetaMathlibExt.exists_prime_ge_seven_dvd_sigmaBiunitary_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#exists-prime-ge-seven-dvd-sigma-biunitar).

## Two prime factors of the biunitary divisor sum of $13^g$

For every integer $g \ge 2$, the
biunitary divisor sum $\sigma^{**}(13^g)$ has two distinct prime factors $q_1$ and $q_2$, neither
of which lies in $\{2, 3, 41, 547\}$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 8 (IV) (`jis-2025-25.4.5-lem-8`).

Stated but not proved: `MetaMathlibExt.exists_two_primes_dvd_sigmaBiunitary_thirteen_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#exists-two-primes-dvd-sigma-biunitary-th).

## Prime factors of the biunitary divisor sum of $41^g$

For every integer $g \ge 1$, the
biunitary divisor sum $\sigma^{**}(41^g)$ has a prime factor $q$ with $q \notin \{2, 3, 5, 13\}$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 8 (V) (`jis-2025-25.4.5-lem-8`).

Stated but not proved: `MetaMathlibExt.exists_prime_dvd_sigmaBiunitary_fortyOne_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#exists-prime-dvd-sigma-biunitary-forty-o).

## Biunitary triperfect numbers divisible by $27$ are divisible by $16$

Let $N$ be a
biunitary triperfect number, that is, a positive integer with $\sigma^{**}(N) = 3N$, where
$\sigma^{**}$ is the biunitary divisor sum. If $3^3$ divides $N$, then $2^4$ divides $N$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 9 (`jis-2025-25.4.5-lem-9`).

Stated but not proved: `MetaMathlibExt.four_le_factorization_two_of_biunitaryTriperfect` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#four-le-factorization-two-of-biunitary-t).

## No biunitary triperfect number divisible by $27$ is exactly divisible by $2^5$

Let $N$
be a biunitary triperfect number, that is, a positive integer with $\sigma^{**}(N) = 3N$, where
$\sigma^{**}$ is the biunitary divisor sum. If $3^3$ divides $N$, then the exact power of $2$
dividing $N$ is not $2^5$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 10 (`jis-2025-25.4.5-lem-10`).

Stated but not proved: `MetaMathlibExt.factorization_two_ne_five_of_biunitaryTriperfect` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#factorization-two-ne-five-of-biunitary-t).

## No biunitary triperfect number divisible by $27$ is exactly divisible by $2^6$

Let $N$
be a biunitary triperfect number, that is, a positive integer with $\sigma^{**}(N) = 3N$, where
$\sigma^{**}$ is the biunitary divisor sum. If $3^3$ divides $N$, then the exact power of $2$
dividing $N$ is not $2^6$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 11 (`jis-2025-25.4.5-lem-11`).

Stated but not proved: `MetaMathlibExt.factorization_two_ne_six_of_biunitaryTriperfect` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#factorization-two-ne-six-of-biunitary-tr).

## No biunitary triperfect number has $3$-exponent $3$ and $2$-exponent at least $7$

Let
$N$ be a positive integer with $\sigma^{**}(N) = 3N$, where $\sigma^{**}$ is the biunitary divisor
sum, and let $e$ and $f$ be the exponents of $2$ and $3$ in the prime factorization of $N$. If
$f \ge 3$, then $e \ge 7$ and $f = 3$ do not both hold.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 12 (`jis-2025-25.4.5-lem-12`).

Stated but not proved: `MetaMathlibExt.not_seven_le_and_factorization_three_eq_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#not-seven-le-and-factorization-three-eq).

## No biunitary triperfect number has $3$-exponent $4$ and $2$-exponent at least $7$

Let
$N$ be a positive integer with $\sigma^{**}(N) = 3N$, where $\sigma^{**}$ is the biunitary divisor
sum, and let $e$ and $f$ be the exponents of $2$ and $3$ in the prime factorization of $N$. If
$f \ge 3$, then $e \ge 7$ and $f = 4$ do not both hold.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 13 (`jis-2025-25.4.5-lem-13`).

Stated but not proved: `MetaMathlibExt.not_seven_le_and_factorization_three_eq_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#not-seven-le-and-factorization-three-eq-2).

## Biunitary triperfect numbers exactly divisible by $2^4$ and by $3^3$ or $3^4$

Let $N$ be
a biunitary triperfect number, that is, a positive integer with $\sigma^{**}(N) = 3N$, where
$\sigma^{**}$ is the biunitary divisor sum. If the exact power of $2$ dividing $N$ is $2^4$ and the
exact power of $3$ dividing $N$ is $3^3$ or $3^4$, then $N = 2160$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 14 (`jis-2025-25.4.5-lem-14`).

Stated but not proved: `MetaMathlibExt.eq_2160_of_factorization_two_eq_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#eq-2160-of-factorization-two-eq-four).

## Biunitary triperfect numbers exactly divisible by $2^4$ and divisible by $3^5$ are prime to $5$

**Biunitary triperfect numbers exactly divisible by $2^4$ and divisible by $3^5$ are prime
to $5$.** Let $N$ be a biunitary triperfect number, that is, a positive integer with
$\sigma^{**}(N) = 3N$, where $\sigma^{**}$ is the biunitary divisor sum. If the exact power of $2$
dividing $N$ is $2^4$ and $3^5$ divides $N$, then $5$ does not divide $N$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 15 (`jis-2025-25.4.5-lem-15`).

Stated but not proved: `MetaMathlibExt.not_five_dvd_of_factorization_two_eq_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/BiunitaryTriperfectWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html#not-five-dvd-of-factorization-two-eq-fou).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Biunitary triperfect numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/biunitary-triperfect-numbers)
