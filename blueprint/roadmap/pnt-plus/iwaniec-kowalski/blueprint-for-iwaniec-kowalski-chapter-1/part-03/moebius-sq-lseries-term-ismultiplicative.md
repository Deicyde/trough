---
declaration: theorem
origin: cited
lean: ArithmeticFunction.moebius_sq_LSeries.term_isMultiplicative
statement: formalized
proof: formalized
---

# moebius-sq-LSeries.term-isMultiplicative

We have that $n\mapsto \mu^2(n)/n^{s}$ is a multiplicative function.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [powOfMultiplicative-isMultiplicative](powofmultiplicative-ismultiplicative.md)
- [LSeries.term-isMultiplicative-if-fun-isMultiplicative](lseries-term-ismultiplicative-if-fun-ismultiplic.md)

## Proof

Follows as a consequence of Lemma LSeries.term-isMultiplicative-if-fun-isMultiplicative and moebius-sq-isMultiplicative.

## Lean

Formalized as [`ArithmeticFunction.moebius_sq_LSeries.term_isMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.moebius_sq_LSeries.term_isMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
