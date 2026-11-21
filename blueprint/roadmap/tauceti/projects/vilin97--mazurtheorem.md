---
declaration: module
origin: cited
lean: EllipticCurves, MazurTorsion
statement: formalized
---

# Mazur Theorem

[Vilin97/MazurTheorem](https://github.com/Vilin97/MazurTheorem) at commit [9327963d](https://github.com/Vilin97/MazurTheorem/tree/9327963d4ec14fba49c7b14b004fd00707ffc2e9), 2026-09-06.

> **A public Lean 4 formalization of the classification of rational torsion on elliptic curves.**

*Quoted from [README.md](https://github.com/Vilin97/MazurTheorem/blob/9327963d4ec14fba49c7b14b004fd00707ffc2e9/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Rational root theorem](../../mathlib/thousand-plus/algebra/12-field-theory-and-polynomials/rational-root-theorem.md)
- [Structure of finitely generated abelian groups](../../mathlib/overview/general-algebra/group-theory/part-02/structure-of-finitely-generated-abelian-groups.md)
- [Greatest common divisor](../../mathlib/overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Natural transformation](../../mathlib/overview/general-algebra/category-theory/natural-transformation.md)
- [Polynomial in one indeterminate](../../mathlib/overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Rupture field](../../mathlib/overview/general-algebra/field-theory/rupture-field.md)
- [Separable polynomial](../../mathlib/overview/general-algebra/polynomials-and-power-series/separable-polynomial.md)
- [Field of fractions of an integral domain](../../mathlib/overview/general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`EllipticCurves`](https://github.com/Vilin97/MazurTheorem/blob/9327963d4ec14fba49c7b14b004fd00707ffc2e9/EllipticCurves.lean), [`MazurTorsion`](https://github.com/Vilin97/MazurTheorem/blob/9327963d4ec14fba49c7b14b004fd00707ffc2e9/MazurTorsion.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Challenge/CyclotomicClassFieldTheory.lean`, `Challenge/DivisorLineBundle.lean`, `Challenge/OrderThirtyFive.lean`, `Challenge/OrderTwentyFive.lean`, `Challenge/XOneElevenCoset.lean`, `Challenge/XOneThirteenNoncusp.lean` hold `sorry` or `admit`.

## Project

- Lean v4.33.0-rc1, Mathlib at [79d0395a](https://github.com/leanprover-community/mathlib4/tree/79d0395a1825a6264ad5d269e35e60537518955e).
- 2,080 .lean files; its Lean libraries `MazurTorsion`, `EllipticCurves`, `Challenge` hold 2,064, declaring 52,151 names, with `sorry` in 6 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE](https://github.com/Vilin97/MazurTheorem/blob/9327963d4ec14fba49c7b14b004fd00707ffc2e9/LICENSE)).

## Builds on

- Mathlib, at [79d0395a](https://github.com/leanprover-community/mathlib4/tree/79d0395a1825a6264ad5d269e35e60537518955e).
- [TauCeti](../README.md) at `a74dfee7`, a GitHub fork of TauCetiProject/TauCeti.

## Placement

Its Lake manifest requires `TauCeti`, a GitHub fork of TauCetiProject/TauCeti, whose modules 25 files of the project import.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (193 of 747 imports, 11.0×), General algebra (429 of 747 imports, 1.6×). *Proof depends on* lists 8 of the 104 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [Vilin97/MazurTheorem at 9327963d](https://github.com/Vilin97/MazurTheorem/tree/9327963d4ec14fba49c7b14b004fd00707ffc2e9)
