---
declaration: theorem
origin: cited
lean: ArithmeticFunction.d_apply_prime_pow
statement: formalized
proof: formalized
---

# d apply prime pow

Explicit formula: $d_k (p^a) = (a + k - 1).choose (k - 1)$ for prime $p$ and $k \geq 1$.

## Depends on

- [d](d.md)

## Proof depends on

- [d one](d-one.md)
- [d succ](d-succ.md)

## Proof

The function $d_k$ counts the number of ways to write a natural number as an ordered product of $k$ natural numbers. For a prime power $p^a$, the number of ways to factor it into $k$ factors corresponds to the number of non-negative integer solutions to the equation $x_1 + x_2 + ... + x_k = a$, where each $x_i$ represents the exponent of $p$ in the factorization of the corresponding factor. This is a classic combinatorial problem, and the number of solutions is given by the formula $(a + k - 1).choose (k - 1)$, which counts the ways to distribute $a$ indistinguishable items (the prime factors) into $k$ distinguishable boxes (the factors).

## Lean

Formalized as [`ArithmeticFunction.d_apply_prime_pow`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.d_apply_prime_pow).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
