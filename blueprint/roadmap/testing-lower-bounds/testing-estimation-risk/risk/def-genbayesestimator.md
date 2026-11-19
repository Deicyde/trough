---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsArgminEstimator
---

# Generalized Bayes estimator

The generalized Bayes estimator for prior $\pi \in \mathcal P(\Theta)$ on $(P, y, \ell')$ is the deterministic estimator $\mathcal X \to \mathcal Z$ given by

$$
\begin{aligned}
x \mapsto \arg\min_z P_\pi^\dagger(x)\left[\theta \mapsto \ell'(y(\theta), z)\right] \: ,
\end{aligned}
$$

if there exists such a measurable argmin.

## Depends on

Its statement uses no other node that has an article here.

## Lean

Formalized as [`ProbabilityTheory.IsArgminEstimator`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.IsArgminEstimator).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 300](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L300)
