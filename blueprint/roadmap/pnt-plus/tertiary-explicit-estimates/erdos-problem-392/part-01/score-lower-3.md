---
declaration: lemma
origin: cited
lean: Erdos392.Factorization.lower_score_3
statement: formalized
proof: formalized
---

# score-lower-3

If there is a prime $p$ in deficit less than $L$, one can remove it without increasing the score.

## Depends on

- [score-def](score-def.md)
- [factorization-def](factorization-def.md)
- [balance-def](balance-def.md)

## Proof depends on

- [waste-def](waste-def.md)
- [score-eq](score-eq.md)
- [score-lower-2](score-lower-2.md)
- [score-lower-1](score-lower-1.md)

## Proof

Without loss of generality we may assume that one is not in the previous two situations, i.e., wlog there are no surplus primes and all primes in deficit are at most $L$. If all deficit primes multiply to $n$ or less, add that product to the factorization (this increases the waste by at most $\log n$, but we save a $\log n$ from now being in balance). Otherwise, greedily multiply all primes together while staying below $n$ until one cannot do so any further; add this product to the factorization, increasing the waste by at most $\log L$.

## Lean

Formalized as [`Erdos392.Factorization.lower_score_3`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Factorization.lower_score_3).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
