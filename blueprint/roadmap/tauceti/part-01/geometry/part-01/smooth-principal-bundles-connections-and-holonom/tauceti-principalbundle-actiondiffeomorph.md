---
declaration: def
origin: cited
lean: TauCeti.PrincipalBundle.actionDiffeomorph
statement: formalized
---

# TauCeti.PrincipalBundle.actionDiffeomorph

The principal action identifies `P × G` diffeomorphically with the self-fibre product,
endowed with its transverse atlas. The inverse is first projection paired with division.

```lean
TauCeti.PrincipalBundle.actionDiffeomorph.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {B : Type u_1}
  {G : Type u_2} {P : B → Type u_3} [TopologicalSpace (Bundle.TotalSpace G P)] [TopologicalSpace B]
  [Group G] [TopologicalSpace G] [(b : B) → TopologicalSpace (P b)] [FiberBundle G P]
  [(b : B) → MulAction Gᵐᵒᵖ (P b)] [TauCeti.PrincipalBundle G P] {EB : Type u_4} {HB : Type u_5}
  {EG : Type u_6} {HG : Type u_7} [NormedAddCommGroup EB] [NormedSpace ℝ EB] [TopologicalSpace HB]
  [NormedAddCommGroup EG] [NormedSpace ℝ EG] [TopologicalSpace HG] {IB : ModelWithCorners ℝ EB HB}
  {IG : ModelWithCorners ℝ EG HG} [ChartedSpace HB B] [ChartedSpace HG G] {n : WithTop ℕ∞}
  [IsManifold IB n B] [LieGroup IG n G] [TauCeti.ContMDiffFiberBundle n G P IB IG] [IB.Boundaryless]
  [IG.Boundaryless] [FiniteDimensional ℝ EB] [FiniteDimensional ℝ EG] (hn : 1 ≤ n) :
  Diffeomorph ((IB.prod IG).prod IG)
    (modelWithCornersSelf ℝ
      (Fin (Module.finrank ℝ (EB × EG) + Module.finrank ℝ (EB × EG) - Module.finrank ℝ EB) → ℝ))
    (TauCeti.ManifoldTotalSpace G P × G)
    { z //
      (fun p => ((TauCeti.ManifoldTotalSpace.homeomorph G P).symm p).proj) z.1 =
        (fun p => ((TauCeti.ManifoldTotalSpace.homeomorph G P).symm p).proj) z.2 }
    n
```

## Depends on

- [TauCeti.ManifoldTotalSpace](tauceti-manifoldtotalspace.md)
- [The transverse fibre-product theorem](the-transverse-fibre-product-theorem.md)

## Proof depends on

- [TauCeti.PrincipalBundle.contMDiff_fiberProductDivision](tauceti-principalbundle-contmdiff-fiberproductdi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PrincipalBundle.actionDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/Principal/FiberProduct.html#TauCeti.PrincipalBundle.actionDiffeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.PrincipalBundle.actionDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/Principal/FiberProduct.html#TauCeti.PrincipalBundle.actionDiffeomorph)
- [Source of `TauCeti.PrincipalBundle.actionDiffeomorph` in TauCeti/Geometry/Manifold/FiberBundle/Principal/FiberProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/FiberBundle/Principal/FiberProduct.lean#L175)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
