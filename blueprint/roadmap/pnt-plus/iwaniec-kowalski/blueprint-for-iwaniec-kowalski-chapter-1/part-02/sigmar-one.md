---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sigmaR_one
statement: formalized
proof: formalized
---

# sigmaR-one

We have that $\sigma^R_s(1)=1$.

## Depends on

- [sigmaR](../part-01/sigmar.md)

## Proof depends on

- [sigmaR-apply](sigmar-apply.md)

## Proof

By definition we have that

$$
\sigma^R_s(1)=\sum_{d \mid 1}d^s=1^s=1.
$$

## Lean

Formalized as [`ArithmeticFunction.sigmaR_one`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sigmaR_one).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
