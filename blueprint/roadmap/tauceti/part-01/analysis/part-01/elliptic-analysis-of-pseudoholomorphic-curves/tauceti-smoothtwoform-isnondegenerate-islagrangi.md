---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding.isTotallyRealEmbedding
statement: formalized
proof: formalized
---

# TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding.isTotallyRealEmbedding

On a nonempty source, a Lagrangian embedding is a smooth totally real embedding for every
smooth almost complex structure tamed by the ambient form.

```lean
TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding.isTotallyRealEmbedding.{u_1, u_2, u_3,
    u_4, u_5, u_6}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} {F : Type u_4} {H' : Type u_5} {N : Type u_6}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [TopologicalSpace H'] {I' : ModelWithCorners ℝ F H'} [TopologicalSpace N] [ChartedSpace H' N]
  {f : N → M} [FiniteDimensional ℝ E] [FiniteDimensional ℝ F] [IsManifold I (↑⊤) M]
  {σ : TauCeti.SmoothTwoForm I M} {hσ : σ.IsNondegenerate} [Nonempty N]
  (h : TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding I' hσ f)
  {J : TauCeti.SmoothAlmostComplexStructure I M} (htame : σ.Tames J) :
  TauCeti.IsTotallyRealEmbedding I' I (↑⊤) J.almostComplexStructureAt f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding.isTotallyRealEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/TotallyReal/Basic.html#TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding.isTotallyRealEmbedding).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding.isTotallyRealEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/TotallyReal/Basic.html#TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding.isTotallyRealEmbedding)
- [Source of `TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianEmbedding.isTotallyRealEmbedding` in TauCeti/Geometry/Manifold/Complex/TotallyReal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/TotallyReal/Basic.lean#L269)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
