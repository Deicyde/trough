---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.Internal.second_residual_mid_primeCounting_lt_start_pow, Nat.SylvesterSchur.Internal.erdos_choose_prime_factor_gt, Nat.exists_prime_gt_and_dvd_ascFactorial
statement: formalized
proof: formalized
---

# Sylvester–Schur theorem: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/index.html).

## Prime-counting estimate for Sylvester–Schur when $38 \le n < 945$

For all natural
numbers $n$ and $k$ with $38 \le n < 945$ and $k \ge 1291$, we have
$n! \cdot (k + n - 1)^{\pi(n)} < k^n$, where $\pi(n)$ denotes the number of primes at most $n$.

The proof checks finitely many explicit numerical certificates.

Formalized by `Nat.SylvesterSchur.Internal.second_residual_mid_primeCounting_lt_start_pow`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLargeCertificates.lean, line 675](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/ResidualLargeCertificates.lean#L675). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/index.html#second-residual-mid-prime-counting-lt-st).

## Erdős key lemma

For all natural numbers $n$ and $k$ with $1 \le n < k$, the binomial
coefficient $\binom{k + n - 1}{n}$ has a prime factor $p > n$.

This is the binomial form of the Sylvester–Schur theorem, as in Erdős's 1934 proof. The case
$n = 1$ is immediate, and the cases $k = n + 1$ and $k = n + 2$ follow directly from Bertrand's
postulate.

Formalized by `Nat.SylvesterSchur.Internal.erdos_choose_prime_factor_gt`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ErdosKey.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/ErdosKey.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/index.html#erdos-choose-prime-factor-gt).

## Sylvester–Schur theorem

Let $n$ and $k$ be natural numbers with $0 < k < n$. Then some
prime $p > k$ divides the product $n(n+1)\cdots(n+k-1)$ of the $k$ consecutive integers starting
at $n$.

Formalized by `Nat.exists_prime_gt_and_dvd_ascFactorial`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/index.html#exists-prime-gt-and-dvd-asc-factorial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sylvester–Schur theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem)
