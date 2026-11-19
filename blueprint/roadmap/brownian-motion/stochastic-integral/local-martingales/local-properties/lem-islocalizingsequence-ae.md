---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isLocalizingSequence_localizingSequenceOfProp
statement: formalized
proof: formalized
---

# isLocalizingSequence_ae

Let $P$ be a predicate on paths and suppose $X$ is a stochastic process satisfying $P$ a.s. Then, defining

$$
\tau_n(\omega) =
\begin{cases}
\infty & \text{if } X(\omega) \text{ satisfies } P \\
0 & \text{otherwise}
\end{cases}
$$

for all $n \in \mathbb{N}$, the sequence $(\tau_n)_{n \in \mathbb{N}}$ is a localizing sequence.

## Depends on

- [Localizing sequence](def-localizingsequence.md)

## Lean

Formalized as [`ProbabilityTheory.isLocalizingSequence_localizingSequenceOfProp`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isLocalizingSequence_localizingSequenceOfProp).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 76](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L76)
