---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsLocalizingSequence.isPrelocalizingSequence_inf_extraction
---

# isPreLocalizingSequence_of_isLocalizingSequence

Let $(\tau_n)_{n \in \mathbb{N}}$ be a localizing sequence and let $(\sigma_{n,k})_{k \in \mathbb{N}}$ be a localizing sequence for each $n$. Then, there exists a strictly increasing sequence $(k_n)_{n \in \mathbb{N}}$ such that the sequence defined by $\tau'_n = \tau_n \wedge \sigma_{n,k_n}$ is a pre-localizing sequence.

## Depends on

- [preLocalizingSequence](def-prelocalizingsequence.md)
- [Localizing sequence](def-localizingsequence.md)

## Proof

For each $n$, since $\sigma_{n,k} \to \infty$ a.s. as $k \to \infty$, we may choose $k_n \in \mathbb{N}$ such that $P(\sigma_{n,k_n} < \tau_n \wedge n) \le 2^{-n}$. Then, defining $\tau'_n = \tau_n \wedge \sigma_{n,k_n}$, we have $\tau_n' \to \infty$ by the Borel-Cantelli lemma.

## Lean

Formalized as [`ProbabilityTheory.IsLocalizingSequence.isPrelocalizingSequence_inf_extraction`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsLocalizingSequence.isPrelocalizingSequence_inf_extraction).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 62](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L62)
