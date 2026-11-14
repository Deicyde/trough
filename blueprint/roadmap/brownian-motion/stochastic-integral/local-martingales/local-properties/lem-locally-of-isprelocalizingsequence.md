---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsStable.locally_of_isPreLocalizingSequence
---

# locally_of_isPreLocalizingSequence

Let $P$ be a stable class of processes and let $(\tau_n)_{n \in \mathbb{N}}$ be a pre-localizing sequence such that for all $n \in \mathbb{N}$, $X^{\tau_n}\mathbb{I}_{\tau_n > 0}$ is in $P$. If the filtration is right-continuous, then $X$ is locally in $P$.

## Depends on

- [Local property](def-locally.md)
- [Localizing sequence](def-localizingsequence.md)
- [stable](def-stable.md)
- [preLocalizingSequence](def-prelocalizingsequence.md)

## Proof depends on

- [isLocalizingSequence_of_isPreLocalizingSequence](lem-islocalizingsequence-of-isprelocalizingseque.md)

## Proof

Using the localizing sequence defined by Lemma [isLocalizingSequence_of_isPreLocalizingSequence](lem-islocalizingsequence-of-isprelocalizingseque.md) suffices.

## Lean

Formalized as [`ProbabilityTheory.IsStable.locally_of_isPreLocalizingSequence`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsStable.locally_of_isPreLocalizingSequence).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 169](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L169)
