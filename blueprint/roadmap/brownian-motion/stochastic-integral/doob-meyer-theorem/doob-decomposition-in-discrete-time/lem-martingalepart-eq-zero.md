---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.IsPredictable.martingalePart_eq
---

# martingalePart_eq_zero

If $X$ is predictable, then $M = X_0$ almost surely.

## Depends on

- [Martingale part](def-martingalepart.md)
- [Predictable process](../../filtrations-processes-and-martingales/predictable-processes/def-predictable.md)

## Proof depends on

- [isStronglyPredictable.predictablePart_eq](lem-isstronglypredictable-predictablepart-eq.md)

## Proof

By definition of the martingale part, $M = X - A$. By Lemma [isStronglyPredictable.predictablePart_eq](lem-isstronglypredictable-predictablepart-eq.md), $A = X - X_0$ almost surely, thus $M = X_0$ almost surely.

## Lean

Formalized as [`MeasureTheory.IsPredictable.martingalePart_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsPredictable.martingalePart_eq).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 388](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L388)
