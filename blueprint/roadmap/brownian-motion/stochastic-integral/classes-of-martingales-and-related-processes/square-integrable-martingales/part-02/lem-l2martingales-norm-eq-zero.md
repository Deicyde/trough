---
declaration: lemma
origin: cited
lean: ProbabilityTheory.SquareIntegrable.injective_toL2
statement: formalized
---

# L2Martingales.norm_eq_zero

For $M \in \mathcal{M}^2(E)$, $\Vert M \Vert = 0$ if and only if $M = 0$.

## Depends on

- [L2Martingales.norm](def-l2martingales-norm.md)

## Proof depends on

- [IsSquareIntegrable.sup_eLpNorm_eq_eLpNorm_limitProcess](../part-01/lem-issquareintegrable-sup-elpnorm-eq-elpnorm-li.md)

## Proof

By Lemma [IsSquareIntegrable.sup_eLpNorm_eq_eLpNorm_limitProcess](../part-01/lem-issquareintegrable-sup-elpnorm-eq-elpnorm-li.md), $\Vert M \Vert = 0$ if and only if for all $t \in T$, $\Vert M_t \Vert_{L^2} = 0$ . Because $M$ is càdlàg, this implies that $M$ is indistinguishable from $0$.

## Lean

Stated as [`ProbabilityTheory.SquareIntegrable.injective_toL2`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SquareIntegrable.injective_toL2); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 477](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L477)
