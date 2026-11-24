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

The outer shadow is the convex hull of the points $\pi(R_o T)$, so it lies in the closed half-plane $\{ z : \langle w, z \rangle \le \langle w, R_i S \rangle \}$. A nonzero linear functional is an open map, so it is strictly less than $\langle w, R_i S \rangle$ on the interior of the outer shadow. The point $\pi(R_i S)$ of the inner shadow is therefore not an interior point of the outer shadow.

## Lean

Formalized as [`Cayley.not_rupPair_of_sep`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.not_rupPair_of_sep).

## Sources

- [Noperthedron blueprint: chapters/prelims.tex, line 75](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/prelims.tex#L75)
