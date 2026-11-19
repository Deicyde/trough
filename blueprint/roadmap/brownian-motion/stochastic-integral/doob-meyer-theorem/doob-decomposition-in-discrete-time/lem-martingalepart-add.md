---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.martingalePart_add
---

# martingalePart_add

The martingale part of $X + Y$ is the sum of the martingale part of $X$ and the martingale part of $Y$.

## Depends on

- [Martingale part](def-martingalepart.md)

## Proof depends on

- [predictablePart_add](lem-predictablepart-add.md)

## Proof

By definition of the martingale part, $M = X - A$. By Lemma [predictablePart_add](lem-predictablepart-add.md), the predictable part of $X + Y$ is $A + B$. Therefore, the martingale part of $X + Y$ is $(X + Y) - (A + B) = M + N$.

## Lean

Formalized as [`MeasureTheory.martingalePart_add`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.martingalePart_add).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 453](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L453)
