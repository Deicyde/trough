---
declaration: lemma
origin: cited
lean: ProbabilityTheory.indist_continuousPart, ProbabilityTheory.indist_discontinuousPart
statement: formalized
proof: formalized
---

# unique_continuousPart

If $M$ is a square integrable martingale, then the decomposition $M = M^c + M^d$ as the sum of a continuous and a purely discontinuous square integrable martingales is unique up to indistinguishability.

## Depends on

- [continuousPartSquareIntegrable](def-continuouspartsquareintegrable.md)
- [discontinuousPart](def-discontinuouspart.md)

## Proof

A closed subspace is the complement of its orthogonal subspace.

## Lean

Formalized as [`ProbabilityTheory.indist_continuousPart`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.indist_continuousPart), [`ProbabilityTheory.indist_discontinuousPart`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.indist_discontinuousPart).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 714](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L714)
