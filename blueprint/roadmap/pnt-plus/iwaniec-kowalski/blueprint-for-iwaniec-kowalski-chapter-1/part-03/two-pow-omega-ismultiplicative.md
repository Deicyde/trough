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

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
