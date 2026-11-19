---
declaration: theorem
origin: cited
lean: Cayley.Pack.pGapOK_sound
statement: formalized
proof: formalized
---

# gap_leaf_sound

If a gap leaf passes on a box, then no admissible point of the box gives a Rupert pair $(s, s\, Q_j(r))$.

## Depends on

- [gap_leaf](def-gap-leaf.md)
- [Gap core](../the-blow-up/thm-gap-core.md)
- [Coefficient bound](../../lower-bounds-of-polynomials/the-coefficient-bound/thm-coef-bound.md)
- [Bernstein bound](../../lower-bounds-of-polynomials/the-bernstein-bound/thm-bern-bound.md)
- [packed_bounds](../../lower-bounds-of-polynomials/kronecker-packing/lem-packed-bounds.md)
- [Norm guard](../../lower-bounds-of-polynomials/kronecker-packing/lem-norm-guard.md)

## Proof depends on

- [Quick test](lem-quick-test.md)

## Proof

Each test that succeeds gives the corresponding hypothesis of Theorem [Gap core](../the-blow-up/thm-gap-core.md) at every point of the box: the quick test by Lemma [Quick test](lem-quick-test.md), the others by Theorems [Coefficient bound](../../lower-bounds-of-polynomials/the-coefficient-bound/thm-coef-bound.md) and [Bernstein bound](../../lower-bounds-of-polynomials/the-bernstein-bound/thm-bern-bound.md).

## Lean

Formalized as [`Cayley.Pack.pGapOK_sound`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.pGapOK_sound).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 170](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L170)
