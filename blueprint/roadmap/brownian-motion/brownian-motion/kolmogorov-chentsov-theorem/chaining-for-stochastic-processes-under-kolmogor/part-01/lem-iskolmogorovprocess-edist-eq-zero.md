---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsAEKolmogorovProcess.edist_eq_zero
---

# IsKolmogorovProcess.edist_eq_zero

If $X : T \to \Omega \to E$ is a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$ and $s, t \in T$ are such that $d_T(s, t) = 0$, then $\mathbb{P}$-a.e. $d_E(X_s, X_t) = 0$.

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)

## Proof

It suffices to show that $d_E(X_s, X_t)^p = 0$ almost everywhere, which is in turn implied by $\mathbb{E}[d_E(X_s, X_t)^p] \le M d_t(s, t)^q = 0$.

## Lean

Formalized as [`ProbabilityTheory.IsAEKolmogorovProcess.edist_eq_zero`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsAEKolmogorovProcess.edist_eq_zero).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 741](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L741)
