---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isGaussianProcess_preBrownian
statement: formalized
proof: formalized
---

# isGaussianProcess_preBrownian

The pre-Brownian process $X$ of Definition [pre-Brownian process](def-prebrownian.md) is a Gaussian process.

## Depends on

- [pre-Brownian process](def-prebrownian.md)
- [Gaussian processes](../../../../mathlib/overview/probability-theory/stochastic-processes/gaussian-processes.md)

## Proof depends on

- [isGaussian_multivariateGaussian](../../gaussian-distributions/gaussian-measures/part-02/lem-isgaussian-multivariategaussian.md)

## Proof

For any $t_1, \ldots, t_n \in \mathbb{R}_+$, the distribution of $(X_{t_1}, \ldots, X_{t_n})$ is given by a finite-dimensional distribution of $P_B$, and therefore is Gaussian.

## Lean

Formalized as [`ProbabilityTheory.isGaussianProcess_preBrownian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isGaussianProcess_preBrownian).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 17](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L17)
