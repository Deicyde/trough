---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.limitProcess_ae_eq
---

# limitProcess_ae_eq

Let $X : T \to \Omega \to E$ be a process such that there exists $g : \Omega \to E$ that is a.e. strongly measurable with respect to $\bigsqcup t, \mathcal{F}_t$ and such that $X$ converges almost surely to $g$. Then $X_\infty$ and $g$ are a.e. equal.

## Depends on

- [limitProcess](def-limitprocess.md)

## Proof

Because there exist a function that is a.e. strongly measurable with respect to $\bigsqcup t, \mathcal{F}_t$ and towards which $X$ converges almost surely, $X_\infty$ is such a function by definition. Because $X$ converges almost surely towards $g$, $g$ and $X_\infty$ are equal on the set where $X$ converges to $X_\infty$ and $X$ converges to $g$ by uniqueness of the limit.

## Lean

Formalized as [`MeasureTheory.Filtration.limitProcess_ae_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.limitProcess_ae_eq).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1161](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1161)
