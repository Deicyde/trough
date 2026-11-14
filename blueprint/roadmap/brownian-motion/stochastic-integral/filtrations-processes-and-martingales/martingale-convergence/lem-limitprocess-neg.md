---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.limitProcess_neg
---

# limitProcess_neg

If $X$ is a stochastic process, then $(-X)_\infty$ is a.e. equal to $-X_\infty$.

## Depends on

- [limitProcess](def-limitprocess.md)

## Proof depends on

- [limitProcess_ae_eq](lem-limitprocess-ae-eq.md)
- [limitProcess_const](lem-limitprocess-const.md)

## Proof

If there exists $g : \Omega \to E$ that is a.e. strongly measurable with respect to $\bigsqcup t, \mathcal{F}_t$ and such that $X$ converges almost surely to $g$, then $-X$ converges almost surely to $-g$ and we can conclude by Lemma [limitProcess_ae_eq](lem-limitprocess-ae-eq.md). Otherwise there does not exist $g : \Omega \to E$ that is a.e. strongly measurable with respect to $\bigsqcup t, \mathcal{F}_t$ and such that $-X$ converges almost surely to $g$, because if it did it would also be the case for $X$, so $X_\infty$ and $(-X)_\infty$ are both a.e. equal to $0$.

## Lean

Formalized as [`MeasureTheory.Filtration.limitProcess_neg`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.limitProcess_neg).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1210](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1210)
