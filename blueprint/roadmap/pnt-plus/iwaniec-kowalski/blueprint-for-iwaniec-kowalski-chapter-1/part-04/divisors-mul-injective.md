---
declaration: theorem
origin: cited
lean: ArithmeticFunction.divisors_mul_injective
statement: formalized
---

# divisors-mul-injective

Let $m$ and $n$ be coprime natural numbers. The function $(a,b) \mapsto ab$ is injective on the product of the divisors of $m$ and $n$.

```
Upstreamed to mathlib via PR #36495.
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $m$ and $n$ are coprime, any element in the product of their divisors can be uniquely expressed as a product of an element from each set. The injectivity follows from the uniqueness of this decomposition.

## Lean

Stated as [`ArithmeticFunction.divisors_mul_injective`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.divisors_mul_injective); the blueprint marks no proof of it as formalized.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
