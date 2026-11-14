---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.martingalePart_zero
---

# martingalePart_zero

$M_0 = X_0$.

## Depends on

- [Martingale part](def-martingalepart.md)

## Proof depends on

- [predictablePart_zero](lem-predictablepart-zero.md)

## Proof

By definition of the martingale part, $M = X - A$. By Lemma [predictablePart_zero](lem-predictablepart-zero.md), $A_0 = 0$, thus $M_0 = X_0 - A_0 = X_0$.

## Lean

Formalized as [`MeasureTheory.martingalePart_zero`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.martingalePart_zero).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 310](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L310)
