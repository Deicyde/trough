---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.covarianceBilin
---

# Covariance in a Hilbert space

The covariance bilinear form of a finite measure $\mu$ with finite second moment on a Hilbert space $E$ is the continuous bilinear form $C_\mu : E \times E \to \mathbb{R}$ with

$$
\begin{aligned}
C'_\mu(x, y) = \int_z \langle x, z - m_\mu \rangle \langle y, z - m_\mu \rangle \: d\mu(z) \: .
\end{aligned}
$$

This is $C_\mu$ applied to the linear maps $L_x, L_y \in E^*$ defined by $L_x(z) = \langle x, z \rangle$ and $L_y(z) = \langle y, z \rangle$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.covarianceBilin`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.covarianceBilin).

## Sources

- [Brownian motion blueprint: chapters/characteristic_function.tex, line 114](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/characteristic_function.tex#L114)
