---
declaration: lemma
origin: cited
lean: Erdos392.Factorization.lower_score_1
statement: formalized
proof: formalized
---

# score-lower-1

If there is a prime $p$ in surplus, one can remove it without increasing the score.

## Depends on

- [score-def](score-def.md)
- [factorization-def](factorization-def.md)
- [balance-def](balance-def.md)

## Proof depends on

- [waste-def](waste-def.md)

## Proof

Locate a factor $a_i$ that contains the surplus prime $p$, then replace $a_i$ with $a_i/p$.

## Lean

Formalized as [`Erdos392.Factorization.lower_score_1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Factorization.lower_score_1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
