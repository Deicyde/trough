---
declaration: def
origin: cited
lean: Metric.Sphere.cogroup, Metric.Sphere.cogroup_isCommMonObj_iff
statement: formalized
---

# Sphere cogroups and sharp cocommutativity

For every n : ℕ and universe u, Metric.Sphere.cogroup n gives the last-axis-north-based ULift.{u} of the unit sphere in EuclideanSpace ℝ (Fin (n + 2)) a group-object structure in the ordinary opposite based-homotopy category, whose specified ordered-pinch monoid structure is commutative exactly when 0 < n.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/formalization.yaml) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Metric.Sphere.cogroup` (def), declared in [SphereTopology/Homotopy/SphereCogroup.lean, line 1200](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/SphereCogroup.lean#L1200).
- `Metric.Sphere.cogroup_isCommMonObj_iff` (theorem), declared in [SphereTopology/Homotopy/SphereCocommutativity.lean, line 119](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/SphereCocommutativity.lean#L119).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: formalization.yaml](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/formalization.yaml)
- [Source of `Metric.Sphere.cogroup` in SphereTopology/Homotopy/SphereCogroup.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/SphereCogroup.lean#L1200)
- [Source of `Metric.Sphere.cogroup_isCommMonObj_iff` in SphereTopology/Homotopy/SphereCocommutativity.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/SphereCocommutativity.lean#L119)
