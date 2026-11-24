---
declaration: theorem
origin: cited
lean: ArithmeticFunction.moebius_sq_eq
statement: formalized
proof: formalized
---

# moebius-sq-eq

I-K (1.33): $\mu^2(n) = \sum_{d^2|n} \mu(d)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [sum-moebius-sq-divisors](sum-moebius-sq-divisors.md)
- [sum-moebius-sq-divisors-is-multiplicative](sum-moebius-sq-divisors-ismultiplicative.md)
- [sum-moebius-sq-divisors-apply](sum-moebius-sq-divisors-apply.md)
- [sum-moebius-sq-divisors-apply-prime-pow](sum-moebius-sq-divisors-apply-prime-pow.md)

## Proof

Apply the previous two lemmas.

## Lean

Formalized as [`ArithmeticFunction.moebius_sq_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.moebius_sq_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
