---
declaration: lemma
origin: cited
lean: Cayley.Pack.gapNrm_mono, Cayley.Pack.gapNrmOK_worst, Cayley.Pack.gapNrmOK_box
statement: formalized
proof: formalized
---

# Norm guard

If a gap leaf's box has scale $2^K$ with $K \le 16$ and its direction has $|w_0|, |w_1| \le 1024$, then every polynomial the leaf decodes has coefficient norm below $2^{390}$.

## Depends on

- [packed_bounds](lem-packed-bounds.md)

## Proof

The norm bounds are computed by the same formulas as the polynomials, with each operation acting on norms; this only adds and multiplies, so it is monotone in the magnitudes of the inputs. Every box of the walk has $|c_i| + |h_i| \le 2 \cdot 2^K$ and the vertex coordinates are below $2^{161}$, so the norms are at most those of the worst box (scale $2^{16}$, all centres and radii $2^{17}$), which are below $2^{390}$ by direct computation.

## Lean

Formalized as [`Cayley.Pack.gapNrm_mono`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.gapNrm_mono), [`Cayley.Pack.gapNrmOK_worst`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.gapNrmOK_worst), [`Cayley.Pack.gapNrmOK_box`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.gapNrmOK_box).

## Sources

- [Noperthedron blueprint: chapters/polybounds.tex, line 160](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/polybounds.tex#L160)
