---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Locally, ProbabilityTheory.Locally.localSeq
---

# Local property

Let $P$ be a class of stochastic processes (or equivalently a predicate on stochastic processes). We say that a stochastic process $X : T \to \Omega \to E$ is locally in $P$ (or satisfies $P$ locally) if there exists a localizing sequence $(\tau_n)_{n \in \mathbb{N}}$ such that for all $n \in \mathbb{N}$, the process $X^{\tau_n}\mathbb{I}_{\tau_n > 0}$ is in $P$ (in which $X^{\tau_n}$ denotes the stopped process). We denote the class of processes that are locally in $P$ by $P_{\mathrm{loc}}$.

## Depends on

- [Localizing sequence](def-localizingsequence.md)
- [Stopped process](../../filtrations-processes-and-martingales/basic-definitions/part-02/def-stoppedprocess.md)

## Lean

Formalized as [`ProbabilityTheory.Locally`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.Locally), [`ProbabilityTheory.Locally.localSeq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.Locally.localSeq).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 94](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L94)
