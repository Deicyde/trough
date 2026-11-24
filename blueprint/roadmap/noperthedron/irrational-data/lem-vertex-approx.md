---
declaration: lemma
origin: cited
lean: Cayley.cTab_err, Cayley.vtxZ, Cayley.vertex_approx, Cayley.Pack.vt_eq, Cayley.Pack.vR_err
statement: formalized
proof: formalized
---

# vertex_approx

Every coordinate of every tabulated vertex is within $2^{-60}$ of the corresponding coordinate of the true vertex of $\operatorname{\mathbf{P}}$.

## Depends on

- [trig_table](lem-trig-table.md)
- [noperthedron](../the-noperthedron/definition-of-the-noperthedron/def-noperthedron.md)

## Proof

The points $C_1, C_2, C_3$ are rational and are rounded to integers $\hat C_i$ over $2^{80}$. The checker's vertex table consists of integers over $2^{160}$, and it is exactly $\pm \hat R_z(2\pi k/15)\, \hat C_i$ computed from the integer tables (checked by evaluation). A vertex is $\pm R_z(2\pi k/15) C_i$; the error of a product of approximations is bounded by the sum of the errors, since all factors are bounded by $1$.

## Lean

Formalized as [`Cayley.cTab_err`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cTab_err), [`Cayley.vtxZ`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.vtxZ), [`Cayley.vertex_approx`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.vertex_approx), [`Cayley.Pack.vt_eq`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.vt_eq), [`Cayley.Pack.vR_err`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.vR_err).

## Sources

- [Noperthedron blueprint: chapters/data.tex, line 52](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/data.tex#L52)
