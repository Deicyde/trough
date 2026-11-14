---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.bayesRisk_le_bayesRisk_comp
---

# Data-processing inequality

For $P : \Theta \rightsquigarrow \mathcal X$ and $\kappa : \mathcal X \rightsquigarrow \mathcal X'$ a Markov kernel, $\mathcal R^{\kappa \circ P}_\pi \ge \mathcal R^{P}_\pi$ (where the estimation problems differ only in the kernel).

## Depends on

- [Bayes risk](def-bayesrisk.md)

## Proof

The risk $\mathcal R^{\kappa \circ P}_\pi$ is

$$
\begin{aligned}
\mathcal R^{\kappa \circ P}_\pi
&= \inf_{\hat{y} : \mathcal X' \rightsquigarrow \mathcal Z} (\pi \otimes (\hat{y} \circ \kappa \circ P))\left[(\theta, z) \mapsto \ell'(y(\theta), z)\right]
\\
&\ge \inf_{\hat{y} : \mathcal X \rightsquigarrow \mathcal Z} (\pi \otimes (\hat{y} \circ P))\left[(\theta, z) \mapsto \ell'(y(\theta), z)\right]
\\
&= \mathcal R^{P}_\pi
\: .
\end{aligned}
$$

The inequality is due to taking an infimum over a larger set: $\{\hat{y} \circ \kappa \mid \hat{y} : \mathcal X' \rightsquigarrow \mathcal Z \text{ Markov}\} \subseteq \{\hat{y}' : \mathcal X \rightsquigarrow \mathcal Z \mid \hat{y} \text{ Markov}\}$ .

## Lean

Formalized as [`ProbabilityTheory.bayesRisk_le_bayesRisk_comp`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesRisk_le_bayesRisk_comp).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 164](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L164)
