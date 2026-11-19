---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont
---

# Right continuation

Assume that $T$ is a partial order. For $\mathcal{F}$ a filtration indexed by $T$ and $t \in T$, we define the *right continuation* as

$$
\mathcal{F}_{t+} =
\begin{cases}
\mathcal{F}_t, & \text{if $t$ is isolated on the right in the order topology}; \\
\mathop{\Large\sqcap}_{s > t} \mathcal{F}_s, & \text{otherwise}.
\end{cases}
$$

Note that $\mathop{\Large\sqcap}$ denotes the infimum in the lattice of sigma-algebras on $\Omega$.

## Depends on

- [Filtration](../basic-definitions/part-01/def-filtration.md)

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 345](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L345)
