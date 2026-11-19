---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.predictablePart_add_one
---

# predictablePart_add_one

For any integer $n \ge 0$, $A_{n+1} = A_n + \mathbb{E}[X_{n+1} - X_n \mid \mathcal{F}_n]$.

## Depends on

- [Predictable part](def-predictablepart.md)

## Proof

Let $n \in \mathbb{N}$. Then

$$
\begin{aligned}
A_{n+1}
& = \sum_{k=0}^n \mathbb{E}[X_{k+1}-X_k \mid \mathcal{F}_k] \\
& = \sum_{k=0}^{n-1} \mathbb{E}[X_{k+1}-X_k \mid \mathcal{F}_k] + \mathbb{E}[X_{n+1}-X_n \mid \mathcal{F}_n] \\
& = A_n + \mathbb{E}[X_{n+1} - X_n \mid \mathcal{F}_n],
\end{aligned}
$$

which concludes the proof.

## Lean

Formalized as [`MeasureTheory.predictablePart_add_one`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.predictablePart_add_one).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 323](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L323)
