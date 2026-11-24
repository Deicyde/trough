---
declaration: definition
origin: cited
lean: Erdos392.Factorization.score
statement: formalized
---

# score-def

The score of a factorization (relative to a cutoff parameter $L$) is equal to its waste, plus $\log p$ for every surplus prime $p$, $\log (n/p)$ for every deficit prime above $L$, $\log L$ for every deficit prime below $L$ and an additional $\log n$ if one is not in total balance.

## Depends on

- [waste-def](waste-def.md)
- [factorization-def](factorization-def.md)
- [balance-def](balance-def.md)

## Lean

Formalized as [`Erdos392.Factorization.score`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Factorization.score).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
