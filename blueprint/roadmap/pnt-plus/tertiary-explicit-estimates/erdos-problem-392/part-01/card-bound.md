---
declaration: proposition
origin: cited
lean: Erdos392.Factorization.card_bound
statement: formalized
proof: formalized
---

# card-bound

Starting from any factorization $f$, one can find a factorization $f'$ in balance whose cardinality is at most $\log n!$ plus the score of $f$, divided by $\log n$.

## Depends on

- [score-def](score-def.md)
- [factorization-def](factorization-def.md)
- [balance-def](balance-def.md)

## Proof depends on

- [waste-eq](waste-eq.md)
- [waste-def](waste-def.md)
- [score-eq](score-eq.md)
- [score-lowest](score-lowest.md)

## Proof

Combine Lemma [score-lowest](score-lowest.md), Lemma [score-eq](score-eq.md), and Lemma [waste-eq](waste-eq.md).

## Lean

Formalized as [`Erdos392.Factorization.card_bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Factorization.card_bound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
