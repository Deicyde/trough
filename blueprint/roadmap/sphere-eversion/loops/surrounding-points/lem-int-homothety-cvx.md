---
declaration: lemma
origin: cited
lean: Convex.subset_interior_image_homothety_of_one_lt
statement: formalized
proof: formalized
---

# int_homothety_cvx

Given a point $c$ of $E$ and a real number $t$, let:

$$
h^c_t \!: E \to E
$$

be the homothety which dilates about $c$ by a scale of $t$.

Suppose $c$ belongs to the interior of a convex subset $C$ of $E$ and $t > 1$, then

$$
C \subseteq \operatorname{Int}(h^c_t(C))
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $h^c_t$ is a homeomorphism with inverse $h^c_{t^{-1}}$, taking $s = t^{-1}$, the required result is equivalent to showing:

$$
h^c_s(C) \subseteq \operatorname{Int}(C)
$$

where $s \in (0, 1)$.

Let $x$ be a point of $C$, we must show there exists an open neighborhood $U$ of $h^c_s(x)$, contained in $C$. In fact we claim:

$$
U = h^x_{1-s}(\operatorname{Int}(C))
$$

is such a set. Indeed $U$ is open since $h^x_{1-s}$ is a homeomorphism and $U$ contains $h^c_s(x)$ since:

$$
h^c_s(x) = h^x_{1-s}(c) \in h^x_{1-s}(\operatorname{Int}(C))
$$

since $c$ belongs to $\operatorname{Int}(C)$. Finally:

$$
h^x_{1-s}(\operatorname{Int}(C)) \subseteq h^x_{1-s}(C) \subseteq C
$$

where the second inclusion follows since $C$ is convex and contains $x$.

## Lean

Formalized as [`Convex.subset_interior_image_homothety_of_one_lt`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/Convex.subset_interior_image_homothety_of_one_lt).

## Sources

- [Sphere eversion blueprint: loops.tex, line 253](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L253)
