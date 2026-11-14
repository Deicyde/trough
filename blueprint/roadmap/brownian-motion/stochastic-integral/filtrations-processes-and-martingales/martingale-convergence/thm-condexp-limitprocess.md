---
declaration: theorem
origin: cited
lean: MeasureTheory.Martingale.condExp_limitProcess_ae_eq
statement: formalized
---

# condExp_limitProcess

If $X$ is a càdlàg and uniformly integrable martingale, then for any $t$, almost surely,

$$
P[X_\infty | \mathcal{F}_t] = X_t.
$$

## Depends on

- [limitProcess](def-limitprocess.md)
- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)

## Lean

Stated as [`MeasureTheory.Martingale.condExp_limitProcess_ae_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.condExp_limitProcess_ae_eq); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1223](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1223)
