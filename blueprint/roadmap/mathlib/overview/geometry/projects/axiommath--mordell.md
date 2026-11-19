---
declaration: theorem
origin: cited
lean: Faltings.group_fg_of_numberField, LeanEval.AlgebraicGeometry.Faltings.faltings, LeanEval.AlgebraicGeometry.Faltings.finite_setOf_place_notMem, Faltings.LeanEval.genus_eq
statement: formalized
proof: formalized
---

# The Mordell Conjecture in Lean

[AxiomMath/Mordell](https://github.com/AxiomMath/Mordell) at commit [82a30cb7](https://github.com/AxiomMath/Mordell/tree/82a30cb7857f6e3cfdb1be91f5533c0ccb57d493), 2026-11-11.

> A Lean 4 (v4.35.0) formalization of Faltings' theorem, the Mordell conjecture, following the proof of E. Bombieri, *The Mordell conjecture revisited* (Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 17 (1990), 615–640), of P. Vojta's theorem (*Siegel's theorem in the compact case*, Ann. of Math. 133 (1991), 509–548), built on [Mathlib](https://github.com/leanprover-community/mathlib4) and on [the Stacks Project in Lean](https://github.com/AxiomMath/Stacks). Lean's kernel checks every proof. There is no `sorry`, no `native_decide` and no added axiom.

*Quoted from [README.md](https://github.com/AxiomMath/Mordell/blob/82a30cb7857f6e3cfdb1be91f5533c0ccb57d493/README.md), Apache-2.0.*

## Depends on

- [33.9 Geometrically integral schemes](../../../../stacks/schemes/33-varieties/part-01/33-9-geometrically-integral-schemes.md)
- [29.42 Proper morphisms](../../../../stacks/schemes/29-morphisms-of-schemes/part-03/29-42-proper-morphisms.md)
- [Field](../../general-algebra/field-theory/field.md)
- [10.18 Local rings](../../../../stacks/preliminaries/part-01/10-commutative-algebra/part-01/10-18-local-rings.md)

## Proof depends on

- [Bézout's identity](../../../undergraduate/ring-theory/divisibility-in-integral-domains/bezouts-identity.md)
- [Algebraic extension](../../general-algebra/field-theory/algebraic-extension.md)
- [Separable polynomial](../../general-algebra/polynomials-and-power-series/separable-polynomial.md)
- [Transcendental elements](../../../undergraduate/ring-theory/field-theory/transcendental-elements.md)
- [Localization](../../general-algebra/rings/localization.md)
- [Krull's principal ideal theorem](../../../thousand-plus/algebra/13-commutative-algebra/krulls-principal-ideal-theorem.md)
- [Infinite](../../combinatorics/pigeonhole-principles/infinite.md)
- [Multilinear map](../../linear-algebra/fundamentals/multilinear-map.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Faltings.group_fg_of_numberField`](https://github.com/AxiomMath/Mordell/blob/82a30cb7857f6e3cfdb1be91f5533c0ccb57d493/Mordell/MordellWeil/Main.lean#L167) (theorem)
- [`LeanEval.AlgebraicGeometry.Faltings.faltings`](https://github.com/AxiomMath/Mordell/blob/82a30cb7857f6e3cfdb1be91f5533c0ccb57d493/Mordell/LeanEval/Faltings.lean#L297) (theorem)
- [`LeanEval.AlgebraicGeometry.Faltings.finite_setOf_place_notMem`](https://github.com/AxiomMath/Mordell/blob/82a30cb7857f6e3cfdb1be91f5533c0ccb57d493/Mordell/LeanEval/Faltings.lean#L124) (theorem)
- [`Faltings.LeanEval.genus_eq`](https://github.com/AxiomMath/Mordell/blob/82a30cb7857f6e3cfdb1be91f5533c0ccb57d493/Mordell/LeanEval/Faltings.lean#L273) (theorem)

No file its headlines import, directly or not (382 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 432 .lean files; its Lean libraries `Mordell` hold 432, declaring 1,449 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/Mordell/blob/82a30cb7857f6e3cfdb1be91f5533c0ccb57d493/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `Stacks` (https://github.com/AxiomMath/Stacks) at `c496df0d`.

## Placement

Of its imports of Mathlib modules in an overview area, 5 of 27 are in Geometry, 7.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (5 of 27 imports, 7.8×), Linear algebra (3 of 27 imports, 1.9×), General algebra (11 of 27 imports, 1.1×). *Proof depends on* lists 8 of the 107 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [AxiomMath/Mordell at 82a30cb7](https://github.com/AxiomMath/Mordell/tree/82a30cb7857f6e3cfdb1be91f5533c0ccb57d493)
