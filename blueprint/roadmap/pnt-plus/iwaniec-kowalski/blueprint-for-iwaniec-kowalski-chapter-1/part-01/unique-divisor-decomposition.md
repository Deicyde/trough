---
declaration: theorem
origin: cited
lean: ArithmeticFunction.unique_divisor_decomposition
statement: formalized
---

# unique divisor decomposition

If $a$ and $b$ are coprime, then any divisor $d$ of $ab$ can be uniquely expressed as a product of a divisor of $a$ and a divisor of $b$.

```
This has been upstreamed #36495.
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $a$ and $b$ be coprime natural numbers, and let $d$ be a divisor of $ab$. Since $a$ and $b$ are coprime, we can use the fact that the divisors of $ab$ correspond to pairs of divisors of $a$ and $b$. Specifically, we can express $d$ as $d = d_a \cdot d_b$, where $d_a$ divides $a$ and $d_b$ divides $b$. The uniqueness of this decomposition follows from the coprimality of $a$ and $b$, which ensures that the divisors of $a$ and $b$ do not share any common factors. Therefore, there is a one-to-one correspondence between the divisors of $ab$ and the pairs of divisors of $a$ and $b$, which guarantees the uniqueness of the decomposition.

## Lean

Formalized as [`ArithmeticFunction.unique_divisor_decomposition`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.unique_divisor_decomposition).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
