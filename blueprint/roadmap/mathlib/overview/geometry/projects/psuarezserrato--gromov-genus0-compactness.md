---
declaration: theorem
origin: cited
lean: GromovCompactness.metric_pos_def, GromovCompactness.concrete_nonconstant_map_positive_energy, GromovCompactness.concrete_nonconstant_map_finite_energy, GromovCompactness.Bookkeeping.countable_diagonal_extraction, GromovCompactness.Analysis.local_smooth_compactness, GromovCompactness.Analysis.local_smooth_compactness_of_arzelaAscoliProperty, GromovCompactness.local_smooth_compactness_of_bounded_geometry_and_eventually_jet_bounds, GromovCompactness.gromov_compactness_genus_zero
statement: formalized
proof: formalized
---

# Genus-Zero Gromov Compactness in Lean 4

[psuarezserrato/gromov-genus0-compactness](https://github.com/psuarezserrato/gromov-genus0-compactness) at commit [b43751c5](https://github.com/psuarezserrato/gromov-genus0-compactness/tree/b43751c5d97679a2272a1d7f90e33601d108aab3), 2026-11-11.

## Depends on

- [5.12 Quasi-compact spaces and maps](../../../../stacks/preliminaries/part-01/5-topology/part-01/5-12-quasi-compact-spaces-and-maps.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Smooth or analytic manifold (with boundary and corners)](../differentiable-manifolds/part-01/smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Normed vector space over a normed field](../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Set](../../data-structures/sets/set.md)
- [Topological space](../../topology/general-topology/part-01/topological-space.md)
- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Nondegenerate forms](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/bilinear-forms/nondegenerate-forms.md)
- [Heine-Cantor theorem](../../topology/uniform-notions/heine-cantor-theorem.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Cauchy filter](../../topology/uniform-notions/cauchy-filter.md)
- [Chain rule](../../../undergraduate/multivariable-calculus/differential-calculus/chain-rule.md)
- [Intermediate value theorem](../../topology/topological-algebra/intermediate-value-theorem.md)
- [Cauchy sequence](../../topology/uniform-notions/cauchy-sequence.md)

## Main results

Its Lean names are 8 of the 42 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`GromovCompactness.metric_pos_def`](https://github.com/psuarezserrato/gromov-genus0-compactness/blob/b43751c5d97679a2272a1d7f90e33601d108aab3/GromovCompactness/Geometry/Target.lean#L90) (theorem)
- [`GromovCompactness.concrete_nonconstant_map_positive_energy`](https://github.com/psuarezserrato/gromov-genus0-compactness/blob/b43751c5d97679a2272a1d7f90e33601d108aab3/GromovCompactness/Analysis/Energy.lean#L709) (theorem)
- [`GromovCompactness.concrete_nonconstant_map_finite_energy`](https://github.com/psuarezserrato/gromov-genus0-compactness/blob/b43751c5d97679a2272a1d7f90e33601d108aab3/GromovCompactness/Analysis/Energy.lean#L702) (theorem)
- [`GromovCompactness.Bookkeeping.countable_diagonal_extraction`](https://github.com/psuarezserrato/gromov-genus0-compactness/blob/b43751c5d97679a2272a1d7f90e33601d108aab3/GromovCompactness/Topology/Subsequence.lean#L78) (theorem)
- [`GromovCompactness.Analysis.local_smooth_compactness`](https://github.com/psuarezserrato/gromov-genus0-compactness/blob/b43751c5d97679a2272a1d7f90e33601d108aab3/GromovCompactness/Analysis/EllipticBootstrap.lean#L6453) (theorem)
- [`GromovCompactness.Analysis.local_smooth_compactness_of_arzelaAscoliProperty`](https://github.com/psuarezserrato/gromov-genus0-compactness/blob/b43751c5d97679a2272a1d7f90e33601d108aab3/GromovCompactness/Analysis/EllipticBootstrap.lean#L7981) (theorem)
- [`GromovCompactness.local_smooth_compactness_of_bounded_geometry_and_eventually_jet_bounds`](https://github.com/psuarezserrato/gromov-genus0-compactness/blob/b43751c5d97679a2272a1d7f90e33601d108aab3/GromovCompactness/Geometry/NormalCharts.lean#L4473) (theorem)
- [`GromovCompactness.gromov_compactness_genus_zero`](https://github.com/psuarezserrato/gromov-genus0-compactness/blob/b43751c5d97679a2272a1d7f90e33601d108aab3/GromovCompactness/Main.lean#L120) (theorem)

No file its headlines import, directly or not (30 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 203 .lean files; its Lean libraries `GromovCompactness` hold 37, declaring 3,085 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License files: `LICENSE.md`; facts only.

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 22 of 209 are in Geometry, 4.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (22 of 209 imports, 4.5×), Topology (43 of 209 imports, 2.8×), Analysis (113 of 209 imports, 2.0×). *Proof depends on* lists 8 of the 59 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [psuarezserrato/gromov-genus0-compactness at b43751c5](https://github.com/psuarezserrato/gromov-genus0-compactness/tree/b43751c5d97679a2272a1d7f90e33601d108aab3)
