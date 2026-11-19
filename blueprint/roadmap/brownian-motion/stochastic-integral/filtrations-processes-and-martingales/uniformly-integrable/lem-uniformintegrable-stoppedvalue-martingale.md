---
declaration: lemma
origin: cited
lean: MeasureTheory.Martingale.uniformIntegrable_stoppedValue
statement: formalized
proof: formalized
---

# uniformIntegrable_stoppedValue_martingale

Let $X$ be a martingale on a discrete index set and let $(\tau_k)_{k \in \mathbb{N}}$ be a sequence of stopping times that are uniformly bounded by $n$. Then, the family of stopped values $\{X_{\tau_k}\}_{k \in \mathbb{N}}$ is uniformly integrable.

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Proof depends on

- [Optional sampling (discrete time)](../optional-sampling/lem-optionalsampling-discrete.md)
- [condExpUI](lem-condexpui.md)

## Proof

By optional sampling (Lemma [Optional sampling (discrete time)](../optional-sampling/lem-optionalsampling-discrete.md)), we have that for each $k$, $X_{\tau_k} = P[X_n \mid \mathcal{F}_{\tau_k}]$. Thus, the result follows by Lemma [condExpUI](lem-condexpui.md) as $\{X_n\}$ is uniformly integrable.

## Lean

Formalized as [`MeasureTheory.Martingale.uniformIntegrable_stoppedValue`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.uniformIntegrable_stoppedValue).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 756](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L756)
