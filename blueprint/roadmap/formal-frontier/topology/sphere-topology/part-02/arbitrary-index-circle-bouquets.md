---
declaration: def
origin: cited
lean: CircleBouquet.space
statement: formalized
---

# Arbitrary-index circle bouquets

[`CircleBouquet.space`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/CircleBouquet.lean) is the wide
pushout of based complex circles, with a common point even for the empty
family and independent index/ambient universes. Inclusions, descent and
extensionality give its universal property; retractions detect the positive
generators as nonidentity.
[`CircleBouquet.generatorEquiv`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/CircleBouquet/FundamentalGroup.lean)
identifies its fundamental group with `FreeGroup I`, sending each free generator
to the included counterclockwise circle class. `CircleBouquet.lift` gives the
unique extension of arbitrary generator values to a homomorphism into any
group, in an independent target universe. Distinct included positive generators
do not commute. The inverse equivalence is noncomputable; no geometric
word-extraction algorithm is asserted.
The continuous map `CircleBouquet.relabel σ` realizes arbitrary relabelings,
preserving the original positive generators and commuting with `FreeGroup.map σ`.
Source and target ambient and label universes are independent, including empty
or infinite families and noninjective label maps. The universal property is
natural under precomposition by this map through `CircleBouquet.lift_comp_relabel`.
Its [topological criteria](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/CircleBouquet/Topology.lean)
characterize closed embeddings exactly by injective label maps and quotient
maps exactly by surjective label maps. Relabeling is a
[closed map exactly when every label fiber is finite](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/CircleBouquet/ClosedMap.lean);
the bouquet has the weak/final topology, not the Hawaiian-earring subspace topology.
The induced fundamental-group homomorphism is injective or surjective exactly
when the label map has the corresponding property. Its kernel is the normal
closure of the differences `positiveGenerator i * (positiveGenerator k)⁻¹`
for equal labels `σ i = σ k`, by `CircleBouquet.ker_mapOfEq_relabel`; no
surjectivity assumption is needed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `CircleBouquet.space` (def), declared in [SphereTopology/Homotopy/CircleBouquet.lean, line 107](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/CircleBouquet.lean#L107).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `CircleBouquet.space` in SphereTopology/Homotopy/CircleBouquet.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/CircleBouquet.lean#L107)
