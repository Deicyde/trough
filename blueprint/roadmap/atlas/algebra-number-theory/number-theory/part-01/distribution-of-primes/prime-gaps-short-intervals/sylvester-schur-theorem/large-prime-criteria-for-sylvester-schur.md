---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_prod_erdos_layers_lt_lower_pow, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_prod_primorial_nthRoot_lt_lower_pow, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_mul_top_pow_sqrt_mul_primorial_lt_four_pow, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_sqrt_mul_primorial_lt_lower_pow, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_primeCounting_lt_lower_pow, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_half_add_one_lt_lower_pow, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_three_mul_div_eight_lt_lower_pow, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_self_pow_mul_top_pow_three_mul_div_eight_lt_lower_pow
statement: formalized
proof: formalized
---

# Large-prime criteria for Sylvester-Schur

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html).

## Large-prime criterion from the Erdős layer bound

Let $N$ and $r$ be natural numbers
with $0 < N$ and $r \le N$, write $m\#$ for the product of the primes at most $m$, and let
$L = \lfloor \log_2 N \rfloor$. Put $P_1 = r\#$ and $P_k = \lfloor N^{1/k} \rfloor\#$ for
$k \ge 2$. If

$$r! \cdot \prod_{k=1}^{L} P_k < (N + 1 - r)^r,$$

then $\binom{N}{r}$ has a prime divisor $p$ with $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_prod_erdos_layers_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-factori).

## Large-prime criterion from the prime-power layer bound

Let $N$ and $r$ be natural
numbers with $0 < N$ and $r \le N$, write $m\#$ for the product of the primes at most $m$, and
let $L = \lfloor \log_2 N \rfloor$. If

$$r! \cdot \prod_{k=1}^{L} \lfloor N^{1/k} \rfloor\# < (N + 1 - r)^r,$$

then $\binom{N}{r}$ has a prime divisor $p$ with $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_prod_primorial_nthRoot_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-factori-2).

## Central-range large-prime criterion from the square-root split bound

Let $N$ and $r$ be
natural numbers with $4 \le r$ and $2r \le N$, and write $r\#$ for the product of the primes at
most $r$. If $r \cdot N^{\lfloor \sqrt{N} \rfloor + 1} \cdot r\# < 4^r$, then $\binom{N}{r}$ has
a prime divisor $p$ with $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_mul_top_pow_sqrt_mul_primorial_lt_four_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-mul-top).

## Large-prime criterion from the square-root split bound

Let $N$ and $r$ be natural
numbers with $0 < N$ and $r \le N$, and write $r\#$ for the product of the primes at most $r$. If
$r! \cdot N^{\lfloor \sqrt{N} \rfloor + 1} \cdot r\# < (N + 1 - r)^r$, then $\binom{N}{r}$ has a
prime divisor $p$ with $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_sqrt_mul_primorial_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-factori-3).

## Large-prime criterion from the prime-counting bound

Let $N$ and $r$ be natural numbers
with $0 < N$ and $r \le N$, and let $\pi(r)$ be the number of primes at most $r$. If
$r! \cdot N^{\pi(r)} < (N + 1 - r)^r$, then $\binom{N}{r}$ has a prime divisor $p$ with $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_primeCounting_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-factori-4).

## Large-prime criterion from the half-plus-one exponent bound

Let $N$ and $r$ be natural
numbers with $0 < N$ and $r \le N$. If $r! \cdot N^{\lfloor r/2 \rfloor + 1} < (N + 1 - r)^r$,
then $\binom{N}{r}$ has a prime divisor $p$ with $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_half_add_one_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-factori-5).

## Large-prime criterion from the 3r/8 exponent bound

Let $N$ and $r$ be natural numbers
with $0 < N$, $38 \le r$ and $r \le N$. If $r! \cdot N^{\lfloor 3r/8 \rfloor} < (N + 1 - r)^r$,
then $\binom{N}{r}$ has a prime divisor $p$ with $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_three_mul_div_eight_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-factori-6).

## Power-only large-prime criterion from the 3r/8 exponent bound

Let $N$ and $r$ be natural
numbers with $0 < N$, $38 \le r$ and $r \le N$. If
$r^r \cdot N^{\lfloor 3r/8 \rfloor} < (N + 1 - r)^r$, then $\binom{N}{r}$ has a prime divisor
$p$ with $p > r$.

This follows from the criterion with $r!$ in place of $r^r$, since $r! \le r^r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_self_pow_mul_top_pow_three_mul_div_eight_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-self-po).

## Large-prime criterion from the r − 1 exponent bound

Let $N$ and $r$ be natural numbers
with $0 < N$, $2 \le r$ and $r \le N$. If $r! \cdot N^{r-1} < (N + 1 - r)^r$, then
$\binom{N}{r}$ has a prime divisor $p$ with $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_top_pow_sub_one_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/LargePrimeCriteria.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-factori-7).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large-prime criteria for Sylvester-Schur](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/large-prime-criteria-for-sylvester-schur)
