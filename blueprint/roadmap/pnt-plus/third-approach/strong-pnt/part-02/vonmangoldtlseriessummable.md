---
declaration: theorem
origin: cited
lean: vonMangoldtLSeriesSummable
statement: formalized
proof: formalized
---

# vonMangoldtLSeriesSummable

The series

$$
\sum_{n=1}^\infty\frac{\Lambda(n)}{n^s}
$$

converges when $1\lt \mathfrak{R}(s)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We know that $\Lambda(n)$ is $O(n^\varepsilon)$ since it is bounded above by $\log(n)$. Thus,

$$
\left|\sum_{n=1}^\infty\frac{\Lambda(n)}{n^s}\right|\leq
\sum_{n=1}^\infty\left|\frac{\Lambda(n)}{n^s}\right|\ll
\sum_{n=1}^\infty\frac{1}{n^{\mathfrak{R}(s)-\varepsilon}}.
$$

Since $\varepsilon$ can be arbitrarily small, we know the left hand side converges by the $p$-test.

## Lean

Formalized as [`vonMangoldtLSeriesSummable`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/vonMangoldtLSeriesSummable).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
