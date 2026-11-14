---
declaration: lemma
origin: cited
lean: Metric.measure_le_of_isCover
statement: formalized
proof: formalized
---

# volume_le_of_isCover

Let $A \subseteq E$ and $C \subseteq E$ be a finite $\varepsilon$-cover of $A$. Then $V(A) \le \vert C \vert V(B_\varepsilon)$, in which $B_\varepsilon$ is the closed ball of radius $\varepsilon$ in $E$.

## Depends on

- [$\varepsilon$-cover](def-iscover.md)

## Proof

Since $C$ is a cover of $A$, $A$ is a subset of the union of the closed balls $B_\varepsilon(c)$ for $c \in C$. Then

$$
\begin{aligned}
V(A) \le V(\bigcup_{c \in C} B_\varepsilon(c))
&\le \sum_{c \in C} V(B_\varepsilon(c))
= \vert C \vert V(B_\varepsilon)
\: .
\end{aligned}
$$

## Lean

Formalized as [`Metric.measure_le_of_isCover`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.measure_le_of_isCover).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 151](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L151)
