---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ConvexOn.map_condExp_le_univ
---

# Jensen's inequality for the conditional expectation

Let $X : \Omega \to E$ be an integrable random variable with values in a normed space $E$ and let $\phi : E \to \mathbb{R}$ be a convex function such that $\phi \circ X$ is integrable. Then, for any sub-$\sigma$-algebra $\mathcal{G}$, we have

$$
\begin{aligned}
\phi\left( \mathbb{E}[X \mid \mathcal{G}] \right)
&\le \mathbb{E}[\phi(X) \mid \mathcal{G}] \quad \text{a.s.}
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Done in a Mathlib PR for finite measures: [\#27953](https://github.com/leanprover-community/mathlib4/pull/27953).

## Lean

Formalized as [`ConvexOn.map_condExp_le_univ`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ConvexOn.map_condExp_le_univ).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 152](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L152)
