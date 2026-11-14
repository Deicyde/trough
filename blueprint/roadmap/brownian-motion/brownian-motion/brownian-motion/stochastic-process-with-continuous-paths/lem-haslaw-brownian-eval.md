---
declaration: lemma
origin: cited
lean: ProbabilityTheory.hasLaw_brownian_eval
statement: formalized
proof: formalized
---

# hasLaw_brownian_eval

For $t \in \mathbb{R}_+$, the law of $B_t$ (the Brownian motion at time $t$) is the real Gaussian measure $\mathcal{N}(0,t)$.

## Depends on

- [Brownian motion](def-brownian.md)

## Proof depends on

- [gaussianLimit](../../projective-family-of-the-brownian-motion/projective-family-of-gaussian-measures/def-gaussianlimit.md)

## Proof

The Brownian motion $B$ is a modification of the pre-Brownian process, and therefore has same finite dimensional distributions. By Definition [gaussianLimit](../../projective-family-of-the-brownian-motion/projective-family-of-gaussian-measures/def-gaussianlimit.md), $B_t$ has law $\mathcal{N}(0,t)$.

## Lean

Formalized as [`ProbabilityTheory.hasLaw_brownian_eval`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.hasLaw_brownian_eval).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 129](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L129)
