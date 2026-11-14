---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsAEKolmogorovProcess.aemeasurable_edist
---

# IsKolmogorovProcess.aemeasurable_edist

If $X : T \to \Omega \to E$ is a process that satisfies the Kolmogorov condition, then for all $s,t \in T$ the function $\omega \mapsto d_E(X_s(\omega), X_t(\omega))$ is $\mathbb{P}$-a.e. measurable.

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)

## Lean

Formalized as [`ProbabilityTheory.IsAEKolmogorovProcess.aemeasurable_edist`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsAEKolmogorovProcess.aemeasurable_edist).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 799](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L799)
