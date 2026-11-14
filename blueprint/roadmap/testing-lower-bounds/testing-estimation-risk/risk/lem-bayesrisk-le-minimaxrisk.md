---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.bayesRisk_le_minimaxRisk
---

# bayesRisk_le_minimaxRisk

$\mathcal R_B^* \le \mathcal R^*$.

## Depends on

- [Bayes risk](def-bayesrisk.md)
- [Minimax risk](def-minimaxrisk.md)

## Proof

For any $\pi \in \mathcal P(\mathcal X)$ and any estimator, $\pi\left[\hat{\mu}_\theta\left[\ell'(y(\theta), \hat{y}(\theta))\right]\right] \le \sup_{\theta \in \Theta}\hat{\mu}_\theta\left[\ell'(y(\theta), \hat{y}(\theta))\right]$.

## Lean

Formalized as [`ProbabilityTheory.bayesRisk_le_minimaxRisk`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesRisk_le_minimaxRisk).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 92](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L92)
