---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.predictablePart
---

# Predictable part

Let $X : \mathbb{N} \to \Omega \to E$ be a process indexed by $\mathbb{N}$, for $E$ a Banach space. Let $(\mathcal{F}_n)_{n\in\mathbb{N}}$ be a filtration on $\Omega$. The predictable part of $X$ is the process $A : \mathbb{N} \to \Omega \to E$ defined for $n \ge 0$ by

$$
A_n = \sum_{k=0}^{n-1} \mathbb{E}[X_{k+1}-X_k \mid \mathcal{F}_k].
$$

## Depends on

- [Filtration](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-filtration.md)

## Lean

Formalized as [`MeasureTheory.predictablePart`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.predictablePart).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 274](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L274)
