---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isGaussianProcess_brownian
statement: formalized
proof: formalized
---

# isGaussianProcess_brownian

The Brownian motion is a Gaussian process.

## Depends on

- [Brownian motion](def-brownian.md)
- [Gaussian processes](../../../../mathlib/overview/probability-theory/stochastic-processes/gaussian-processes.md)

## Proof depends on

- [isGaussianProcess_of_modification](../../gaussian-distributions/gaussian-processes/lem-isgaussianprocess-of-modification.md)
- [isGaussianProcess_preBrownian](lem-isgaussianprocess-prebrownian.md)

## Proof

The pre-Brownian process is a Gaussian process by Lemma [isGaussianProcess_preBrownian](lem-isgaussianprocess-prebrownian.md). The Brownian motion is a modification of the pre-Brownian process by Definition [Brownian motion](def-brownian.md). Thus, the Brownian motion is a Gaussian process as well by Lemma [isGaussianProcess_of_modification](../../gaussian-distributions/gaussian-processes/lem-isgaussianprocess-of-modification.md).

## Lean

Formalized as [`ProbabilityTheory.isGaussianProcess_brownian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isGaussianProcess_brownian).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 86](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L86)
