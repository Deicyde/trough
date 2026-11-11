---
declaration: theorem
origin: cited
lean: TauCeti.PrincipalBundle.mlieBracket_rightFundamentalVectorField
statement: formalized
proof: formalized
---

# Lie bracket homomorphism on a principal bundle

On a `C²` principal `G`-bundle with a `C³`
Lie group `G`, `[ξ♯, η♯] = ⁅ξ, η⁆♯`.

```lean
TauCeti.PrincipalBundle.mlieBracket_rightFundamentalVectorField.{u_1, u_2, u_3, u_4, u_5, u_6, u_7,
    u_8}
  {𝕜 : Type u_1} {B : Type u_2} {G : Type u_3} [NontriviallyNormedField 𝕜] {EB : Type u_4}
  [NormedAddCommGroup EB] [NormedSpace 𝕜 EB] {HB : Type u_5} [TopologicalSpace HB]
  {IB : ModelWithCorners 𝕜 EB HB} [TopologicalSpace B] [ChartedSpace HB B] {EG : Type u_6}
  [NormedAddCommGroup EG] [NormedSpace 𝕜 EG] {HG : Type u_7} [TopologicalSpace HG]
  {IG : ModelWithCorners 𝕜 EG HG} [Group G] [TopologicalSpace G] [ChartedSpace HG G]
  {P : B → Type u_8} [TopologicalSpace (Bundle.TotalSpace G P)] [(b : B) → TopologicalSpace (P b)]
  [FiberBundle G P] [(b : B) → MulAction Gᵐᵒᵖ (P b)] [TauCeti.PrincipalBundle G P]
  [CompleteSpace EB] [CompleteSpace EG] [LieGroup IG (minSmoothness 𝕜 3) G]
  [IsManifold IB (minSmoothness 𝕜 2) B] [TauCeti.ContMDiffFiberBundle (minSmoothness 𝕜 2) G P IB IG]
  (ξ η : GroupLieAlgebra IG G) :
  VectorField.mlieBracket (IB.prod IG) (TauCeti.rightFundamentalVectorField (IB.prod IG) ξ)
      (TauCeti.rightFundamentalVectorField (IB.prod IG) η) =
    TauCeti.rightFundamentalVectorField (IB.prod IG) ⁅ξ, η⁆
```

## Depends on

- [TauCeti.ManifoldTotalSpace](tauceti-manifoldtotalspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PrincipalBundle.mlieBracket_rightFundamentalVectorField`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/Principal/FundamentalVectorField.html#TauCeti.PrincipalBundle.mlieBracket_rightFundamentalVectorField).

## Sources

- [Tau Ceti documentation: `TauCeti.PrincipalBundle.mlieBracket_rightFundamentalVectorField`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/Principal/FundamentalVectorField.html#TauCeti.PrincipalBundle.mlieBracket_rightFundamentalVectorField)
- [Source of `TauCeti.PrincipalBundle.mlieBracket_rightFundamentalVectorField` in TauCeti/Geometry/Manifold/FiberBundle/Principal/FundamentalVectorField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/FiberBundle/Principal/FundamentalVectorField.lean#L135)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
