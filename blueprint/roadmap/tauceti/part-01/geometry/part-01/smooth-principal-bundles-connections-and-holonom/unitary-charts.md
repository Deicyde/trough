---
declaration: def
origin: cited
lean: Bundle.Trivialization.orthonormalLpSectionEquiv
statement: formalized
---

# Unitary charts

Over the base set `U` of an atlas chart `e`, reading sections in the
Gram–Schmidt orthonormal frame of `e` is a linear isometry from `Lᵖ(E, μ|_U)` onto `Lp V p μ|_U`.

```lean
Bundle.Trivialization.orthonormalLpSectionEquiv.{u_1, u_2, u_3, u_4, u_5, u_6} {𝕜 : Type u_1}
  {B : Type u_2} [RCLike 𝕜] [TopologicalSpace B] [MeasurableSpace B] [OpensMeasurableSpace B]
  [SecondCountableTopology B] (p : ENNReal) [Fact (1 ≤ p)] (μ : MeasureTheory.Measure B)
  {F : Type u_3} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {E : B → Type u_4}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(x : B) → NormedAddCommGroup (E x)]
  [(x : B) → InnerProductSpace 𝕜 (E x)] [FiberBundle F E] [VectorBundle 𝕜 F E]
  [TauCeti.ContinuousFiberNorm F E] {V : Type u_5} [NormedAddCommGroup V] [InnerProductSpace 𝕜 V]
  {ι : Type u_6} [Fintype ι] [LinearOrder ι] [LocallyFiniteOrderBot ι]
  (e : Bundle.Trivialization F Bundle.TotalSpace.proj) [MemTrivializationAtlas e]
  (c : Module.Basis ι 𝕜 F) (b : OrthonormalBasis ι 𝕜 V) :
  TauCeti.LpSection 𝕜 F E p (μ.restrict e.baseSet) ≃ₗᵢ[𝕜]
    ↥(MeasureTheory.Lp V p (μ.restrict e.baseSet))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Bundle.Trivialization.orthonormalLpSectionEquiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSection/Chart.html#Bundle.Trivialization.orthonormalLpSectionEquiv).

## Sources

- [Tau Ceti documentation: `Bundle.Trivialization.orthonormalLpSectionEquiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSection/Chart.html#Bundle.Trivialization.orthonormalLpSectionEquiv)
- [Source of `Bundle.Trivialization.orthonormalLpSectionEquiv` in TauCeti/MeasureTheory/Function/LpSection/Chart.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/LpSection/Chart.lean#L106)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
