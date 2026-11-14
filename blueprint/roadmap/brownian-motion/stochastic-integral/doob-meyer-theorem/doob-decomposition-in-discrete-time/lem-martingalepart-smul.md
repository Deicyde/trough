---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.martingalePart_smul
---

# martingalePart_smul

For any scalar $c$, the martingale part of $c X$ is $c M$.

## Depends on

- [Martingale part](def-martingalepart.md)

## Proof depends on

- [predictablePart_smul](lem-predictablepart-smul.md)

## Proof

By definition of the martingale part, $M = X - A$. By Lemma [predictablePart_smul](lem-predictablepart-smul.md), the predictable part of $c X$ is $c A$. Therefore, the martingale part of $c X$ is $c X - c A = c M$.

## Lean

Formalized as [`MeasureTheory.martingalePart_smul`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.martingalePart_smul).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 427](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L427)
