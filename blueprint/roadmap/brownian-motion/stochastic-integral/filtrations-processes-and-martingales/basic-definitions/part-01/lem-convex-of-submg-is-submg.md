---
declaration: lemma
origin: cited
lean: MeasureTheory.Submartingale.monotone_convex_comp
statement: formalized
proof: formalized
---

# convex_of_submg_is_submg

Let $X : T \rightarrow \Omega \rightarrow E$ a sub-martingale. Let $\phi:E \rightarrow \mathbb{R}$ convex, continuous, and increasing such that $\phi(X_t)\in L^1(\Omega)$ for every $t\in T$. Then $\phi(X)$ is a sub-martingale.

## Depends on

- [Submartingale](def-submartingale.md)

## Proof

By Jensen and the fact that $\phi$ is increasing $\phi(X_t) \leq \phi\left( \mathbb{E}[X_T\ |\ \mathcal{F}_t] \right)\leq \mathbb{E}[\phi(X_T)\ |\ \mathcal{F}_t]$.

## Lean

Formalized as [`MeasureTheory.Submartingale.monotone_convex_comp`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.monotone_convex_comp).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 219](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L219)
