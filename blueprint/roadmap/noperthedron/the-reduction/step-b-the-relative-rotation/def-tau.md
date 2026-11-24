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

- [Noperthedron blueprint: chapters/reduction.tex, line 123](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/reduction.tex#L123)
