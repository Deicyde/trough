---
declaration: lemma
origin: cited
lean: MeasureTheory.Submartingale.uniformIntegrable_stoppedValue
statement: formalized
---

# uniformIntegrable_stoppedValue_submartingale

Let $X$ be a submartingale on a discrete index set and let $(\tau_k)_{k \in \mathbb{N}}$ be a sequence of stopping times that are uniformly bounded by $p$. Then, the family of stopped values $\{X_{\tau_k}\}_{k \in \mathbb{N}}$ is uniformly integrable.

## Depends on

- [Submartingale](../basic-definitions/part-01/def-submartingale.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Proof depends on

- [Martingale part](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/def-martingalepart.md)
- [martingale_martingalePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-martingale-martingalepart.md)
- [Predictable part](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/def-predictablepart.md)
- [predictable_predictablePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-predictable-predictablepart.md)
- [uniformIntegrable_stoppedValue_martingale](lem-uniformintegrable-stoppedvalue-martingale.md)
- [uniformIntegrableAdd](lem-uniformintegrableadd.md)
- [uniformIntegrableDominatedSingleton](lem-uniformintegrabledominatedsingleton.md)
- [predictablePart_zero](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-predictablepart-zero.md)
- [Submartingale.monotone_predictablePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-submartingale-monotone-predictablepart.md)

## Proof

Use Doob decomposition to write $X_n = M_n + A_n$, where $M$ (Definition [Martingale part](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/def-martingalepart.md)) is a martingale (Lemma [martingale_martingalePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-martingale-martingalepart.md)) and $A$ (Definition [Predictable part](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/def-predictablepart.md)) is a predictable process (Lemma [predictable_predictablePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-predictable-predictablepart.md)). We know from Lemma [uniformIntegrable_stoppedValue_martingale](lem-uniformintegrable-stoppedvalue-martingale.md) that $(M_{\tau_k})_{k \in \mathbb{N}}$ is uniformly integrable. Combining Lemma [uniformIntegrableAdd](lem-uniformintegrableadd.md) and Lemma [uniformIntegrableDominatedSingleton](lem-uniformintegrabledominatedsingleton.md), it suffices to show that $(A_{\tau_k})_{k \in \mathbb{N}}$ is dominated. It is dominated by $A_p$ thanks to Lemma [predictablePart_zero](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-predictablepart-zero.md) and Lemma [Submartingale.monotone_predictablePart](../../doob-meyer-theorem/doob-decomposition-in-discrete-time/lem-submartingale-monotone-predictablepart.md).

## Lean

Stated as [`MeasureTheory.Submartingale.uniformIntegrable_stoppedValue`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.uniformIntegrable_stoppedValue); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 856](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L856)
