---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsArgminEstimator.isBayesEstimator, ProbabilityTheory.HasArgminEstimator.bayesRisk_eq
---

# isBayesEstimator_genBayesEstimator

When the generalized Bayes estimator is well defined, it is a Bayes estimator. The value of the Bayes risk with respect to the prior $\pi \in \mathcal M(\Theta)$ is then

$$
\begin{aligned}
\mathcal R^P_\pi = (P \circ \pi)\left[x \mapsto \inf_{z \in \mathcal Z} P_\pi^\dagger(x) \left[\theta \mapsto \ell'(y(\theta), z)\right]\right]
\: .
\end{aligned}
$$

## Depends on

- [Bayes estimator](def-bayesestimator.md)
- [Generalized Bayes estimator](def-genbayesestimator.md)
- [Bayes risk](def-bayesrisk.md)

## Proof depends on

- [bayesianRisk_ge_inf_bayesInv](lem-bayesianrisk-ge-inf-bayesinv.md)
- [bayesianRisk_genBayesEstimator](lem-bayesianrisk-genbayesestimator.md)

## Proof

By Lemma [bayesianRisk_ge_inf_bayesInv](lem-bayesianrisk-ge-inf-bayesinv.md), the Bayesian risk of the generalized Bayes estimator obtained in Lemma [bayesianRisk_genBayesEstimator](lem-bayesianrisk-genbayesestimator.md) is a lower bound for the Bayesian risk.

## Lean

Formalized as [`ProbabilityTheory.IsArgminEstimator.isBayesEstimator`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.IsArgminEstimator.isBayesEstimator), [`ProbabilityTheory.HasArgminEstimator.bayesRisk_eq`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.HasArgminEstimator.bayesRisk_eq).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 330](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L330)
