---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsStable.locally_locally_iff
---

# locally_locally

Suppose that the filtration is right-continuous. For any stable class of processes $P$, we have $(P_{\mathrm{loc}})_{\mathrm{loc}} = P_{\mathrm{loc}}$.

## Depends on

- [Local property](def-locally.md)
- [stable](def-stable.md)

## Proof depends on

- [locally_of_isPreLocalizingSequence](lem-locally-of-isprelocalizingsequence.md)
- [isStable_locally](lem-isstable-locally.md)
- [isPreLocalizingSequence_of_isLocalizingSequence](lem-isprelocalizingsequence-of-islocalizingseque.md)

## Proof

$(P_{\mathrm{loc}})_{\mathrm{loc}} \supseteq P_{\mathrm{loc}}$ by Lemma [isStable_locally](lem-isstable-locally.md) so we only prove the reverse inclusion.

Let $X$ be a process in $(P_{\mathrm{loc}})_{\mathrm{loc}}$. By definition there exists a localizing sequence $(\tau_n)_{n \in \mathbb{N}}$ such that for all $n \in \mathbb{N}$, $X^{\tau_n}\mathbb{I}_{\tau_n > 0}$ is in $P_{\mathrm{loc}}$. By definition of $P_{\mathrm{loc}}$, for each $n$ there exists a localizing sequence $(\sigma_{n,k})_{k \in \mathbb{N}}$ such that for all $k \in \mathbb{N}$, $(X^{\tau_n}\mathbb{I}_{\tau_n > 0})^{\sigma_{n,k}}\mathbb{I}_{\sigma_{n,k} > 0}$ is in $P$.

By Lemma [locally_of_isPreLocalizingSequence](lem-locally-of-isprelocalizingsequence.md), it suffices to show that there exists a pre-localizing sequence $(\tau'_n)_{n \in \mathbb{N}}$ such that for all $n \in \mathbb{N}$, $X^{\tau'_n}\mathbb{I}_{\tau'_n > 0}$ is in $P$. Thus, using the localizing sequences $\tau'_n = \tau_n \wedge \sigma_{n, k_n}$ defined by Lemma [isPreLocalizingSequence_of_isLocalizingSequence](lem-isprelocalizingsequence-of-islocalizingseque.md), it remains to argue that by stability of $P$, $X^{\tau'_n}\mathbb{I}_{\tau'_n > 0}$ is in $P$ for all $n$. Indeed, this follows as $X^{\tau'_n}\mathbb{I}_{\tau'_n > 0} = ((X^{\tau_n}\mathbb{I}_{\tau_n > 0})^{\sigma_{n,k_n}}\mathbb{I}_{\sigma_{n,k_n} > 0})^{\tau'_n}\mathbb{I}_{\tau'_n > 0}$ where $(X^{\tau_n}\mathbb{I}_{\tau_n > 0})^{\sigma_{n,k_n}}\mathbb{I}_{\sigma_{n,k_n} > 0}$ is in $P$ by construction and $P$ is stable.

## Lean

Formalized as [`ProbabilityTheory.IsStable.locally_locally_iff`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsStable.locally_locally_iff).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 183](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L183)
