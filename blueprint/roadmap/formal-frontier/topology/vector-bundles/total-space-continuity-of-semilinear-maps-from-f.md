---
declaration: theorem
origin: cited
lean: LinearMap.continuous_total_of_local_coordinates_of_basis_semilinear
statement: formalized
proof: formalized
---

# Total-space continuity of semilinear maps from finite local bases

Let `p : T → X` be continuous, with given `R`-module structures and subspace
topologies on its equality-subtype fibres, and let `σ : R →+* S` be a homomorphism
of semirings, with a topology on `S`. Coordinate models with finite bases may vary
over an arbitrary open cover. If their scalar basis coordinates composed with `σ`
and exact inverse vector coordinates are continuous, parameter-continuity of the
images of the basis vectors gives continuity of the total semilinear fibre map
into any `S`-module with continuous addition and scalar multiplication. No topology
on `R`, continuity of `σ`, continuous operations on the models or fibres,
injectivity, forward-realization continuity, norm, completeness or separation is
required. See
[`LinearMap.continuous_total_of_local_coordinates_of_basis_semilinear`](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/LocalCoordinates.lean).
The linear criterion
[`LinearMap.continuous_total_of_local_coordinates_of_basis`](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/LocalCoordinates.lean)
is the identity-hom specialization.
Over a complete nontrivially normed field, finite-dimensional Hausdorff
topological coordinate models supply the bases and scalar-coordinate continuity;
fixed-vector frame continuity gives the corollary
[`LinearMap.continuous_total_of_local_coordinates`](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/LocalCoordinates.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/README.md#headline-results) of [FormalFrontier/vector-bundles](https://github.com/FormalFrontier/vector-bundles) at commit [e3fb9de3](https://github.com/FormalFrontier/vector-bundles/tree/e3fb9de334c8b60bdb707b3e48b2094b2202c725), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `LinearMap.continuous_total_of_local_coordinates_of_basis_semilinear` (theorem), declared in [VectorBundles/Topology/Module/LocalCoordinates.lean, line 51](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/LocalCoordinates.lean#L51).

Read from the source at commit [e3fb9de3](https://github.com/FormalFrontier/vector-bundles/tree/e3fb9de334c8b60bdb707b3e48b2094b2202c725), without running Lean.

## Sources

- [vector-bundles at e3fb9de3: README, headline results](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/README.md#headline-results)
- [Source of `LinearMap.continuous_total_of_local_coordinates_of_basis_semilinear` in VectorBundles/Topology/Module/LocalCoordinates.lean](https://github.com/FormalFrontier/vector-bundles/blob/e3fb9de334c8b60bdb707b3e48b2094b2202c725/VectorBundles/Topology/Module/LocalCoordinates.lean#L51)
