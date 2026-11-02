---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sigmaR_eq_zeta_mul_powR
statement: formalized
proof: formalized
---

# sigmaR-eq-zeta-mul-powR

$\sigma^R(\nu) = \zeta * \text{pow}^R(\nu)$, where $\zeta$ is the constant function $1$.

## Depends on

- [sigmaR](../part-01/sigmar.md)
- [powR](powr.md)

## Proof depends on

- [sigmaR-apply](sigmar-apply.md)

## Proof

The function $\sigma^R(\nu)$ is defined as the sum of the $\nu$-th powers of the divisors of $n$. The function $\text{pow}^R(\nu)$ is defined as $n \mapsto n^\nu$ for $n \neq 0$ and $0$ for $n = 0$. The Dirichlet convolution of $\zeta$ (the constant function $1$) and $\text{pow}^R(\nu)$ is exactly $\sigma^R(\nu)$, since for each divisor $d$ of $n$, we have $(\zeta * \text{pow}^R(\nu))(n) = \sum_{d|n} 1 \cdot d^\nu = \sigma^R(\nu)(n)$. Thus, we have $\sigma^R(\nu) = \zeta * \text{pow}^R(\nu)$.

## Lean

Formalized as [`ArithmeticFunction.sigmaR_eq_zeta_mul_powR`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sigmaR_eq_zeta_mul_powR).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
