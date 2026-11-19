---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.avgRisk_eq_lintegral_posterior_prod
---

# bayesianRisk_bayesInv

The Bayesian risk of a Markov kernel $\hat{y} : \mathcal X \rightsquigarrow \mathcal Z$ with respect to a prior $\pi \in \mathcal M(\Theta)$ on $(P, y, \ell')$ satisfies

$$
\begin{aligned}
R^P_\pi(\hat{y}) = ((P_\pi^\dagger \times \hat{y}) \circ P \circ \pi)\left[(\theta, z) \mapsto \ell'(y(\theta), z)\right] \: ,
\end{aligned}
$$

whenever the Bayesian inverse $P_\pi^\dagger$ of $P$ with respect to $\pi$ exists (Definition [bayesInv](../../probability-transition-kernels/bayesian-inverse-of-a-kernel/def-bayesinv.md)).

## Depends on

- [Bayesian risk](def-bayesianrisk.md)
- [bayesInv](../../probability-transition-kernels/bayesian-inverse-of-a-kernel/def-bayesinv.md)

## Proof

Use the main property of the Bayesian inverse.

$$
\begin{aligned}
(P_\pi^\dagger \times \hat{y}) \circ P \circ \pi
&= (\mathrm{id} \parallel \hat{y}) \circ (P_\pi^\dagger \times \mathrm{id}) \circ (P \circ \pi)
\\
&= (\mathrm{id} \parallel \hat{y}) \circ (\mathrm{id} \times P) \circ \pi
\\
&= (\mathrm{id} \times (\hat{y} \circ P)) \circ \pi
\\
&= \pi \otimes (\hat{y} \circ P)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.avgRisk_eq_lintegral_posterior_prod`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.avgRisk_eq_lintegral_posterior_prod).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 244](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L244)
