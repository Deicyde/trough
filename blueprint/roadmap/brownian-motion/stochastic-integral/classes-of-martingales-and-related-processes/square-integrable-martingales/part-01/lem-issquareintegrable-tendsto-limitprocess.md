---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable.ae_tendsto_limitProcess, ProbabilityTheory.IsSquareIntegrable.tendsto_eLpNorm_two_limitProcess
statement: formalized
---

# IsSquareIntegrable.tendsto_limitProcess

For $M$ a square integrable martingale, we have $M_t \to M_\infty$ almost surely and in $L^2$ as $t \to \infty$ .

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)
- [limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/def-limitprocess.md)

## Proof depends on

- [tendsto_limitProcess_of_cadlag](../../../filtrations-processes-and-martingales/martingale-convergence/thm-tendsto-limitprocess-of-cadlag.md)

## Proof

TODO: use a martingale convergence theorem. Check whether Theorem [tendsto_limitProcess_of_cadlag](../../../filtrations-processes-and-martingales/martingale-convergence/thm-tendsto-limitprocess-of-cadlag.md) is what we need.

## Lean

Stated as [`ProbabilityTheory.IsSquareIntegrable.ae_tendsto_limitProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.ae_tendsto_limitProcess), [`ProbabilityTheory.IsSquareIntegrable.tendsto_eLpNorm_two_limitProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.tendsto_eLpNorm_two_limitProcess); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 259](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L259)
