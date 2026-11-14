---
declaration: lemma
origin: cited
lean: Cayley.eq_Rz_mul_outerRot
statement: formalized
proof: formalized
---

# outer_unique

If $R \in SO(3)$ has the same third row as $s(u, v)$, then $R = R_z(\gamma)\, s(u, v)$ for some $\gamma$.

## Depends on

- [outer_view](lem-outer-view.md)

## Proof

$R\, s(u,v)^T$ fixes $e_z$, so it is a rotation about the $z$-axis.

## Lean

Formalized as [`Cayley.eq_Rz_mul_outerRot`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.eq_Rz_mul_outerRot).

## Sources

- [Noperthedron blueprint: chapters/cayley.tex, line 144](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/cayley.tex#L144)
