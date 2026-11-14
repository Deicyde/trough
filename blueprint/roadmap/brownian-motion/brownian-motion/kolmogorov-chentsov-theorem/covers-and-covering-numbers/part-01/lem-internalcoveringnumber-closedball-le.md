---
declaration: lemma
origin: cited
lean: Metric.coveringNumber_closedEBall_le
statement: formalized
proof: formalized
---

# internalCoveringNumber_closedBall_le

$N_\varepsilon^{int}(B_1) \le \left(\frac{2}{\varepsilon} + 1\right)^d$.

## Depends on

- [Internal covering number](def-internalcoveringnumber.md)

## Proof depends on

- [internalCoveringNumber_le_volume_div](lem-internalcoveringnumber-le-volume-div.md)

## Proof

By Lemma [internalCoveringNumber_le_volume_div](lem-internalcoveringnumber-le-volume-div.md),

$$
\begin{aligned}
N^{int}_\varepsilon(B_1)
&\le \frac{V(B_1 + B_{\varepsilon/2})}{V(B_{\varepsilon/2})}
= \frac{V(B_{1 + \varepsilon/2})}{V(B_{\varepsilon/2})}
= \frac{(1 + \varepsilon/2)^d}{(\varepsilon/2)^d}
\: .
\end{aligned}
$$

## Lean

Formalized as [`Metric.coveringNumber_closedEBall_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.coveringNumber_closedEBall_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 268](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L268)
