---
declaration: theorem
origin: cited
lean: Cayley.Pack.pDomOK_sound, Cayley.Pack.pChartOK_sound, Cayley.Pack.pOrbitOK_sound
statement: formalized
proof: formalized
---

# dom_leaf_sound

If a domain leaf passes on a box, then no admissible point of the box is reduced.

## Depends on

- [dom_leaf](def-dom-leaf.md)
- [Coefficient bound](../../lower-bounds-of-polynomials/the-coefficient-bound/thm-coef-bound.md)
- [packed_bounds](../../lower-bounds-of-polynomials/kronecker-packing/lem-packed-bounds.md)
- [group_approx](../../irrational-data/lem-group-approx.md)

## Proof

The disk and wedge tests are monotonicity arguments on the box. The chart and orbit tests bound polynomials from below with Theorem [Coefficient bound](../../lower-bounds-of-polynomials/the-coefficient-bound/thm-coef-bound.md); for the orbit test, the error of the tabulated rotations is bounded with Lemma [group_approx](../../irrational-data/lem-group-approx.md) and the fact that the entries of a rotation are at most $1$ in absolute value.

## Lean

Formalized as [`Cayley.Pack.pDomOK_sound`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.pDomOK_sound), [`Cayley.Pack.pChartOK_sound`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.pChartOK_sound), [`Cayley.Pack.pOrbitOK_sound`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.pOrbitOK_sound).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 227](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L227)
