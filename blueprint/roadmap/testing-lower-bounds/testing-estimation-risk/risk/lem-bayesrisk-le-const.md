---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.bayesRisk_le_iInf
---

# bayesRisk_le_const

The Bayes risk of a prior $\pi \in \mathcal M(\Theta)$ on $(P, y, \ell')$ with $P$ a Markov kernel satisfies

$$
\begin{aligned}
\mathcal R^P_\pi \le \inf_{z \in \mathcal Z} \pi\left[ \theta \mapsto \ell'(y(\theta), z) \right]
\: .
\end{aligned}
$$

## Depends on

- [Bayes risk](def-bayesrisk.md)

## Proof

The infimum over all Markov kernels in the definition of the Bayes risk of $\pi$ is bounded from above by the infimum restricted to constant, deterministic Markov kernels.

## Lean

Formalized as [`ProbabilityTheory.bayesRisk_le_iInf`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesRisk_le_iInf).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 111](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L111)
