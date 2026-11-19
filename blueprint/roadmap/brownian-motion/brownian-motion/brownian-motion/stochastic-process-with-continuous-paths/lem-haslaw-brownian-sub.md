---
declaration: lemma
origin: cited
lean: ProbabilityTheory.hasLaw_brownian_sub
statement: formalized
proof: formalized
---

# hasLaw_brownian_sub

For $s, t \in \mathbb{R}_+$, the law of $B_t - B_s$ is the real Gaussian measure $\mathcal{N}(0,\vert t - s \vert)$.

## Depends on

- [Brownian motion](def-brownian.md)

## Proof depends on

- [hasLaw_preBrownian_sub](lem-haslaw-prebrownian-sub.md)

## Proof

The Brownian motion $B$ is a modification of the pre-Brownian process, and therefore has same finite dimensional distributions. By Lemma [hasLaw_preBrownian_sub](lem-haslaw-prebrownian-sub.md), $B_t - B_s$ has law $\mathcal{N}(0,\vert t - s \vert)$.

## Lean

Formalized as [`ProbabilityTheory.hasLaw_brownian_sub`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.hasLaw_brownian_sub).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 142](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L142)
