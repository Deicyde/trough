---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.limitProcess_congr
---

# limitProcess_congr

Let $X$ and $Y$ be two indistinguishable processes. Then $X_\infty$ and $Y_\infty$ are a.e. equal.

## Depends on

- [limitProcess](def-limitprocess.md)

## Proof depends on

- [limitProcess_ae_eq](lem-limitprocess-ae-eq.md)

## Proof

If there exists $g : \Omega \to E$ that is a.e. strongly measurable with respect to $\bigsqcup t, \mathcal{F}_t$ and such that $X$ converges almost surely to $g$, then it is enough to show that $Y$ converges almost surely to $g$ by Lemma [limitProcess_ae_eq](lem-limitprocess-ae-eq.md). This follows from indistinguishability.

Otherwise, $X_\infty = 0$, and by indistinguishability there does not exist $g : \Omega \to E$ that is a.e. strongly measurable with respect to $\bigsqcup t, \mathcal{F}_t$ and such that $Y$ converges almost surely to $g$, so $Y_\infty = 0$ as well.

## Lean

Formalized as [`MeasureTheory.Filtration.limitProcess_congr`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.limitProcess_congr).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1172](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1172)
