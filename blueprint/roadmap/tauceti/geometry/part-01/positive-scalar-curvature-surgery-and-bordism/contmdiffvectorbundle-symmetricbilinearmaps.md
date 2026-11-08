---
declaration: theorem
origin: cited
lean: ContMDiffVectorBundle.symmetricBilinearMaps
statement: formalized
proof: formalized
---

# ContMDiffVectorBundle.symmetricBilinearMaps

When two is invertible, the symmetric bilinear maps on the fibres of a `C^n` vector bundle
form a `C^n` vector bundle.

```lean
ContMDiffVectorBundle.symmetricBilinearMaps.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] [NeZero 2] {EB : Type u_2} [NormedAddCommGroup EB] [NormedSpace 𝕜 EB]
  {HB : Type u_3} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB} {B : Type u_4}
  [TopologicalSpace B] [ChartedSpace HB B] {F : Type u_5} [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  {V : B → Type u_6} [(x : B) → AddCommGroup (V x)] [(x : B) → _root_.Module 𝕜 (V x)]
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : B) → TopologicalSpace (V x)] [FiberBundle F V]
  [VectorBundle 𝕜 F V] {G : Type u_7} [NormedAddCommGroup G] [NormedSpace 𝕜 G] {n : WithTop ℕ∞}
  [ContMDiffVectorBundle n F V IB] :
  ContMDiffVectorBundle n (↥(TauCeti.symmetricBilinearMaps 𝕜 F G))
    (fun x => ↥(TauCeti.symmetricBilinearMaps 𝕜 (V x) G)) IB
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContMDiffVectorBundle.symmetricBilinearMaps`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Bilinear/Symmetric.html#ContMDiffVectorBundle.symmetricBilinearMaps).

## Sources

- [Tau Ceti documentation: `ContMDiffVectorBundle.symmetricBilinearMaps`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Bilinear/Symmetric.html#ContMDiffVectorBundle.symmetricBilinearMaps)
- [Source of `ContMDiffVectorBundle.symmetricBilinearMaps` in TauCeti/Geometry/Manifold/VectorBundle/Bilinear/Symmetric.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/Bilinear/Symmetric.lean#L126)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
