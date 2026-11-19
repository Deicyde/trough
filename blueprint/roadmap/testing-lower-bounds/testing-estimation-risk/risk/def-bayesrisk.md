---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.bayesRisk
---

# Bayes risk

The Bayes risk of $(P, y, \ell')$ for prior $\pi \in \mathcal M(\Theta)$ is $\mathcal R^P_\pi = \inf_{\hat{y} : \mathcal X \rightsquigarrow \mathcal Z} R^P_\pi(\hat{y})$ , where the infimum is over Markov kernels.

The Bayes risk of $(P, y, \ell')$ is $\mathcal R^*_B = \sup_{\pi \in \mathcal P(\Theta)} \mathcal R^P_\pi \: .$

## Depends on

- [Bayesian risk](def-bayesianrisk.md)

## Lean

Formalized as [`ProbabilityTheory.bayesRisk`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesRisk).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 62](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L62)
