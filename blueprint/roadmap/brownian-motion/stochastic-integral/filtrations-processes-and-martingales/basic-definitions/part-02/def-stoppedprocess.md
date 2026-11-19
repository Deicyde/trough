---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.stoppedProcess
---

# Stopped process

Let $X : T \to \Omega \to E$ be a stochastic process and let $\tau : \Omega \to T$. The stopped process with respect to $\tau$ is defined by

$$
\begin{aligned}
(X^{\tau})_t = \begin{cases}
X_t & \text{if } t \le \tau \\
X_{\tau} & \text{otherwise}
\end{cases}
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MeasureTheory.stoppedProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.stoppedProcess).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 265](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L265)
