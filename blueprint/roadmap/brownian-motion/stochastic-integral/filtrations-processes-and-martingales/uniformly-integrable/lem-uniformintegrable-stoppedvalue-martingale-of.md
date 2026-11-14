---
declaration: lemma
origin: cited
lean: MeasureTheory.Martingale.uniformIntegrable_stoppedValue_of_countable_range
statement: formalized
proof: formalized
---

# uniformIntegrable_stoppedValue_martingale_of_countable_range

Let $X$ be a martingale and let $(\tau_k)_{k \in \mathbb{N}}$ be a sequence of stopping times that are uniformly bounded by $n$. Then, the family of stopped values $\{X_{\tau_k}\}_{k \in \mathbb{N}}$ is uniformly integrable if for each $k$, $\tau_k$ takes value in a countable set.

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Proof depends on

- [Optional sampling (discrete time)](../optional-sampling/lem-optionalsampling-discrete.md)
- [condExpUI](lem-condexpui.md)

## Proof

Same proof as in Lemma [uniformIntegrable_stoppedValue_martingale](lem-uniformintegrable-stoppedvalue-martingale.md).

## Lean

Formalized as [`MeasureTheory.Martingale.uniformIntegrable_stoppedValue_of_countable_range`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.uniformIntegrable_stoppedValue_of_countable_range).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 772](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L772)
