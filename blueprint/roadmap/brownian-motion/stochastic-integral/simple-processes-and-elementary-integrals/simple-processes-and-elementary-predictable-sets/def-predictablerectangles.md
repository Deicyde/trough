---
declaration: definition
origin: cited
lean: MeasureTheory.Filtration.predictableRectangles
statement: formalized
---

# Predictable rectangles

The class of *predictable rectangles* on $T \times \Omega$ is

$$
\begin{aligned}
\mathcal{R}_T :=
\big\{(s, t] \times F : s, t \in T,\ s < t,\ F \in \mathcal{F}_s\big\}
\cup \big\{\{0\} \times F : F \in \mathcal{F}_0\big\}
\: .
\end{aligned}
$$

## Depends on

- [Filtration](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-filtration.md)

## Lean

Formalized as [`MeasureTheory.Filtration.predictableRectangles`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.predictableRectangles).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 127](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L127)
