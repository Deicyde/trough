---
declaration: def
origin: cited
lean: TauCeti.diffeomorphOfCohomologous
statement: formalized
---

# Cohomologous cocycles glue to diffeomorphic bundles

If `c' i j = (h j)⁻¹ * c i j * h i`
on the overlaps for a `C^n` `0`-cochain `h` with values in a `C^n` Lie group acting `C^n`-smoothly
on `F`, then the total spaces of the bundles glued from `c` and `c'`, charted through the fibre,
are `C^n` diffeomorphic over the base, by the map acting by `(h i b)⁻¹` on the fibre coordinates of
chart `i`.

```lean
TauCeti.diffeomorphOfCohomologous.{u, v, w, t, u_1, u_2, u_3, u_4, u_5, u_6, u_7} {n : WithTop ℕ∞}
  {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {EB : Type u_2} [NormedAddCommGroup EB]
  [NormedSpace 𝕜 EB] {HB : Type u_3} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB}
  {EG : Type u_4} [NormedAddCommGroup EG] [NormedSpace 𝕜 EG] {HG : Type u_5} [TopologicalSpace HG]
  {IG : ModelWithCorners 𝕜 EG HG} {EF : Type u_6} [NormedAddCommGroup EF] [NormedSpace 𝕜 EF]
  {HF : Type u_7} [TopologicalSpace HF] (IF : ModelWithCorners 𝕜 EF HF) {ι : Type u} {B : Type v}
  {G : Type w} [Group G] [TopologicalSpace B] [ChartedSpace HB B] [TopologicalSpace G]
  [ChartedSpace HG G] {F : Type t} [TopologicalSpace F] [ChartedSpace HF F] [MulAction G F]
  [ContinuousSMul G F] {U : ι → Set B} {c : ι → ι → B → G}
  {hc : ∀ (i j k : ι), ∀ b ∈ U i ∩ U j ∩ U k, c j k b * c i j b = c i k b}
  {hU : ∀ (i : ι), IsOpen (U i)} {indexAt : B → ι} {hindex : ∀ (b : B), b ∈ U (indexAt b)}
  {hcontinuous : ∀ (i j : ι), ContinuousOn (c i j) (U i ∩ U j)} (c' : ι → ι → B → G)
  (hc' : ∀ (i j k : ι), ∀ b ∈ U i ∩ U j ∩ U k, c' j k b * c' i j b = c' i k b)
  (hcontinuous' : ∀ (i j : ι), ContinuousOn (c' i j) (U i ∩ U j)) [LieGroup IG n G]
  [ContMDiffSMul IG IF n G F] (h : ι → B → G) (hh : ∀ (i : ι), ContMDiffOn IB IG n (h i) (U i))
  (hcc' : ∀ (i j : ι), ∀ b ∈ U i ∩ U j, c' i j b = (h j b)⁻¹ * c i j b * h i b) :
  Diffeomorph (IB.prod IF) (IB.prod IF)
    (TauCeti.ManifoldTotalSpace F
      (TauCeti.fiberBundleCoreOfGroupCocycle U c hc F hU indexAt hindex hcontinuous).Fiber)
    (TauCeti.ManifoldTotalSpace F
      (TauCeti.fiberBundleCoreOfGroupCocycle U c' hc' F hU indexAt hindex hcontinuous').Fiber)
    n
```

## Depends on

- [TauCeti.ManifoldTotalSpace](tauceti-manifoldtotalspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.diffeomorphOfCohomologous`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/GroupCocycle.html#TauCeti.diffeomorphOfCohomologous).

## Sources

- [Tau Ceti documentation: `TauCeti.diffeomorphOfCohomologous`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberBundle/GroupCocycle.html#TauCeti.diffeomorphOfCohomologous)
- [Source of `TauCeti.diffeomorphOfCohomologous` in TauCeti/Geometry/Manifold/FiberBundle/GroupCocycle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/FiberBundle/GroupCocycle.lean#L134)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
