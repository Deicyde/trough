---
declaration: lemma
origin: cited
lean: Metric.le_measure_of_isSeparated
statement: formalized
proof: formalized
---

# le_volume_of_isSeparated

Let $A \subseteq E$ and let $S \subseteq A$ be an $\varepsilon$-separated set. Then $\vert S \vert V(B_{\varepsilon/2}) \le V(A + B_{\varepsilon/2})$.

## Depends on

- [Separated set](def-isseparated.md)

## Proof

Since $S$ is $\varepsilon$-separated, the closed balls $B_{\varepsilon/2}(s)$ for $s \in S$ are pairwise disjoint. Furthermore, these balls are contained in $A + B_{\varepsilon/2}$. Thus, we have

$$
\begin{aligned}
\vert S \vert V(B_{\varepsilon/2})
&= \sum_{s \in S} V(B_{\varepsilon/2}(s))
= V(\bigcup_{s \in S} B_{\varepsilon/2}(s))
\le V(A + B_{\varepsilon/2})
\: .
\end{aligned}
$$

## Lean

Formalized as [`Metric.le_measure_of_isSeparated`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.le_measure_of_isSeparated).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 187](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L187)
