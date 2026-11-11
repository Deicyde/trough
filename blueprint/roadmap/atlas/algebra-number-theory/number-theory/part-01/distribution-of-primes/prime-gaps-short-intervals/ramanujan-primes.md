---
declaration: section
origin: cited
lean: MetaMathlibExt.IsLabosPrime, MetaMathlibExt.IsRamanujanPrime, MetaMathlibExt.IsNthRamanujanPrime, MetaMathlibExt.primeCountingWithin, MetaMathlibExt.IsVPRamanujanNumber, MetaMathlibExt.laishram_ramanujan_prime_bound
statement: formalized
---

# Ramanujan primes

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes/index.html).

## Labos prime

Write $\pi(x)$ for the number of primes $p \le x$. For natural numbers $n$
and $L$, $L$ is the $n$-th Labos prime when $n \ge 1$, $L \ge 1$,
$\pi(L) - \pi(\lfloor L/2 \rfloor) = n$, and no integer $m$ with $1 \le m < L$ satisfies
$\pi(m) - \pi(\lfloor m/2 \rfloor) = n$; that is, $L$ is the least positive integer with
$\pi(L) - \pi(\lfloor L/2 \rfloor) = n$.

Formalized by `MetaMathlibExt.IsLabosPrime`, a definition declared in [MathlibExt/NumberTheory/LabosPrime.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LabosPrime.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes/index.html#is-labos-prime).

## Primes satisfying the Ramanujan counting condition

Let $\pi$ be the prime-counting
function. For natural numbers $R$ and $n$, $R$ satisfies the Ramanujan counting condition for
$n$ when $R$ is prime and $\pi(R) - \pi(R/2) = n$.

Here $\pi(x)$ counts the primes $p \le x$, so $\pi(R/2) = \pi(\lfloor R/2 \rfloor)$.

Formalized by `MetaMathlibExt.IsRamanujanPrime`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/RamanujanPrime.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/RamanujanPrime.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes/index.html#is-ramanujan-prime).

## The $n$-th Ramanujan prime

Let $\pi$ be the prime-counting function. For natural numbers
$R$ and $n$, $R$ is the $n$-th Ramanujan prime when $n \ge 1$, $R$ is a prime with
$\pi(R) - \pi(R/2) = n$, and every prime $p$ with $\pi(p) - \pi(p/2) = n$ satisfies $p \le R$.
That is, $R$ is the largest prime satisfying the Ramanujan counting condition for $n$.

Here $\pi(x)$ counts the primes $p \le x$, so $\pi(R/2) = \pi(\lfloor R/2 \rfloor)$.

Formalized by `MetaMathlibExt.IsNthRamanujanPrime`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/RamanujanPrime.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/RamanujanPrime.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes/index.html#is-nth-ramanujan-prime).

## Counting members of a set up to a real bound

For a set $P$ of natural numbers and a
real number $x$, $\pi_P(x)$ is the number of members of $P$ that are at most $x$.

In the intended application $P$ is an infinite set of primes.

Formalized by `MetaMathlibExt.primeCountingWithin`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/VPRamanujanNumber.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/VPRamanujanNumber.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes/index.html#prime-counting-within).

## Generalized Ramanujan numbers

Let $P$ be a set of natural numbers, $v$ a real number and
$m$, $R$ natural numbers, and write $\pi_P(x)$ for the number of members of $P$ that are at most
$x$. Then $R$ is the $(v, P)$-Ramanujan number of index $m$ when $P$ is an infinite set of
primes, $v > 1$, and $R$ is the least natural number such that $\pi_P(x) - \pi_P(x/v) \ge m$
for every real $x \ge R$, that is, every interval $(x/v, x]$ with $x \ge R$ contains at least
$m$ members of $P$.

Formalized by `MetaMathlibExt.IsVPRamanujanNumber`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/VPRamanujanNumber.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/VPRamanujanNumber.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes/index.html#is-vpramanujan-number).

## Laishram's upper bound for Ramanujan primes

Let $p_k$ denote the $k$-th prime, so that
$p_1 = 2$. For all natural numbers $n$ and $R$, if $R$ is the $n$-th Ramanujan prime (which
entails $n \ge 1$), then $R < p_{3n}$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL14/Noe/noe12.tex, theorem lines 152-160, definition lines 105-117.

Stated but not proved: `MetaMathlibExt.laishram_ramanujan_prime_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/LaishramRamanujanPrimeBoundWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/LaishramRamanujanPrimeBoundWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes/index.html#laishram-ramanujan-prime-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/ramanujan-primes)
