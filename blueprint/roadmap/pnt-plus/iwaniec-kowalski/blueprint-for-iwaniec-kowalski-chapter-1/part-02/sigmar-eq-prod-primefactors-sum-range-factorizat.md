---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sigmaR_eq_prod_primeFactors_sum_range_factorization_pow_mul
statement: formalized
proof: formalized
---

# sigmaR-eq-prod-primeFactors-sum-range-factorization-pow-mul

We have that

$$
\sigma^R_s(n)=\prod_{p\mid n}\sum_{j=0}^{v_p(n)}p^{js}.
$$

## Depends on

- [sigmaR](../part-01/sigmar.md)

## Proof depends on

- [isMultiplicative-sigmaR](ismultiplicative-sigmar.md)
- [sigmaR-apply-prime-pow](sigmar-apply-prime-pow.md)

## Proof

Since $\sigma^R_s$ is multiplicative, it suffices to understand it at primes powers.

$$
\sigma^R_s(n)=\prod_{p\mid n}\sigma^R_s(p^{v_p(n)}).
$$

Applying Lemma sigmaR-apply-prime-pow.

## Lean

Formalized as [`ArithmeticFunction.sigmaR_eq_prod_primeFactors_sum_range_factorization_pow_mul`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sigmaR_eq_prod_primeFactors_sum_range_factorization_pow_mul).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
