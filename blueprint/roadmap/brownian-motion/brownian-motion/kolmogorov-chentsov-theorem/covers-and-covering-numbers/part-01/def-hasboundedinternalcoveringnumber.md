---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: Metric.HasCoveringExponent
---

# Bounded internal covering number

Let $\mathrm{diam}(A)$ be the diameter of $A \subseteq E$, i.e. $\mathrm{diam}(A) = \sup_{x,y \in A} d_E(x, y)$. A set $A \subseteq E$ has bounded internal covering number with constant $c>0$ and exponent $t>0$ if for all $\varepsilon \in (0, \mathrm{diam}(A)]$, $N^{int}_\varepsilon(A) \le c \varepsilon^{-t}$.

## Depends on

- [Internal covering number](def-internalcoveringnumber.md)

## Lean

Formalized as [`Metric.HasCoveringExponent`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.HasCoveringExponent).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 290](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L290)
