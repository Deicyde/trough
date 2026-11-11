---
declaration: def
origin: cited
lean: TauCeti.weightL2Isometry
statement: formalized
---

# The weight ↔ measure isometry

For an almost-everywhere-positive weight `w`, multiplication
by `√w` is a linear isometric equivalence `L²(w·μ; E) ≃ₗᵢ[𝕜] L²(μ; E)`.

```lean
TauCeti.weightL2Isometry.{u_1, u_2, u_3} (𝕜 : Type u_1) {E : Type u_2} {α : Type u_3} [NormedRing 𝕜]
  [NormedAddCommGroup E] [NormedSpace ℝ E] [_root_.Module 𝕜 E] [IsBoundedSMul 𝕜 E]
  [SMulCommClass ℝ 𝕜 E] [MeasurableSpace α] (μ : MeasureTheory.Measure α) (w : α → ℝ)
  (hwpos : ∀ᵐ (x : α) ∂μ, 0 < w x) (hwm : AEMeasurable w μ) :
  ↥(MeasureTheory.Lp E 2 (μ.withDensity fun x => ENNReal.ofReal (w x))) ≃ₗᵢ[𝕜]
    ↥(MeasureTheory.Lp E 2 μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.weightL2Isometry`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/WeightL2Isometry.html#TauCeti.weightL2Isometry).

## Sources

- [Tau Ceti documentation: `TauCeti.weightL2Isometry`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/WeightL2Isometry.html#TauCeti.weightL2Isometry)
- [Source of `TauCeti.weightL2Isometry` in TauCeti/MeasureTheory/Function/WeightL2Isometry.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/WeightL2Isometry.lean#L91)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalL2Bases/STATUS.md)
