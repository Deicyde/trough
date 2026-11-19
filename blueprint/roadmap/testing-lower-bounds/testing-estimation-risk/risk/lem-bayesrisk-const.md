---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.bayesRisk_const
---

# bayesRisk_const

The Bayes risk of a prior $\pi \in \mathcal M(\Theta)$ on $(P, y, \ell')$ with $P$ a constant Markov kernel is

$$
\begin{aligned}
\mathcal R^P_\pi
= \inf_{z \in \mathcal Z} \pi\left[\theta \mapsto \ell'(y(\theta), z)\right]
\: .
\end{aligned}
$$

In particular, it does not depend on $P$.

## Depends on

- [Bayes risk](def-bayesrisk.md)

## Proof

Let $\xi$ be the measure such that $P(\theta) = \xi$ for all $\theta$.

$$
\begin{aligned}
\mathcal R^P_\pi
&= \inf_{\hat{y}}(\pi \times (\hat{y} \circ \xi))\left[(\theta, z)\mapsto \ell'(y(\theta), z)\right]
\\
&= \inf_{\mu \in \mathcal P(\mathcal X)} (\pi \times \mu)\left[(\theta, z)\mapsto \ell'(y(\theta), z)\right]
\\
&= \inf_{\mu \in \mathcal P(\mathcal X)} \mu\left[ z \mapsto \pi\left[\theta \mapsto \ell'(y(\theta), z)\right]\right]
\\
&= \inf_{z \in \mathcal Z} \pi\left[\theta \mapsto \ell'(y(\theta), z)\right]
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.bayesRisk_const`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesRisk_const).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 129](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L129)
