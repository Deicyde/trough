---
declaration: theorem
origin: cited
lean: SmoothedOctagon.octagon_density
statement: formalized
proof: formalized
---

# The Reinhardt conjecture, in Lean 4

[vltanh/lean4-smoothed-octagon](https://github.com/vltanh/lean4-smoothed-octagon) at commit [af448b53](https://github.com/vltanh/lean4-smoothed-octagon/tree/af448b5312461133ff60bb3e1c2834e09fda7161), 2026-11-13.

> Which centrally symmetric convex shape packs the plane worst? Pack copies of a disk as tightly as possible and they cover `π/√12 = 90.69…%` of the plane; a regular octagon does a little worse.

*Quoted from [README.md](https://github.com/vltanh/lean4-smoothed-octagon/blob/af448b5312461133ff60bb3e1c2834e09fda7161/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Equivalence of norms in finite dimension](../../normed-vector-spaces-banach-spaces/equivalence-of-norms-in-finite-dimension.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions (Analysis)](../../differentiability/derivative-of-a-composition-of-functions.md)
- [Convex function](../../convexity/convex-function.md)
- [Real number](../../../general-algebra/numbers/real-number.md)
- [Intermediate value theorem](../../../topology/topological-algebra/intermediate-value-theorem.md)
- [Orthogonal group](../../../../undergraduate/group-theory/classical-automorphism-groups/orthogonal-group.md)
- [Logarithm](../../special-functions/logarithm.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`SmoothedOctagon.octagon_density`](https://github.com/vltanh/lean4-smoothed-octagon/blob/af448b5312461133ff60bb3e1c2834e09fda7161/SmoothedOctagon/Foundations/Problem.lean#L61) (theorem)

No file its headlines import, directly or not (1 file), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.36.0-rc2, Mathlib at [9d581dff](https://github.com/leanprover-community/mathlib4/tree/9d581dfff2e41de989072ea63abf3daf69311520).
- 459 .lean files; its Lean libraries `Cited`, `SmoothedOctagon`, `Palomar` hold 458, declaring 6,428 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/vltanh/lean4-smoothed-octagon/blob/af448b5312461133ff60bb3e1c2834e09fda7161/LICENSE)).

## Builds on

- Mathlib, at [9d581dff](https://github.com/leanprover-community/mathlib4/tree/9d581dfff2e41de989072ea63abf3daf69311520).
- `OptimalControl` (https://github.com/vltanh/lean4-optimal-control) at `88689a80`.
- `SmoothedPolygons` (https://github.com/vltanh/lean4-smoothed-polygon) at `b9846532`.

## Placement

Of its imports of Mathlib modules in an overview area, 167 of 201 are in Analysis, 3.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (167 of 201 imports, 3.1×). *Proof depends on* lists 8 of the 48 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [vltanh/lean4-smoothed-octagon at af448b53](https://github.com/vltanh/lean4-smoothed-octagon/tree/af448b5312461133ff60bb3e1c2834e09fda7161)
