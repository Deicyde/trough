---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_card_maxPrimeFac_prime_add_gt_rpow, MetaMathlibExt.exists_rpow_div_log_le_mul_card_prime_dvd_prime_sub_one, MetaMathlibExt.carmichael_constant_run_length_isBigO, MetaMathlibExt.totient_nonincreasing_run_length_isEquivalent
statement: formalized
---

# Large prime factors of shifted primes

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-prime-factors-of-shifted-primes/index.html).

## Baker–Harman: shifted primes with a large prime factor

For every integer $a$ and every
real $\theta$ with $0 < \theta \le 0.677$ there is a real $\delta$ with $0 < \delta < 1$ such that,
for all sufficiently large real $x$, the number of primes $p \le x$ for which the largest prime
factor $P(|p + a|)$ of $|p + a|$ exceeds $x^\theta$ is greater than $\delta x / \log x$. Here
$P(0) = 0$ and $P(1) = 1$.

The statement covers every integer $a$, as the cited lemma is printed; Baker and Harman state the
bound for a nonzero shift, and the case $a = 0$ follows from the prime number theorem, since every
prime in $(x^\theta, x]$ qualifies and these number $(1 + o(1)) x / \log x$.

## Sources

- Noah Lebowitz-Lockard and J.C. Saunders, *Runs of Integers with Constant Values of the Carmichael Function*, INTEGERS 24 (2024), Article A91, Lemma 1, quoted there from Baker and Harman.

Stated but not proved: `MetaMathlibExt.exists_card_maxPrimeFac_prime_add_gt_rpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ShiftedPrimeLargestFactorWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/ShiftedPrimeLargestFactorWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-prime-factors-of-shifted-primes/index.html#exists-card-max-prime-fac-prime-add-gt-r).

## Large prime divisors of shifted primes

There is a real number $C > 0$ such that for all
sufficiently large real $x$ we have $x^{0.677} / \log x \le C \cdot N(x)$, where $N(x)$ is the
number of primes $q \le x$ with $q > x^{0.677}$ such that $q \mid p - 1$ for some prime $p \le x$.

The condition $q \le x$ is automatic, since $q \mid p - 1$ with $p \le x$ forces $q < x$.

## Sources

- Noah Lebowitz-Lockard and J.C. Saunders, *Runs of Integers with Constant Values of the Carmichael Function*, INTEGERS 24 (2024), Article A91, Lemma 2.

Stated but not proved: `MetaMathlibExt.exists_rpow_div_log_le_mul_card_prime_dvd_prime_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ShiftedPrimeLargestFactorWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/ShiftedPrimeLargestFactorWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-prime-factors-of-shifted-primes/index.html#exists-rpow-div-log-le-mul-card-prime-dv).

## Runs of constant Carmichael values

For real $x$, let $F_\lambda(x)$ be the largest natural
number $k$ for which there is a natural number $n \ge 0$ with $n + k \le x$ and
$\lambda(n + 1) = \lambda(n + 2) = \cdots = \lambda(n + k)$ (and $0$ if there is no such $k$), where
$\lambda$ is the Carmichael function. Then $F_\lambda(x) = O\left((\log x)^{1000/677}\right)$ as
$x \to \infty$; that is, $F_\lambda(x) = O\left((\log x)^{1/c}\right)$ with $c = 0.677$.

This follows the definition of $F_f(x)$ in the arXiv version (arXiv:2402.06832v4, Section 1):
$F_f(x)$ is the largest $k$ for which $f(n+1) = \cdots = f(n+k)$ has a solution with $n + k \le x$.

## Sources

- Noah Lebowitz-Lockard and J.C. Saunders, *Runs of Integers with Constant Values of the Carmichael Function*, INTEGERS 24 (2024), Article A91, Theorem 3.

Stated but not proved: `MetaMathlibExt.carmichael_constant_run_length_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ShiftedPrimeLargestFactorWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/ShiftedPrimeLargestFactorWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-prime-factors-of-shifted-primes/index.html#carmichael-constant-run-length-is-big-o).

## Pollack–Pomerance–Treviño: nonincreasing runs of Euler's function

For real $x$, let
$G_\varphi(x)$ be the largest natural number $k$ for which there is a natural number $n \ge 0$ with
$n + k \le x$ and $\varphi(n + 1) \ge \varphi(n + 2) \ge \cdots \ge \varphi(n + k)$ (and $0$ if
there is no such $k$), where $\varphi$ is Euler's totient function. Then
$G_\varphi(x) \sim \log_3 x / \log_6 x$ as $x \to \infty$, where $\log_j$ denotes the $j$-fold
iterate of the natural logarithm.

This follows the definition of $G_f(x)$ in the paper (arXiv:2402.06832v4, Section 1): $G_f(x)$ is
the largest $k$ for which $f(n+1) \ge f(n+2) \ge \cdots \ge f(n+k)$ has a solution with
$n + k \le x$.

## Sources

- Noah Lebowitz-Lockard and J.C. Saunders, *Runs of Integers with Constant Values of the Carmichael Function*, INTEGERS 24 (2024), Article A91, Theorem 1, quoted there from Pollack, Pomerance, and Treviño.

Stated but not proved: `MetaMathlibExt.totient_nonincreasing_run_length_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ShiftedPrimeLargestFactorWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/ShiftedPrimeLargestFactorWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-prime-factors-of-shifted-primes/index.html#totient-nonincreasing-run-length-is-equi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large prime factors of shifted primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-prime-factors-of-shifted-primes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-prime-factors-of-shifted-primes)
