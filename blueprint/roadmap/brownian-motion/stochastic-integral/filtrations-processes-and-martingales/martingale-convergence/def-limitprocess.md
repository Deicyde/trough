---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.limitProcess
---

# limitProcess

Let $X : T \to \Omega \to E$ be a stochastic process, let $\mathcal{F}$ be a filtration on $\Omega$ indexed by $T$ and let $P$ be a measure on $\Omega$. If there exists a function $Y : \Omega \to E$ which is measurable with respect to $\mathcal{F}_\infty$ such that for $P$-almost surely, $X_t$ converges to $Y$ as $t$ goes to infinity, then we say that $Y$ is the limit of $X$. We denote it by $X_\infty$.

## Depends on

- [Filtration](../basic-definitions/part-01/def-filtration.md)

## Lean

Formalized as [`MeasureTheory.Filtration.limitProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.limitProcess).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1139](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1139)
