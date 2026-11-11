---
declaration: theorem
origin: cited
lean: ContMDiffVectorBundle.exists_trivialization_baseSet_eq_univ_iff_exists_ne_zero
statement: formalized
proof: formalized
---

# The trivial line bundle criterion

A `C^n` line bundle has a trivialization over the whole
base in the maximal atlas of `C^n` trivializations, that is, it is trivial as a `C^n` vector
bundle, exactly when it has a `C^n` section that vanishes nowhere. For a holomorphic line bundle,
over `𝓘(ℂ, EB)` with `n = ∞`, this says that it is holomorphically trivial exactly when it has a
nowhere-vanishing holomorphic section.

```lean
ContMDiffVectorBundle.exists_trivialization_baseSet_eq_univ_iff_exists_ne_zero.{u_1, u_2, u_3, u_4,
    u_5, u_6}
  {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {EB : Type u_2} [NormedAddCommGroup EB]
  [NormedSpace 𝕜 EB] {HB : Type u_3} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB}
  {B : Type u_4} [TopologicalSpace B] [ChartedSpace HB B] {F : Type u_5} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {V : B → Type u_6} [TopologicalSpace (Bundle.TotalSpace F V)]
  [(x : B) → AddCommGroup (V x)] [(x : B) → _root_.Module 𝕜 (V x)]
  [(x : B) → TopologicalSpace (V x)] [FiberBundle F V] {n : WithTop ℕ∞} [VectorBundle 𝕜 F V]
  [CompleteSpace 𝕜] [ContMDiffVectorBundle n F V IB] (hF : Module.finrank 𝕜 F = 1) :
  (∃ e,
      ∃ (_ : Bundle.Trivialization.IsLinear 𝕜 e),
        e.toOpenPartialHomeomorph ∈
            StructureGroupoid.maximalAtlas (Bundle.TotalSpace F V)
              (contMDiffFiberwiseLinear B F IB n) ∧
          e.baseSet = Set.univ) ↔
    ∃ σ,
      (ContMDiff IB (IB.prod (modelWithCornersSelf 𝕜 F)) n fun x => ⟨x, σ x⟩) ∧ ∀ (x : B), σ x ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff](bundle-trivialization-mem-maximalatlas-contmdiff.md)

## Lean

Formalized in Tau Ceti as [`ContMDiffVectorBundle.exists_trivialization_baseSet_eq_univ_iff_exists_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/FrameTrivialization.html#ContMDiffVectorBundle.exists_trivialization_baseSet_eq_univ_iff_exists_ne_zero).

## Sources

- [Tau Ceti documentation: `ContMDiffVectorBundle.exists_trivialization_baseSet_eq_univ_iff_exists_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/FrameTrivialization.html#ContMDiffVectorBundle.exists_trivialization_baseSet_eq_univ_iff_exists_ne_zero)
- [Source of `ContMDiffVectorBundle.exists_trivialization_baseSet_eq_univ_iff_exists_ne_zero` in TauCeti/Geometry/Manifold/VectorBundle/FrameTrivialization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/FrameTrivialization.lean#L490)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexManifolds/STATUS.md)
