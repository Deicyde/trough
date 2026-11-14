---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Martingale.predictablePart_eq_zero
---

# Martingale.predictablePart_eq_zero

If $X$ is a martingale, then $A = 0$ almost surely.

## Depends on

- [Predictable part](def-predictablepart.md)
- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)

## Proof

By the martingale property, each conditional expectation in the definition of $A$ is zero.

## Lean

Formalized as [`MeasureTheory.Martingale.predictablePart_eq_zero`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.predictablePart_eq_zero).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 361](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L361)
