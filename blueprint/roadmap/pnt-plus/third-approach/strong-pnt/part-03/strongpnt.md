---
declaration: theorem
origin: cited
lean: StrongPNT
statement: formalized
proof: formalized
---

# StrongPNT

We have

$$
\sum_{n \leq x}\Lambda(n)=x+O(x \exp(-c(\log x)^{1/2})).
$$

## Depends on

- [ChebyshevPsi](../../../second-approach/proof-of-medium-pnt/part-01/chebyshevpsi.md)

## Proof depends on

- [LogDerivZetaUniformLogSquaredBound](logderivzetauniformlogsquaredbound.md)
- [LogDerivZetaUniformLogSquaredBoundStrip](logderivzetauniformlogsquaredboundstrip.md)
- [ZeroInequality](../part-02/zeroinequality.md)
- [LogDerivZetaHasBound](../../../second-approach/proof-of-medium-pnt/part-01/logderivzetahasbound.md)
- [ZetaNoZerosInBox](../../../second-approach/zeta-bounds/part-02/zetanozerosinbox.md)
- [GenStrengthPNT](../../../second-approach/mediumpnt/genstrengthpnt.md)

## Proof

This follows as a corollary of Theorems [GenStrengthPNT](../../../second-approach/mediumpnt/genstrengthpnt.md) and [LogDerivZetaUniformLogSquaredBound](logderivzetauniformlogsquaredbound.md).

## Lean

Formalized as [`StrongPNT`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/StrongPNT).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
