---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_apply
---

# rightContDef

Suppose $T$ is a topological space with the topology being the order topology. For $t \in T$, the right continuation of $\mathcal{F}$ at $t$ is given by

$$
\mathcal{F}_{t+} =
\begin{cases}
\mathcal{F}_t, & \text{if $t$ is isolated on the right}; \\
\mathop{\Large\sqcap}_{s > t} \mathcal{F}_s, & \text{otherwise}.
\end{cases}
$$

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof

This follows from Definition [Right continuation](def-rightlimitfiltration.md) because the topology on $T$ agrees with the one used to define the right continuation.

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_apply`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_apply).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 387](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L387)
