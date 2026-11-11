---
declaration: section
origin: cited
lean: MetaMathlibExt.prime_gap_factorial_general, MetaMathlibExt.prime_gap_factorial, MetaMathlibExt.prime_sub_primorial_prime_of_between_consecutive_primes_general, MetaMathlibExt.prime_sub_primorial_prime_of_between_consecutive_primes, MetaMathlibExt.AreConsecutivePrimes.prime_sub_primorial_prime
statement: formalized
proof: formalized
---

# Primes just above factorials and primorials

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-just-above-factorials-and-primorials/index.html).

## Prime gaps near $n!$, general form

Let $n$, $p$ and $r$ be natural numbers such that
every prime $q > n$ satisfies $q \ge r$. If $p$ is a prime with $n! + 1 < p < n! + r^2$, then
$p - n!$ is prime.

Formalized by `MetaMathlibExt.prime_gap_factorial_general`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/PrimeGapFactorial.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/PrimeGapFactorial.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-just-above-factorials-and-primorials/index.html#prime-gap-factorial-general).

## Prime gaps near $n!$

Let $n$ be a natural number and let $r$ be the smallest prime greater
than $n$. If $p$ is a prime with $n! + 1 < p < n! + r^2$, then $p - n!$ is prime.

The source's proof: if $p - n!$ were composite, its least prime factor $m$ would satisfy
$m^2 \le p - n! < r^2$, so $m < r$ and hence $m \le n$. Then $m$ divides $n!$ and therefore $p$,
contradicting $p > n! + 1$.

## Sources

- Antonín Čejchan, Michal Křížek, and Lawrence Somer, "On Remarkable Properties of Primes Near Factorials and Primorials," Journal of Integer Sequences 25 (2022), Article 22.1.4, Theorem, lines 153–159, https://cs.uwaterloo.ca/journals/JIS/VOL25/Krizek/krizek3.tex

Formalized by `MetaMathlibExt.prime_gap_factorial`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/PrimeGapFactorial.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/PrimeGapFactorial.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-just-above-factorials-and-primorials/index.html#prime-gap-factorial).

## Primes just above a primorial, general form

Let $q$ and $r$ be natural numbers such
that no prime $s$ satisfies $q < s < r$, and let $q\#$ be the primorial of $q$, the product of
all primes at most $q$. If $p$ is a prime with $q\# + 1 < p < q\# + r^2$, then $p - q\#$ is
prime.

Neither $q$ nor $r$ needs to be prime, and $q < r$ is not assumed.

Formalized by `MetaMathlibExt.prime_sub_primorial_prime_of_between_consecutive_primes_general`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapsNearPrimorials.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeGapsNearPrimorials.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-just-above-factorials-and-primorials/index.html#prime-sub-primorial-prime-of-between-con).

## Primes just above a primorial (Čejchan–Křížek–Somer)

Let $q < r$ be consecutive primes,
so that no prime lies strictly between them, and let $q\#$ be the primorial of $q$, the product
of all primes at most $q$. If $p$ is a prime with $q\# + 1 < p < q\# + r^2$, then $p - q\#$ is
prime.

## Sources

- Antonín Čejchan, Michal Křížek, and Lawrence Somer, "On Remarkable Properties of Primes Near Factorials and Primorials," Journal of Integer Sequences 25 (2022), Article 22.1.4, Theorem, lines 471–477, https://cs.uwaterloo.ca/journals/JIS/VOL25/Krizek/krizek3.tex It follows from `prime_sub_primorial_prime_of_between_consecutive_primes_general`; the hypotheses `hq`, `hr` and `hqr` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.prime_sub_primorial_prime_of_between_consecutive_primes`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapsNearPrimorials.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeGapsNearPrimorials.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-just-above-factorials-and-primorials/index.html#prime-sub-primorial-prime-of-between-con-2).

## Primes just above a primorial, for a consecutive-prime pair

Let $q < r$ be consecutive
primes and let $q\#$ be the primorial of $q$, the product of all primes at most $q$. If $p$ is a
prime with $q\# + 1 < p < q\# + r^2$, then $p - q\#$ is prime.

Formalized by `MetaMathlibExt.AreConsecutivePrimes.prime_sub_primorial_prime`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapsNearPrimorials.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeGapsNearPrimorials.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-just-above-factorials-and-primorials/index.html#prime-sub-primorial-prime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primes just above factorials and primorials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-just-above-factorials-and-primorials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/primes-just-above-factorials-and-primorials)
