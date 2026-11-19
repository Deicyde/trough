---
declaration: definition
origin: cited
lean: ProbabilityTheory.ClassDL
statement: formalized
---

# Class DL

A stochastic process $(X_t)$ is of class DL if it is progressively measurable and for all $t \ge 0$, the set $\{X_\tau \mid \tau \text{ is a stopping time with } \tau \le t\}$ is uniformly integrable.

## Depends on

- [Stopping time](../../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Lean

Formalized as [`ProbabilityTheory.ClassDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.ClassDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 438](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L438)
