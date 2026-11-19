---
declaration: theorem
origin: cited
lean: AmbidextrousSofa.Main.volume_le, AmbidextrousSofa.Main.volume_eq_iff, AmbidextrousSofa.Main.quarter_turns, AmbidextrousSofa.Main.isAmbidextrous_image_referenceSofa, AmbidextrousSofa.Main.convexHull_referenceSofa, AmbidextrousSofa.Main.existsUnique_root, AmbidextrousSofa.Main.value_eq_romik, FormalConjectures.MovingSofa.ambidextrousSofaConstant_eq_romiksSofa_area
statement: formalized
proof: formalized
---

# lean4-ambidextrous-sofa

*Optimality and uniqueness of Romik's ambidextrous sofa, in Lean 4*

[vltanh/lean4-ambidextrous-sofa](https://github.com/vltanh/lean4-ambidextrous-sofa) at commit [5e90d029](https://github.com/vltanh/lean4-ambidextrous-sofa/tree/5e90d029cab30151441a5794db31423bc277aad8), 2026-11-14.

> The ambidextrous moving sofa problem asks for the largest area of a shape that can be moved around the right-angled corner of a hallway of unit width that turns right, and also, from the same starting position, around one that turns left.

*Quoted from [README.md](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/README.md), Apache-2.0.*

## Depends on

- [Set](../../../data-structures/sets/set.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Convex hull of a subset of an affine real space](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)

## Proof depends on

- [Hausdorff distance](../../../topology/metric-spaces/hausdorff-distance.md)
- [Fundamental theorem of calculus, part 2](../../measures-and-integral-calculus/part-01/fundamental-theorem-of-calculus-part-2.md)
- [Trigonometric functions](../../special-functions/trigonometric-functions.md)
- [Inverse trigonometric functions](../../special-functions/inverse-trigonometric-functions.md)
- [Intermediate value theorem](../../../topology/topological-algebra/intermediate-value-theorem.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Measurable function](../../measures-and-integral-calculus/part-01/measurable-function.md)
- [Dominated convergence theorem](../../measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`AmbidextrousSofa.Main.volume_le`](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/AmbidextrousSofa/Main.lean#L132) (theorem)
- [`AmbidextrousSofa.Main.volume_eq_iff`](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/AmbidextrousSofa/Main.lean#L164) (theorem)
- [`AmbidextrousSofa.Main.quarter_turns`](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/AmbidextrousSofa/Main.lean#L176) (theorem)
- [`AmbidextrousSofa.Main.isAmbidextrous_image_referenceSofa`](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/AmbidextrousSofa/Main.lean#L149) (theorem)
- [`AmbidextrousSofa.Main.convexHull_referenceSofa`](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/AmbidextrousSofa/Main.lean#L157) (theorem)
- [`AmbidextrousSofa.Main.existsUnique_root`](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/AmbidextrousSofa/Main.lean#L76) (theorem)
- [`AmbidextrousSofa.Main.value_eq_romik`](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/AmbidextrousSofa/Main.lean#L116) (theorem)
- [`FormalConjectures.MovingSofa.ambidextrousSofaConstant_eq_romiksSofa_area`](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/AmbidextrousSofa/FormalConjectures/Bridge.lean#L784) (theorem)

No file its headlines import, directly or not (515 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc3, Mathlib at [c55e6e78](https://github.com/leanprover-community/mathlib4/tree/c55e6e786f49471c72fbddbec5415808896aec1e).
- 518 .lean files; its Lean libraries `MovingSofaOptimality`, `AmbidextrousSofa`, `Challenge`, `Solution` hold 517, declaring 5,968 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/vltanh/lean4-ambidextrous-sofa/blob/5e90d029cab30151441a5794db31423bc277aad8/LICENSE)).

## Builds on

- Mathlib, at [c55e6e78](https://github.com/leanprover-community/mathlib4/tree/c55e6e786f49471c72fbddbec5415808896aec1e).

## Placement

Of its imports of Mathlib modules in an overview area, 169 of 199 are in Analysis, 3.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (169 of 199 imports, 3.1×), Topology (21 of 199 imports, 1.4×). *Proof depends on* lists 8 of the 46 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [vltanh/lean4-ambidextrous-sofa at 5e90d029](https://github.com/vltanh/lean4-ambidextrous-sofa/tree/5e90d029cab30151441a5794db31423bc277aad8)
