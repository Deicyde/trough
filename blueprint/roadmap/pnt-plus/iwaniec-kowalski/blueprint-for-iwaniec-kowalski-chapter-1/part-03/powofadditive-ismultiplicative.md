---
declaration: theorem
origin: cited
lean: ArithmeticFunction.powOfAdditive_isMultiplicative
statement: formalized
proof: formalized
---

# powOfAdditive-isMultiplicative

If $f$ is an additive function, then so to is $n\mapsto k^{f(n)}$ for any fixed $k$.

## Depends on

- [IsAdditive](../part-01/isadditive.md)

## Proof

Note that $k^{f(mn)}=k^{f(m)+f(n)}=k^{f(m)}k^{f(n)}$.

## Lean

Formalized as [`ArithmeticFunction.powOfAdditive_isMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.powOfAdditive_isMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
