---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsGaussianProcess.congr
---

# isGaussianProcess_of_modification

Let $X, Y : T \to \Omega \to E$ be two stochastic processes that are modifications of each other (that is, for all $t \in T$, $X_t =_{a.e.} Y_t$). If $X$ is a Gaussian process, then $Y$ is a Gaussian process as well.

## Depends on

- [Gaussian processes](../../../../mathlib/overview/probability-theory/stochastic-processes/gaussian-processes.md)

## Proof depends on

- [map_eq_of_modification](../../stochastic-processes/lem-map-eq-of-modification.md)

## Proof

Being a Gaussian process is defined in terms of the distribution of finite-dimensional random vectors. By Lemma [map_eq_of_modification](../../stochastic-processes/lem-map-eq-of-modification.md), the random vector $(Y_{t_1}, \ldots, Y_{t_n})$ has the same distribution as the random vector $(X_{t_1}, \ldots, X_{t_n})$ for all $t_1, \ldots, t_n \in T$.

## Lean

Formalized as [`ProbabilityTheory.IsGaussianProcess.congr`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsGaussianProcess.congr).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 501](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L501)
