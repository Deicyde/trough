---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.IsStronglyPredictable.predictablePart_eq
---

# isStronglyPredictable.predictablePart_eq

If $X$ is predictable, then $A = X - X_0$ almost surely.

## Depends on

- [Predictable part](def-predictablepart.md)
- [Predictable process](../../filtrations-processes-and-martingales/predictable-processes/def-predictable.md)

## Proof

Since $X$ is predictable, for all $n \in \mathbb{N}$, $X_{n+1}$ is $\mathcal{F}_n$-measurable and thus $\mathbb{E}[X_{n+1} - X_n \mid \mathcal{F}_n] = X_{n+1} - X_n$ a.s.. We get a telescoping sum in the definition of $A$ and thus $A_n = X_n - X_0$ a.s. for all $n \in \mathbb{N}$.

## Lean

Formalized as [`MeasureTheory.IsStronglyPredictable.predictablePart_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsStronglyPredictable.predictablePart_eq).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 374](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L374)
