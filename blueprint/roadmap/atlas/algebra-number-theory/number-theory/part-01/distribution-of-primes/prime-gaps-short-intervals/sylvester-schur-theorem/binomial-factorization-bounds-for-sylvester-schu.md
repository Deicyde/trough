---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.choose_eq_prod_small_prime_powers_of_no_large, Nat.SylvesterSchur.choose_le_top_pow_primeCounting_of_no_large, Nat.SylvesterSchur.choose_le_top_pow_sub_one_of_no_large, Nat.SylvesterSchur.choose_le_top_pow_half_add_one_of_no_large, Nat.SylvesterSchur.choose_le_top_pow_three_mul_div_eight_of_no_large, Nat.SylvesterSchur.choose_le_prod_primorial_nthRoot_of_no_large, Nat.SylvesterSchur.choose_le_prod_erdos_layers_of_no_large, Nat.SylvesterSchur.choose_le_prod_erdos_div_three_layers_of_no_large
statement: formalized
proof: formalized
---

# Binomial factorization bounds for Sylvester-Schur

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html).

## Truncating the prime factorization of a binomial coefficient

Let $r \le N$ be natural
numbers such that every prime divisor of $\binom{N}{r}$ is at most $r$. Then
$\prod_{p=0}^{r} p^{v_p(\binom{N}{r})} = \binom{N}{r}$, where $v_p(m)$ is the exponent of $p$ in
the prime factorization of $m$ (zero when $p$ is not prime).

Formalized by `Nat.SylvesterSchur.choose_eq_prod_small_prime_powers_of_no_large`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html#choose-eq-prod-small-prime-powers-of-no).

## Prime-counting bound for binomial coefficients without large prime factors

Let $0 < N$
and $r \le N$ be natural numbers such that every prime divisor of $\binom{N}{r}$ is at most $r$.
Then $\binom{N}{r} \le N^{\pi(r)}$, where $\pi(r)$ is the number of primes $p \le r$.

Formalized by `Nat.SylvesterSchur.choose_le_top_pow_primeCounting_of_no_large`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html#choose-le-top-pow-prime-counting-of-no-l).

## Elementary power bound for binomial coefficients without large prime factors

Let
$0 < N$ and $2 \le r \le N$ be natural numbers such that every prime divisor of $\binom{N}{r}$
is at most $r$. Then $\binom{N}{r} \le N^{r-1}$.

Formalized by `Nat.SylvesterSchur.choose_le_top_pow_sub_one_of_no_large`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html#choose-le-top-pow-sub-one-of-no-large).

## Half-exponent bound for binomial coefficients without large prime factors

Let $0 < N$
and $r \le N$ be natural numbers such that every prime divisor of $\binom{N}{r}$ is at most $r$.
Then $\binom{N}{r} \le N^{\lfloor r/2 \rfloor + 1}$.

Formalized by `Nat.SylvesterSchur.choose_le_top_pow_half_add_one_of_no_large`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html#choose-le-top-pow-half-add-one-of-no-lar).

## Three-eighths exponent bound for binomial coefficients without large prime factors

Let
$0 < N$ and $38 \le r \le N$ be natural numbers such that every prime divisor of
$\binom{N}{r}$ is at most $r$. Then $\binom{N}{r} \le N^{\lfloor 3r/8 \rfloor}$.

Formalized by `Nat.SylvesterSchur.choose_le_top_pow_three_mul_div_eight_of_no_large`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html#choose-le-top-pow-three-mul-div-eight-of).

## Erdős root-layer bound for binomial coefficients without large prime factors

Let
$0 < N$ and $r \le N$ be natural numbers such that every prime divisor of $\binom{N}{r}$ is at
most $r$. Write $P(m)$ for the product of all primes $p \le m$ and let
$L = \lfloor \log_2 N \rfloor$. Then
$\binom{N}{r} \le \prod_{k=1}^{L} P(\lfloor N^{1/k} \rfloor)$.

Formalized by `Nat.SylvesterSchur.choose_le_prod_primorial_nthRoot_of_no_large`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html#choose-le-prod-primorial-nth-root-of-no).

## Erdős layer bound for binomial coefficients without large prime factors

Let $0 < N$ and
$r \le N$ be natural numbers such that every prime divisor of $\binom{N}{r}$ is at most $r$.
Write $P(m)$ for the product of all primes $p \le m$ and let $L = \lfloor \log_2 N \rfloor$. Then
$\binom{N}{r} \le \prod_{k=1}^{L} a_k$, where $a_1 = P(r)$ and $a_k = P(\lfloor N^{1/k} \rfloor)$
for $k \ge 2$.

This matches the product estimate in Erdős's proof.

Formalized by `Nat.SylvesterSchur.choose_le_prod_erdos_layers_of_no_large`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html#choose-le-prod-erdos-layers-of-no-large).

## Erdős layer bound with a one-third first layer

Let $N \ge 6$ and $r$ be natural numbers
with $2r \le N$ (hence $r \le N$) such that every prime divisor of $\binom{N}{r}$ is at most $r$.
Write $P(m)$ for the product of all primes $p \le m$ and let $L = \lfloor \log_2 N \rfloor$. Then
$\binom{N}{r} \le \prod_{k=1}^{L} a_k$, where $a_1 = P(\lfloor N/3 \rfloor)$ and
$a_k = P(\lfloor N^{1/k} \rfloor)$ for $k \ge 2$.

Formalized by `Nat.SylvesterSchur.choose_le_prod_erdos_div_three_layers_of_no_large`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ChooseFactorization.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html#choose-le-prod-erdos-div-three-layers-of).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial factorization bounds for Sylvester-Schur](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/binomial-factorization-bounds-for-sylvester-schu)
