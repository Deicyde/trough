---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isSquareIntegrable_of_limitProcess
statement: formalized
proof: formalized
---

# isSquareIntegrable_of_limitProcess

A càdlàg and uniformly integrable martingale $M$ is square integrable if and only if $M_\infty$ is in $\mathrm L^2$.

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)
- [limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/def-limitprocess.md)

## Proof

It is a càdlàg martingale by hypothesis, and the bound follows from Lemma lem:IsSquareIntegrable.iSup_eLpNorm_le_eLpNorm_limitProcess.

## Lean

Formalized as [`ProbabilityTheory.isSquareIntegrable_of_limitProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isSquareIntegrable_of_limitProcess).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 341](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L341)
