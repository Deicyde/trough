---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsLocalizingSequence
---

# Localizing sequence

A localizing sequence is a sequence of stopping times $(\tau_n)_{n \in \mathbb{N}}$ such that $\tau_n$ is non-decreasing and $\tau_n \to \infty$ as $n \to \infty$ (a.s.). That is, it is a pre-localizing sequence that is also almost surely non-decreasing.

## Depends on

- [preLocalizingSequence](def-prelocalizingsequence.md)

## Lean

Formalized as [`ProbabilityTheory.IsLocalizingSequence`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsLocalizingSequence).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 16](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L16)
