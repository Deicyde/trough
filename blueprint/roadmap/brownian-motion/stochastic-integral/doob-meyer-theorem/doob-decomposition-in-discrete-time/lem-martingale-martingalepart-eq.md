---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Martingale.martingalePart_eq
---

# Martingale.martingalePart_eq

If $X$ is a martingale, then $M = X$ almost surely.

## Depends on

- [Martingale part](def-martingalepart.md)
- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)

## Proof depends on

- [Martingale.predictablePart_eq_zero](lem-martingale-predictablepart-eq-zero.md)

## Proof

By definition of the martingale part, $M = X - A$. By Lemma [Martingale.predictablePart_eq_zero](lem-martingale-predictablepart-eq-zero.md), $A = 0$ almost surely, thus $M = X$ almost surely.

## Lean

Formalized as [`MeasureTheory.Martingale.martingalePart_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.martingalePart_eq).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 401](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L401)
