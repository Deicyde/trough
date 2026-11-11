---
declaration: theorem
origin: cited
lean: MeasureTheory.VectorMeasure.withDensityᵥ_scalarRNDeriv
statement: formalized
proof: formalized
---

# Scalar Radon–Nikodym theorem

If the variation of a scalar measure is absolutely
continuous with respect to a sigma-finite measure, its scalar density reconstructs it.

```lean
MeasureTheory.VectorMeasure.withDensityᵥ_scalarRNDeriv.{u_1, u_2} {X : Type u_1} {𝕜 : Type u_2}
  [MeasurableSpace X] [RCLike 𝕜] (μ : MeasureTheory.VectorMeasure X 𝕜) (ν : MeasureTheory.Measure X)
  [MeasureTheory.SigmaFinite ν] (hμν : μ.variation.AbsolutelyContinuous ν) :
  ν.withDensityᵥ (μ.scalarRNDeriv ν) = μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.VectorMeasure.withDensityᵥ_scalarRNDeriv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/VectorMeasure/Decomposition/RadonNikodym.html#MeasureTheory.VectorMeasure.withDensity%E1%B5%A5_scalarRNDeriv).

## Sources

- [Tau Ceti documentation: `MeasureTheory.VectorMeasure.withDensityᵥ_scalarRNDeriv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/VectorMeasure/Decomposition/RadonNikodym.html#MeasureTheory.VectorMeasure.withDensity%E1%B5%A5_scalarRNDeriv)
- [Source of `MeasureTheory.VectorMeasure.withDensityᵥ_scalarRNDeriv` in TauCeti/MeasureTheory/VectorMeasure/Decomposition/RadonNikodym.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/VectorMeasure/Decomposition/RadonNikodym.lean#L103)
