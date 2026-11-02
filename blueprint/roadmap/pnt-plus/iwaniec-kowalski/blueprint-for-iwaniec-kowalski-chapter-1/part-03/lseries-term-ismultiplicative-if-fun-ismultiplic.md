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

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
