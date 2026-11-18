---
declaration: theorem
origin: cited
lean: Jacobians.Axioms.AX_curve_image_subgroup_isOpen, Jacobians.ofCurve_isJacobian, Jacobians.isJacobian_unique, genus_eq_zero_iff_homeo, Jacobian.ofCurve_inj, Jacobians.Axioms.AX_AbelTheorem, Jacobians.ProjectiveCurve.EllipticOfCurveInj.elliptic_ofCurve_injective, Jacobians.Extensions.HyperellipticEven.genus_HyperellipticEven_eq
statement: formalized
---

# Jacobians of Compact Riemann Surfaces

[mrdouglasny/jacobian-challenge](https://github.com/mrdouglasny/jacobian-challenge) at commit [8ce1ec28](https://github.com/mrdouglasny/jacobian-challenge/tree/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143), 2026-06-17.

> *Blow-by-blow discharge history lives in [`docs/history.md`](docs/history.md); this file keeps the current state and the ideas.*

*Quoted from [README.md](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/README.md), Apache-2.0.*

## Depends on

- [5.12 Quasi-compact spaces and maps](../../../../stacks/preliminaries/part-01/5-topology/part-01/5-12-quasi-compact-spaces-and-maps.md)
- [Connectedness](../../topology/general-topology/part-01/connectedness.md)
- [Smooth or analytic manifold (with boundary and corners)](../differentiable-manifolds/part-01/smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Set](../../data-structures/sets/set.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Topological space](../../topology/general-topology/part-01/topological-space.md)
- [Smooth map between manifolds](../differentiable-manifolds/part-01/smooth-map-between-manifolds.md)

## Proof depends on

- [Sequential compactness is equivalent to compactness (Bolzano-Weierstrass)](../../topology/metric-spaces/sequential-compactness-is-equivalent-to-compactn.md)
- [Holomorphic stability under uniform convergence](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-stability-under-uniform-convergence.md)
- [Arzela-Ascoli theorem](../../topology/metric-spaces/arzela-ascoli-theorem.md)
- [Fundamental theorem of calculus, part 2](../../analysis/measures-and-integral-calculus/part-01/fundamental-theorem-of-calculus-part-2.md)
- [$\C$ is algebraically closed](../../general-algebra/field-theory/c-is-algebraically-closed.md)
- [Path connectedness](../../../undergraduate/topology/topology-and-metric-spaces/path-connectedness.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Nullstellensatz](../algebraic-geometry/nullstellensatz.md)

## Main results

Its Lean names are 8 of the 12 theorems its README names in code:

- [`Jacobians.Axioms.AX_curve_image_subgroup_isOpen`](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/Jacobians/Axioms/AlbaneseInterface.lean#L85) (theorem)
- [`Jacobians.ofCurve_isJacobian`](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/Jacobians/UniversalProperty.lean#L901) (theorem)
- [`Jacobians.isJacobian_unique`](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/Jacobians/UniversalProperty.lean#L947) (theorem)
- [`genus_eq_zero_iff_homeo`](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/Jacobians/Challenge.lean#L75) (lemma)
- [`Jacobian.ofCurve_inj`](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/Jacobians/Challenge.lean#L148) (lemma)
- [`Jacobians.Axioms.AX_AbelTheorem`](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/Jacobians/Axioms/AbelTheorem.lean#L145) (theorem)
- [`Jacobians.ProjectiveCurve.EllipticOfCurveInj.elliptic_ofCurve_injective`](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/Jacobians/ProjectiveCurve/Elliptic/OfCurveInj.lean#L237) (theorem)
- [`Jacobians.Extensions.HyperellipticEven.genus_HyperellipticEven_eq`](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/Jacobians/Extensions/HyperellipticEven.lean#L161) (theorem)

Of the files its headlines import, directly or not, `Jacobians/RiemannSurface/Cohomology/RiemannRochAnchor.lean` hold `sorry` or `admit`.

## Project

- Lean v4.30.0, Mathlib at [c5ea0035](https://github.com/leanprover-community/mathlib4/tree/c5ea00351c28e24afc9f0f84379aa41082b1188f).
- 867 .lean files; its Lean libraries `Jacobians` hold 241, declaring 2,965 names, with `sorry` in 1 file and 7 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/mrdouglasny/jacobian-challenge/blob/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143/LICENSE)).

## Builds on

- Mathlib, at [c5ea0035](https://github.com/leanprover-community/mathlib4/tree/c5ea00351c28e24afc9f0f84379aa41082b1188f).
- `jacobian`.

## Placement

Of its imports of Mathlib modules in an overview area, 36 of 180 are in Geometry, 8.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (36 of 180 imports, 8.5×), Linear algebra (22 of 180 imports, 2.1×), Topology (25 of 180 imports, 1.9×). *Proof depends on* names 8 of the 79 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [mrdouglasny/jacobian-challenge at 8ce1ec28](https://github.com/mrdouglasny/jacobian-challenge/tree/8ce1ec28aed1c78b3b39d0bae26e2858c82f5143)
