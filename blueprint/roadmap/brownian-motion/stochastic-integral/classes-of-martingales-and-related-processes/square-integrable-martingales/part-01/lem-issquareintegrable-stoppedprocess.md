---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable.stoppedProcess
statement: formalized
proof: formalized
---

# IsSquareIntegrable.stoppedProcess

If $M$ is a square integrable martingale and $\tau$ is a stopping time, then $M^\tau$ is a square integrable martingale.

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)

## Proof depends on

- [isSquareIntegrable_of_limitProcess](lem-issquareintegrable-of-limitprocess.md)
- [Martingale.classD_iff_uniformIntegrable](../../../local-martingales/doob-meyer-class/part-01/lem-martingale-classd-iff-uniformintegrable.md)
- [doob_lp_norm_top](../../../filtrations-processes-and-martingales/doobs-lp-inequality/cor-doob-lp-norm-top.md)
- [IsSquareIntegrable.uniformIntegrable](lem-issquareintegrable-uniformintegrable.md)
- [limitProcess_stoppedProcess](../../../filtrations-processes-and-martingales/martingale-convergence/lem-limitprocess-stoppedprocess.md)

## Proof

We apply Lemma [isSquareIntegrable_of_limitProcess](lem-issquareintegrable-of-limitprocess.md). First, $M^\tau$ is a martingale. Moreover, $M$ is uniformly integrable by Lemma [IsSquareIntegrable.uniformIntegrable](lem-issquareintegrable-uniformintegrable.md), thus it is of class D by Lemma [Martingale.classD_iff_uniformIntegrable](../../../local-martingales/doob-meyer-class/part-01/lem-martingale-classd-iff-uniformintegrable.md), thus $M^\tau$ is uniformly integrable. Finally, we have

$$
\begin{aligned}
\|M^\tau_\infty\|_2^2 & = \|M_\tau\|^2 \\
& \le \int (\sup_t \|M_t(\omega)\|)^2 P(\mathrm d\omega) \\
& \le 4 \|M_\infty\|^2_2 \\
& < \infty.
\end{aligned}
$$

The first equality follows from Lemma [limitProcess_stoppedProcess](../../../filtrations-processes-and-martingales/martingale-convergence/lem-limitprocess-stoppedprocess.md). The first inequality is obtained as follows: if $\tau(\omega) = \infty$, then $M_\tau = M_\infty$ and $M_t \longrightarrow M_\infty$ almost surely so $\|M_\infty(\omega)\| \le \sup_t \|M_t(\omega)\|$. Otherwise the inequality is obvious. The second inequality is Corollary [doob_lp_norm_top](../../../filtrations-processes-and-martingales/doobs-lp-inequality/cor-doob-lp-norm-top.md).

## Lean

Formalized as [`ProbabilityTheory.IsSquareIntegrable.stoppedProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.stoppedProcess).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 355](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L355)
