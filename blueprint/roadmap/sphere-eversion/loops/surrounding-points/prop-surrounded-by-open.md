---
declaration: proposition
origin: cited
lean: surrounded_of_convexHull
statement: formalized
proof: formalized
---

# surrounded_by_open

If a point $x$ of $E$ lies in the convex hull of an open set $P$, then it is surrounded by some collection of points belonging to $P$.

## Depends on

- [surrounds_points](def-surrounds-points.md)

## Proof depends on

- [Carathéodory's lemma](lem-caratheodory.md)
- [interior_chab](lem-interior-chab.md)
- [int_homothety_cvx](lem-int-homothety-cvx.md)

## Proof

*Proof of Proposition surrounded_by_open.* It follows from [Lemma interior_chab](lem-interior-chab.md) that we need only show that $E$ has an affine basis $b$ of points belonging to $P$ such that $x$ lies in the interior of the convex hull of $b$.

Carathéodory's lemma [Carathéodory's lemma](lem-caratheodory.md) provides affinely independent points $p_0, \dots, p_k$ in $P$ such that $x$ belongs to their convex hull. Since $P$ is open, we may extend $p_i$ to an affine basis

$$
\hat b = \{p_0, \ldots, p_d\},
$$

where all points still belong to $P$. Note that $x$ belongs to the convex hull of $\hat b$.

Now let $c$ be a point in the interior of the convex hull of $\hat b$ (e.g., the centroid) and for each $\epsilon > 0$, consider the homothety

$$
h_{1+\epsilon} \!: E \to E,
$$

which dilates about $c$ by a scale of $1 + \epsilon$.

Since $\hat b$ is finite and contained in $P$, and $P$ is open, there exists $\epsilon > 0$ such that

$$
h_{1+\epsilon} (\hat b) \subseteq P.
$$

We claim the required basis is:

$$
b = h_{1+\epsilon} (\hat b)
$$

for any such $\epsilon$. Indeed, applying [Lemma int_homothety_cvx](lem-int-homothety-cvx.md) to $\operatorname{Conv}(\hat b)$ we see:

$$
\begin{aligned}
x \in \operatorname{Conv}(\hat b) &\subseteq \operatorname{Int} (h_{1+\epsilon} (\operatorname{Conv}(\hat b)))\\
&= \operatorname{Int} (\operatorname{Conv}(h_{1+\epsilon} (\hat b)))
\end{aligned}
$$

as required.

## Lean

Formalized as [`surrounded_of_convexHull`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/surrounded_of_convexHull).

## Sources

- [Sphere eversion blueprint: loops.tex, line 173](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L173)
