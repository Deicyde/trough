---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsPurelyDiscontinuous.stoppedProcess
statement: formalized
proof: formalized
---

# IsPurelyDiscontinuous.stoppedProcess

If $M$ is a purely discontinuous martingale and $\tau$ is a stopping time, then $M^\tau$ is a purely discontinuous martingale.

## Depends on

- [IsPurelyDiscontinuous](../part-01/def-ispurelydiscontinuous.md)

## Proof depends on

- [IsSquareIntegrable.stoppedProcess](../part-01/lem-issquareintegrable-stoppedprocess.md)
- [limitProcess_stoppedProcess](../../../filtrations-processes-and-martingales/martingale-convergence/lem-limitprocess-stoppedprocess.md)
- [condExp_limitProcess_stopped](../part-01/lem-condexp-limitprocess-stopped.md)

## Proof

By Lemma [IsSquareIntegrable.stoppedProcess](../part-01/lem-issquareintegrable-stoppedprocess.md) $M^\tau$ is a square integrable martingale. Let $N$ be a continuous square integrable martingale. Then again by Lemma [IsSquareIntegrable.stoppedProcess](../part-01/lem-issquareintegrable-stoppedprocess.md), $N^\tau$ is a continuous square integrable martingale. We thus have

$$
\begin{aligned}
P[\langle M^\tau_\infty, N_\infty\rangle] & = P[\langle M_\tau, N_\infty\rangle] \\
& = P[\langle M_\tau, P[M_\infty | \mathcal{F}_\tau]\rangle] \\
& = P[\langle M_\tau, N_\tau\rangle] \\
& = P[\langle M_\infty, N_\tau\rangle] \\
& = 0.
\end{aligned}
$$

The first equality is Lemma [limitProcess_stoppedProcess](../../../filtrations-processes-and-martingales/martingale-convergence/lem-limitprocess-stoppedprocess.md), the second is the pull-out property of the conditional expectation, the third one is Lemma [condExp_limitProcess_stopped](../part-01/lem-condexp-limitprocess-stopped.md), the fourth one is the same as before and the last one is the fact that $M$ is purely discontinuous while $N^\tau$ is continuous.

## Lean

Formalized as [`ProbabilityTheory.IsPurelyDiscontinuous.stoppedProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsPurelyDiscontinuous.stoppedProcess).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 727](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L727)
