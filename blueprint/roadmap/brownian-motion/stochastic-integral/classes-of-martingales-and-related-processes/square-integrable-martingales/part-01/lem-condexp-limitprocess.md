---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable.condExp_limitProcess_ae_eq
statement: formalized
proof: formalized
---

# condExp_limitProcess

For $M$ a square integrable martingale and $t \in T$, we have that $P[X_\infty | \mathcal{F}_t]$ is a.e. equal to $X_t$.

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)
- [limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/def-limitprocess.md)

## Proof depends on

- [condExp_limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/thm-condexp-limitprocess.md)
- [IsSquareIntegrable.uniformIntegrable](lem-issquareintegrable-uniformintegrable.md)

## Proof

Apply Theorem [condExp_limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/thm-condexp-limitprocess.md).

## Lean

Formalized as [`ProbabilityTheory.IsSquareIntegrable.condExp_limitProcess_ae_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.condExp_limitProcess_ae_eq).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 298](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L298)
