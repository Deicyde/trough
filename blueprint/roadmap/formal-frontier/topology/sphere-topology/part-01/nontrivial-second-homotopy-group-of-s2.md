---
declaration: theorem
origin: cited
lean: Metric.Sphere.id_not_nullhomotopic_two
statement: formalized
proof: formalized
---

# Nontrivial second homotopy group of S²

[`Metric.Sphere.id_not_nullhomotopic_two`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SphereNontrivial.lean)
shows that the identity of the unit two-sphere in `EuclideanSpace ℝ (Fin 3)`,
lifted to any universe, is not homotopic to any constant map.
`Metric.Sphere.homotopyQuotient_id_ne_const_two` distinguishes its identity
class from the constant class at the last-axis north pole in the based-homotopy
category. `HomotopyGroup.nontrivial_sphere_two` proves that the corresponding
`π₂` is nontrivial. The sphere is `Metric.Sphere.basedSpace 1`; no computation
of the second homotopy group is asserted.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Metric.Sphere.id_not_nullhomotopic_two` (theorem), declared in [SphereTopology/Homotopy/HomotopyGroup/SphereNontrivial.lean, line 51](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SphereNontrivial.lean#L51).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `Metric.Sphere.id_not_nullhomotopic_two` in SphereTopology/Homotopy/HomotopyGroup/SphereNontrivial.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SphereNontrivial.lean#L51)
