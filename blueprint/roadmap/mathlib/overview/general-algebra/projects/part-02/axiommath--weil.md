---
declaration: theorem
origin: cited
lean: Weil.exists_map_int_eq_rationalFrobeniusCharpolyReverse, Weil.exists_map_int_eq_rationalFrobeniusCharpolyReverse_and, AlgebraicGeometry.Scheme.finiteDimensional_complexCohomology, Weil.natDegree_rationalFrobeniusCharpolyReverse, LeanEval.AlgebraicGeometry.WeilConjectures.weil_conjectures
statement: formalized
proof: formalized
---

# The Weil Conjectures in Lean

[AxiomMath/Weil](https://github.com/AxiomMath/Weil) at commit [27cdb204](https://github.com/AxiomMath/Weil/tree/27cdb2049be62ee2911429b47f54774078450e32), 2026-11-06.

> A Lean 4 (v4.34.0-rc2) formalization of the proof of the Weil conjectures, following E. Freitag and R. Kiehl, *Étale Cohomology and the Weil Conjecture* (Ergebnisse der Mathematik 13, Springer, 1988), built on [Mathlib](https://github.com/leanprover-community/mathlib4) and on [the Stacks Project in Lean](https://github.com/AxiomMath/Stacks). All four Weil conjectures are proved: rationality, the functional equation, the Riemann hypothesis (Deligne's theorem) and the Betti-number statement. Lean's kernel checks every proof. There is no `sorry`, no `native_decide` and no added axiom.

*Quoted from [README.md](https://github.com/AxiomMath/Weil/blob/27cdb2049be62ee2911429b47f54774078450e32/README.md), Apache-2.0.*

## Depends on

- [29.35 Smooth morphisms](../../../../../stacks/schemes/29-morphisms-of-schemes/part-02/29-35-smooth-morphisms.md)
- [Polynomial in one indeterminate](../../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Characteristic of a ring](../../field-theory/characteristic-of-a-ring.md)
- [29.44 Projective morphisms](../../../../../stacks/schemes/29-morphisms-of-schemes/part-03/29-44-projective-morphisms.md)
- [Scheme](../../../geometry/algebraic-geometry/scheme.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [9.7 Finite extensions](../../../../../stacks/preliminaries/part-01/9-fields/part-01/9-7-finite-extensions.md)
- [Associative algebra over a commutative ring](../../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [33.8 Geometrically irreducible schemes](../../../../../stacks/schemes/33-varieties/part-01/33-8-geometrically-irreducible-schemes.md)
- [28.3 Integral, irreducible, and reduced schemes](../../../../../stacks/schemes/28-properties-of-schemes/part-01/28-3-integral-irreducible-and-reduced-schemes.md)
- [29.42 Proper morphisms](../../../../../stacks/schemes/29-morphisms-of-schemes/part-03/29-42-proper-morphisms.md)
- [Field](../../field-theory/field.md)
- [Multiset](../../../data-structures/sets/multiset.md)

## Proof depends on

- [Tensor algebra of a commutative ring](../../algebras-over-a-ring/tensor-algebra-of-a-commutative-ring.md)
- [Connected components](../../../../undergraduate/topology/topology-and-metric-spaces/connected-components.md)
- [Adjunction](../../category-theory/adjunction.md)
- [Natural transformation](../../category-theory/natural-transformation.md)
- [Noetherian module](../../../linear-algebra/fundamentals/noetherian-module.md)
- [Abelian category](../../category-theory/abelian-category.md)
- [Yoneda embedding](../../category-theory/yoneda-embedding.md)
- [Holomorphic stability under uniform convergence](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-stability-under-uniform-convergence.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Weil.exists_map_int_eq_rationalFrobeniusCharpolyReverse`](https://github.com/AxiomMath/Weil/blob/27cdb2049be62ee2911429b47f54774078450e32/Weil/AlgebraicGeometry/EtaleCohomology/Trace/CharpolyIntegrality.lean#L222) (theorem)
- [`Weil.exists_map_int_eq_rationalFrobeniusCharpolyReverse_and`](https://github.com/AxiomMath/Weil/blob/27cdb2049be62ee2911429b47f54774078450e32/Weil/AlgebraicGeometry/EtaleCohomology/Trace/CharpolyIntegrality.lean#L260) (theorem)
- [`AlgebraicGeometry.Scheme.finiteDimensional_complexCohomology`](https://github.com/AxiomMath/Weil/blob/27cdb2049be62ee2911429b47f54774078450e32/Weil/AlgebraicGeometry/EtaleCohomology/Trace/BettiNumber.lean#L68) (theorem)
- [`Weil.natDegree_rationalFrobeniusCharpolyReverse`](https://github.com/AxiomMath/Weil/blob/27cdb2049be62ee2911429b47f54774078450e32/Weil/AlgebraicGeometry/EtaleCohomology/Trace/CharpolyDegree.lean#L67) (theorem)
- [`LeanEval.AlgebraicGeometry.WeilConjectures.weil_conjectures`](https://github.com/AxiomMath/Weil/blob/27cdb2049be62ee2911429b47f54774078450e32/Weil/LeanEval/WeilConjectures.lean#L185) (theorem)

No file its headlines import, directly or not (173 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.0-rc2, Mathlib at [16edf57d](https://github.com/leanprover-community/mathlib4/tree/16edf57de7933555826307a3d81b4391a3657a09).
- 980 .lean files; its Lean libraries `Weil` hold 980, declaring 9,840 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/Weil/blob/27cdb2049be62ee2911429b47f54774078450e32/LICENSE)).

## Builds on

- Mathlib, at [16edf57d](https://github.com/leanprover-community/mathlib4/tree/16edf57de7933555826307a3d81b4391a3657a09).
- `Stacks` (https://github.com/AxiomMath/Stacks) at `012108f6`.

## Placement

4 of the 7 Mathlib concepts its headline statements name are in General algebra.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (172 of 1040 imports, 7.0×), General algebra (677 of 1040 imports, 1.8×). *Proof depends on* names 8 of the 134 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/Weil at 27cdb204](https://github.com/AxiomMath/Weil/tree/27cdb2049be62ee2911429b47f54774078450e32)
