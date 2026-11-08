---
declaration: def
origin: cited
lean: Homeomorph.compactlyGeneratedCurry
statement: formalized
---

# Compactly generated compact-open currying

([`Homeomorph.compactlyGeneratedCurry`](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/CompactOpen/CompactlyGeneratedCurryHomeomorph.lean)).
For original `UCompactlyGeneratedSpace.{u}` spaces `P` and `A` and any
topological space `Y`, currying is a homeomorphism
`κ_u C_co(κ_u (P × A), Y) ≃ₜ κ_u C_co(P, κ_u C_co(A, Y))`.
Here `C_co` has the ordinary compact-open topology and `κ_u` denotes refinement
by compact Hausdorff probes in universe `u`. The product uses the original
factor topologies, and the right-hand compact-open space uses the refined
inner mapping space as target. The probe and all three carrier universes are
independent, with no local compactness or separation hypotheses. Its whole
underlying equivalence is
[`ContinuousMap.compactlyGeneratedCurryEquiv`](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/CompactOpen/CompactlyGeneratedCurry.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/README.md#headline-results) of [FormalFrontier/fundamental-groupoids](https://github.com/FormalFrontier/fundamental-groupoids) at commit [ce38a38f](https://github.com/FormalFrontier/fundamental-groupoids/tree/ce38a38faef1a147e75b68b78b02bbfd6ad82948), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Homeomorph.compactlyGeneratedCurry` (def), declared in [FundamentalGroupoids/Topology/CompactOpen/CompactlyGeneratedCurryHomeomorph.lean, line 70](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/CompactOpen/CompactlyGeneratedCurryHomeomorph.lean#L70).

Read from the source at commit [ce38a38f](https://github.com/FormalFrontier/fundamental-groupoids/tree/ce38a38faef1a147e75b68b78b02bbfd6ad82948), without running Lean.

## Sources

- [fundamental-groupoids at ce38a38f: README, headline results](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/README.md#headline-results)
- [Source of `Homeomorph.compactlyGeneratedCurry` in FundamentalGroupoids/Topology/CompactOpen/CompactlyGeneratedCurryHomeomorph.lean](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/CompactOpen/CompactlyGeneratedCurryHomeomorph.lean#L70)
