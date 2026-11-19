---
declaration: corollary
origin: cited
mathlib: true
mathlib_declaration: norm_condExp_le
---

# norm_condExp_le

Let $X : \Omega \to E$ be an integrable random variable with values in a normed space $E$. Then, for any sub-$\sigma$-algebra $\mathcal{G}$, we have

$$
\begin{aligned}
\Vert \mathbb{E}[X \mid \mathcal{G}] \Vert
&\le \mathbb{E}[\Vert X \Vert \mid \mathcal{G}] \quad \text{a.s.}
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Jensen's inequality for the conditional expectation](lem-conditional-jensen.md)

## Lean

Formalized as [`norm_condExp_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/norm_condExp_le).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 168](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L168)
