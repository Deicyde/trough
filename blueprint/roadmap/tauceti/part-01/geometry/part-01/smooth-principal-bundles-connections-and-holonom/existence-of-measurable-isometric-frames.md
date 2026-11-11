---
declaration: theorem
origin: cited
lean: TauCeti.exists_isMeasurableIsometricFrame
statement: formalized
proof: formalized
---

# Existence of measurable isometric frames

A finite-rank vector bundle with continuous fibre
metric over a second-countable base has a global measurable isometric frame, modelled on any
finite-dimensional inner product space `V` of the same dimension as the model fibre, for every
measure on the base. It is obtained by gluing Gram–Schmidt frames of countably many atlas charts
along the Borel partition of the base they induce.

```lean
TauCeti.exists_isMeasurableIsometricFrame.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1} {B : Type u_2}
  (F : Type u_3) [RCLike 𝕜] [TopologicalSpace B] [MeasurableSpace B] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] (E : B → Type u_4) [TopologicalSpace (Bundle.TotalSpace F E)]
  [(x : B) → NormedAddCommGroup (E x)] [(x : B) → InnerProductSpace 𝕜 (E x)] [FiberBundle F E]
  [VectorBundle 𝕜 F E] (V : Type u_5) [NormedAddCommGroup V] [InnerProductSpace 𝕜 V]
  [OpensMeasurableSpace B] [SecondCountableTopology B] [TauCeti.ContinuousFiberNorm F E]
  [FiniteDimensional 𝕜 F] [FiniteDimensional 𝕜 V] (hV : Module.finrank 𝕜 V = Module.finrank 𝕜 F) :
  ∃ Φ, ∀ (μ : MeasureTheory.Measure B), TauCeti.IsMeasurableIsometricFrame F μ Φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isMeasurableIsometricFrame`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSection/Measurable.html#TauCeti.exists_isMeasurableIsometricFrame).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isMeasurableIsometricFrame`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSection/Measurable.html#TauCeti.exists_isMeasurableIsometricFrame)
- [Source of `TauCeti.exists_isMeasurableIsometricFrame` in TauCeti/MeasureTheory/Function/LpSection/Measurable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/LpSection/Measurable.lean#L410)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
