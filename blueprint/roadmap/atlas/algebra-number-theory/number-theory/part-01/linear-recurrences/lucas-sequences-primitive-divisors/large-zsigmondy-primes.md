---
declaration: section
origin: cited
lean: MetaMathlibExt.IsLargeZsigmondyPrime, MetaMathlibExt.isLargeZsigmondyPrime_two_one_three_seven, MetaMathlibExt.sqrt_div_two_le_totient, MetaMathlibExt.homogenizedCyclotomic_prime_pow_mul, MetaMathlibExt.prod_divisors_homogenizedCyclotomic, MetaMathlibExt.homogenizedCyclotomic_mem_Icc, MetaMathlibExt.homogenizedCyclotomic_prime_mul, MetaMathlibExt.padicValInt_homogenizedCyclotomic_odd
statement: formalized
---

# Large Zsigmondy primes

15 results, 2 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html).

## Large Zsigmondy prime

Let $a$, $b$, $n$ and $p$ be natural numbers. Then $p$ is a large
Zsigmondy prime for $(a, b, n)$ when $p$ is a primitive prime divisor of the term $a^n - b^n$ of
the integer sequence $(a^m - b^m)_{m \ge 0}$, that is, $n \ge 1$, $p$ is prime, $p$ divides
$a^n - b^n$ and $p$ divides no $a^m - b^m$ with $1 \le m < n$, and moreover $p^2$ divides
$a^n - b^n$ or $p > n + 1$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Section 1 (definition after Theorem 1).

Formalized by `MetaMathlibExt.IsLargeZsigmondyPrime`, a definition declared in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#is-large-zsigmondy-prime).

## $7$ is a large Zsigmondy prime for $(2, 1, 3)$

The prime $7$ is a large Zsigmondy prime
for $(a, b, n) = (2, 1, 3)$: it divides $2^3 - 1 = 7$, divides neither $2^1 - 1$ nor $2^2 - 1$,
and $7 > 3 + 1$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Section 1 (definition after Theorem 1).

Formalized by `MetaMathlibExt.isLargeZsigmondyPrime_two_one_three_seven`, a theorem declared in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#is-large-zsigmondy-prime-two-one-three-s).

## Square-root lower bound for Euler's totient

For every positive integer $n$,
$\varphi(n) \ge \sqrt{n}/2$, where $\varphi$ is Euler's totient function.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 1 (quoted from reference [2]).

Stated but not proved: `MetaMathlibExt.sqrt_div_two_le_totient` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#sqrt-div-two-le-totient).

## Homogenized cyclotomic values at $p^\beta k$

Let $p$ be a prime, let $\beta \ge 1$ and
$k \ge 1$ be integers with $p \nmid k$, and let $a, b$ be integers; write $\Phi_m(a, b)$ for the
homogenized cyclotomic value. Then
$\Phi_{p^\beta k}(a, b) = \Phi_{pk}(a^{p^{\beta - 1}}, b^{p^{\beta - 1}})$ and
$\Phi_{p^\beta k}(a, b) \cdot \Phi_k(a^{p^{\beta - 1}}, b^{p^{\beta - 1}}) =
\Phi_k(a^{p^\beta}, b^{p^\beta})$.

The paper states the second identity as a quotient; here it is cleared of its denominator.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Corollary 1.

Stated but not proved: `MetaMathlibExt.homogenizedCyclotomic_prime_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#homogenized-cyclotomic-prime-pow-mul).

## Factorization of $a^n - b^n$ into homogenized cyclotomic values

For every positive
integer $n$ and all integers $a$ and $b$,

$$a^n - b^n = \prod_{d \mid n} \Phi_d(a, b),$$

where the product runs over the positive divisors $d$ of $n$ and $\Phi_d(a, b)$ is the
homogenized cyclotomic value.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 3 (i) (quoted from reference [6]).

Stated but not proved: `MetaMathlibExt.prod_divisors_homogenizedCyclotomic` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#prod-divisors-homogenized-cyclotomic).

## Bounds for homogenized cyclotomic values

Let $a > b$ be positive integers and let
$n \ge 1$. Then the homogenized cyclotomic value $\Phi_n(a, b)$ satisfies
$(a - b)^{\varphi(n)} \le \Phi_n(a, b) \le (a + b)^{\varphi(n)}$, where $\varphi$ is Euler's
totient function.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 3 (ii) (quoted from reference [6]).

Stated but not proved: `MetaMathlibExt.homogenizedCyclotomic_mem_Icc` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#homogenized-cyclotomic-mem-icc).

## Homogenized cyclotomic values at $pn$

Let $p$ be a prime, $n$ a positive integer and
$a, b$ integers, and write $\Phi_m(a, b)$ for the homogenized cyclotomic value. If $p \mid n$,
then $\Phi_{pn}(a, b) = \Phi_n(a^p, b^p)$. If $p \nmid n$, then
$\Phi_{pn}(a, b) \cdot \Phi_n(a, b) = \Phi_n(a^p, b^p)$.

The paper states the case $p \nmid n$ as a quotient; here it is cleared of its denominator.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 3 (iii) (quoted from reference [6]).

Stated but not proved: `MetaMathlibExt.homogenizedCyclotomic_prime_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#homogenized-cyclotomic-prime-mul).

## $p$-adic valuation of homogenized cyclotomic values at an odd prime

Let $a > b$ be
positive integers, let $p$ be an odd prime dividing neither $a$ nor $b$, and let $k$ be the least
positive integer such that $p$ divides $a^k - b^k$. Write $v_p$ for the $p$-adic valuation and
$\Phi_n(a, b)$ for the homogenized cyclotomic value. Then for every positive integer $n$:
$v_p(\Phi_n(a, b)) = v_p(a^k - b^k)$ if $n = k$; $v_p(\Phi_n(a, b)) = 1$ if $n = p^\beta k$ for
some $\beta \ge 1$; and $v_p(\Phi_n(a, b)) = 0$ otherwise.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 3 (iv) (quoted from reference [6]).

Stated but not proved: `MetaMathlibExt.padicValInt_homogenizedCyclotomic_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#padic-val-int-homogenized-cyclotomic-odd).

## $2$-adic valuation of homogenized cyclotomic values

Let $a > b$ be odd positive
integers. Write $v_2$ for the $2$-adic valuation and $\Phi_n(a, b)$ for the homogenized
cyclotomic value. Then for every positive integer $n$: $v_2(\Phi_n(a, b)) = v_2(a - b)$ if
$n = 1$; $v_2(\Phi_n(a, b)) = v_2(a + b)$ if $n = 2$; $v_2(\Phi_n(a, b)) = 1$ if $n = 2^\beta$
for some $\beta \ge 2$; and $v_2(\Phi_n(a, b)) = 0$ if $n$ is not a power of $2$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 3 (v) (quoted from reference [6]).

Stated but not proved: `MetaMathlibExt.padicValInt_two_homogenizedCyclotomic` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#padic-val-int-two-homogenized-cyclotomic).

## Prime divisors of homogenized cyclotomic values

Let $a > b$ be coprime positive
integers, let $n \ge 2$, let $\Phi_n(a, b)$ be the homogenized cyclotomic value, let $p$ be a
prime dividing $\Phi_n(a, b)$, and let $k$ be the least positive integer such that $p$ divides
$a^k - b^k$. Then one of the following holds: (i) $p = 2$ and $n = 2^\beta$ for some
$\beta \ge 1$; (ii) $p \ge 3$, $n = k$, and $p$ is a primitive prime divisor of the term
$a^n - b^n$ of the sequence $(a^m - b^m)_{m \ge 0}$; (iii) $p$ is the greatest prime factor of
$n$, $p > 2$, $n = p^\beta k$ for some $\beta \ge 1$, and the $p$-adic valuation of
$\Phi_n(a, b)$ is $1$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 4.

Stated but not proved: `MetaMathlibExt.prime_dvd_homogenizedCyclotomic_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#prime-dvd-homogenized-cyclotomic-cases).

## Zsigmondy primes divide the homogenized cyclotomic value

Let $a$ and $b$ be distinct
coprime positive integers and let $n \ge 2$. If $p$ is a primitive prime divisor of the term
$a^n - b^n$ of the integer sequence $(a^m - b^m)_{m \ge 0}$ (a Zsigmondy prime for $(a, b, n)$),
then $p$ divides the homogenized cyclotomic value $\Phi_n(a, b)$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 5.

Stated but not proved: `MetaMathlibExt.dvd_homogenizedCyclotomic_of_isPrimitivePrimeDivisor` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#dvd-homogenized-cyclotomic-of-is-primiti).

## A Zsigmondy prime $q$ that is not large satisfies $n = q - 1$

Let $a > b$ be coprime
positive integers and let $n \ge 2$. If $q$ is a primitive prime divisor of the term $a^n - b^n$
of the integer sequence $(a^m - b^m)_{m \ge 0}$ and $q$ is not a large Zsigmondy prime for
$(a, b, n)$, then $n = q - 1$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 6.

Stated but not proved: `MetaMathlibExt.eq_sub_one_of_not_isLargeZsigmondyPrime` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#eq-sub-one-of-not-is-large-zsigmondy-pri).

## A size criterion for a large Zsigmondy prime

Let $a$ and $b$ be distinct coprime
positive integers and let $n \ge 3$. If $(n + 1) q < \Phi_n(a, b)$ for every prime factor $q$ of
$n$, where $\Phi_n(a, b)$ is the homogenized cyclotomic value, then there is a large Zsigmondy
prime for $(a, b, n)$.

Equivalently, the hypothesis asks that $n + 1$ times the greatest prime factor of $n$ be less
than $\Phi_n(a, b)$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 7.

Stated but not proved: `MetaMathlibExt.exists_isLargeZsigmondyPrime_of_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#exists-is-large-zsigmondy-prime-of-lt).

## Large Zsigmondy primes for exponents $n > 1$ outside six values

Let $a > b$ be coprime
positive integers and let $n > 1$ with $n \notin \{2, 4, 6, 10, 12, 18\}$. Then there is a
large Zsigmondy prime for $(a, b, n)$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 8.

Stated but not proved: `MetaMathlibExt.exists_isLargeZsigmondyPrime_of_not_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#exists-is-large-zsigmondy-prime-of-not-m).

## Avcı's classification of large Zsigmondy primes

Let $a > b$ be coprime positive
integers and let $n > 1$. There is a large Zsigmondy prime for $(a, b, n)$ if and only if none
of the following holds: $n = 2$ and $a + b = 2^s$ or $a + b = 3 \cdot 2^s$ for some natural
number $s$; $n = 4$ and $(a, b) \in \{(2, 1), (3, 1)\}$; $n = 6$ and
$(a, b) \in \{(2, 1), (3, 1), (3, 2), (5, 1), (5, 4)\}$; $n = 10$ and
$(a, b) \in \{(2, 1), (3, 2)\}$; $n = 12$ and $(a, b) = (2, 1)$; $n = 18$ and $(a, b) = (2, 1)$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Theorem 1 (the converse is the classification in the proof of Theorem 1).

Stated but not proved: `MetaMathlibExt.exists_isLargeZsigmondyPrime_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeZsigmondyPrimesWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html#exists-is-large-zsigmondy-prime-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large Zsigmondy primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/large-zsigmondy-primes)
