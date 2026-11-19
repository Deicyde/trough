---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsAESquareIntegrable.limitProcess_sub
statement: formalized
---

# IsSquareIntegrable.limitProcess_sub

For $M$ and $N$ two square integrable martingales, $(M - N)_\infty$ and $M_\infty - N_\infty$ are a.e. equal.

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)
- [limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/def-limitprocess.md)

## Proof depends on

- [IsSquareIntegrable.tendsto_limitProcess](lem-issquareintegrable-tendsto-limitprocess.md)

## Proof

Lemma [limitProcess_ae_eq](../../../filtrations-processes-and-martingales/martingale-convergence/lem-limitprocess-ae-eq.md) with $g := M_\infty - N_\infty$.

## Lean

Stated as [`ProbabilityTheory.IsAESquareIntegrable.limitProcess_sub`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsAESquareIntegrable.limitProcess_sub); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 285](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L285)
