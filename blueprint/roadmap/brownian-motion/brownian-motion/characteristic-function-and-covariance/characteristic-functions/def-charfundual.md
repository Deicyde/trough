---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.charFunDual
---

# Characteristic function

The characteristic function of a measure $\mu$ on a normed space $E$ is the function $E^* \to \mathbb{C}$ defined by

$$
\begin{aligned}
\hat{\mu}(L) = \int_E e^{i L(x)} \: d\mu(x) \: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MeasureTheory.charFunDual`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.charFunDual).

## Sources

- [Brownian motion blueprint: chapters/characteristic_function.tex, line 7](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/characteristic_function.tex#L7)
