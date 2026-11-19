---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable.isLocallySquareIntegrable
statement: formalized
proof: formalized
---

# IsSquareIntegrable.isLocallySquareIntegrable

Every square-integrable martingale is locally square-integrable: $\mathcal{M}^2 \subseteq \mathcal{M}^2_{\mathrm{loc}}$ .

## Depends on

- [Square integrable martingales](../square-integrable-martingales/part-01/def-issquareintegrable.md)
- [Locally square-integrable martingales](def-islocallysquareintegrable.md)

## Proof depends on

- [implies_locally](../../local-martingales/local-properties/lem-implies-locally.md)

## Proof

This follows from Lemma [implies_locally](../../local-martingales/local-properties/lem-implies-locally.md).

## Lean

Formalized as [`ProbabilityTheory.IsSquareIntegrable.isLocallySquareIntegrable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.isLocallySquareIntegrable).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 793](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L793)
