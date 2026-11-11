---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.pow_mul_choose_le_pow_mul_choose, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_prod_erdos_div_three_layers_lt_lower_pow, Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_mul_prod_erdos_div_three_layers_lt_four_pow
statement: formalized
proof: formalized
---

# Erdős layer products for Sylvester-Schur

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/erd-s-layer-products-for-sylvester-schur/index.html).

## Scaled monotonicity of binomial coefficients

For natural numbers $r$, $M$ and $N$ with
$r \le M \le N$, we have $N^r \binom{M}{r} \le M^r \binom{N}{r}$.

In other words, $\binom{N}{r} / N^r$ is nondecreasing in $N$ for $N \ge \max(r, 1)$.

Formalized by `Nat.SylvesterSchur.pow_mul_choose_le_pow_mul_choose`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ErdosLayers.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ErdosLayers.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/erd-s-layer-products-for-sylvester-schur/index.html#pow-mul-choose-le-pow-mul-choose).

## Erdős layer criterion, factorial form

Let $N$ and $r$ be natural numbers with $0 < N$,
$r \le N$, $2r \le N$ and $6 \le N$. For a natural number $x$ write $x\#$ for the primorial of
$x$, the product of all primes $p \le x$, and let $L = \lfloor \log_2 N \rfloor$. If
$r! \cdot \lfloor N/3 \rfloor\# \cdot \prod_{m=2}^{L} \lfloor N^{1/m} \rfloor\# < (N + 1 - r)^r$,
then the binomial coefficient $\binom{N}{r}$ has a prime factor $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_factorial_mul_prod_erdos_div_three_layers_lt_lower_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ErdosLayers.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ErdosLayers.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/erd-s-layer-products-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-factori).

## Erdős layer criterion, power-of-four form

Let $N$ and $r$ be natural numbers with
$4 \le r$, $2r \le N$ and $6 \le N$. For a natural number $x$ write $x\#$ for the primorial of
$x$, the product of all primes $p \le x$, and let $L = \lfloor \log_2 N \rfloor$. If
$r \cdot \lfloor N/3 \rfloor\# \cdot \prod_{m=2}^{L} \lfloor N^{1/m} \rfloor\# < 4^r$, then the
binomial coefficient $\binom{N}{r}$ has a prime factor $p > r$.

Formalized by `Nat.SylvesterSchur.exists_large_prime_dvd_choose_of_mul_prod_erdos_div_three_layers_lt_four_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ErdosLayers.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ErdosLayers.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/erd-s-layer-products-for-sylvester-schur/index.html#exists-large-prime-dvd-choose-of-mul-pro).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős layer products for Sylvester-Schur](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/erd-s-layer-products-for-sylvester-schur/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/erd-s-layer-products-for-sylvester-schur)
