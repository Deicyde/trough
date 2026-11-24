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

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
