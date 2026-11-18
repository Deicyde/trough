---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeries.term_isMultiplicative_if_fun_isMultiplicative
statement: formalized
proof: formalized
---

# LSeries.term-isMultiplicative-if-fun-isMultiplicative

If $f$ is a multiplicative function, then so to is $n\mapsto f(n)/n^s$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Note that $f(mn)/(mn)^s=f(m)f(n)/(m^sn^s)=(f(m)/m^s)(f(n)/n^s)$.

## Lean

Formalized as [`ArithmeticFunction.LSeries.term_isMultiplicative_if_fun_isMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeries.term_isMultiplicative_if_fun_isMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
