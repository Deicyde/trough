---
declaration: theorem
origin: cited
lean: MediumPNT
statement: formalized
proof: formalized
---

# MediumPNT

We have

$$
\sum_{n \leq x}\Lambda(n)=x+O(x \exp(-c(\log x)^{1/10})).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [LogDerivZetaHolcLargeT9](../zeta-bounds/part-02/logderivzetaholclarget9.md)
- [LogDerivZetaBndUnif99](../zeta-bounds/part-03/logderivzetabndunif99.md)
- [LogDerivZetaHasBound](../proof-of-medium-pnt/part-01/logderivzetahasbound.md)
- [GenStrengthPNT](genstrengthpnt.md)

## Proof

This follows as a corollary of Theorems [GenStrengthPNT](genstrengthpnt.md) and [LogDerivZetaBnd](../zeta-bounds/part-02/logderivzetabnd.md).

## Lean

Formalized as [`MediumPNT`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MediumPNT).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/MediumPNT.lean)
