---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_not_forall_prime_dvd_le, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_upper_lt_lower, Nat.SylvesterSchur.primeCounting_le_sub_one, Nat.SylvesterSchur.primeCounting_le_half_add_one, Nat.SylvesterSchur.primeCounting_le_three_mul_div_eight
statement: formalized
proof: formalized
---

# Prime-counting estimates for Sylvester-Schur

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/prime-counting-estimates-for-sylvester-schur/index.html).

## Negating the no-large-prime condition for $\binom{N}{r}$

Let $N$ and $r$ be natural
numbers. If it is not the case that every prime dividing $\binom{N}{r}$ is at most $r$, then some
prime $p$ with $r < p$ divides $\binom{N}{r}$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_not_forall_prime_dvd_le`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/prime-counting-estimates-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-not-for).

## A prime divisor of $\binom{N}{r}$ above $r$ from an upper bound below the lower bound

Let $N$, $r$ and $U$ be natural numbers, and let $m = \max(N + 1 - r, 0)$. Suppose that
$\binom{N}{r} \le U$ whenever every prime dividing $\binom{N}{r}$ is at most $r$, and that
$U < m^r / r!$ as rational numbers. Then some prime $p$ with $r < p$ divides $\binom{N}{r}$.

The quotient $m^r / r!$ is the standard lower bound for $\binom{N}{r}$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_upper_lt_lower`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/prime-counting-estimates-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-upper-l).

## At most $r - 1$ primes up to $r$

For every natural number $r \ge 2$, the number
$\pi(r)$ of primes $p \le r$ satisfies $\pi(r) \le r - 1$, since all such primes lie in
$\{2, \dots, r\}$.

Formalized by `Nat.SylvesterSchur.primeCounting_le_sub_one`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/prime-counting-estimates-for-sylvester-schur/index.html#prime-counting-le-sub-one).

## At most $\lfloor r/2 \rfloor + 1$ primes up to $r$

For every natural number $r$, the
number $\pi(r)$ of primes $p \le r$ satisfies $\pi(r) \le \lfloor r/2 \rfloor + 1$.

Formalized by `Nat.SylvesterSchur.primeCounting_le_half_add_one`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/prime-counting-estimates-for-sylvester-schur/index.html#prime-counting-le-half-add-one).

## Erdős's $3r/8$ prime-counting bound

For every natural number $r \ge 38$, the number
$\pi(r)$ of primes $p \le r$ satisfies $\pi(r) \le \lfloor 3r/8 \rfloor$.

The infinite tail follows from the residue-class estimate modulo $30$; the range
$38 \le r < 91$ is checked directly.

Formalized by `Nat.SylvesterSchur.primeCounting_le_three_mul_div_eight`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/PrimeCounting.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/prime-counting-estimates-for-sylvester-schur/index.html#prime-counting-le-three-mul-div-eight).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime-counting estimates for Sylvester-Schur](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/prime-counting-estimates-for-sylvester-schur/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/prime-counting-estimates-for-sylvester-schur)
