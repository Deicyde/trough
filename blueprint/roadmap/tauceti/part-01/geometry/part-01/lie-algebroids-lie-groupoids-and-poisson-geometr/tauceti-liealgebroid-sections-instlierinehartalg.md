---
declaration: theorem
origin: cited
lean: TauCeti.LieAlgebroid.Sections.instLieRinehartAlgebra
statement: formalized
proof: formalized
---

# TauCeti.LieAlgebroid.Sections.instLieRinehartAlgebra

The sections of a Lie algebroid form a Lie–Rinehart algebra over the smooth functions.

```lean
TauCeti.LieAlgebroid.Sections.instLieRinehartAlgebra.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  {H : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] {V : M → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] (A : TauCeti.LieAlgebroid I F V) [FiniteDimensional ℝ E] [T2Space M]
  [ContMDiffVectorBundle (↑⊤) F V I] :
  LieRinehartAlgebra ℝ (ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤) A.Sections
```

## Depends on

- [TauCeti.LieAlgebroid](tauceti-liealgebroid.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LieAlgebroid.Sections.instLieRinehartAlgebra`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LieAlgebroid/Basic.html#TauCeti.LieAlgebroid.Sections.instLieRinehartAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.LieAlgebroid.Sections.instLieRinehartAlgebra`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LieAlgebroid/Basic.html#TauCeti.LieAlgebroid.Sections.instLieRinehartAlgebra)
- [Source of `TauCeti.LieAlgebroid.Sections.instLieRinehartAlgebra` in TauCeti/Geometry/Manifold/LieAlgebroid/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/LieAlgebroid/Basic.lean#L355)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
