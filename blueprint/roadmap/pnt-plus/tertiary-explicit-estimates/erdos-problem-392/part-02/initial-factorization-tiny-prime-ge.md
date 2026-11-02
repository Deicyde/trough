---
declaration: lemma
origin: cited
lean: Erdos392.Params.initial.balance_tiny_prime_ge
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/515
---

# initial-factorization-tiny-prime-ge

A tiny prime $p \leq L$ can be in deficit by at most $M\log n + ML\pi(n)$.

## Depends on

- [params-set](../part-01/params-set.md)
- [initial-factorization-def](../part-01/initial-factorization-def.md)
- [balance-def](../part-01/balance-def.md)

## Proof depends on

- [factorization-def](../part-01/factorization-def.md)

## Proof

In addition to the Legendre calculations, one potentially removes factors of the form $plq$ with $l \leq L$ and $q \leq n$ a prime up to $M$ times each, with at most $L$ copies of $p$ removed at each factor.

## Lean

Formalized as [`Erdos392.Params.initial.balance_tiny_prime_ge`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.balance_tiny_prime_ge).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
