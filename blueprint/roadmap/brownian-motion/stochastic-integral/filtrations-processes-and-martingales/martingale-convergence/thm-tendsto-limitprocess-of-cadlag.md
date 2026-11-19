---
declaration: theorem
origin: cited
lean: MeasureTheory.Martingale.ae_tendsto_limitProcess
statement: formalized
---

# tendsto_limitProcess_of_cadlag

Let $X$ be an uniformly integrable cadlag martingale with respect to the filtration $\mathcal{F}$. Then there exists a limit process $X_\infty$ measurable with respect to $\mathcal{F}_\infty$ such that $X_t$ converges to $X_\infty$ almost surely as $t$ goes to infinity. Furthermore, $X_t = P[X_\infty \mid \mathcal{F}_t]$ almost surely.

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [limitProcess](def-limitprocess.md)
- [Cadlag function](../basic-definitions/part-01/def-iscadlag.md)

## Lean

Stated as [`MeasureTheory.Martingale.ae_tendsto_limitProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.ae_tendsto_limitProcess); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1152](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1152)
