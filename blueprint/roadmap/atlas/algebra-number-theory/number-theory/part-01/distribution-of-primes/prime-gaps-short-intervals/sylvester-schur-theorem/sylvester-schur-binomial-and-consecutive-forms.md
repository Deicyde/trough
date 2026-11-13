---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.prime_dvd_choose_of_dvd_consecutive, Nat.SylvesterSchur.exists_dvd_consecutive_of_prime_dvd_choose, Nat.SylvesterSchur.consecutive_of_exists_prime_dvd_choose
statement: formalized
proof: formalized
---

# Sylvester-Schur: binomial and consecutive forms

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/sylvester-schur-binomial-and-consecutive-forms/index.html).

## Large prime divisors of a block term divide the binomial coefficient

Let $n$, $k$ and
$j$ be natural numbers with $j < n$, and let $p$ be a prime with $p > n$. If $p$ divides
$k + j$, one of the $n$ consecutive integers $k, \dots, k+n-1$, then $p$ divides
$\binom{k+n-1}{n}$.

Formalized by `Nat.SylvesterSchur.prime_dvd_choose_of_dvd_consecutive`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Bridge.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Bridge.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/sylvester-schur-binomial-and-consecutive-forms/index.html#prime-dvd-choose-of-dvd-consecutive).

## Prime divisors of the block binomial coefficient divide a block term

Let $n$ and $k$ be
natural numbers and let $p$ be a prime. If $p$ divides $\binom{k+n-1}{n}$, then $p$ divides
$k + i$ for some $i$ with $0 \le i < n$.

Formalized by `Nat.SylvesterSchur.exists_dvd_consecutive_of_prime_dvd_choose`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Bridge.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Bridge.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/sylvester-schur-binomial-and-consecutive-forms/index.html#exists-dvd-consecutive-of-prime-dvd-choo).

## From a large prime divisor of the binomial coefficient to one in the block

Let $n$ and
$k$ be natural numbers. If some prime $p > n$ divides $\binom{k+n-1}{n}$, then some prime
$p > n$ divides one of the integers $k + i$ with $0 \le i < n$.

Formalized by `Nat.SylvesterSchur.consecutive_of_exists_prime_dvd_choose`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Bridge.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Bridge.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/sylvester-schur-binomial-and-consecutive-forms/index.html#consecutive-of-exists-prime-dvd-choose).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sylvester-Schur: binomial and consecutive forms](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/sylvester-schur-binomial-and-consecutive-forms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/sylvester-schur-binomial-and-consecutive-forms)
