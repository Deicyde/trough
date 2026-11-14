---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsArgminEstimator.avgRisk_eq_lintegral_iInf
---

# bayesianRisk_genBayesEstimator

The Bayesian risk of the generalized Bayes estimator $\hat{y}_B$ is

$$
\begin{aligned}
R^P_\pi(\hat{y}_B) = (P \circ \pi)\left[x \mapsto \inf_{z \in \mathcal Z} P_\pi^\dagger(x) \left[\theta \mapsto \ell'(y(\theta), z)\right]\right]
\: .
\end{aligned}
$$

## Depends on

- [Bayesian risk](def-bayesianrisk.md)
- [Generalized Bayes estimator](def-genbayesestimator.md)

## Proof depends on

- [bayesianRisk_bayesInv](lem-bayesianrisk-bayesinv.md)

## Proof

Start from the equality of Lemma [bayesianRisk_bayesInv](lem-bayesianrisk-bayesinv.md) and use the definition of the generalized Bayes estimator.

## Lean

Formalized as [`ProbabilityTheory.IsArgminEstimator.avgRisk_eq_lintegral_iInf`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.IsArgminEstimator.avgRisk_eq_lintegral_iInf).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 313](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L313)
