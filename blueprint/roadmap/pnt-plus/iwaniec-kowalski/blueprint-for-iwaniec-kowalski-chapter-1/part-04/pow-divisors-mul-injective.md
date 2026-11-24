---
declaration: theorem
origin: cited
lean: ArithmeticFunction.pow_divisors_mul_injective
statement: formalized
proof: formalized
---

# pow-divisors-mul-injective

Let $m$ and $n$ be coprime natural numbers and let $k$ be fixed. The map $(a,b) \mapsto ab$ is injective on the product of $\{a \mid m : a^k \mid m\}$ and $\{b \mid n : b^k \mid n\}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [divisors-mul-injective](divisors-mul-injective.md)

## Proof

This is the restriction of Lemma divisors-mul-injective to a subset of the divisor product, so injectivity is preserved.

## Lean

Formalized as [`ArithmeticFunction.pow_divisors_mul_injective`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.pow_divisors_mul_injective).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
