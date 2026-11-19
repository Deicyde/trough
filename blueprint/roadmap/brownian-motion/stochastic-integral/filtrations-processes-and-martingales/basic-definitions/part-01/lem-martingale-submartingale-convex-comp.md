---
declaration: lemma
origin: cited
lean: MeasureTheory.Martingale.submartingale_convex_comp
statement: formalized
proof: formalized
---

# Martingale.submartingale_convex_comp

Let $X : T \rightarrow \Omega\rightarrow E$ a martingale with values in a normed space $E$. Let $\phi : E \rightarrow \mathbb{R}$ convex and continuous such that $\phi(X_t)\in L^1(\Omega)$ for every $t\in T$. Then $\phi(X)$ is a sub-martingale.

## Depends on

- [Martingale](../../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Submartingale](def-submartingale.md)

## Proof depends on

- [Jensen's inequality for the conditional expectation](lem-conditional-jensen.md)

## Proof

By the conditional Jensen inequality (Lemma [Jensen's inequality for the conditional expectation](lem-conditional-jensen.md)), $\phi(X_t) = \phi\left( \mathbb{E}[X_T\ |\ \mathcal{F}_t] \right)\leq \mathbb{E}[\phi(X_T)\ |\ \mathcal{F}_t]$.

## Lean

Formalized as [`MeasureTheory.Martingale.submartingale_convex_comp`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.submartingale_convex_comp).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 186](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L186)
