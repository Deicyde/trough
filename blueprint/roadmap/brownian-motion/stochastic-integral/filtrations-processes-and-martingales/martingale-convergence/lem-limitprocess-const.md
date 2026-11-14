---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.limitProcess_const
---

# limitProcess_const

Let $c \in E$ and $X$ be the constant process equal to $c$. Then $X_\infty$ is a.e. equal to $c$.

## Depends on

- [limitProcess](def-limitprocess.md)

## Proof depends on

- [limitProcess_ae_eq](lem-limitprocess-ae-eq.md)

## Proof

This follows from Lemma [limitProcess_ae_eq](lem-limitprocess-ae-eq.md) as a constant function converges to a constant, and a constant function is a.e. strongly measurable with respect to any sigma-algebra.

## Lean

Formalized as [`MeasureTheory.Filtration.limitProcess_const`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.limitProcess_const).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1186](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1186)
