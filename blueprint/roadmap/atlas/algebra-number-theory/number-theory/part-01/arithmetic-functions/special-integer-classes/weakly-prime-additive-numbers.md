---
declaration: section
origin: cited
lean: MetaMathlibExt.IsPrimeDivisorPowerSum, MetaMathlibExt.IsWeaklyPrimeAdditive, MetaMathlibExt.weaklyPrimeAdditiveLength, MetaMathlibExt.isPrimeDivisorPowerSum_thirty, MetaMathlibExt.isWeaklyPrimeAdditive_thirty, MetaMathlibExt.weaklyPrimeAdditiveLength_le, MetaMathlibExt.infinite_weaklyPrimeAdditive_length_four_dvd, MetaMathlibExt.infinite_primes_dvd_four_prime_power_sum
statement: formalized
---

# Weakly prime-additive numbers

10 results, 6 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html).

## Sums of powers of distinct prime divisors

For natural numbers $n$ and $t$, $n$ is a sum
of positive powers of $t$ distinct prime divisors of $n$ when there are a set $s$ of $t$ distinct
primes, each dividing $n$, and positive integers $e_p$ for $p \in s$ such that
$n = \sum_{p \in s} p^{e_p}$.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Section 1, Definition (after Erdős and Hegyvári).

Formalized by `MetaMathlibExt.IsPrimeDivisorPowerSum`, a definition declared in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#is-prime-divisor-power-sum).

## Weakly prime-additive numbers

A natural number $n$ is weakly prime-additive if it has at
least two distinct prime divisors and is a sum $n = \sum_{p \in s} p^{e_p}$ of positive powers
$p^{e_p}$, $e_p \ge 1$, over some set $s$ of distinct prime divisors of $n$.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Section 1, Definition.

Formalized by `MetaMathlibExt.IsWeaklyPrimeAdditive`, a definition declared in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#is-weakly-prime-additive).

## Weakly prime-additive length

For a natural number $n$, the length $\kappa_n$ is the least
$t$ such that $n$ is a sum of positive powers of $t$ distinct prime divisors of $n$, and
$\kappa_n = 0$ when $n$ has no such representation.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Section 1, Definition.

Formalized by `MetaMathlibExt.weaklyPrimeAdditiveLength`, a definition declared in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#weakly-prime-additive-length).

## Thirty is a sum of powers of three of its prime divisors

The number $30$ is a sum of
positive powers of three distinct prime divisors of $30$, namely $30 = 2 + 3 + 5^2$.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Section 1, Definition.

Formalized by `MetaMathlibExt.isPrimeDivisorPowerSum_thirty`, a theorem declared in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#is-prime-divisor-power-sum-thirty).

## Thirty is weakly prime-additive

The number $30$ is weakly prime-additive.

Indeed, $30$ has the distinct prime divisors $2$, $3$, $5$ and $30 = 2 + 3 + 5^2$.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Section 1, Definition.

Formalized by `MetaMathlibExt.isWeaklyPrimeAdditive_thirty`, a theorem declared in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#is-weakly-prime-additive-thirty).

## The length is at most the size of any representation

For natural numbers $n$ and $t$,
if $n$ is a sum of positive powers of $t$ distinct prime divisors of $n$, then the length
$\kappa_n$ of $n$ is at most $t$.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Section 1, Definition (minimality of `κ_n`).

Formalized by `MetaMathlibExt.weaklyPrimeAdditiveLength_le`, a theorem declared in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#weakly-prime-additive-length-le).

## Weakly prime-additive multiples of length four

Assume $(\ast)$: for all natural numbers
$a$, $f$, $g$ with $1 \le a \le f$, $\gcd(a, f) = 1$ and $4 \mid f$, and $g$ an odd prime dividing
$f$ with Jacobi symbol $\left(\frac{g}{a}\right) = -1$, there is a prime $\ell \equiv a \pmod f$
such that $g$ is a primitive root modulo $\ell$. Then for every positive integer $m$ there are
infinitely many weakly prime-additive numbers $n$ with $m \mid n$ and length $\kappa_n = 4$.

The paper states $(\ast)$ with the Kronecker symbol; since $a$ is coprime to $f$ and $4 \mid f$,
$a$ is odd, so it is the Jacobi symbol.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Theorem 1.

Stated but not proved: `MetaMathlibExt.infinite_weaklyPrimeAdditive_length_four_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#infinite-weakly-prime-additive-length-fo).

## Primes completing a four-term prime-power divisibility

Assume $(\ast)$: for all natural
numbers $a$, $f$, $g$ with $1 \le a \le f$, $\gcd(a, f) = 1$ and $4 \mid f$, and $g$ an odd prime
dividing $f$ with Jacobi symbol $\left(\frac{g}{a}\right) = -1$, there is a prime
$\ell \equiv a \pmod f$ such that $g$ is a primitive root modulo $\ell$. Let $p$, $q$, $r$ be
distinct odd primes, at least one of which is congruent to $3$ or $5$ modulo $8$. Then there are
infinitely many primes $s$, distinct from $p$, $q$ and $r$, for each of which there are
infinitely many quadruples $(e_1, e_2, e_3, e_4)$ of positive integers with
$pqrs \mid p^{e_1} + q^{e_2} + r^{e_3} + s^{e_4}$.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Theorem 2.

Stated but not proved: `MetaMathlibExt.infinite_primes_dvd_four_prime_power_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#infinite-primes-dvd-four-prime-power-sum).

## Fang–Chen theorem on shortest weakly prime-additive multiples

For every positive integer
$m$, there are infinitely many weakly prime-additive numbers $n$ with $m \mid n$ and length
$\kappa_n = 3$ if and only if $8 \nmid m$.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Theorem 5 (Fang and Chen, Corollary 1.1).

Stated but not proved: `MetaMathlibExt.infinite_shortest_weaklyPrimeAdditive_dvd_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#infinite-shortest-weakly-prime-additive).

## Weakly prime-additive multiples of length at most four

Assume $(\ast)$: for all natural
numbers $a$, $f$, $g$ with $1 \le a \le f$, $\gcd(a, f) = 1$ and $4 \mid f$, and $g$ an odd prime
dividing $f$ with Jacobi symbol $\left(\frac{g}{a}\right) = -1$, there is a prime
$\ell \equiv a \pmod f$ such that $g$ is a primitive root modulo $\ell$. Then for every positive
integer $m$ there are infinitely many weakly prime-additive numbers $n$ with $m \mid n$ and
length $\kappa_n \le 4$.

## Sources

- Wing Hong Leung, *On the Weakly Prime-Additive Numbers with Length 4*, INTEGERS 24 (2024), Article A9, Theorem 6.

Stated but not proved: `MetaMathlibExt.infinite_weaklyPrimeAdditive_length_le_four_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeaklyPrimeAdditiveWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html#infinite-weakly-prime-additive-length-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weakly prime-additive numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/weakly-prime-additive-numbers)
