---
declaration: lemma
origin: cited
lean: Cayley.cayleyMatrix_apply_sub, Cayley.num_sub_denom
statement: formalized
proof: formalized
---

# Rodrigues form

For every $S \in \operatorname{\mathbb{R}}^3$,

$$
N(r) S - D(r) S = 2\,\bigl(r \times S + r \times (r \times S)\bigr).
$$

Equivalently $\mathrm{Cay}(r) S - S = \frac{2}{D(r)} \bigl(r \times S + r \times (r \times S)\bigr)$.

## Depends on

- [cayley](def-cayley.md)

## Proof

Expand $N(r) S = (1 - |r|^2) S + 2 r (r \cdot S) + 2 r \times S$ and use $r \times (r \times S) = r (r \cdot S) - |r|^2 S$.

## Lean

Formalized as [`Cayley.cayleyMatrix_apply_sub`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cayleyMatrix_apply_sub), [`Cayley.num_sub_denom`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.num_sub_denom).

## Sources

- [Noperthedron blueprint: chapters/cayley.tex, line 46](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/cayley.tex#L46)
