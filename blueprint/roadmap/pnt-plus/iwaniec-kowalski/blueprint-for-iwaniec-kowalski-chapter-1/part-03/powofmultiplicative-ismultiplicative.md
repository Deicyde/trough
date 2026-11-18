---
declaration: theorem
origin: cited
lean: ArithmeticFunction.powOfMultiplicative_isMultiplicative
statement: formalized
proof: formalized
---

# powOfMultiplicative-isMultiplicative

If $f$ is a multiplicative function, then so to is $n\mapsto f(n)^k$ for any $k\in\mathbb{N}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Note that $f(mn)^k=(f(m)f(n))^k=(f(m)^k)(f(n)^k)$.

## Lean

Formalized as [`ArithmeticFunction.powOfMultiplicative_isMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.powOfMultiplicative_isMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
