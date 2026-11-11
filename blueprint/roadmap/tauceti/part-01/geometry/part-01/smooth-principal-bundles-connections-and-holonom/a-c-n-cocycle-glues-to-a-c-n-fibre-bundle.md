---
declaration: theorem
origin: cited
lean: TauCeti.contMDiffFiberBundle_fiberBundleCoreOfGroupCocycle
statement: formalized
proof: formalized
---

# A `C^n` cocycle glues to a `C^n` fibre bundle

If `G` acts `C^n`-smoothly on `F` and the
transition functions `c i j` are `C^n` on the overlaps, then the bundle glued from `c` is a `C^n`
fibre bundle.

```lean
TauCeti.contMDiffFiberBundle_fiberBundleCoreOfGroupCocycle.{u, v, w, t, u_1, u_2, u_3, u_4, u_5,
    u_6, u_7}
  (n : WithTop ℕ∞) {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {EB : Type u_2}
  [NormedAddCommGroup EB] [NormedSpace 𝕜 EB] {HB : Type u_3} [TopologicalSpace HB]
  (IB : ModelWithCorners 𝕜 EB HB) {EG : Type u_4} [NormedAddCommGroup EG] [NormedSpace 𝕜 EG]
  {HG : Type u_5} [TopologicalSpace HG] {IG : ModelWithCorners 𝕜 EG HG} {EF : Type u_6}
  [NormedAddCommGroup EF] [NormedSpace 𝕜 EF] {HF : Type u_7} [TopologicalSpace HF]
  (IF : ModelWithCorners 𝕜 EF HF) {ι : Type u} {B : Type v} {G : Type w} [Group G]
  [TopologicalSpace B] [ChartedSpace HB B] [TopologicalSpace G] [ChartedSpace HG G] (F : Type t)
  [TopologicalSpace F] [ChartedSpace HF F] [MulAction G F] [ContinuousSMul G F] (U : ι → Set B)
  (c : ι → ι → B → G) (hc : ∀ (i j k : ι), ∀ b ∈ U i ∩ U j ∩ U k, c j k b * c i j b = c i k b)
  (hU : ∀ (i : ι), IsOpen (U i)) (indexAt : B → ι) (hindex : ∀ (b : B), b ∈ U (indexAt b))
  (hcontinuous : ∀ (i j : ι), ContinuousOn (c i j) (U i ∩ U j)) [ContMDiffSMul IG IF n G F]
  (hsmooth : ∀ (i j : ι), ContMDiffOn IB IG n (c i j) (U i ∩ U j)) :
  TauCeti.ContMDiffFiberBundle n F
    (TauCeti.fiberBundleCoreOfGroupCocycle U c hc F hU indexAt hindex hcontinuous).Fiber IB IF
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.contMDiffFiberBundle_fiberBundleCoreOfGroupCocycle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/GroupCocycle.html#TauCeti.contMDiffFiberBundle_fiberBundleCoreOfGroupCocycle).

## Sources

- [Tau Ceti documentation: `TauCeti.contMDiffFiberBundle_fiberBundleCoreOfGroupCocycle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/GroupCocycle.html#TauCeti.contMDiffFiberBundle_fiberBundleCoreOfGroupCocycle)
- [Source of `TauCeti.contMDiffFiberBundle_fiberBundleCoreOfGroupCocycle` in TauCeti/Geometry/Manifold/FiberBundle/GroupCocycle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/FiberBundle/GroupCocycle.lean#L75)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
