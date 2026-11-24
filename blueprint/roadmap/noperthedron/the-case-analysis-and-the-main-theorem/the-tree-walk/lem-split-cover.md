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

If $2^K X_d \le c_d$ the point lies in the lower half, otherwise in the upper half; the other coordinates are unchanged (or all doubled, when the scale is increased).

## Lean

Formalized as [`Cayley.Pack.split_cover`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.split_cover), [`Cayley.Pack.split_inv`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.split_inv).

## Sources

- [Noperthedron blueprint: chapters/main.tex, line 51](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/main.tex#L51)
