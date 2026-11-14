---
declaration: lemma
origin: cited
lean: convexHull_eq_union
statement: formalized
proof: formalized
---

# Carathéodory's lemma

If a point $x$ of $E$ lies in the convex hull of a set $P$, then $x$ belongs to the convex hull of a finite set of affinely independent points of $P$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By assumption, there is a finite set of points $t_i$ in $P$ and weights $f_i$ such that $x = \sum f_i t_i$, each $f_i$ is non-negative and $\sum f_i = 1$. Choose such a set of points of minimum cardinality. We argue by contradiction that such a set must be affinely independent.

Thus suppose that there is some vanishing combination $\sum g_i t_i$ with $\sum g_i = 0$ and not all $g_i$ vanish. Let $S = \{i | g_i > 0\}$. Let $i_0$ in $S$ be an index minimizing $f_i/g_i$. We shall obtain our contradiction by showing that $x$ belongs to the convex hull of the set $\{t_i| i \ne i_0\}$, which has cardinality strictly smaller than $\{t_i\}$.

We thus define new weights $k_i = f_i - g_i f_{i_0}/g_{i_0}$. These weights sum to $\sum f_i - (\sum g_i)f_{i_0}/g_{i_0} = 1$ and $k_{i_0} = 0$. Each $k_i$ is non-negative, thanks to the choice of $i_0$ if $i$ is in $S$ or using that $f_i$, $-g_i$ and $f_{i_0}/g_{i_0}$ are all non-negative when $i$ is not in $S$. It remain to compute

$$
\begin{aligned}
\sum_{i ≠ i_0} k_i t_i &= \sum_i k_i t_i \\
&= \sum_i (f_i - g_i f_{i_0}/g_{i_0}) t_i  \\
&= \sum_i f_i t_i - \left(\sum_i g_i t_i\right)f_{i_0}/g_{i_0})   \\
&= x
\end{aligned}
$$

where we use $k_{i_0} = 0$ in the first equality.

## Lean

Formalized as [`convexHull_eq_union`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/convexHull_eq_union).

## Sources

- [Sphere eversion blueprint: loops.tex, line 184](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L184)
