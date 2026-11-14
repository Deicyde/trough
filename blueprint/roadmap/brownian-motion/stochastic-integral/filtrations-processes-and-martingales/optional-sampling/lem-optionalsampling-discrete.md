---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Martingale.stoppedValue_min_ae_eq_condExp
---

# Optional sampling (discrete time)

Let $X$ be a discrete time martingale with respect to the filtration $\mathcal{F}$ and let $\tau, \sigma$ be stopping times. Then, if $\tau$ is bounded, we have that almost surely, $X_{\tau \wedge \sigma} = P[X_{\tau} \mid \mathcal{F}_{\sigma}]$.

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Lean

Formalized as [`MeasureTheory.Martingale.stoppedValue_min_ae_eq_condExp`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.stoppedValue_min_ae_eq_condExp).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 946](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L946)
