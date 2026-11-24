---
declaration: theorem
origin: cited
lean: ArithmeticFunction.isMultiplicative_sigmaR
statement: formalized
proof: formalized
---

# isMultiplicative-sigmaR

For fixed $s$ function $n\mapsto\sigma^R_s(n)$ is multiplicative.

## Depends on

- [sigmaR](../part-01/sigmar.md)

## Proof depends on

- [isMultiplicative-powR](ismultiplicative-powr.md)
- [sigmaR-eq-zeta-mul-powR](sigmar-eq-zeta-mul-powr.md)
- [powR](powr.md)

## Proof

Recall from Lemma sigmaR-eq-zeta-mul-powR that $\sigma^R$ is $\zeta$ convolved with Definition [powR](powr.md). Since both of these are multiplicative functions, their convolution is also multiplicative.

## Lean

Formalized as [`ArithmeticFunction.isMultiplicative_sigmaR`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.isMultiplicative_sigmaR).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
