---
declaration: def
origin: cited
lean: TauCeti.PrincipalBundle.verticalLinearEquiv
statement: formalized
---

# The canonical vertical-fibre isomorphism `𝔤 ≃ₗ[𝕜] V_x P`

At every point `x` of a `C¹`
principal `G`-bundle, evaluation of fundamental vector fields identifies `GroupLieAlgebra IG G`
linearly with the vertical tangent space `(mfderiv proj x).ker`.

```lean
TauCeti.PrincipalBundle.verticalLinearEquiv.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8} {𝕜 : Type u_1}
  {B : Type u_2} {G : Type u_3} [NontriviallyNormedField 𝕜] {EB : Type u_4} [NormedAddCommGroup EB]
  [NormedSpace 𝕜 EB] {HB : Type u_5} [TopologicalSpace HB] (IB : ModelWithCorners 𝕜 EB HB)
  [TopologicalSpace B] [ChartedSpace HB B] {EG : Type u_6} [NormedAddCommGroup EG]
  [NormedSpace 𝕜 EG] {HG : Type u_7} [TopologicalSpace HG] (IG : ModelWithCorners 𝕜 EG HG) [Group G]
  [TopologicalSpace G] [ChartedSpace HG G] {P : B → Type u_8}
  [TopologicalSpace (Bundle.TotalSpace G P)] [(b : B) → TopologicalSpace (P b)] [FiberBundle G P]
  [(b : B) → MulAction Gᵐᵒᵖ (P b)] [TauCeti.PrincipalBundle G P] [ContMDiffMul IG 1 G]
  [TauCeti.ContMDiffFiberBundle 1 G P IB IG] (x : TauCeti.ManifoldTotalSpace G P) :
  GroupLieAlgebra IG G ≃ₗ[𝕜]
    ↥(↑((mfderiv% fun y => ((TauCeti.ManifoldTotalSpace.homeomorph G P).symm y).proj) x)).ker
```

## Depends on

- [TauCeti.ManifoldTotalSpace](tauceti-manifoldtotalspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PrincipalBundle.verticalLinearEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/Principal/FundamentalVectorField.html#TauCeti.PrincipalBundle.verticalLinearEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.PrincipalBundle.verticalLinearEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/Principal/FundamentalVectorField.html#TauCeti.PrincipalBundle.verticalLinearEquiv)
- [Source of `TauCeti.PrincipalBundle.verticalLinearEquiv` in TauCeti/Geometry/Manifold/FiberBundle/Principal/FundamentalVectorField.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/FiberBundle/Principal/FundamentalVectorField.lean#L243)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
