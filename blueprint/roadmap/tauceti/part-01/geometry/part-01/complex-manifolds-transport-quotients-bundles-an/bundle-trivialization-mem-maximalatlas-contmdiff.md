---
declaration: theorem
origin: cited
lean: Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff
statement: formalized
proof: formalized
---

# Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff

A linear trivialization lies in the maximal atlas of `C^n` trivializations exactly when its
fibrewise coordinate changes with every trivialization of the bundle's atlas, in both directions,
are `C^n` on the overlaps of the base sets.

```lean
Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff.{u_1, u_2, u_3, u_4, u_5, u_6}
  {𝕜 : Type u_1} {B : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [TopologicalSpace B] {E : B → Type u_4}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(x : B) → AddCommMonoid (E x)]
  [(x : B) → _root_.Module 𝕜 (E x)] {EB : Type u_5} {HB : Type u_6} [NormedAddCommGroup EB]
  [NormedSpace 𝕜 EB] [TopologicalSpace HB] [ChartedSpace HB B] (IB : ModelWithCorners 𝕜 EB HB)
  (n : WithTop ℕ∞) [(x : B) → TopologicalSpace (E x)] [FiberBundle F E] [VectorBundle 𝕜 F E]
  (e : Bundle.Trivialization F Bundle.TotalSpace.proj) [Bundle.Trivialization.IsLinear 𝕜 e] :
  e.toOpenPartialHomeomorph ∈
      StructureGroupoid.maximalAtlas (Bundle.TotalSpace F E) (contMDiffFiberwiseLinear B F IB n) ↔
    ∀ (e' : Bundle.Trivialization F Bundle.TotalSpace.proj) [inst : MemTrivializationAtlas e'],
      ContMDiffOn IB (modelWithCornersSelf 𝕜 (F →L[𝕜] F)) n
          (fun b => ↑(Bundle.Trivialization.coordChangeL 𝕜 e e' b)) (e.baseSet ∩ e'.baseSet) ∧
        ContMDiffOn IB (modelWithCornersSelf 𝕜 (F →L[𝕜] F)) n
          (fun b => ↑(Bundle.Trivialization.coordChangeL 𝕜 e' e b)) (e.baseSet ∩ e'.baseSet)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/MaximalAtlas.html#Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff).

## Sources

- [Tau Ceti documentation: `Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/MaximalAtlas.html#Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff)
- [Source of `Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff` in TauCeti/Geometry/Manifold/VectorBundle/MaximalAtlas.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/MaximalAtlas.lean#L305)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexManifolds/STATUS.md)
