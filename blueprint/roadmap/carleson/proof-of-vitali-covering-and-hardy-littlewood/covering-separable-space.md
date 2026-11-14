---
declaration: lemma
origin: cited
lean: Metric.dense_iff_iUnion_ball, TopologicalSpace.exists_countable_dense
statement: formalized
proof: formalized
---

# covering separable space

For each $r > 0$, there exists a countable collection $C(r) \subset X$ of points such that

$$
X \subset \bigcup_{c \in C(r)} B(c, r)\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

It clearly suffices to construct finite collections $C(r,k)$ such that

$$
B(o, r2^k) \subset \bigcup_{c \in C(r,k)} B(c,r)\,,
$$

since then the collection $C(r) = \bigcup_{k \in \mathbb{N}} C(r,k)$ has the desired property.

Suppose that $Y \subset B(o, r2^k)$ is a collection of points such that for all $y, y' \in Y$ with $y \ne y'$, we have $\rho(y,y') \ge r$. Then the balls $B(y, r/2)$ are pairwise disjoint and contained in $B(o, r2^{k+1})$. If $y \in B(o, r)$, then $B(o, r2^{k+1}) \subset B(y, r2^{k+2})$. Thus, by the doubling property [(5)](../introduction/README.md),

$$
\mu(B(y, \frac{r}{2})) \ge 2^{-(k+2)a} \mu(B(o, r2^{k+1}))\,.
$$

Thus, we have

$$
\mu(B(o, r2^{k+1})) \ge \sum_{y \in Y} \mu(B(y, \frac{r}{2})) \ge |Y| 2^{-(k+2)a} \mu(B(o, r2^{k+1}))\,.
$$

We conclude that $|Y| \le 2^{(k+2)a}$. In particular, there exists a set $Y$ of maximal cardinality. Define $C(r,k)$ to be such a set.

If $x \in B(o, r2^k)$ and $x \notin C(r,k)$, then there must exist $y \in C(r,k)$ with $\rho(x,y) < r$. Thus $C(r,k)$ has the desired property.

## Lean

Formalized as [`Metric.dense_iff_iUnion_ball`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Metric.dense_iff_iUnion_ball), [`TopologicalSpace.exists_countable_dense`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TopologicalSpace.exists_countable_dense).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6711](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6711)
