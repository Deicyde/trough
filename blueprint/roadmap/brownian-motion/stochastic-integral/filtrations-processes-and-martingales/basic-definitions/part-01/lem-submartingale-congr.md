---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Submartingale.congr
---

# Submartingale.congr

If $X$ is a submartingale and $Y$ is an adapted modification of $X$, then $Y$ is a submartingale.

## Depends on

- [Submartingale](def-submartingale.md)
- [adapted](def-adapted.md)

## Proof

Let $i \le j$ in $T$. We want to show that $P[Y_j \mid \mathcal{F}_i] \ge Y_i$ almost surely. It suffices to show that $\int_A Y_j \: dP \ge \int_A Y_i \: dP$ for all $A \in \mathcal{F}_i$. Let then $A \in \mathcal{F}_i$.

$$
\begin{aligned}
\int_A Y_j \: dP
&= \int_A X_j \: dP
\ge \int_A X_i \: dP
= \int_A Y_i \: dP
\: .
\end{aligned}
$$

## Lean

Formalized as [`MeasureTheory.Submartingale.congr`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.congr).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 131](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L131)
