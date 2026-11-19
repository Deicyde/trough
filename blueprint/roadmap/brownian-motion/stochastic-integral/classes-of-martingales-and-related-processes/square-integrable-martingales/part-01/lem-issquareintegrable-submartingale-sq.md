---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable.submartingale_sq_norm
statement: formalized
proof: formalized
---

# IsSquareIntegrable.submartingale_sq

If $M$ is a square integrable martingale, then $\Vert M \Vert^2$ is a submartingale.

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)
- [Submartingale](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-submartingale.md)

## Proof depends on

- [Martingale.submartingale_convex_comp](../../../filtrations-processes-and-martingales/basic-definitions/part-01/lem-martingale-submartingale-convex-comp.md)

## Proof

Apply Lemma [Martingale.submartingale_convex_comp](../../../filtrations-processes-and-martingales/basic-definitions/part-01/lem-martingale-submartingale-convex-comp.md) with the convex function $f: x \mapsto \Vert x \Vert^2$ .

## Lean

Formalized as [`ProbabilityTheory.IsSquareIntegrable.submartingale_sq_norm`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.submartingale_sq_norm).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 221](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L221)
