---
declaration: definition
origin: cited
lean: Cayley.K.KBox, Cayley.K.KBox.pts, Cayley.kpt, Cayley.K.KBox.exists_kpt, Cayley.Pack.Inv
statement: formalized
---

# box

A *box* consists of a chart $j \in \{0, \dots, 4\}$, a face $f \in \{0, \dots, 5\}$ (used only in charts 0 and 4), a scale $K \in \operatorname{\mathbb{N}}$, and integer centres $c_i$ and radii $h_i \ge 0$ for $i = 0, \dots, 4$, with $|c_i| + |h_i| \le 2 \cdot 2^K$. Its *points* are the $X \in \operatorname{\mathbb{R}}^5$ with $|2^K X_i - c_i| \le h_i$ for all $i$. Every point is $X(t)$ for some normalized coordinates $t \in [-1,1]^5$, where $X_i(t) = (c_i + h_i t_i) / 2^K$.

## Depends on

- [faces](../../the-reduction/blowing-up-charts-0-and-4/def-faces.md)

## Lean

Formalized as [`Cayley.K.KBox`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.KBox), [`Cayley.K.KBox.pts`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.KBox.pts), [`Cayley.kpt`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.kpt), [`Cayley.K.KBox.exists_kpt`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.KBox.exists_kpt), [`Cayley.Pack.Inv`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Inv).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 6](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/certificates.tex#L6)
