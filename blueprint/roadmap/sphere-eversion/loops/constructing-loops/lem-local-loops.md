---
declaration: lemma
origin: cited
lean: local_loops
statement: formalized
proof: formalized
---

# local_loops

Assume $Ω$ is open over some neighborhood of $x_0$. If $g(x_0)$ is in the convex hull of the connected component of $Ω_{x_0}$ containing $β(x_0)$, then there is a continuous family of loops defined near $x_0$, based at $β$, taking value in $Ω$ and surrounding $g$.

## Depends on

- [family_surrounds](def-family-surrounds.md)

## Proof depends on

- [loop_of_hull](lem-loop-of-hull.md)
- [smooth_barycentric_coord](../surrounding-points/lem-smooth-barycentric-coord.md)

## Proof

In this proof we don't mention the $t$ parameter since it plays no role, but it is still there. [Lemma loop_of_hull](lem-loop-of-hull.md) gives a loop $γ$ based at $β(x_0)$, taking values in $Ω_{x_0}$ and surrounding $g(x_0)$. We set $γ_x(s) = β(x) + (γ(s) - β(x_0))$. Each $γ_x$ takes values in $Ω_x$ because $Ω$ is open over some neighborhood of $x_0$. [Lemma smooth_barycentric_coord](../surrounding-points/lem-smooth-barycentric-coord.md) guarantees that this loop surrounds $g(x)$ for $x$ close enough to $x_0$.

## Lean

Formalized as [`local_loops`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/local_loops).

## Sources

- [Sphere eversion blueprint: loops.tex, line 434](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L434)
