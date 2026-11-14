---
declaration: definition
origin: cited
lean: Cayley.tauR
statement: formalized
---

# tau

Let $(x, y)$ be the first two coordinates of $C_3$. The matrix

$$
\tau = \begin{pmatrix}
-\frac{x^2 - y^2}{x^2 + y^2} & -\frac{2xy}{x^2 + y^2} & 0 \\
-\frac{2xy}{x^2 + y^2} & \frac{x^2 - y^2}{x^2 + y^2} & 0 \\
0 & 0 & -1
\end{pmatrix}
$$

is minus the reflection in the vertical plane through $C_3$; it is a half-turn about a horizontal axis, and it has rational entries.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Cayley.tauR`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.tauR).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 108](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L108)
