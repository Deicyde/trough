---
declaration: corollary
origin: cited
lean: ProbabilityTheory.integral_iSup_norm_rpow_le
statement: formalized
---

# doob_lp_norm_top

Let $X : \mathbb{R} \rightarrow \Omega\rightarrow E$ be a right-continuous martingale with values in a normed space $E$. For every $T$ and $p>1$ we have

$$
\begin{aligned}
\mathbb{E}\left[ \sup_t \lVert X_t \rVert ^ p \right]
\leq \left(\frac{p}{p-1}\right)^p \sup_t \mathbb{E}[\lVert X_t \rVert ^p]
\: .
\end{aligned}
$$

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Right continuous function](../basic-definitions/part-01/def-rightcontinuous.md)

## Proof depends on

- [Doob's Lp inequality for normed spaces](cor-doob-lp-norm.md)

## Proof

Take limits on both sides in Corollary [Doob's Lp inequality for normed spaces](cor-doob-lp-norm.md).

## Lean

Stated as [`ProbabilityTheory.integral_iSup_norm_rpow_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.integral_iSup_norm_rpow_le); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1456](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1456)
