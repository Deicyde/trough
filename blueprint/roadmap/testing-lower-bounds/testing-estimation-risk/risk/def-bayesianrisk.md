---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.avgRisk
---

# Bayesian risk

The Bayesian risk of an estimator $\hat{y}$ on $(P, y, \ell')$ for a prior $\pi \in \mathcal M(\Theta)$ is $R^P_\pi(\hat{y}) = \pi\left[\theta \mapsto r^P_\theta(\hat{y})\right]$ . It can also be expanded as $R^P_\pi(\hat{y}) = (\pi \otimes (\hat{y} \circ P))\left[ (\theta, z) \mapsto \ell'(y(\theta), z) \right]$ .

## Depends on

Its statement uses no other node that has an article here.

## Lean

Formalized as [`ProbabilityTheory.avgRisk`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.avgRisk).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 51](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L51)
