---
declaration: definition
origin: cited
lean: MeasureTheory.DiscreteApproxSequence
statement: formalized
---

# Discrete approximation sequence

Given a stopping time $\tau : \Omega \to T \cup \{\infty\}$, a sequence of stopping times $(\tau_n)_{n \in \mathbb{N}}$ is called an discrete approximation of $\tau$ if $\tau_n(\Omega)$ is countable for each $n$ and $\tau_n \downarrow \tau$ a.s. as $n \to \infty$.

## Depends on

- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)

## Lean

Formalized as [`MeasureTheory.DiscreteApproxSequence`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.DiscreteApproxSequence).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 985](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L985)
