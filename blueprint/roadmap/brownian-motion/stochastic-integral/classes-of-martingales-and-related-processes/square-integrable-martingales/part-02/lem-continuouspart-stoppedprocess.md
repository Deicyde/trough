---
declaration: lemma
origin: cited
lean: ProbabilityTheory.continuousPart_stoppedProcess, ProbabilityTheory.discontinuousPart_stoppedProcess
statement: formalized
proof: formalized
---

# continuousPart_stoppedProcess

If $M$ is a square integrable martingale and $\tau$ is a stopping time, then $(M^\tau)^c = (M^c)^\tau$ and $(M^\tau)^d = (M^d)^\tau$.

## Depends on

- [continuousPartSquareIntegrable](def-continuouspartsquareintegrable.md)

## Proof depends on

- [unique_continuousPart](lem-unique-continuouspart.md)
- [IsPurelyDiscontinuous.stoppedProcess](lem-ispurelydiscontinuous-stoppedprocess.md)

## Proof

We can write $M^\tau = (M^c + M^d)^\tau = (M^c)^\tau + (M^d)^\tau$. We conclude by Lemma [unique_continuousPart](lem-unique-continuouspart.md) thanks to Lemma [IsPurelyDiscontinuous.stoppedProcess](lem-ispurelydiscontinuous-stoppedprocess.md).

## Lean

Formalized as [`ProbabilityTheory.continuousPart_stoppedProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.continuousPart_stoppedProcess), [`ProbabilityTheory.discontinuousPart_stoppedProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.discontinuousPart_stoppedProcess).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 749](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L749)
