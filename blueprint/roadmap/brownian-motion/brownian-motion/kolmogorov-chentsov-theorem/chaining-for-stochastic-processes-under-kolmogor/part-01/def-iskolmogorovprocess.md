---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsAEKolmogorovProcess
---

# Kolmogorov condition

Let $X : T \to \Omega \to E$ be a stochastic process, where $(T, d_T)$ and $(E, d_E)$ are pseudo-metric spaces and $(\Omega, \mathbb{P})$ is a measure space. Let $p, q > 0$. We say that $X$ satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$ if for all $s, t \in T$, $(X_s, X_t)$ is $\mathbb{P}$-a.e. measurable for the Borel $\sigma$-algebra on $E^2$ and

$$
\begin{aligned}
\mathbb{E}[d_E(X_s, X_t)^p] \le M d_T(s, t)^q
\: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.IsAEKolmogorovProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsAEKolmogorovProcess).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 725](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L725)
