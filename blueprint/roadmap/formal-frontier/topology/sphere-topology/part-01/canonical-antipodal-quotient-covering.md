---
declaration: theorem
origin: cited
lean: Metric.Sphere.isQuotientCoveringMap_toProjectivization
statement: formalized
proof: formalized
---

# Canonical antipodal quotient covering

For `E : Type w` with
`[NormedAddCommGroup E] [NormedSpace ℝ E]`,
[`Metric.Sphere.isQuotientCoveringMap_toProjectivization`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/Projectivization.lean)
makes the canonical continuous map
`Metric.Sphere.toProjectivization : C(Metric.sphere (0 : E) 1, Projectivization ℝ E)`
a quotient covering for the scalar action of `Metric.sphere (0 : ℝ) 1`,
whose elements act by identity and negation. The sphere uses the original norm;
the target has the quotient topology from nonzero vectors. No inner product,
dimension, completeness, local compactness, nonemptiness, nontriviality or
freeness hypothesis is required. This includes the zero space's empty-to-empty
map and the two-point-to-one-point map for `E = ℝ`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Metric.Sphere.isQuotientCoveringMap_toProjectivization` (theorem), declared in [SphereTopology/Geometry/Projectivization.lean, line 164](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/Projectivization.lean#L164).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `Metric.Sphere.isQuotientCoveringMap_toProjectivization` in SphereTopology/Geometry/Projectivization.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/Projectivization.lean#L164)
