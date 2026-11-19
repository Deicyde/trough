---
declaration: lemma
origin: cited
lean: Metric.coveringNumber_closedEBall_ge
statement: formalized
proof: formalized
---

# internalCoveringNumber_closedBall_ge

$N_\varepsilon^{int}(B_1) \ge \frac{1}{\varepsilon^d}$.

## Depends on

- [Internal covering number](def-internalcoveringnumber.md)

## Proof depends on

- [volume_div_le_internalCoveringNumber](lem-volume-div-le-internalcoveringnumber.md)

## Proof

By Lemma [volume_div_le_internalCoveringNumber](lem-volume-div-le-internalcoveringnumber.md),

$$
\begin{aligned}
N^{int}_\varepsilon(B_1)
&\ge \frac{V(B_1)}{V(B_\varepsilon)}
= \frac{1}{\varepsilon^d}
\: .
\end{aligned}
$$

## Lean

Formalized as [`Metric.coveringNumber_closedEBall_ge`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.coveringNumber_closedEBall_ge).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 248](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L248)
