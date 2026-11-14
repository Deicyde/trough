---
declaration: lemma
origin: cited
lean: ProbabilityTheory.hasIndepIncrements_brownian
statement: formalized
proof: formalized
---

# hasIndepIncrements_brownian

The Brownian motion has independent increments.

## Depends on

- [Brownian motion](def-brownian.md)
- [HasIndepIncrements](def-hasindepincrements.md)

## Proof

Let $t_1 \le t_2 \le \ldots \le t_n$ be $n$ times in $\mathbb{R}_+$. Then $(B_{t_2} - B_{t_1}, B_{t_3} - B_{t_2}, \ldots, B_{t_n} - B_{t_{n-1}})$ is a linear transformation of $(B_{t_1}, \ldots, B_{t_n})$, hence it is Gaussian. We can compute its mean (which is $0$) and its covariance matrix. The covariance matrix is diagonal, which means the the random variables are uncorrelated. Because they are jointly Gaussian, this implies that they are independent.

## Lean

Formalized as [`ProbabilityTheory.hasIndepIncrements_brownian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.hasIndepIncrements_brownian).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 162](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L162)
