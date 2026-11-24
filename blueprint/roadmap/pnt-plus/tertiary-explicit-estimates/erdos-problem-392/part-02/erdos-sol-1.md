---
declaration: theorem
origin: cited
lean: Erdos392.Solution_1
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/648
---

# erdos-sol-1

One can find a balanced factorization of $n!$ with cardinality at most $n - n / \log n + o(n / \log n)$.-

## Depends on

- [factorization-def](../part-01/factorization-def.md)
- [balance-def](../part-01/balance-def.md)

## Proof depends on

- [card-bound](../part-01/card-bound.md)
- [params-set](../part-01/params-set.md)
- [score-def](../part-01/score-def.md)
- [initial-score](initial-score.md)
- [initial-factorization-def](../part-01/initial-factorization-def.md)

## Proof

Combine Proposition [initial-score](initial-score.md) with Proposition [card-bound](../part-01/card-bound.md) and the Stirling approximation.

## Lean

Formalized as [`Erdos392.Solution_1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Solution_1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
