---
declaration: lemma
origin: cited
lean: Metric.measure_le_externalCoveringNumber_mul
statement: formalized
proof: formalized
---

# volume_le_externalCoveringNumber_mul

If $0 < \varepsilon$ then $V(A) \le N^{ext}_\varepsilon(A) V(B_\varepsilon)$.

## Depends on

- [External covering number](def-externalcoveringnumber.md)

## Proof depends on

- [volume_le_of_isCover](lem-volume-le-of-iscover.md)

## Proof

If $A$ has no $\varepsilon$-cover, then $N^{ext}_\varepsilon(A) = \infty$, and because $0 < \varepsilon$, we have that $0 < V(B_\varepsilon)$, so the right-hand side is infinite and the inequality follows.

Otherwise there exists an $\varepsilon$-cover which realizes $N^{ext}_\varepsilon(A)$. We can conclude by Lemma [volume_le_of_isCover](lem-volume-le-of-iscover.md).

## Lean

Formalized as [`Metric.measure_le_externalCoveringNumber_mul`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.measure_le_externalCoveringNumber_mul).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 172](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L172)
