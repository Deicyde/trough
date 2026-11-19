---
declaration: definition
origin: cited
lean: Cayley.K.KBox, Cayley.kpt, Cayley.Pack.Inv
statement: formalized
---

# box

A *box* consists of a chart $j \in \{0, \dots, 4\}$, a face $f \in \{0, \dots, 5\}$ (used only in charts 0 and 4), a scale $K \in \operatorname{\mathbb{N}}$, and integer centres $c_i$ and radii $h_i \ge 0$ for $i = 0, \dots, 4$, with $|c_i| + |h_i| \le 2 \cdot 2^K$. The point of the box at normalized coordinates $t \in [-1,1]^5$ is $X(t)$ with $X_i = (c_i + h_i t_i) / 2^K$.

## Depends on

- [faces](../../the-reduction/blowing-up-charts-0-and-4/def-faces.md)

## Lean

Formalized as [`Cayley.K.KBox`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.KBox), [`Cayley.kpt`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.kpt), [`Cayley.Pack.Inv`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Inv).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 6](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L6)
