---
declaration: definition
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable
statement: formalized
---

# Square integrable martingales

Let $T$ be a linear order with bottom element 0, on which we have a filtration $\mathcal{F}$ satisfying the usual conditions. We say that a martingale $M : T \to \Omega \to E$ is square integrable if it is càdlàg and $\sup_{t \in T} \Vert M_t \Vert_{L^2} < \infty$ (Lean remark: use `eLpNorm (M t) 2`).

## Depends on

- [Martingale](../../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)

## Lean

Formalized as [`ProbabilityTheory.IsSquareIntegrable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 184](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L184)
