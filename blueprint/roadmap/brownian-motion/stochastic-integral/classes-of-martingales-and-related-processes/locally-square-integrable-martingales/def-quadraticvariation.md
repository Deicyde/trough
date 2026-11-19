---
declaration: definition
origin: cited
lean: ProbabilityTheory.predQuadVariation
statement: formalized
---

# Predictable quadratic variation

For $M \in \mathcal{M}^2_{\mathrm{loc}}$ with càdlàg paths, the predictable quadratic variation of $M$ is defined as the predictable part of the Doob-Meyer decomposition of the local submartingale $\Vert M \Vert^2$ . We denote it by $\langle M \rangle$ .

## Depends on

- [Locally square-integrable martingales](def-islocallysquareintegrable.md)
- [Cadlag function](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Doob-Meyer decomposition](../../doob-meyer-theorem/local-version-of-the-doob-meyer-decomposition/thm-local-doobmeyer.md)
- [IsLocallySquareIntegrable.isLocalSubmartingale_sq_norm](lem-islocallysquareintegrable-islocalsubmartinga.md)

## Lean

Formalized as [`ProbabilityTheory.predQuadVariation`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.predQuadVariation).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 833](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L833)
