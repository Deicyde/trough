---
declaration: definition
origin: cited
lean: Cayley.cayleyDenom, Cayley.cayleyNumeratorMatrix, Cayley.cayleyMatrix
statement: formalized
---

# cayley

For $r = (x, y, z) \in \operatorname{\mathbb{R}}^3$ let $D(r) = 1 + x^2 + y^2 + z^2$ and

$$
N(r) = \begin{pmatrix}
1 + x^2 - y^2 - z^2 & 2(xy - z) & 2(xz + y) \\
2(xy + z) & 1 - x^2 + y^2 - z^2 & 2(yz - x) \\
2(xz - y) & 2(yz + x) & 1 - x^2 - y^2 + z^2
\end{pmatrix}.
$$

The *Cayley rotation* of $r$ is $\mathrm{Cay}(r) = N(r) / D(r)$. It is the rotation by the unit quaternion proportional to $(1, x, y, z)$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Cayley.cayleyDenom`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cayleyDenom), [`Cayley.cayleyNumeratorMatrix`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cayleyNumeratorMatrix), [`Cayley.cayleyMatrix`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cayleyMatrix).

## Sources

- [Noperthedron blueprint: chapters/cayley.tex, line 8](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/cayley.tex#L8)
