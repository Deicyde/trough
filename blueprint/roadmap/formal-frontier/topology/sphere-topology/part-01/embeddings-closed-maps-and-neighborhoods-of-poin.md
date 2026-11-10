---
declaration: theorem
origin: cited
lean: TopCat.isEmbedding_widePushoutDesc_point
statement: formalized
proof: formalized
---

# Embeddings, closed maps and neighborhoods of point-wide-pushouts

[`TopCat.isEmbedding_widePushoutDesc_point`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/OpenEmbedding.lean)
promotes point-preserving component embeddings to an embedding of the
canonical wide pushouts; open or closed component embeddings give an open or
closed embedding, respectively. Point reflection and component open or closed
maps also suffice for the corresponding map property. The index may be
arbitrary or empty, and source and target universes are independent, with no
separation assumptions. The [ULift caller](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/PointLift.lean)
accommodates smaller original factors. For a given function relabeling factors
with finite label fibers, the [closed-map criterion](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/ClosedMap.lean)
assumes closed component maps, point reflection, and the head and factor equations.
The function is closed exactly when each omitted target factor has a closed chosen-point
singleton, with no continuity or separation assumption. Closed rays based at zero give a proper
closed embedding that is not open. For open neighborhoods of the attaching points,
[`TopCat.widePushoutPointNeighborhoodHomeomorph`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/OpenNeighborhood.lean)
identifies their wide pushout with its open range in the ordinary subtype topology.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TopCat.isEmbedding_widePushoutDesc_point` (theorem), declared in [SphereTopology/Topology/WidePushout/OpenEmbedding.lean, line 189](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/OpenEmbedding.lean#L189).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `TopCat.isEmbedding_widePushoutDesc_point` in SphereTopology/Topology/WidePushout/OpenEmbedding.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/OpenEmbedding.lean#L189)
