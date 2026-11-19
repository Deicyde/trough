---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isLocalizingSequence_leastGE
statement: formalized
---

# isLocalizingSequence_leastGE

Assume $T$ has a bottom element and that its closed intervals are compact, and that the filtration is right-continuous. If $X$ is a real-valued càdlàg and adapted process, then the sequence $\tau_n := \inf \{t | X_t \ge n\}$ is a localizing sequence.

## Depends on

- [leastGE](../../../debut-theorem/hitting-times/def-leastge.md)
- [Localizing sequence](../../local-properties/def-localizingsequence.md)
- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Right-continuous filtration](../../../filtrations-processes-and-martingales/right-continuous-filtrations/def-rightcontinuous.md)

## Proof depends on

- [isBounded_image_of_isCadlag_of_isCompact](lem-isbounded-image-of-iscadlag-of-iscompact.md)

## Proof

By Corollary [isStoppingTime_leastGE_of_rightContinuous](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L779), each $\tau_n$ is a stopping time. Moreover, for all $n \in \mathbb{N}$, $X_t \ge n+1 \implies X_t \ge n$, thus $\tau_n \le \tau_{n+1}$. Finally, for every $\omega \in \Omega$ and $t_0 \in T$ there exists $N \in \mathbb{N}$ such that for all $s \le t_0$, $X_s \le N$ thanks to Lemma [isBounded_image_of_isCadlag_of_isCompact](lem-isbounded-image-of-iscadlag-of-iscompact.md). Thus for all $n \ge N$, $\tau_n(\omega) \ge t_0$, proving that $\tau_n$ tends to infinity as n goes to infinity.

## Lean

Stated as [`ProbabilityTheory.isLocalizingSequence_leastGE`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isLocalizingSequence_leastGE); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 729](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L729)
