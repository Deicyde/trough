---
declaration: theorem
origin: cited
lean: LogDerivZetaUniformLogSquaredBound
statement: formalized
proof: formalized
---

# LogDerivZetaUniformLogSquaredBound

There exists a constant $F\in(0,1/42)$ such that for all $t\in\mathbb{R}$ with $|t|\geq 3$ one has

$$
1-\frac{F}{\log|t|}\leq\sigma\implies\left|\frac{\zeta'}{\zeta}(\sigma+it)\right|\ll\log^2|t|
$$

where the implied constant is uniform in $\sigma$.

## Depends on

- [LogDerivZetaUniformLogSquaredBoundStrip](logderivzetauniformlogsquaredboundstrip.md)
- [ZeroInequality](../part-02/zeroinequality.md)

## Proof depends on

- [LogDerivZetaBdd-of-Re-ge-three-halves](logderivzetabdd-of-re-ge-three-halves.md)

## Proof

Put the previous two Lemmas together.

## Lean

Formalized as [`LogDerivZetaUniformLogSquaredBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogDerivZetaUniformLogSquaredBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
