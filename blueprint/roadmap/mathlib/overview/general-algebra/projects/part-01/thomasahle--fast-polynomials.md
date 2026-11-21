---
declaration: theorem
origin: cited
lean: FastPoly.LowerBound.General.no_rationalInverse_general, FastPoly.Char2Finite.monic_evaluation
statement: formalized
proof: formalized
---

# Fast Polynomials

[thomasahle/fast-polynomials](https://github.com/thomasahle/fast-polynomials) at commit [09a36b0e](https://github.com/thomasahle/fast-polynomials/tree/09a36b0e7a6c153462bd43b91d4a3bb7ac886bef), 2026-10-13.

> Evaluate a polynomial of degree *n* with about *n*/2 multiplications instead of Horner's *n*, after a one-time, exact preprocessing of its coefficients.

*Quoted from [README.md](https://github.com/thomasahle/fast-polynomials/blob/09a36b0e7a6c153462bd43b91d4a3bb7ac886bef/README.md), MIT, Copyright (c) 2026 Thomas Ahle.*

## Depends on

- [Ring-valued matrix](../../../linear-algebra/matrices/ring-valued-matrix.md)

## Proof depends on

- [Characteristic p](../../field-theory/characteristic-p.md)
- [Finite](../../../combinatorics/pigeonhole-principles/finite.md)
- [Polynomial in one indeterminate](../../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Lagrange interpolation](../../../../undergraduate/numerical-analysis/approximation-of-numerical-functions/lagrange-interpolation.md)
- [Frobenius morphism](../../field-theory/frobenius-morphism.md)
- [Associative algebra over a commutative ring](../../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-02/the-binomial-theorem.md)
- [Field](../../field-theory/field.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`FastPoly.LowerBound.General.no_rationalInverse_general`](https://github.com/thomasahle/fast-polynomials/blob/09a36b0e7a6c153462bd43b91d4a3bb7ac886bef/FastPoly/LowerBound/General/Main.lean#L134) (theorem)
- [`FastPoly.Char2Finite.monic_evaluation`](https://github.com/thomasahle/fast-polynomials/blob/09a36b0e7a6c153462bd43b91d4a3bb7ac886bef/FastPoly/Examples/Char2Finite.lean#L108) (theorem)

No file its headlines import, directly or not (195 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.27.0-rc1, Mathlib at [16635ad4](https://github.com/leanprover-community/mathlib4/tree/16635ad47947fa897163ee5f3362a2f18f61b6fd).
- 372 .lean files; its Lean libraries `FastPoly` hold 372, declaring 7,090 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/thomasahle/fast-polynomials/blob/09a36b0e7a6c153462bd43b91d4a3bb7ac886bef/LICENSE)).

## Builds on

- Mathlib, at [16635ad4](https://github.com/leanprover-community/mathlib4/tree/16635ad47947fa897163ee5f3362a2f18f61b6fd).

## Placement

Of its imports of Mathlib modules in an overview area, 64 of 90 are in General algebra, 2.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (64 of 90 imports, 2.0×), Linear algebra (10 of 90 imports, 1.9×). *Proof depends on* lists 8 of the 21 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [thomasahle/fast-polynomials at 09a36b0e](https://github.com/thomasahle/fast-polynomials/tree/09a36b0e7a6c153462bd43b91d4a3bb7ac886bef)
