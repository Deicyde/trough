---
declaration: lemma
origin: cited
lean: Erdos392.Factorization.lowest_score
statement: formalized
proof: formalized
---

# score-lowest

One can bring any factorization into balance without increasing the score.

## Depends on

- [score-def](score-def.md)
- [factorization-def](factorization-def.md)
- [balance-def](balance-def.md)

## Proof depends on

- [score-lower-2](score-lower-2.md)
- [score-lower-3](score-lower-3.md)
- [score-lower-1](score-lower-1.md)

## Proof

Apply strong induction on the total imbalance of the factorization and use the previous three sublemmas.

## Lean

Formalized as [`Erdos392.Factorization.lowest_score`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Factorization.lowest_score).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
