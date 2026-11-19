---
declaration: lemma
origin: cited
lean: Metric.IsCover.edist_nearestPt_le
statement: formalized
proof: formalized
---

# dist_nearestPt_of_isCover

Let $C_\varepsilon$ be a finite $\varepsilon$-cover of $A \subseteq E$ (assuming such a finite cover exists). Then for all $x \in A$, $d_E(x, \pi(x, C_\varepsilon)) \le \varepsilon$.

## Depends on

- [nearestPt](def-nearestpt.md)
- [$\varepsilon$-cover](../../covers-and-covering-numbers/part-01/def-iscover.md)

## Lean

Formalized as [`Metric.IsCover.edist_nearestPt_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.IsCover.edist_nearestPt_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 370](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L370)
