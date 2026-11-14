---
declaration: lemma
origin: cited
lean: MeasureTheory.Supermartingale.condExp_ae_le_stoppedValue_min_nat
statement: formalized
---

# optionalSampling_discrete_supermartingale

Let $X$ be a discrete time supermartingale with respect to the filtration $\mathcal{F}$ taking values in a real Banach space $E$. Assume $E$ is an order-closed partial order, an ordered monoid and an ordered module. Let $\tau, \sigma$ be stopping times. Then, if $\tau$ is bounded, we have that almost surely, $X_{\tau \wedge \sigma} \ge P[X_{\tau} \mid \mathcal{F}_{\sigma}]$.

## Depends on

- [Order-closed topology](def-orderclosedtopology.md)
- [Ordered Monoid](def-isorderedaddmonoid.md)
- [Ordered Module](def-isorderedmodule.md)
- [Submartingale](../basic-definitions/part-01/def-submartingale.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Proof depends on

- [optionalSampling_discrete_submartingale](lem-optionalsampling-discrete-submartingale.md)

## Proof

We know that $-X$ is a submartingale, so from Lemma [optionalSampling_discrete_submartingale](lem-optionalsampling-discrete-submartingale.md) we obtain that almost surely, $-X_{\tau \wedge \sigma} \le P[-X_{\tau} \mid \mathcal{F}_{\sigma}]$. Multiplying by $-1$ yields the desired result.

## Lean

Stated as [`MeasureTheory.Supermartingale.condExp_ae_le_stoppedValue_min_nat`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Supermartingale.condExp_ae_le_stoppedValue_min_nat); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 973](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L973)
