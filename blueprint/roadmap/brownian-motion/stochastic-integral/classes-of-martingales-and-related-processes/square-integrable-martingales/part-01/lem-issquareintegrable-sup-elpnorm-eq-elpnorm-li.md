---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable.iSup_eLpNorm_eq_eLpNorm_limitProcess
statement: formalized
---

# IsSquareIntegrable.sup_eLpNorm_eq_eLpNorm_limitProcess

For $M$ a square integrable martingale,

$$
\begin{aligned}
\sup_{t \in T} \Vert M_t \Vert_{L^2}
&= \Vert M_\infty \Vert_{L^2}
\: .
\end{aligned}
$$

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)
- [limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/def-limitprocess.md)

## Proof depends on

- [IsSquareIntegrable.eLpNorm_two_mono](lem-issquareintegrable-elpnorm-two-mono.md)
- [IsSquareIntegrable.tendsto_limitProcess](lem-issquareintegrable-tendsto-limitprocess.md)

## Lean

Stated as [`ProbabilityTheory.IsSquareIntegrable.iSup_eLpNorm_eq_eLpNorm_limitProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.iSup_eLpNorm_eq_eLpNorm_limitProcess); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 376](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L376)
