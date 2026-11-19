---
declaration: theorem
origin: cited
lean: Cayley.not_rupPair_of_sep
statement: formalized
proof: formalized
---

# Separation criterion

Let $S$ be a vertex of $\operatorname{\mathbf{P}}$ and $w \ne 0$. If

$$
\langle w, R_o T \rangle \le \langle w, R_i S \rangle
$$

for every vertex $T$ of $\operatorname{\mathbf{P}}$, then $(R_o, R_i)$ is not a Rupert pair.

## Depends on

- [shadow](def-shadow.md)

## Proof

The outer shadow is the convex hull of the points $\pi(R_o T)$, so it lies in the closed half-plane $\{ z : \langle w, z \rangle \le \langle w, R_i S \rangle \}$. The point $\pi(R_i S)$ of the inner shadow lies on the boundary line of this half-plane, so it is not an interior point of the outer shadow.

## Lean

Formalized as [`Cayley.not_rupPair_of_sep`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.not_rupPair_of_sep).

## Sources

- [Noperthedron blueprint: chapters/prelims.tex, line 91](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/prelims.tex#L91)
