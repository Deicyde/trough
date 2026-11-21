---
declaration: lemma
origin: cited
lean: MvPowerSeries.isRestricted_abs_iff, MvPolynomial.norm_toRestricted, MvPowerSeries.Restricted.residueRingHom, MvPowerSeries.Restricted.residueEquiv, isAdmissible_coeffVal_of_isRestricted, isNewtonPolygonOf_coeffVal_of_isRestricted, radiusOfConvergence, isRestricted_of_lt_radiusOfConvergence
statement: formalized
proof: formalized
---

# Layout

[WilliamCoram/PhD](https://github.com/WilliamCoram/PhD) at commit [659ce260](https://github.com/WilliamCoram/PhD/tree/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3), 2026-10-14.

> Ongoing PhD project to formalise quaternionic modular forms and results on the slopes of compact Hecke operators.

*Quoted from [README.md](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/README.md), Apache-2.0.*

## Depends on

- [Polynomial in several indeterminates](../../polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Ideal of a commutative ring](../../ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Set](../../../data-structures/sets/set.md)
- [Power series](../../polynomials-and-power-series/power-series.md)
- [Associative algebra over a commutative ring](../../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)

## Proof depends on

- [Closed graph theorem](../../../../thousand-plus/analysis/46-functional-analysis/closed-graph-theorem.md)
- [Sequence](../../../data-structures/list-like-structures/sequence.md)
- [Metrization theorems](../../../../thousand-plus/geometry-and-topology/54-general-topology/metrization-theorems.md)
- [Banach open mapping theorem](../../../analysis/normed-vector-spaces-banach-spaces/banach-open-mapping-theorem.md)
- [Isomorphism with $K^n$](../../../linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Banach-Steinhaus theorem](../../../analysis/normed-vector-spaces-banach-spaces/banach-steinhaus-theorem.md)
- [Hilbert basis theorem](../../polynomials-and-power-series/hilbert-basis-theorem.md)
- [Complete metric spaces](../../../../undergraduate/topology/topology-and-metric-spaces/complete-metric-spaces.md)

## Main results

Its Lean names are 8 of the 57 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`MvPowerSeries.isRestricted_abs_iff`](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/PhD/Main/LegacyCode/PR'd/MvRestricted.lean#L38) (lemma)
- [`MvPolynomial.norm_toRestricted`](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/PhD/Main/ForMathlib/RingTheory/MvPowerSeries/Restricted/GaussNorm.lean#L343) (lemma)
- [`MvPowerSeries.Restricted.residueRingHom`](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/PhD/Main/ForMathlib/RingTheory/MvPowerSeries/Restricted/Residue.lean#L131) (def)
- [`MvPowerSeries.Restricted.residueEquiv`](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/PhD/Main/ForMathlib/RingTheory/MvPowerSeries/Restricted/Residue.lean#L253) (def)
- [`isAdmissible_coeffVal_of_isRestricted`](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/PhD/Main/NewtonPolygons/CoeffVal.lean#L116) (lemma)
- [`isNewtonPolygonOf_coeffVal_of_isRestricted`](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/PhD/Main/NewtonPolygons/CoeffVal.lean#L147) (theorem)
- [`radiusOfConvergence`](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/PhD/Main/NewtonPolygons/RadiusOfConvergence.lean#L109) (def)
- [`isRestricted_of_lt_radiusOfConvergence`](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/PhD/Main/NewtonPolygons/RadiusOfConvergence.lean#L141) (theorem)

No file its headlines import, directly or not (31 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0-rc1, Mathlib at [bbc4475e](https://github.com/leanprover-community/mathlib4/tree/bbc4475e9e8fd25fbc8e26d636dd8b37be8f105a).
- 650 .lean files; its Lean libraries `PhD` hold 584, declaring 9,464 names, with `sorry` in 48 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE](https://github.com/WilliamCoram/PhD/blob/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3/LICENSE)).

## Builds on

- Mathlib, at [bbc4475e](https://github.com/leanprover-community/mathlib4/tree/bbc4475e9e8fd25fbc8e26d636dd8b37be8f105a).

## Placement

4 of the 6 Mathlib concepts its headline statements name are in General algebra.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Topology (139 of 958 imports, 1.9×), Linear algebra (102 of 958 imports, 1.8×), General algebra (483 of 958 imports, 1.4×). *Proof depends on* lists 8 of the 130 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [WilliamCoram/PhD at 659ce260](https://github.com/WilliamCoram/PhD/tree/659ce26088bc541137cc28cc13ebbf0e3c9fbcc3)
