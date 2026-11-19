---
declaration: lemma
origin: cited
lean: AffineBasis.interior_convexHull
statement: formalized
proof: formalized
---

# interior_chab

Given an affine basis $b$ of $E$, the interior of the convex hull of $b$ is the set of points with strictly positive barycentric coordinates.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For each $i$, let:

$$
w_i \!: E \to ℝ
$$

be the $i^{\rm th}$ barycentric coordinate with respect to the basis $b$. Since $E$ is finite-dimensional, each $w_i$ is a continuous open map. For such a map, the operation of taking interior commutes with preimage, and so we have:

$$
\begin{aligned}
\operatorname{IntConv}(b) &= \operatorname{Int}\left(\bigcap_i w_i^{-1}([0, \infty))\right)\\
&= \bigcap_i \operatorname{Int}(w_i^{-1}([0, \infty))\\
&= \bigcap_i w_i^{-1}(\operatorname{Int}([0, \infty))\\
&= \bigcap_i w_i^{-1}((0, \infty))
\end{aligned}
$$

as required.

## Lean

Formalized as [`AffineBasis.interior_convexHull`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/AffineBasis.interior_convexHull).

## Sources

- [Sphere eversion blueprint: loops.tex, line 227](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L227)
