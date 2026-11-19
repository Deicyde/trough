---
declaration: lemma
origin: cited
lean: MeasureTheory.Martingale.stoppedValue_min_ae_eq_condExp'
statement: formalized
proof: formalized
---

# Optional sampling (continuous time)

Let $X$ be a right-continuous $\mathcal{F}$-martingale on an approximable time index. Then, for any stopping times $\sigma, \tau$ with $\tau$ bounded, we have that $X_{\sigma \wedge \tau} = P[X_{\tau} \mid \mathcal{F}_{\sigma}]$ almost surely.

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)
- [Right continuous function](../basic-definitions/part-01/def-rightcontinuous.md)
- [Approximable time index](def-approximabletimeindex.md)

## Proof depends on

- [StoppingTimeGenMono](../basic-definitions/part-01/lem-stoppingtimegenmono.md)
- [uniformIntegrable_stoppedValue_martingale](../uniformly-integrable/lem-uniformintegrable-stoppedvalue-martingale.md)
- [tendsto_eLpNorm_stoppedValue_discreteApproxSequence](lem-tendsto-elpnorm-stoppedvalue-discreteapproxs.md)

## Proof

Fixing $A \in \mathcal{F}_{\sigma}$, we need to show that $P[X_{\tau} \mathbb{I}_A] = P[X_{\sigma \wedge \tau} \mathbb{I}_A]$.

Let $(\tau_n), (\sigma_n)$ be discrete approximation sequences of $\tau$ and $\sigma$ respectively. As $\tau_n, \sigma_n$ take values in a countable set, we have by the discrete time optional sampling theorem (Lemma [Optional sampling (discrete time)](lem-optionalsampling-discrete.md)) that

$$
X_{\sigma_n \wedge \tau_n} = P[X_{\tau_n} \mid \mathcal{F}_{\sigma_n}]
$$

and so, as $\mathcal{F}_{\sigma} \subseteq \mathcal{F}_{\sigma_n}$ by Lemma [StoppingTimeGenMono](../basic-definitions/part-01/lem-stoppingtimegenmono.md), we have that $P[X_{\sigma_n \wedge \tau_n} \mathbb{I}_A] = P[X_{\tau_n} \mathbb{I}_A]$. On the other hand, by Lemma [uniformIntegrable_stoppedValue_martingale](../uniformly-integrable/lem-uniformintegrable-stoppedvalue-martingale.md), the families $\{X_{\tau_n}\}$ and $\{X_{\sigma_n \wedge \tau_n}\}$ are uniformly integrable. Thus, as $X$ is right-continuous, $(X_{\sigma_n \wedge \tau_n}, X_{\tau_n}) \to (X_{\sigma \wedge \tau}, X_{\tau})$ a.s. We have $P[X_{\tau} \mathbb{I}_A] = P[X_{\sigma \wedge \tau} \mathbb{I}_A]$ by Lemma [tendsto_eLpNorm_stoppedValue_discreteApproxSequence](lem-tendsto-elpnorm-stoppedvalue-discreteapproxs.md) as desired.

## Lean

Formalized as [`MeasureTheory.Martingale.stoppedValue_min_ae_eq_condExp'`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.stoppedValue_min_ae_eq_condExp').

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1084](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1084)
