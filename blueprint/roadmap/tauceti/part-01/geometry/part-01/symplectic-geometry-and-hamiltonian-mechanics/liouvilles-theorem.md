---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsSymplectic.measurePreserving_globalFlowDiffeomorph_liouvilleMeasure
statement: formalized
proof: formalized
---

# Liouville's theorem

For a symplectic form `σ` and a smooth function `f` with complete
Hamiltonian vector field, every time-`t` map of the Hamiltonian flow of `f` preserves the Liouville
measure.

```lean
TauCeti.SmoothTwoForm.IsSymplectic.measurePreserving_globalFlowDiffeomorph_liouvilleMeasure.{u_1,
    u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [MeasurableSpace M] [BorelSpace M] [LindelofSpace M]
  {n : ℕ} [hn : Fact (Module.finrank ℝ E = 2 * n)] [T2Space M] [I.Boundaryless]
  {σ : TauCeti.SmoothTwoForm I M} {f : M → ℝ} (hσ : σ.IsSymplectic)
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f)
  (hc : TauCeti.IsCompleteVectorField (σ.hamiltonianVectorField f)) (t : ℝ) :
  MeasureTheory.MeasurePreserving (⇑(TauCeti.globalFlowDiffeomorph hc ⋯ ⋯ t))
    (TauCeti.SmoothTwoForm.liouvilleMeasure n σ) (TauCeti.SmoothTwoForm.liouvilleMeasure n σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../../part-02/manifold/part-01/cartans-magic-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.measurePreserving_globalFlowDiffeomorph_liouvilleMeasure`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/LiouvilleMeasure.html#TauCeti.SmoothTwoForm.IsSymplectic.measurePreserving_globalFlowDiffeomorph_liouvilleMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsSymplectic.measurePreserving_globalFlowDiffeomorph_liouvilleMeasure`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/LiouvilleMeasure.html#TauCeti.SmoothTwoForm.IsSymplectic.measurePreserving_globalFlowDiffeomorph_liouvilleMeasure)
- [Source of `TauCeti.SmoothTwoForm.IsSymplectic.measurePreserving_globalFlowDiffeomorph_liouvilleMeasure` in TauCeti/Geometry/Symplectic/Manifold/LiouvilleMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Manifold/LiouvilleMeasure.lean#L150)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
