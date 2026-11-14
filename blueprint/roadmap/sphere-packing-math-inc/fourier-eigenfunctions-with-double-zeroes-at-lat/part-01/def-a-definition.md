---
declaration: definition
origin: cited
lean: MagicFunction.a.RealIntegrals.a', MagicFunction.a.RadialFunctions.a
statement: formalized
---

# a-definition

Define $a_{\mathrm{rad}} : \mathbb{R} \to \mathbb{C}$ by

$$
\begin{aligned}
a_\mathrm{rad}(r) := I_1(r) + I_2(r) + I_3(r) + I_4(r) + I_5(r) + I_6(r)\qquad\text{(8)}\end{aligned}
$$

where

$$
\begin{aligned}
I_1(r) &:= \int_{-1}^{-1 + i} \phi_0 \left(\frac{-1}{z+1}\right) (z + 1)^2 e^{\pi i r z} \mathrm{d} z\qquad\text{(9)}\\
I_2(r) &:= \int_{-1 + i}^{i} \phi_0 \left(\frac{-1}{z+1}\right) (z + 1)^2 e^{\pi i r z} \mathrm{d} z\qquad\text{(10)}\\
I_3(r) &:= \int_{1}^{1 + i} \phi_0 \left(\frac{-1}{z-1}\right) (z - 1)^2 e^{\pi i r z} \mathrm{d} z\qquad\text{(11)}\\
I_4(r) &:= \int_{1 + i}^{i} \phi_0 \left(\frac{-1}{z-1}\right) (z - 1)^2 e^{\pi i r z} \mathrm{d} z\qquad\text{(12)}\\
I_5(r) &:= -2 \int_{0}^{i} \phi_0 \left(\frac{-1}{z}\right) z^2 e^{\pi i r z} \mathrm{d} z\qquad\text{(13)}\\
I_6(r) &:= 2 \int_{i}^{i\infty} \phi_0(z) e^{\pi i r z} \mathrm{d} z\qquad\text{(14)}\end{aligned}
$$

Here all the contours are chosen to be straight line segments. Now, define $a(x) := a_{\mathrm{rad}}(\|x\|^2)$ for $x \in \mathbb{R}^8$.

## Depends on

- [phi4-phi2-phi0](def-phi4-phi2-phi0.md)

## Lean

Formalized as [`MagicFunction.a.RealIntegrals.a'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.RealIntegrals.a'), [`MagicFunction.a.RadialFunctions.a`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.RadialFunctions.a).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 69](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L69)
