---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.riskIncrease
---

# riskIncrease

The Bayes risk increase $I^P_{\pi}(\kappa)$ of a kernel $\kappa : \mathcal X \rightsquigarrow \mathcal X'$ with respect to the estimation problem $(P, y, \ell')$ and the prior $\pi \in \mathcal M(\Theta)$ is the difference of the Bayes risk of $(\kappa \circ P, y, \ell')$ and that of $(P, y, \ell')$. That is,

$$
\begin{aligned}
I^P_{\pi}(\kappa)
&= \mathcal R^{\kappa \circ P}_\pi - \mathcal R^P_\pi
\\
&= \inf_{\hat{y} : \mathcal X' \rightsquigarrow \mathcal Z} (\pi \otimes (\hat{y} \circ \kappa \circ P))\left[(\theta, z) \mapsto \ell'(y(\theta), z)\right]
- \inf_{\hat{y} : \mathcal X \rightsquigarrow \mathcal Z} (\pi \otimes (\hat{y} \circ P))\left[(\theta, z) \mapsto \ell'(y(\theta), z)\right]
\: .
\end{aligned}
$$

## Depends on

- [Bayes risk](def-bayesrisk.md)

## Lean

Formalized as [`ProbabilityTheory.riskIncrease`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.riskIncrease).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 446](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L446)
