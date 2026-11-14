---
declaration: definition
origin: cited
lean: Cayley.Bad, Cayley.PtOK, Cayley.Pack.Covered
statement: formalized
---

# bad

A point $X$ of a box is *bad* if, with $r$ the Cayley vector of $X$ (Definition [faces](../../the-reduction/blowing-up-charts-0-and-4/def-faces.md)), the tuple $(X_0, X_1, j, r)$ is reduced and $\bigl(s(X_0, X_1),\ s(X_0, X_1)\, Q_j(r)\bigr)$ is a Rupert pair. It is *admissible* if $X_0^2 + X_1^2 \le 1$ and $|r_i| \le 2$ for all $i$, and, in charts 0 and 4, also $0 \le \rho \le 2$ and $|s_0|, |s_1| \le 1$. A box is *covered* if none of its admissible points is bad.

## Depends on

- [box](def-box.md)
- [reduced](../../the-reduction/the-reduced-domain/def-reduced.md)

## Lean

Formalized as [`Cayley.Bad`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Bad), [`Cayley.PtOK`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.PtOK), [`Cayley.Pack.Covered`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Covered).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 20](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L20)
