---
declaration: section
origin: cited
lean: MetaMathlibExt.binomialPowerSeq, MetaMathlibExt.doldRealizable, MetaMathlibExt.doldRealizable_dvd, MetaMathlibExt.doldRealizable_nonneg, MetaMathlibExt.doldRealizable_of_dvd_and_nonneg, MetaMathlibExt.binomial_power_sequence_dold_realizable, MetaMathlibExt.binomialPowerSeq_dold_congruences, MetaMathlibExt.binomialPowerSeq_moebius_sum_nonneg
statement: formalized
---

# Dold and realizable sequences

22 results, 13 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html).

## Binomial-power sequences

For natural numbers $r$, $s$ and $n$, the binomial-power number
$A_{r,s}(n)$ is the natural number

$$A_{r,s}(n) = \sum_{k=0}^{n} \binom{n}{k}^r \binom{n+k}{k}^s.$$

Special cases include the central Delannoy numbers ($r = s = 1$), the Apéry numbers
($r = s = 2$) and the Franel numbers of order $r$ ($s = 0$).

## Sources

- Geng-Rui Zhang, "Realizability of Some Combinatorial Sequences," Journal of Integer Sequences 27 (2024), Article 24.3.3, Theorem, lines 143–144, https://cs.uwaterloo.ca/journals/JIS/VOL27/Zhang/zhang9.tex with `A(n,r,s)` at lines 120–122 and realizability at lines 86–93.

Formalized by `MetaMathlibExt.binomialPowerSeq`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#binomial-power-seq).

## Dold realizable sequences

An integer sequence $(a(n))_{n \ge 0}$ is Dold realizable when,
for every integer $n \ge 1$, the Möbius transform $\sum_{d \mid n} \mu(d)\, a(n/d)$ is divisible
by $n$ and non-negative, where $\mu$ is the Möbius function and $d$ runs over the positive
divisors of $n$.

The divisibility condition alone is the classical Dold condition.

## Sources

- Wójcik, Lemma 3, for an equivalent form of the Dold condition.

Formalized by `MetaMathlibExt.doldRealizable`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#dold-realizable).

## Dold realizable sequences satisfy the Dold congruences

If an integer sequence
$(a(n))_{n \ge 0}$ is Dold realizable, then for every integer $n \ge 1$, $n$ divides
$\sum_{d \mid n} \mu(d)\, a(n/d)$, where $\mu$ is the Möbius function and $d$ runs over the
positive divisors of $n$.

Formalized by `MetaMathlibExt.doldRealizable_dvd`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#dold-realizable-dvd).

## The Möbius transform of a Dold realizable sequence is non-negative

If an integer sequence
$(a(n))_{n \ge 0}$ is Dold realizable, then for every integer $n \ge 1$,
$\sum_{d \mid n} \mu(d)\, a(n/d) \ge 0$, where $\mu$ is the Möbius function and $d$ runs over
the positive divisors of $n$.

Formalized by `MetaMathlibExt.doldRealizable_nonneg`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#dold-realizable-nonneg).

## Criterion for Dold realizability

Let $(a(n))_{n \ge 0}$ be an integer sequence and let
$\mu$ be the Möbius function. If for every integer $n \ge 1$ the sum
$\sum_{d \mid n} \mu(d)\, a(n/d)$ over the positive divisors $d$ of $n$ is divisible by $n$, and
for every integer $n \ge 1$ this sum is non-negative, then $a$ is Dold realizable.

Formalized by `MetaMathlibExt.doldRealizable_of_dvd_and_nonneg`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#dold-realizable-of-dvd-and-nonneg).

## Binomial-power sequences are Dold realizable

Let $r \ge 1$ and $s \ge 0$ be integers and
let $A_{r,s}(n) = \sum_{k=0}^{n} \binom{n}{k}^r \binom{n+k}{k}^s$. Then the integer sequence
$(A_{r,s}(n))_{n \ge 0}$ is Dold realizable: for every integer $n \ge 1$, the sum
$\sum_{d \mid n} \mu(d)\, A_{r,s}(n/d)$ over the positive divisors $d$ of $n$, where $\mu$ is
the Möbius function, is non-negative and divisible by $n$.

## Sources

- Zhang 2024, J. Integer Seq. 27, Article 24.3.3, Theorem 1.13.

Formalized by `MetaMathlibExt.binomial_power_sequence_dold_realizable`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean, line 1891](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean#L1891). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#binomial-power-sequence-dold-realizable).

## Dold congruences for binomial-power sequences

Let $r \ge 1$ and $s \ge 0$ be integers
and let $A_{r,s}(m) = \sum_{k=0}^{m} \binom{m}{k}^r \binom{m+k}{k}^s$. Then for every integer
$n \ge 1$, $n$ divides $\sum_{d \mid n} \mu(d)\, A_{r,s}(n/d)$, where $\mu$ is the Möbius
function and $d$ runs over the positive divisors of $n$.

Formalized by `MetaMathlibExt.binomialPowerSeq_dold_congruences`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean, line 1964](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean#L1964). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#binomial-power-seq-dold-congruences).

## Non-negativity of the Möbius transform of binomial-power sequences

Let $r \ge 1$ and
$s \ge 0$ be integers and let $A_{r,s}(m) = \sum_{k=0}^{m} \binom{m}{k}^r \binom{m+k}{k}^s$.
Then for every integer $n \ge 1$, $\sum_{d \mid n} \mu(d)\, A_{r,s}(n/d) \ge 0$, where $\mu$
is the Möbius function and $d$ runs over the positive divisors of $n$.

Formalized by `MetaMathlibExt.binomialPowerSeq_moebius_sum_nonneg`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean, line 1972](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/BinomialPowerRealizability.lean#L1972). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#binomial-power-seq-moebius-sum-nonneg).

## Dold sequences

A sequence $a_0, a_1, a_2, \dots$ of integers is a Dold sequence when
for every integer $m \ge 1$ there is an $m \times m$ matrix $A$ with integer entries such that
$a_n = \operatorname{tr}(A^n)$ for every $n$ with $1 \le n \le m$. The term $a_0$ is not
constrained.

## Sources

- Wójcik, *Binomial Transform and Dold Sequences*, Lemma 3; this equivalent trace characterization is taken here as the definition.

Formalized by `MetaMathlibExt.IsDoldSequence`, a definition declared in [MathlibExt/NumberTheory/DoldSequence.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DoldSequence.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#is-dold-sequence).

## Fermat sequence

Given a sequence $b : \mathbb{N} \to \mathbb{C}$, the Fermat sequence
generated by $b$ is the sequence $a : \mathbb{N} \to \mathbb{C}$ given by
$a_n = \sum_{m \mid n} m \, b_m$ for $n \ge 1$, the sum running over the positive divisors $m$
of $n$, and $a_0 = 0$.

The source defines the sequence only for positive indices; the value $a_0 = 0$ comes from
summing over the empty set of divisors of $0$.

## Sources

- B.-S. Du, S.-S. Huang, and M.-C. Li, *Newton, Fermat, and Exactly Realizable Sequences*, Journal of Integer Sequences 8 (2005), lines 181–190, <https://cs.uwaterloo.ca/journals/JIS/VOL8/Huang/huang11.tex>.

Formalized by `MetaMathlibExt.fermatSequence`, a definition declared in [MathlibExt/NumberTheory/FermatSequence.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FermatSequence.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#fermat-sequence).

## Almost realizable sequences

A sequence $a$ of natural numbers $a(0), a(1), \dots$ is
almost realizable when there is an integer $m \ge 1$ such that the integer sequence
$(m\, a(n))_{n \ge 0}$ is Dold realizable: for every $n \ge 1$, the sum
$\sum_{d \mid n} \mu(d)\, m\, a(n/d)$ over the positive divisors $d$ of $n$, where $\mu$ is the
Möbius function, is non-negative and divisible by $n$.

This is Miska and Ward's notion that some positive integer multiple of $a$ is realizable. The
value $a(0)$ is not used.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Definition 3.

Formalized by `MetaMathlibExt.IsAlmostRealizableSeq`, a definition declared in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#is-almost-realizable-seq).

## The zero sequence is almost realizable

The constant sequence $a(n) = 0$ is almost
realizable.

It is realized by the self-map of the empty set, with multiplier $m = 1$.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Definition 3.

Formalized by `MetaMathlibExt.isAlmostRealizableSeq_zero`, a theorem declared in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#is-almost-realizable-seq-zero).

## Binomial-power sequences are almost realizable

For all natural numbers $r \ge 1$ and $s$,
the binomial-power sequence $n \mapsto \sum_{k=0}^{n} \binom{n}{k}^r \binom{n+k}{k}^s$ is almost
realizable.

Every Dold realizable sequence is almost realizable (take the multiplier $m = 1$), and the
binomial-power sequences are Dold realizable.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Definition 3 and Theorem 13.

Formalized by `MetaMathlibExt.isAlmostRealizableSeq_binomialPowerSeq`, a theorem declared in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#is-almost-realizable-seq-binomial-power).

## Domb-type sums are Dold realizable

For all natural numbers $r \ge 1$, $s$ and $t$, the
integer sequence $(D(n, r, s, t))_{n \ge 0}$ of Domb-type sums
$D(n, r, s, t) = \sum_{k=0}^{n} \binom{n}{k}^r \binom{2k}{k}^s \binom{2(n-k)}{n-k}^t$ is Dold
realizable.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Theorem 15 (`jis-2024-24.3.3-thm-15`).

Stated but not proved: `MetaMathlibExt.doldRealizable_dombTypeSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#dold-realizable-domb-type-sum).

## The Catalan, Motzkin and large Schröder numbers are not almost realizable

None of the
following three sequences of non-negative integers is almost realizable: the Catalan numbers
$C_n = \frac{1}{n+1}\binom{2n}{n}$, the Motzkin numbers $M(n)$, and the large Schröder numbers
$S(n)$ (OEIS A006318), given by $S(0) = 1$ and $S(n+1) = S(n) + \sum_{i=0}^{n} S(i) S(n-i)$.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Theorem 21 (`jis-2024-24.3.3-thm-21`).

Stated but not proved: `MetaMathlibExt.not_isAlmostRealizableSeq_catalan_motzkin_schroder` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#not-is-almost-realizable-seq-catalan-mot).

## Helou–Terjanian congruence for primes $p \ge 5$

Let $p \ge 5$ be a prime and let $m$ and
$n$ be integers with $0 < m < n$. Then $\binom{np}{mp} \equiv \binom{n}{m} \pmod{p^e}$, where
$e = 3 + \max(\nu_p(m), \nu_p(n - m)) + \nu_p\big(\binom{n}{m}\big)$ and $\nu_p$ is the $p$-adic
valuation.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Lemma 26 (1) (`jis-2024-24.3.3-lem-26`).

Stated but not proved: `MetaMathlibExt.choose_mul_prime_modEq_of_five_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#choose-mul-prime-mod-eq-of-five-le).

## Helou–Terjanian congruence for $p = 3$

Let $m$ and $n$ be integers with $0 < m < n$.
Then $\binom{3n}{3m} \equiv \binom{n}{m} \pmod{3^e}$, where
$e = 2 + \max(\nu_3(m), \nu_3(n - m)) + \nu_3\big(\binom{n}{m}\big)$ and $\nu_3$ is the $3$-adic
valuation.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Lemma 26 (2) (`jis-2024-24.3.3-lem-26`).

Stated but not proved: `MetaMathlibExt.choose_three_mul_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#choose-three-mul-mod-eq).

## Helou–Terjanian congruence for $p = 2$

Let $m$ and $n$ be integers with $0 < m < n$.
Then $\binom{2n}{2m} \equiv \binom{n}{m} \pmod{2^e}$, where
$e = 1 + \max(\nu_2(m), \nu_2(n - m)) + \nu_2\big(\binom{n}{m}\big)$ and $\nu_2$ is the $2$-adic
valuation.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Lemma 26 (3) (`jis-2024-24.3.3-lem-26`).

Stated but not proved: `MetaMathlibExt.choose_two_mul_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#choose-two-mul-mod-eq).

## Binomial coefficients at multiples of a prime divisor

Let $p$ be a prime and let
$n \ge 1$ be an integer divisible by $p$. Then for every integer $\lambda \ge 0$ with
$\lambda p \ne n$,

$$\binom{n}{\lambda p} \equiv \binom{n/p}{\lambda} \pmod{p^e},$$

where $e = \max(\nu_p(n), \nu_p(n - \lambda p))$ and $\nu_p$ is the $p$-adic valuation; the
integer $n - \lambda p$ may be negative, and $\nu_p(n - \lambda p)$ is the valuation of its
absolute value.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Lemma 27 (`jis-2024-24.3.3-lem-27`).

Stated but not proved: `MetaMathlibExt.choose_mul_prime_modEq_choose_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#choose-mul-prime-mod-eq-choose-div).

## Möbius transforms of sequences growing by a factor of at least $1.221$ are nonnegative

Let $b$ be a sequence of real numbers and $C \ge 1.221$ a real number such that $b(n) \ge 0$ and
$b(n+1) \ge C\, b(n)$ for every $n \ge 1$. Then for every $n \ge 1$, with $\mu$ the Möbius
function,

$$\sum_{d \mid n} \mu(n/d)\, b(d) \ge 0,$$

that is, the Dirichlet convolution $\mu * b$ is nonnegative at $n$.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Lemma 28 (`jis-2024-24.3.3-lem-28`).

Stated but not proved: `MetaMathlibExt.moebius_conv_nonneg_of_geometric_growth` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#moebius-conv-nonneg-of-geometric-growth).

## Dold congruences via prime-power congruences

Let $(V(n))_{n \ge 1}$ be a sequence of
integers and let $\mu$ denote the Möbius function. Then
$V(n p^m) \equiv V(n p^{m-1}) \pmod{p^m}$ holds for all integers $n, m \ge 1$ and all primes $p$
if and only if $n$ divides $\sum_{d \mid n} \mu(n/d) V(d)$ for every integer $n \ge 1$.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Lemma 30 (`jis-2024-24.3.3-lem-30`).

Stated but not proved: `MetaMathlibExt.prime_power_congruence_iff_dold` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#prime-power-congruence-iff-dold).

## Even-binomial-type sums are Dold realizable

Let $r \ge 1$, $s$, $t$ and $u$ be natural
numbers with $t + u \ge 1$, and let

$$T(n) = \sum_{k=0}^{n} \binom{n}{2k}^r \binom{n+k}{k}^s \binom{2k}{k}^t \binom{2(n-k)}{n-k}^u.$$

Then the integer sequence $(T(n))_{n \ge 0}$ is Dold realizable.

The hypothesis $t + u \ge 1$ is added to the source: for $t = u = 0$ the Möbius transform at
$n = 2$ is $T(2) - T(1) = 3^s$, which is odd, so the sequence is not Dold realizable.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Theorem 18 (`jis-2024-24.3.3-thm-18`).

Stated but not proved: `MetaMathlibExt.doldRealizable_evenBinomialTypeSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RealizableCombinatorialSequencesWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html#dold-realizable-even-binomial-type-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dold and realizable sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/dold-and-realizable-sequences)
