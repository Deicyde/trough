---
declaration: lemma
origin: cited
lean: Cayley.cTab_err, Cayley.vertex_approx, Cayley.Pack.vR_err
statement: formalized
proof: formalized
---

# vertex_approx

Every coordinate of every tabulated vertex is within $2^{-60}$ of the corresponding coordinate of the true vertex of $\operatorname{\mathbf{P}}$.

## Depends on

- [trig_table](lem-trig-table.md)
- [noperthedron](../the-noperthedron/definition-of-the-noperthedron/def-noperthedron.md)

## Proof

The points $C_1, C_2, C_3$ are rational and tabulated within $2^{-80}$. A vertex is $\pm R_z(2\pi k/15) C_i$; the error of a product of approximations is bounded by the sum of the errors, since all factors are bounded by $1$.

## Lean

Formalized as [`Cayley.cTab_err`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cTab_err), [`Cayley.vertex_approx`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.vertex_approx), [`Cayley.Pack.vR_err`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.vR_err).

## Sources

- [Noperthedron blueprint: chapters/data.tex, line 52](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/data.tex#L52)
