---
declaration: lemma
origin: cited
lean: Erdos392.Params.initial.balance_small_prime_le
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/513
---

# initial-factorization-small-prime-le

A small prime $p \leq \sqrt{n}$ can be in surplus by at most $M\log n$.

## Depends on

- [params-set](../part-01/params-set.md)
- [initial-factorization-def](../part-01/initial-factorization-def.md)
- [balance-def](../part-01/balance-def.md)

## Proof depends on

- [factorization-def](../part-01/factorization-def.md)

## Proof

Routine computation using Legendre's formula, noting that at most $\log n / \log 2$ powers of $p$ divide any given number up to $n$.

## Lean

Formalized as [`Erdos392.Params.initial.balance_small_prime_le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.balance_small_prime_le).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
