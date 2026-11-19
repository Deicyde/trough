---
declaration: definition
origin: cited
lean: ProbabilityTheory.IsLocalMartingale
statement: formalized
---

# Local martingale

We say a stochastic process $(M_t)_{t \in T}$ is a local martingale if it is locally a cadlag martingale in the sense of Definition [Local property](../local-properties/def-locally.md). That is, there exists a localizing sequence $(\tau_n)_{n \in \mathbb{N}}$ such that for all $n \in \mathbb{N}$, the process $M^{\tau_n}\mathbb{I}_{\tau_n > 0}$ is a cadlag martingale.

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Local property](../local-properties/def-locally.md)
- [Cadlag function](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Stopped process](../../filtrations-processes-and-martingales/basic-definitions/part-02/def-stoppedprocess.md)
- [Localizing sequence](../local-properties/def-localizingsequence.md)

## Lean

Formalized as [`ProbabilityTheory.IsLocalMartingale`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsLocalMartingale).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 337](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L337)
