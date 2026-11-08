---
declaration: def
origin: cited
lean: EuclideanSpace.onePointHomeomorphSphere
statement: formalized
---

# Last-axis one-point compactification coordinates

[`EuclideanSpace.onePointHomeomorphSphere`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/OnePointSphere.lean)
identifies `OnePoint (EuclideanSpace ℝ (Fin n))` with the unit sphere in
`EuclideanSpace ℝ (Fin (n+1))`, for every `n`, including zero. Infinity maps
to the last unit vector and finite zero to its antipode. Finite coordinates
have denominator `‖x‖²+4`, and the off-pole inverse has coordinates
`2*p_i/(1-p_last)`. The underlying append-zero-last linear isometry also
applies over `RCLike` scalars; only the sphere homeomorphism is real.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `EuclideanSpace.onePointHomeomorphSphere` (def), declared in [SphereTopology/Geometry/OnePointSphere.lean, line 169](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/OnePointSphere.lean#L169).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `EuclideanSpace.onePointHomeomorphSphere` in SphereTopology/Geometry/OnePointSphere.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/OnePointSphere.lean#L169)
