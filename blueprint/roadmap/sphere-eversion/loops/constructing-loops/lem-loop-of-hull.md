---
declaration: lemma
origin: cited
lean: surrounding_loop_of_convexHull
statement: formalized
proof: formalized
---

# loop_of_hull

If a vector $v$ is in the convex hull of a connected open subset $O$ then, for every base point $b ∈ O$, there is a continuous family of loops $γ \!: [0, 1] × 𝕊^1 → E, (t, s) ↦ γ^t(s)$ such that, for all $t$ and $s$:

- $γ^t$ is based at $b$
- $γ^0(s) = b$
- $γ^t(s) ∈ O$
- $γ^1$ surrounds $v$

## Depends on

- [surrounds](def-surrounds.md)

## Proof depends on

- [surrounded_by_open](../surrounding-points/prop-surrounded-by-open.md)

## Proof

Since $O$ is open, [Proposition surrounded_by_open](../surrounding-points/prop-surrounded-by-open.md) gives points $p_i$ in $O$ surrounding $x$. Since $O$ is open and connected, it is path connected. Let $λ \!: [0, 1] → Ω_x$ be a continuous path starting at $b$ and going through the points $p_i$. We can concatenate $λ$ and its opposite to get $γ^1$. This is a round-trip loop: it back-tracks when it reaches $λ(1)$ at $s = 1/2$. We then define $γ^t$ as the round-trip that stops at $s = t/2$, stays still until $s = 1-t/2$ and then backtracks.

## Lean

Formalized as [`surrounding_loop_of_convexHull`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/surrounding_loop_of_convexHull).

## Sources

- [Sphere eversion blueprint: loops.tex, line 371](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L371)
