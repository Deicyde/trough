---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsAESquareIntegrable.memLp_two_stoppedValue'
statement: formalized
proof: formalized
---

# memLp_two_stoppedValue

If $M$ is a square integrable martingale and $\tau$ is a stopping time, then $M_\tau$ is in $\mathrm L^2$.

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)

## Proof depends on

- [limitProcess_stoppedProcess](../../../filtrations-processes-and-martingales/martingale-convergence/lem-limitprocess-stoppedprocess.md)
- [IsSquareIntegrable.stoppedProcess](lem-issquareintegrable-stoppedprocess.md)

## Proof

This follows from the fact that $M_\tau = M^\tau_\infty$ by Lemma [limitProcess_stoppedProcess](../../../filtrations-processes-and-martingales/martingale-convergence/lem-limitprocess-stoppedprocess.md), $M^\tau$ is square integrable by Lemma [IsSquareIntegrable.stoppedProcess](lem-issquareintegrable-stoppedprocess.md) and the stopped process of a square integrable martingale is in $\mathrm L^2$.

## Lean

Formalized as [`ProbabilityTheory.IsAESquareIntegrable.memLp_two_stoppedValue'`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsAESquareIntegrable.memLp_two_stoppedValue').

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 422](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L422)
