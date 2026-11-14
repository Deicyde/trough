---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.hittingAfter
---

# Hitting time

For $X : T \to \Omega \to E$ a stochastic process, $B$ a subset of $E$ and $t_0 \in T$, the hitting time of $X$ in $B$ after $t_0$ is the random variable $\Omega \to T\cup\{\infty\}$ defined by

$$
\begin{aligned}
\tau_{B, t_0}(\omega) = \inf\{t \in T \mid t \ge t_0, \: X_t(\omega) \in B\} \: ,
\end{aligned}
$$

in which the infimum is infinite if the set is empty.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MeasureTheory.hittingAfter`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.hittingAfter).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 292](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L292)
