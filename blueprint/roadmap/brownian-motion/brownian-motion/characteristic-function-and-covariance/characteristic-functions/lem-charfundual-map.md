---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.charFunDual_map
---

# charFunDual_map

Let $\mu$ be a measure on a normed space $E$ and let $L$ be a continuous linear map from $E$ to $F$. Then for all $L' \in F^*$,

$$
\begin{aligned}
\widehat{L_*\mu}(L') = \hat{\mu}(L' \circ L) \: .
\end{aligned}
$$

## Depends on

- [Characteristic function](def-charfundual.md)

## Lean

Formalized as [`MeasureTheory.charFunDual_map`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.charFunDual_map).

## Sources

- [Brownian motion blueprint: chapters/characteristic_function.tex, line 67](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/characteristic_function.tex#L67)
