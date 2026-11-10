---
declaration: def
origin: cited
lean: TopCat.widePushoutPointChartFundamentalGroupDesc
statement: formalized
---

# Fundamental groups of factor-plus-core charts

[`TopCat.widePushoutPointChartFundamentalGroupDesc`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/FundamentalGroup.lean)
glues homomorphisms on an arbitrary path-connected open neighborhood of the
common point and its charts, assuming path connectedness of each whole
factor. Only agreement on the core is required. The inclusion-induced
core and chart restrictions characterize the result, for arbitrary target
groups in an independent universe, empty index families and coincident
charts. If each original factor's core-preimage inclusion induces the trivial
fundamental-group map, the factor inclusion-induced coproduct map `q` is split
injective. The specified splitting extends factor homomorphisms to arbitrary
independently universed monoid targets. These hypotheses alone do not imply
surjectivity of `q` or uniqueness of these extensions. Under just the path-connected
core and whole-factor hypotheses,
[`TopCat.widePushoutPointChartFundamentalGroupColimitEquiv`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/FundamentalGroupColimit.lean)
identifies the raw group colimit of the core-to-chart star with the ambient
fundamental group. Both directions preserve every core and chart inclusion
map, including for an empty index family; no core-preimage nullity is needed.
With the split-injectivity hypotheses above,
[`FundamentalGroupKernel`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/FundamentalGroupKernel.lean)
identifies the kernel of the ambient-to-original-factor-coproduct retraction
`ρ` with the ambient algebraic normal closure of `⋃ i, γᵢ(ker pᵢ)`.
Here `γᵢ` is induced by chart inclusion; `pᵢ` comes from restricting the
ambient factor collapse to that chart and then applying the inverse ULift
homeomorphism to the original factor. Consequently, `q` is surjective exactly
when `ker pᵢ ≤ ker γᵢ` for every chart. Under this condition, `q` and the specified
`ρ` form a multiplicative equivalence, and these extensions are unique
for arbitrary independently universed monoid targets. For the inclusion family
into the ambient fundamental group, this condition is also necessary for
uniqueness: when it fails, the identity and `q.comp ρ` agree on all original-factor
restrictions but differ. No simply connected core, path-connected core preimages
or chart–factor homotopy equivalences are required.
Index and space universes are independent, and an empty family retains its point
head. No vanishing of these chart defects or free-product computation from
ordinary contractibility of chosen factor neighborhoods is asserted.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TopCat.widePushoutPointChartFundamentalGroupDesc` (def), declared in [SphereTopology/Topology/WidePushout/FundamentalGroup.lean, line 166](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/FundamentalGroup.lean#L166).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `TopCat.widePushoutPointChartFundamentalGroupDesc` in SphereTopology/Topology/WidePushout/FundamentalGroup.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Topology/WidePushout/FundamentalGroup.lean#L166)
