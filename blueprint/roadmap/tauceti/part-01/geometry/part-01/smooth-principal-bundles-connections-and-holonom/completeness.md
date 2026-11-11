---
declaration: theorem
origin: cited
lean: TauCeti.LpSection.instCompleteSpace
statement: formalized
proof: formalized
---

# Completeness

For a finite-rank bundle with continuous fibre metric over a second-countable
base, `Lᵖ(E, μ)` is complete for every measure `μ` on the Borel sets of the base.

```lean
TauCeti.LpSection.instCompleteSpace.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {B : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [TopologicalSpace B] [MeasurableSpace B] [OpensMeasurableSpace B]
  [SecondCountableTopology B] [NormedAddCommGroup F] [NormedSpace 𝕜 F] {E : B → Type u_4}
  [TopologicalSpace (Bundle.TotalSpace F E)] {p : ENNReal} {μ : MeasureTheory.Measure B}
  [(x : B) → NormedAddCommGroup (E x)] [(x : B) → InnerProductSpace 𝕜 (E x)] [FiberBundle F E]
  [VectorBundle 𝕜 F E] [TauCeti.ContinuousFiberNorm F E] [FiniteDimensional 𝕜 F] [Fact (1 ≤ p)] :
  CompleteSpace (TauCeti.LpSection 𝕜 F E p μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Existence of measurable isometric frames](existence-of-measurable-isometric-frames.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LpSection.instCompleteSpace`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSection/Basic.html#TauCeti.LpSection.instCompleteSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.LpSection.instCompleteSpace`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSection/Basic.html#TauCeti.LpSection.instCompleteSpace)
- [Source of `TauCeti.LpSection.instCompleteSpace` in TauCeti/MeasureTheory/Function/LpSection/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/LpSection/Basic.lean#L486)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
