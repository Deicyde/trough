---
declaration: theorem
origin: cited
lean: ArithmeticFunction.two_pow_omega_isMultiplicative
statement: formalized
proof: formalized
---

# two-pow-omega-isMultiplicative

The function $n\mapsto 2^{\omega(n)}$ is multiplicative.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [powOfAdditive-isMultiplicative](powofadditive-ismultiplicative.md)

## Proof

This follows directly from Lemma powOfAdditive-isMultiplicative and the fact that $\omega(mn)=\omega(m)+\omega(n)$.

## Lean

Formalized as [`ArithmeticFunction.two_pow_omega_isMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.two_pow_omega_isMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
