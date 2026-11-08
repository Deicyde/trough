---
declaration: theorem
origin: cited
lean: IsCoveringMap.isProperMap_iff_finite_fibers, IsCoveringMap.monodromyQuotientEquiv, IsCoveringMap.isProperMap_iff_finiteIndex, IsCoveringMap.injective_homotopyGroup_mapFun, IsCoveringMap.bijective_homotopyGroup_mapFun, IsCoveringMap.homotopyGroupMulEquiv
statement: formalized
---

# Covering fibers, cosets, properness and homotopy groups

For a covering p : E → B between arbitrary topological spaces in independent universes, properness is equivalent to finite point fibers and, when E is path connected with chosen e₀, monodromy identifies the fiber over p(e₀) with the left cosets of im(π₁(E,e₀) → π₁(B,p(e₀))) and properness is equivalent to finite index of that image subgroup, while for every e : E postcomposition on based homotopy classes of N-cubes relative to their coordinate-face boundary is injective for nonempty N and bijective for N with at least two elements in an independent cube universe, with a multiplicative equivalence HomotopyGroup N E e ≃* HomotopyGroup N B (p e) in the latter case when N has decidable equality.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/formalization.yaml) of [FormalFrontier/fundamental-groupoids](https://github.com/FormalFrontier/fundamental-groupoids) at commit [ce38a38f](https://github.com/FormalFrontier/fundamental-groupoids/tree/ce38a38faef1a147e75b68b78b02bbfd6ad82948), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `IsCoveringMap.isProperMap_iff_finite_fibers` (theorem), declared in [FundamentalGroupoids/Topology/Covering/Proper.lean, line 64](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/Proper.lean#L64).
- `IsCoveringMap.monodromyQuotientEquiv` (def), declared in [FundamentalGroupoids/Topology/Covering/Monodromy.lean, line 205](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/Monodromy.lean#L205).
- `IsCoveringMap.isProperMap_iff_finiteIndex` (theorem), declared in [FundamentalGroupoids/Topology/Covering/FiniteIndex.lean, line 47](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/FiniteIndex.lean#L47).
- `IsCoveringMap.injective_homotopyGroup_mapFun` (theorem), declared in [FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean, line 52](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean#L52).
- `IsCoveringMap.bijective_homotopyGroup_mapFun` (theorem), declared in [FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean, line 73](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean#L73).
- `IsCoveringMap.homotopyGroupMulEquiv` (def), declared in [FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean, line 96](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean#L96).

Read from the source at commit [ce38a38f](https://github.com/FormalFrontier/fundamental-groupoids/tree/ce38a38faef1a147e75b68b78b02bbfd6ad82948), without running Lean.

## Sources

- [fundamental-groupoids at ce38a38f: formalization.yaml](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/formalization.yaml)
- [Source of `IsCoveringMap.isProperMap_iff_finite_fibers` in FundamentalGroupoids/Topology/Covering/Proper.lean](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/Proper.lean#L64)
- [Source of `IsCoveringMap.monodromyQuotientEquiv` in FundamentalGroupoids/Topology/Covering/Monodromy.lean](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/Monodromy.lean#L205)
- [Source of `IsCoveringMap.isProperMap_iff_finiteIndex` in FundamentalGroupoids/Topology/Covering/FiniteIndex.lean](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/FiniteIndex.lean#L47)
- [Source of `IsCoveringMap.injective_homotopyGroup_mapFun` in FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean#L52)
- [Source of `IsCoveringMap.bijective_homotopyGroup_mapFun` in FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean#L73)
- [Source of `IsCoveringMap.homotopyGroupMulEquiv` in FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean](https://github.com/FormalFrontier/fundamental-groupoids/blob/ce38a38faef1a147e75b68b78b02bbfd6ad82948/FundamentalGroupoids/Topology/Covering/HomotopyGroup.lean#L96)
