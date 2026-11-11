---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_scaled_ternary_erdos_layers_bound, Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_central_offset_erdos_div_three_layers_bound, Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_two_mul_add_two_small, Nat.SylvesterSchur.Internal.second_residual_tiny_has_large_prime_factor, Nat.SylvesterSchur.Internal.second_residual_mid_has_large_prime_factor
statement: formalized
proof: formalized
---

# Finite residual checks for the Sylvester-Schur theorem

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/finite-residual-checks-for-the-sylvester-schur-t/index.html).

## A numerical criterion for a prime divisor of $\binom{N}{r}$ above $r$ when $N \ge 3r$

Let $N$ and $r$ be natural numbers with $r \ge 4$ and $3r \le N$, and let
$e = r + \lfloor \sqrt{N} \rfloor + \lfloor N^{1/3} \rfloor \cdot \lfloor \log_2 N \rfloor$. If
$r \cdot 2^r \cdot (3r)^r \cdot 4^e < 3^r \cdot 4^r \cdot N^r$, then some prime $p$ with $r < p$
divides $\binom{N}{r}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_scaled_ternary_erdos_layers_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/finite-residual-checks-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-scaled-ternar).

## A numerical criterion for a prime divisor of $\binom{N}{r}$ above $r$ when $N = 2r + i$

Let $r$, $i$ and $N$ be natural numbers with $r \ge 4$, $i \le r$, $N = 2r + i$ and $N \ge 6$. For a
natural number $n$ write $n\#$ for the product of the primes $p \le n$. Let
$L = \lfloor \log_2 N \rfloor$, let $a_0 = \lfloor N/3 \rfloor\#$ and
$a_j = \lfloor N^{1/(j+1)} \rfloor\#$ for $j \ge 1$, and put $P = \prod_{j=0}^{L-1} a_j$. If
$r \cdot 2^i \cdot P < 3^i \cdot 4^r$, then some prime $p$ with $r < p$ divides $\binom{N}{r}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_central_offset_erdos_div_three_layers_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/finite-residual-checks-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-central-offse).

## A prime divisor of $\binom{2n+2}{n}$ above $n$ for small $n$

For every natural number
$n$ with $7 \le n < 512$, some prime $p$ with $n < p$ divides $\binom{2n+2}{n}$.

These cases are handled by an explicit short prime-gap certificate.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_two_mul_add_two_small`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/finite-residual-checks-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-two-mul-add-two).

## A block term with a large prime factor, small range

Let $n$ and $k$ be natural numbers
with $7 \le n < 38$ and $n + 3 \le k < 100$. Then there are a natural number $i < n$ and a
prime $p > n$ such that $p$ divides $k + i$.

The witness comes from a table of prime gaps.

Formalized by `Nat.SylvesterSchur.Internal.second_residual_tiny_has_large_prime_factor`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/finite-residual-checks-for-the-sylvester-schur-t/index.html#second-residual-tiny-has-large-prime-fac).

## A block term with a large prime factor, middle range

Let $n$ and $k$ be natural numbers
with $38 \le n < 945$ and $n + 3 \le k < 1291$. Then there are a natural number $i < n$ and a
prime $p > n$ such that $p$ divides $k + i$.

The witness comes from a table of prime gaps.

Formalized by `Nat.SylvesterSchur.Internal.second_residual_mid_has_large_prime_factor`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualFinite.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/finite-residual-checks-for-the-sylvester-schur-t/index.html#second-residual-mid-has-large-prime-fact).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite residual checks for the Sylvester-Schur theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/finite-residual-checks-for-the-sylvester-schur-t/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/finite-residual-checks-for-the-sylvester-schur-t)
