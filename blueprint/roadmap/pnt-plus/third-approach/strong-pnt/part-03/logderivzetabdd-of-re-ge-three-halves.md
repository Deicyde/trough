---
declaration: theorem
origin: cited
lean: LogDerivZetaBdd_of_Re_ge_three_halves
statement: formalized
proof: formalized
---

# LogDerivZetaBdd-of-Re-ge-three-halves

There exists a uniform constant $C$ such that for $z=\sigma+it$ one has

$$
3/2\leq\sigma\implies\left|\frac{\zeta'}{\zeta}(z)\right|\leq C.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [vonMangoldtLSeriesSummable](../part-02/vonmangoldtlseriessummable.md)
- [LogDerivativeDirichlet](../../../second-approach/proof-of-medium-pnt/part-01/logderivativedirichlet.md)

## Proof

Note that

$$
\left|\frac{\zeta'}{\zeta}(z)\right|=\left|\sum_{n=1}^\infty\frac{\Lambda(n)}{n^z}\right|\leq
\sum_{n=1}^\infty\frac{\Lambda(n)}{|n^z|}=\sum_{n=1}^\infty\frac{\Lambda(n)}{n^\sigma}\leq
\sum_{n=1}^\infty\frac{\Lambda(n)}{n^{3/2}}\lt \infty
$$

by [vonMangoldtLSeriesSummable](../part-02/vonmangoldtlseriessummable.md).

## Lean

Formalized as [`LogDerivZetaBdd_of_Re_ge_three_halves`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogDerivZetaBdd_of_Re_ge_three_halves).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
