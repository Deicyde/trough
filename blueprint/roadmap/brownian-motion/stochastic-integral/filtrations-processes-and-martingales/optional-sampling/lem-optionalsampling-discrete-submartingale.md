---
declaration: lemma
origin: cited
lean: MeasureTheory.Submartingale.stoppedValue_min_ae_le_condExp_nat
statement: formalized
---

# optionalSampling_discrete_submartingale

Let $X$ be a discrete time submartingale with respect to the filtration $\mathcal{F}$ taking values in a real Banach space $E$. Assume $E$ is an order-closed partial order, an ordered monoid and an ordered module. Let $\tau, \sigma$ be stopping times. Then, if $\tau$ is bounded, we have that almost surely, $X_{\tau \wedge \sigma} \le P[X_{\tau} \mid \mathcal{F}_{\sigma}]$.

## Depends on

- [Order-closed topology](def-orderclosedtopology.md)
- [Ordered Monoid](def-isorderedaddmonoid.md)
- [Ordered Module](def-isorderedmodule.md)
- [Submartingale](../basic-definitions/part-01/def-submartingale.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Proof depends on

- [martingale_martingalePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-martingale-martingalepart.md)
- [predictable_predictablePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-predictable-predictablepart.md)
- [Optional sampling (discrete time)](lem-optionalsampling-discrete.md)
- [Submartingale.monotone_predictablePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-submartingale-monotone-predictablepart.md)

## Proof

Use Doob decomposition to write $X_n = M_n + A_n$, where $M$ (Definition [Martingale part](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/def-martingalepart.md)) is a martingale (Lemma [martingale_martingalePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-martingale-martingalepart.md)) and $A$ (Definition [Predictable part](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/def-predictablepart.md)) is a predictable process (Lemma [predictable_predictablePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-predictable-predictablepart.md)). By Lemma [Optional sampling (discrete time)](lem-optionalsampling-discrete.md), we have that almost surely, $M_{\tau \wedge \sigma} = P[M_{\tau} \mid \mathcal{F}_{\sigma}]$. Because $A$ is predictable and $\tau \wedge \sigma \le \sigma$, we deduce that almost surely, $A_{\tau \wedge \sigma} = P[A_{\tau \wedge \sigma} \mid \mathcal{F}_\sigma]$. Moreover, by Lemma [Submartingale.monotone_predictablePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-submartingale-monotone-predictablepart.md), we know that almost surely, $A$ is nondecreasing. Therefore, using the fact $\tau \wedge \sigma \le \tau$, we get that $P[A_{\tau \wedge \sigma} \mid \mathcal{F}_\sigma] \le P[A_\tau \mid \mathcal{F}_\sigma]$. We deduce that almost surely,

$$
X_{\tau \wedge \sigma} = M_{\tau \wedge \sigma} + A_{\tau \wedge \sigma} \le P[M_\tau \mid \mathcal{F}_\sigma] + P[A_\tau \mid \mathcal{F}_\sigma] = P[X_\tau \mid \mathcal{F}_\sigma],
$$

concluding the proof.

## Lean

Stated as [`MeasureTheory.Submartingale.stoppedValue_min_ae_le_condExp_nat`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.stoppedValue_min_ae_le_condExp_nat); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 959](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L959)
