---
declaration: theorem
origin: cited
lean: HJO.finiteSeries_eq_qPochhammer_mul_boundedGF, HJO.conjecture_of_one_lt_of_lt, HJO.conjecture_of_le, HJO.conjecture
statement: formalized
proof: formalized
---

# Rogers-Ramanujan Identities from the Geometry of X^a=Y^b

[AxiomMath/HJO](https://github.com/AxiomMath/HJO) at commit [6a58dfa6](https://github.com/AxiomMath/HJO/tree/6a58dfa6ab98bd35d841cb2cf8fd9081f62fad03), 2026-10-07.

> This is a Lean formalization of the Huang–Jiang–Oblomkov conjecture on the point counts of pairs of commuting nilpotent matrices satisfying `A^a = B^b`.

*Quoted from [README.md](https://github.com/AxiomMath/HJO/blob/6a58dfa6ab98bd35d841cb2cf8fd9081f62fad03/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Free algebra of a commutative ring](../../algebras-over-a-ring/free-algebra-of-a-commutative-ring.md)
- [Invertible elements](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Newton's identities](../../../../undergraduate/ring-theory/polynomial-rings/newtons-identities.md)
- [Field of fractions of an integral domain](../../field-theory/field-of-fractions-of-an-integral-domain.md)
- [Power series](../../polynomials-and-power-series/power-series.md)
- [Associative algebra over a commutative ring](../../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Polynomial in several indeterminates](../../polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Direct sum](../../../../undergraduate/linear-algebra/fundamentals/direct-sum.md)

## Main results

Its Lean names are the theorems of its top-level module named Main, MainTheorem(s) or Statement(s):

- [`HJO.finiteSeries_eq_qPochhammer_mul_boundedGF`](https://github.com/AxiomMath/HJO/blob/6a58dfa6ab98bd35d841cb2cf8fd9081f62fad03/HJO/Main.lean#L46) (theorem)
- [`HJO.conjecture_of_one_lt_of_lt`](https://github.com/AxiomMath/HJO/blob/6a58dfa6ab98bd35d841cb2cf8fd9081f62fad03/HJO/Main.lean#L53) (theorem)
- [`HJO.conjecture_of_le`](https://github.com/AxiomMath/HJO/blob/6a58dfa6ab98bd35d841cb2cf8fd9081f62fad03/HJO/Main.lean#L59) (theorem)
- [`HJO.conjecture`](https://github.com/AxiomMath/HJO/blob/6a58dfa6ab98bd35d841cb2cf8fd9081f62fad03/HJO/Main.lean#L74) (theorem)

No file its headlines import, directly or not (720 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.0-rc1, Mathlib at [de5ce8a9](https://github.com/leanprover-community/mathlib4/tree/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11).
- 860 .lean files; its Lean libraries `HJO`, `Challenge`, `Solution` hold 860, declaring 15,231 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/HJO/blob/6a58dfa6ab98bd35d841cb2cf8fd9081f62fad03/LICENSE)).

## Builds on

- Mathlib, at [de5ce8a9](https://github.com/leanprover-community/mathlib4/tree/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11).
- `QSeriesLib` (https://github.com/AxiomMath/QSeriesLib.git) at `17dee126`.

## Placement

Of its imports of Mathlib modules in an overview area, 174 of 271 are in General algebra, 1.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (174 of 271 imports, 1.8×), Data structures (39 of 271 imports, 1.0×). *Proof depends on* names 8 of the 52 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/HJO at 6a58dfa6](https://github.com/AxiomMath/HJO/tree/6a58dfa6ab98bd35d841cb2cf8fd9081f62fad03)
