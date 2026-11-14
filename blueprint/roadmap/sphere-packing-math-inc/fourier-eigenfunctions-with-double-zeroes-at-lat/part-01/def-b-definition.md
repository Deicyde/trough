---
declaration: definition
origin: cited
lean: MagicFunction.b.RealIntegrals.b', MagicFunction.b.RadialFunctions.b
statement: formalized
---

# b-definition

Define $b_\mathrm{rad} : \mathbb{R} \to \mathbb{C}$ by

$$
b_\mathrm{rad}(r) := J_1(r) + J_2(r) + J_3(r) + J_4(r) + J_5(r) + J_6(r)\qquad\text{(30)}
$$

where for $r \in \mathbb{R}$,

$$
\begin{aligned}
J_1(r) &:= \int_{-1}^{-1 + i} \psi_T(z) e^{\pi i r z} \, \mathrm{d} z,\qquad\text{(31)}\\
J_2(r) &:= \int_{-1 + i}^{i} \psi_T(z) e^{\pi i r z} \, \mathrm{d} z,\qquad\text{(32)}\\
J_3(r) &:= \int_{1}^{1 + i} \psi_T(z) e^{\pi i r z} \, \mathrm{d} z,\qquad\text{(33)}\\
J_4(r) &:= \int_{1 + i}^{i} \psi_T(z) e^{\pi i r z} \, \mathrm{d} z,\qquad\text{(34)}\\
J_5(r) &:= -2 \int_{0}^{i} \psi_I(z) e^{\pi i r z} \, \mathrm{d} z,\qquad\text{(35)}\\
J_6(r) &:= -2 \int_{i}^{i \infty} \psi_S(z) e^{\pi i r z} \, \mathrm{d} z.\qquad\text{(36)}\end{aligned}
$$

Here all the contours are straight line segments. Then we define $b : \mathbb{R}^8 \to \mathbb{C}$ by $b(x) := b_\mathrm{rad}(\|x\|^2)$.

## Depends on

- [psiI-psiT-psiS](def-psii-psit-psis.md)

## Lean

Formalized as [`MagicFunction.b.RealIntegrals.b'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.RealIntegrals.b'), [`MagicFunction.b.RadialFunctions.b`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.RadialFunctions.b).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 486](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L486)
