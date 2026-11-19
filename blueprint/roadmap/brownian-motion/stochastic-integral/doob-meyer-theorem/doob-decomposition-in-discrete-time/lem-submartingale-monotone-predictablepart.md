---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Submartingale.monotone_predictablePart
---

# Submartingale.monotone_predictablePart

The predictable part of a real-valued submartingale is an almost surely nondecreasing process.

## Depends on

- [Predictable part](def-predictablepart.md)
- [Submartingale](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-submartingale.md)

## Proof depends on

- [condExp_sub_nonneg](../../filtrations-processes-and-martingales/basic-definitions/part-01/lem-condexp-sub-nonneg.md)
- [predictablePart_add_one](lem-predictablepart-add-one.md)

## Proof

Let $X$ be a submartingale and let $A$ be its predictable part. Then for all $n \geq 0$, from Lemma [condExp_sub_nonneg](../../filtrations-processes-and-martingales/basic-definitions/part-01/lem-condexp-sub-nonneg.md) we have that almost surely

$$
\begin{aligned}
A_{n+1} &= A_n + \mathbb{E}\left[ X_{n+1} - X_n | \mathcal{F}_n \right]
\ge A_n
\: .
\end{aligned}
$$

The first equality comes from Lemma [predictablePart_add_one](lem-predictablepart-add-one.md). As $\mathbb{N}$ is countable, we deduce that almost surely, for all $n \in \mathbb{N}$, $A_{n+1} \ge A_n$. Thus, $(A_n)_{n \in \mathbb{N}}$ is almost surely nondecreasing.

## Lean

Formalized as [`MeasureTheory.Submartingale.monotone_predictablePart`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.monotone_predictablePart).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 504](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L504)
