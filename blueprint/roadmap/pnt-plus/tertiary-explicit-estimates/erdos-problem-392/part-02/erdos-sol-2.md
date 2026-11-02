---
declaration: theorem
origin: cited
lean: Erdos392.Solution_2
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/649
---

# erdos-sol-2

One can factorize $n!$ into at most $n/2 - n / 2\log n + o(n / \log n)$ numbers of size at most $n^2$.-

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [factorization-def](../part-01/factorization-def.md)
- [balance-def](../part-01/balance-def.md)
- [erdos-sol-1](erdos-sol-1.md)
- [balance-zero](../part-01/balance-zero.md)

## Proof

Group the factorization arising in Theorem [erdos-sol-1](erdos-sol-1.md) into pairs, using Lemma [balance-zero](../part-01/balance-zero.md).

## Lean

Formalized as [`Erdos392.Solution_2`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Solution_2).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
