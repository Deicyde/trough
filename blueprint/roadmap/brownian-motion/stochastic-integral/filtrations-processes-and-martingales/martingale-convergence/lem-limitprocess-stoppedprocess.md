---
declaration: lemma
origin: cited
lean: MeasureTheory.Filtration.limitProcess_stoppedProcess
statement: formalized
proof: formalized
---

# limitProcess_stoppedProcess

Let $M$ be a càdlàg uniformly integrable martingale and $\tau$ be a stopping time. Then almost surely, $X^\tau_\infty = X_\tau$.

## Depends on

- [limitProcess](def-limitprocess.md)
- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)

## Proof depends on

- [Adapted.isStronglyProgressive_of_rightContinuous](../basic-definitions/part-01/lem-adapted-isstronglyprogressive-of-rightcontin.md)

## Proof

We apply Lemma [limitProcess_ae_eq](lem-limitprocess-ae-eq.md). Because $M$ is right-continuous and adapted, it is progressively measurable by Lemma [Adapted.isStronglyProgressive_of_rightContinuous](../basic-definitions/part-01/lem-adapted-isstronglyprogressive-of-rightcontin.md). Therefore $X_\tau$ is $\mathcal{F}_\tau$-measurable. Convergence is obvious.

## Lean

Formalized as [`MeasureTheory.Filtration.limitProcess_stoppedProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.limitProcess_stoppedProcess).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1245](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1245)
