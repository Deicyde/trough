---
declaration: lemma
origin: cited
lean: MeasureTheory.tendsto_eLpNorm_stoppedValue_of_discreteApproxSequence
statement: formalized
proof: formalized
---

# tendsto_eLpNorm_stoppedValue_discreteApproxSequence

Let $\tau$ be a stopping time bounded by $t \in T$ and $(\tau_n)$ be a discrete approximation sequence of $\tau$. Then, for any right continuous martingale $X$, $X_{\tau} \in L^1$ and $X_{\tau_n \wedge t} \to X_{\tau}$ in $L^1$ as $n \to \infty$.

## Depends on

- [Right continuous function](../basic-definitions/part-01/def-rightcontinuous.md)
- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)
- [Discrete approximation sequence](def-approxseq.md)

## Proof depends on

- [tendsto_stoppedValue_discreteApproxSequence](lem-tendsto-stoppedvalue-discreteapproxsequence.md)
- [memLp_of_tendstoInMeasure](../uniformly-integrable/lem-memlp-of-tendstoinmeasure.md)
- [Vitali convergence theorem](../uniformly-integrable/lem-vitali.md)
- [uniformIntegrable_stoppedValue_discreteApproxSequence](lem-uniformintegrable-stoppedvalue-discreteappro.md)

## Proof

By Lemma [tendsto_stoppedValue_discreteApproxSequence](lem-tendsto-stoppedvalue-discreteapproxsequence.md), as $X$ is right continuous we have that $X_{\tau_n \wedge t} \to X_{\tau}$ a.s. and so, also in probability. Moreover, by Lemma [uniformIntegrable_stoppedValue_discreteApproxSequence](lem-uniformintegrable-stoppedvalue-discreteappro.md), the sequence $(X_{\tau_n \wedge t})$ is uniformly integrable. Thus, by Lemma [memLp_of_tendstoInMeasure](../uniformly-integrable/lem-memlp-of-tendstoinmeasure.md) and the Vitali convergence theorem (Lemma [Vitali convergence theorem](../uniformly-integrable/lem-vitali.md)), it follows that $X_{\tau} \in L^1$ and $X_{\tau_n \wedge t} \to X_{\tau}$ in $L^1$ as $n \to \infty$.

## Lean

Formalized as [`MeasureTheory.tendsto_eLpNorm_stoppedValue_of_discreteApproxSequence`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.tendsto_eLpNorm_stoppedValue_of_discreteApproxSequence).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1039](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1039)
