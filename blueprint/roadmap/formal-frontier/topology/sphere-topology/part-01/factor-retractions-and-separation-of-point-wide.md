---
declaration: def
origin: cited
lean: TopCat.widePushoutPointRetraction
statement: formalized
---

# Factor retractions and separation of point-wide-pushouts

[`TopCat.widePushoutPointRetraction`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushoutRetraction.lean)
retracts the categorical wide pushout of arbitrary chosen-point spaces onto
any selected factor, and each factor inclusion is an embedding. The
[retractions jointly distinguish points](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/Separation.lean),
without separation or finiteness assumptions, even for the empty index family.
The pushout is T₀, T₁ or Hausdorff exactly when every factor has that property;
factorwise inheritance is available by instance inference. Index and space
universes are independent. No embedding into the product is asserted.
The circle-bouquet retractions specialize this construction.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TopCat.widePushoutPointRetraction` (def), declared in [SphereTopology/Topology/WidePushoutRetraction.lean, line 79](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushoutRetraction.lean#L79).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `TopCat.widePushoutPointRetraction` in SphereTopology/Topology/WidePushoutRetraction.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushoutRetraction.lean#L79)
