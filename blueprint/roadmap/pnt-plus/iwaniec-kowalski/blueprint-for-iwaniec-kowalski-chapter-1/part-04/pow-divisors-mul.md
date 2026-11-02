---
declaration: theorem
origin: cited
lean: ArithmeticFunction.pow_divisors_mul
statement: formalized
proof: formalized
---

# pow-divisors-mul

Let $m$ and $n$ be coprime natural numbers and let $k$ be fixed. The divisors $x$ of $mn$ with $x^k \mid mn$ are exactly the products $ab$ where $a \mid m$, $a^k \mid m$, $b \mid n$, and $b^k \mid n$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $m$ and $n$ are coprime, every divisor of $mn$ factors uniquely as $ab$ with $a \mid m$ and $b \mid n$. For such a factorization, $x^k \mid mn$ is equivalent to $a^k \mid m$ and $b^k \mid n$, again by coprimality.

## Lean

Formalized as [`ArithmeticFunction.pow_divisors_mul`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.pow_divisors_mul).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
