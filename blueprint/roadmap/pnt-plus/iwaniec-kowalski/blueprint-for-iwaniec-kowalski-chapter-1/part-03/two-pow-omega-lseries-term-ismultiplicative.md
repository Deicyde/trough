---
declaration: theorem
origin: cited
lean: ArithmeticFunction.two_pow_omega_LSeries.term_isMultiplicative
statement: formalized
proof: formalized
---

# two-pow-omega-LSeries.term-isMultiplicative

We have that $n\mapsto 2^{\omega(n)}/n^{s}$ is a multiplicative function.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [LSeries.term-isMultiplicative-if-fun-isMultiplicative](lseries-term-ismultiplicative-if-fun-ismultiplic.md)
- [two-pow-omega-isMultiplicative](two-pow-omega-ismultiplicative.md)

## Proof

Follows as a consequence of Lemma LSeries.term-isMultiplicative-if-fun-isMultiplicative and two-pow-omega-isMultiplicative.

## Lean

Formalized as [`ArithmeticFunction.two_pow_omega_LSeries.term_isMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.two_pow_omega_LSeries.term_isMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
