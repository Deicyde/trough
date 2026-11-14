---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Submartingale.predictablePart_nonneg
---

# Submartingale.predictablePart_nonneg

The predictable part of a real-valued submartingale is almost surely nonnegative.

## Depends on

- [Predictable part](def-predictablepart.md)
- [Submartingale](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-submartingale.md)

## Proof depends on

- [Submartingale.monotone_predictablePart](lem-submartingale-monotone-predictablepart.md)
- [predictablePart_zero](lem-predictablepart-zero.md)

## Proof

By Lemma [Submartingale.monotone_predictablePart](lem-submartingale-monotone-predictablepart.md), the predictable part $A$ is almost surely nondecreasing. By Lemma [predictablePart_zero](lem-predictablepart-zero.md), $A_0 = 0$. Therefore, $A_n \ge 0$ almost surely for all $n \in \mathbb{N}$.

## Lean

Formalized as [`MeasureTheory.Submartingale.predictablePart_nonneg`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.predictablePart_nonneg).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 524](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L524)
