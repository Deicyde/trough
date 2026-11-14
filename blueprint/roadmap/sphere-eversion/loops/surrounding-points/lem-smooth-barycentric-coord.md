---
declaration: lemma
origin: cited
lean: smooth_surrounding
statement: formalized
proof: formalized
---

# smooth_barycentric_coord

For every $x$ in $E$ and every collection of points $p ∈ E^{d+1}$ surrounding $x$, there is a function $w \!: E × E^{d+1} → ℝ^{d+1}$ such that, for every $(y, q)$ in a neighborhood of $(x, p)$,

- $w$ is smooth at $(y, q)$
- $w(y, q) > 0$
- $\sum_{i=0}^d w_i(y, q) = 1$
- $y = \sum_{i=0}^d w_i(y, q)q_i$.

## Depends on

- [surrounds_points](def-surrounds-points.md)

## Proof

Let:

$$
\begin{aligned}
A = E \times \{ q \in E^{d+1} ~|~ \mbox{$q$ is an affine basis for $E$} \},
\end{aligned}
$$

and define:

$$
\begin{aligned}
w \!: A &\to ℝ^{d+1}\\
(y, q) &\mapsto \mbox{barycentric coordinates of $y$ with respect to $q$}.
\end{aligned}
$$

If we fix an affine basis $b$ of $E$, we may express $w$ as a ratio of determinants in terms of coordinates relative to $b$. More precisely, by Cramer's rule, if $0 \le i \le d$ and $w_i$ is the $i^{\rm th}$ component of $w$, then:

$$
\begin{aligned}
w_i (y, q) = \det M_i (y, q) / \det N (q)
\end{aligned}
$$

where $N(q)$ is the $(d+1)\times (d+1)$ matrix whose columns are the barycentric coordinates of the components of $q$ relative to $b$, and $M_i (y, q)$ is $N(q)$ except with column $i$ replaced by the barycentric coordinates of $y$ relative to $b$.

Since determinants are smooth functions and $(y, q) \mapsto \det N(q)$ is non-vanishing on $A$, $w$ is smooth on $A$.

Finally define:

$$
\begin{aligned}
U = w^{-1}((0, \infty)^{d+1}),
\end{aligned}
$$

and note that $U$ is open in $A$, since it is the preimage of an open set under the continuous map $w$. In fact since $A$ is open, $U$ is open as a subset of $E \times E^{d+1}$. Note that $(x, p) \in U$ since $p$ surrounds $x$.

We may extend $w$ to $E \times E^{d+1}$ by giving it any values at all outside $A$.

## Lean

Formalized as [`smooth_surrounding`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/smooth_surrounding).

## Sources

- [Sphere eversion blueprint: loops.tex, line 105](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L105)
