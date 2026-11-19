---
declaration: lemma
origin: cited
lean: Cayley.Pack.split_cover, Cayley.Pack.split_inv
statement: formalized
proof: formalized
---

# split_cover

Every point of a box is a point of one of its two halves.

## Depends on

- [kcheck](def-kcheck.md)

## Proof

If $t_d \le 0$ the point is the point of the lower half at $2 t_d + 1$, otherwise of the upper half at $2 t_d - 1$.

## Lean

Formalized as [`Cayley.Pack.split_cover`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.split_cover), [`Cayley.Pack.split_inv`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.split_inv).

## Sources

- [Noperthedron blueprint: chapters/main.tex, line 51](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/main.tex#L51)
