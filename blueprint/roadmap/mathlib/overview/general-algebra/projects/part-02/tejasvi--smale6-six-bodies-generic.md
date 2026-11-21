---
declaration: theorem
origin: cited
lean: CC6Full.elim_integral_int, CC6Full.macaulay_transfer, CC6Full.biMacaulay_transfer_poly, CC6Full.Six.d64_poly_of_noZero, CC6Full.goodred, CC6Full.goodred_torus_opt, CC6Full.exists_germ
statement: formalized
proof: formalized
---

# smale6-six-bodies-generic

*Smale's sixth problem for six bodies in the plane: finiteness of central configurations for generic masses, with a proof formalized in Lean*

[tejasvi/smale6-six-bodies-generic](https://github.com/tejasvi/smale6-six-bodies-generic) at commit [84bbcf27](https://github.com/tejasvi/smale6-six-bodies-generic/tree/84bbcf276d029fdf31375c4a21c6a7e136955e51), 2026-10-19.

> Programs and certificates for the paper of the same title by Tejasvi Singh Tomar (ORCID 0000-0003-4668-3639).

*Quoted from [README.md](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/README.md), Apache-2.0.*

## Depends on

- [Polynomial in several indeterminates](../../polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Set](../../../data-structures/sets/set.md)
- [Field](../../field-theory/field.md)
- [Finite set](../../../data-structures/sets/finite-set.md)
- [Ideal of a commutative ring](../../ideals-and-quotients/ideal-of-a-commutative-ring.md)

## Proof depends on

- [Going-up and going-down theorems](../../../../thousand-plus/algebra/13-commutative-algebra/going-up-and-going-down-theorems.md)
- [Nullstellensatz](../../../geometry/algebraic-geometry/nullstellensatz.md)
- [Transcendental elements](../../../../undergraduate/ring-theory/field-theory/transcendental-elements.md)
- [First isomorphism theorem for commutative rings](../../ideals-and-quotients/first-isomorphism-theorem-for-commutative-rings.md)
- [Algebraic elements](../../../../undergraduate/ring-theory/field-theory/algebraic-elements.md)
- [Field of fractions of an integral domain](../../field-theory/field-of-fractions-of-an-integral-domain.md)
- [Subring](../../rings/subring.md)
- [Generating sets](../../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`CC6Full.elim_integral_int`](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/lean/full/CC6Full/Algebra/Elim.lean#L331) (theorem)
- [`CC6Full.macaulay_transfer`](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/lean/full/CC6Full/Algebra/Macaulay.lean#L348) (theorem)
- [`CC6Full.biMacaulay_transfer_poly`](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/lean/full/CC6Full/Algebra/MacaulayBi.lean#L707) (theorem)
- [`CC6Full.Six.d64_poly_of_noZero`](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/lean/full/CC6Full/Six/D64NoZero.lean#L281) (theorem)
- [`CC6Full.goodred`](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/lean/full/CC6Full/Algebra/GoodRed.lean#L480) (theorem)
- [`CC6Full.goodred_torus_opt`](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/lean/full/CC6Full/Algebra/GoodRedTorus.lean#L192) (theorem)
- [`CC6Full.exists_germ`](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/lean/full/CC6Full/Curve/GermOfPlace.lean#L402) (theorem)

No file its headlines import, directly or not (39 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc3, Mathlib at [c55e6e78](https://github.com/leanprover-community/mathlib4/tree/c55e6e786f49471c72fbddbec5415808896aec1e).
- 5,586 .lean files; its Lean libraries `CC6Full` hold 66, declaring 1,744 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/tejasvi/smale6-six-bodies-generic/blob/84bbcf276d029fdf31375c4a21c6a7e136955e51/LICENSE)).

## Builds on

- Mathlib, at [c55e6e78](https://github.com/leanprover-community/mathlib4/tree/c55e6e786f49471c72fbddbec5415808896aec1e).

## Placement

3 of the 5 Mathlib concepts its headline statements name are in General algebra.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (80 of 102 imports, 2.2×). *Proof depends on* lists 8 of the 33 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [tejasvi/smale6-six-bodies-generic at 84bbcf27](https://github.com/tejasvi/smale6-six-bodies-generic/tree/84bbcf276d029fdf31375c4a21c6a7e136955e51)
