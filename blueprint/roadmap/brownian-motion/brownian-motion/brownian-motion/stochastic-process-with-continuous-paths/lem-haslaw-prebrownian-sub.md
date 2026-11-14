---
declaration: lemma
origin: cited
lean: ProbabilityTheory.hasLaw_preBrownian_sub
statement: formalized
proof: formalized
---

# hasLaw_preBrownian_sub

Let $X$ be the pre-Brownian process of Definition [pre-Brownian process](def-prebrownian.md). Then, for all $s, t \in \mathbb{R}_+$, the random variable $X_t - X_s$ is a Gaussian random variable with mean $0$ and variance $|t - s|$.

## Depends on

- [pre-Brownian process](def-prebrownian.md)

## Proof depends on

- [isGaussianProcess_preBrownian](lem-isgaussianprocess-prebrownian.md)
- [isGaussian_map](../../gaussian-distributions/gaussian-measures/part-01/lem-isgaussian-map.md)

## Proof

The map

$$
\begin{aligned}
L : \mathbb{R}^2 &\to \mathbb{R} \\
(x_1, x_2) &\mapsto x_2 - x_1
\end{aligned}
$$

is a continuous linear map, and $(X_s, X_t)$ is Gaussian by Lemma [isGaussianProcess_preBrownian](lem-isgaussianprocess-prebrownian.md), therefore $X_t - X_s$ is Gaussian by Lemma [isGaussian_map](../../gaussian-distributions/gaussian-measures/part-01/lem-isgaussian-map.md). By definition of $P_B$, we have

$$
\mathbb{E}[X_t - X_s] = \mathbb{E}[X_t] - \mathbb{E}[X_s] = 0 - 0 = 0,
$$

and

$$
\mathrm{Var}(X_t - X_s) = \mathrm{Var}(X_t) - 2\mathrm{Cov}(X_t, X_s) + \mathrm{Var}(X_s) = t - 2(t \land s) + s = t \lor s - t \land s = |t - s|.
$$

Therefore $X_t - X_s$ is Gaussian with mean $0$ and variance $|t - s|$.

## Lean

Formalized as [`ProbabilityTheory.hasLaw_preBrownian_sub`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.hasLaw_preBrownian_sub).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 30](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L30)
