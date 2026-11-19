---
declaration: lemma
origin: cited
lean: MeasureTheory.uniformIntegrable_stoppedValue_discreteApproxSequence
statement: formalized
proof: formalized
---

# uniformIntegrable_stoppedValue_discreteApproxSequence

Let $\tau$ be a stopping time bounded by $t \in T$ and $(\tau_n)$ be a discrete approximation sequence of $\tau$. Then, for any martingale $X$, the sequence of stopped values $(X_{\tau_n \wedge t})$ is uniformly integrable.

## Depends on

- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)
- [Discrete approximation sequence](def-approxseq.md)

## Proof depends on

- [discreteApproxSequence_of](lem-discreteapproxsequence-of.md)
- [uniformIntegrable_stoppedValue_martingale_of_countable_range](../uniformly-integrable/lem-uniformintegrable-stoppedvalue-martingale-of.md)

## Proof

Follows directly by Lemma [uniformIntegrable_stoppedValue_martingale_of_countable_range](../uniformly-integrable/lem-uniformintegrable-stoppedvalue-martingale-of.md) and Lemma [discreteApproxSequence_of](lem-discreteapproxsequence-of.md).

## Lean

Formalized as [`MeasureTheory.uniformIntegrable_stoppedValue_discreteApproxSequence`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.uniformIntegrable_stoppedValue_discreteApproxSequence).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1025](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1025)
