---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.leastGE
---

# leastGE

Let $T$ be a conditionally complete linear order with a bottom element and let $R$ be a preorder. For a process $X : T \to Ω \to R$ and $a \in R$, define the random time

$$
\begin{aligned}
\tau_{X \ge a} = \inf\{t \in T \mid X_t \ge a\} \: ,
\end{aligned}
$$

in which the infimum is infinite if the set is empty.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MeasureTheory.leastGE`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.leastGE).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 752](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L752)
