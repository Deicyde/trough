---
declaration: theorem
origin: cited
lean: CalabiYau.complexMongeAmpere, CalabiYau.calabiConjecture_of_sub_eq_mddbar, CalabiYau.ricciFlat_of_ricciForm_eq_mddbar, CalabiYau.calabiConjecture, CalabiYau.ricciFlat_of_firstChernClass_eq_zero
statement: formalized
proof: formalized
---

# Calabi–Yau

[wxkj99/calabi-yau](https://github.com/wxkj99/calabi-yau) at commit [91b1ddf0](https://github.com/wxkj99/calabi-yau/tree/91b1ddf000c7028bc42ae6102eba0e2042eb37ff), 2026-10-03.

> A formalization in [Lean 4](https://lean-lang.org/) and [Mathlib](https://github.com/leanprover-community/mathlib4) of Yau's solution of the Calabi conjecture.

*Quoted from [README.md](https://github.com/wxkj99/calabi-yau/blob/91b1ddf000c7028bc42ae6102eba0e2042eb37ff/README.md), Apache-2.0.*

## Depends on

- [Borel sigma-algebra](../../measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Smooth map between manifolds](../../../geometry/differentiable-manifolds/part-01/smooth-map-between-manifolds.md)
- [Sigma-algebra](../../measures-and-integral-calculus/part-01/sigma-algebra.md)
- [Exponential](../../special-functions/exponential.md)

## Proof depends on

- [(smooth) Hom bundle](../../../geometry/smooth-vector-and-fiber-bundles/smooth-hom-bundle.md)
- [Compact open topology](../../../topology/general-topology/part-01/compact-open-topology.md)
- [Decomposition into transpositions](../../../../undergraduate/group-theory/permutation-group/decomposition-into-transpositions.md)
- [Interior of a manifold](../../../geometry/differentiable-manifolds/part-01/interior-of-a-manifold.md)
- [Hölder continuity](../../../topology/metric-spaces/holder-continuity.md)
- [0-manifolds are discrete spaces](../../../geometry/differentiable-manifolds/part-02/0-manifolds-are-discrete-spaces.md)
- [Norm](../../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/euclidean-and-hermitian-spaces/norm.md)
- [Heine-Borel theorem (proper metric space version)](../../../topology/metric-spaces/heine-borel-theorem-proper-metric-space-version.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`CalabiYau.complexMongeAmpere`](https://github.com/wxkj99/calabi-yau/blob/91b1ddf000c7028bc42ae6102eba0e2042eb37ff/Comparator/Challenge.lean#L49) (theorem)
- [`CalabiYau.calabiConjecture_of_sub_eq_mddbar`](https://github.com/wxkj99/calabi-yau/blob/91b1ddf000c7028bc42ae6102eba0e2042eb37ff/Comparator/Challenge.lean#L59) (theorem)
- [`CalabiYau.ricciFlat_of_ricciForm_eq_mddbar`](https://github.com/wxkj99/calabi-yau/blob/91b1ddf000c7028bc42ae6102eba0e2042eb37ff/Comparator/Challenge.lean#L70) (theorem)
- [`CalabiYau.calabiConjecture`](https://github.com/wxkj99/calabi-yau/blob/91b1ddf000c7028bc42ae6102eba0e2042eb37ff/Comparator/Challenge.lean#L81) (theorem)
- [`CalabiYau.ricciFlat_of_firstChernClass_eq_zero`](https://github.com/wxkj99/calabi-yau/blob/91b1ddf000c7028bc42ae6102eba0e2042eb37ff/Comparator/Challenge.lean#L91) (theorem)

No file its headlines import, directly or not (929 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.1, Mathlib at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- 931 .lean files; its Lean libraries `CalabiYau`, `Comparator` hold 931, declaring 4,854 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/wxkj99/calabi-yau/blob/91b1ddf000c7028bc42ae6102eba0e2042eb37ff/LICENSE)).

## Builds on

- Mathlib, at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).

## Placement

3 of the 4 Mathlib concepts its headline statements name are in Analysis.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (258 of 1501 imports, 7.3×), Linear algebra (202 of 1501 imports, 2.3×), Analysis (747 of 1501 imports, 1.8×). *Proof depends on* lists 8 of the 123 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [wxkj99/calabi-yau at 91b1ddf0](https://github.com/wxkj99/calabi-yau/tree/91b1ddf000c7028bc42ae6102eba0e2042eb37ff)
