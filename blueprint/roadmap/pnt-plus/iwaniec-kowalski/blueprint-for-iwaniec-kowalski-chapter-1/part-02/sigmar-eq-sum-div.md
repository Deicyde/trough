---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sigmaR_eq_sum_div
statement: formalized
proof: formalized
---

# sigmaR-eq-sum-div

We have that $\sigma^R_s(n)=\sum_{d\mid n}(n/d)^s$.

## Depends on

- [sigmaR](../part-01/sigmar.md)

## Proof depends on

- [sigmaR-apply](sigmar-apply.md)

## Proof

Note that $d \mapsto n/d$ forms a one-to-one mapping between the divisors of $n$. Using this in combination with the definiton we have that

$$
\sigma^R_s(n)=\sum_{d\mid n}d^s=\sum_{d\mid n}(n/d)^s.
$$

## Lean

Formalized as [`ArithmeticFunction.sigmaR_eq_sum_div`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sigmaR_eq_sum_div).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
