---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.lintegral_iInf_posterior_le_avgRisk
---

# bayesianRisk_ge_inf_bayesInv

The Bayesian risk of a Markov kernel $\hat{y} : \mathcal X \rightsquigarrow \mathcal Z$ with respect to a prior $\pi \in \mathcal M(\Theta)$ on $(P, y, \ell')$ satisfies

$$
\begin{aligned}
R^P_\pi(\hat{y}) \ge (P \circ \pi)\left[x \mapsto \inf_{z \in \mathcal Z} P_\pi^\dagger(x) \left[\theta \mapsto \ell'(y(\theta), z)\right]\right] \: .
\end{aligned}
$$

## Depends on

- [Bayesian risk](def-bayesianrisk.md)
- [bayesInv](../../probability-transition-kernels/bayesian-inverse-of-a-kernel/def-bayesinv.md)

## Proof depends on

- [bayesianRisk_bayesInv](lem-bayesianrisk-bayesinv.md)

## Proof

Starting from the equality of Lemma [bayesianRisk_bayesInv](lem-bayesianrisk-bayesinv.md), we get

$$
\begin{aligned}
R^P_\pi(\hat{y})
&= ((P_\pi^\dagger \times \hat{y}) \circ P \circ \pi)\left[(\theta, z) \mapsto \ell'(y(\theta), z)\right]
\\
&= (P \circ \pi)\left[x \mapsto (P_\pi^\dagger(x) \times \hat{y}(x)) \left[(\theta, z) \mapsto \ell'(y(\theta), z)\right]\right]
\\
&= (P \circ \pi)\left[x \mapsto \hat{y}(x)\left[z \mapsto P_\pi^\dagger(x) \left[\theta \mapsto \ell'(y(\theta), z)\right]\right]\right]
\\
&\ge (P \circ \pi)\left[x \mapsto \inf_{z \in \mathcal Z} P_\pi^\dagger(x) \left[\theta \mapsto \ell'(y(\theta), z)\right]\right]
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.lintegral_iInf_posterior_le_avgRisk`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.lintegral_iInf_posterior_le_avgRisk).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 272](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L272)
