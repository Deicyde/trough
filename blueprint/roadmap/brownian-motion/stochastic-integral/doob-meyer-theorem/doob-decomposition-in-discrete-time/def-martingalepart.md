---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.martingalePart
---

# Martingale part

Let $X : \mathbb{N} \to \Omega \to E$ be a process indexed by $\mathbb{N}$, for $E$ a Banach space. Let $(\mathcal{F}_n)_{n\in\mathbb{N}}$ be a filtration on $\Omega$ and let $A$ be the predictable part of $X$ for that filtration. The martingale part of $X$ is the process $M : \mathbb{N} \to \Omega \to E$ defined by $M_n = X_n - A_n$.

## Depends on

- [Predictable part](def-predictablepart.md)

## Lean

Formalized as [`MeasureTheory.martingalePart`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.martingalePart).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 285](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L285)
