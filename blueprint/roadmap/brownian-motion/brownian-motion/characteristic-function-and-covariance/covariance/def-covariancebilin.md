---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.covarianceBilinDual, ProbabilityTheory.covarianceBilinDual_apply, ProbabilityTheory.covarianceBilinDual_apply'
---

# Covariance

The covariance bilinear form of a measure $\mu$ on $F$ with finite second moment is the continuous bilinear form $C_\mu : F^* \times F^* \to \mathbb{R}$ with

$$
\begin{aligned}
C_\mu(L_1, L_2)
&= \int_x (L_1(x) - L_1(m_\mu)) (L_2(x) - L_2(m_\mu)) \: d\mu(x)
\\
&= \int_x L_1(x - m_\mu) L_2(x- m_\mu) \: d\mu(x)
\: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.covarianceBilinDual`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.covarianceBilinDual), [`ProbabilityTheory.covarianceBilinDual_apply`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.covarianceBilinDual_apply), [`ProbabilityTheory.covarianceBilinDual_apply'`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.covarianceBilinDual_apply').

## Sources

- [Brownian motion blueprint: chapters/characteristic_function.tex, line 89](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/characteristic_function.tex#L89)
