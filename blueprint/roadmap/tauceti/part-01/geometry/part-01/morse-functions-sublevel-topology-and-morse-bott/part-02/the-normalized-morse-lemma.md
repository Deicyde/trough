---
declaration: theorem
origin: cited
lean: TauCeti.MorseChart.eq_quadratic_normalizedChart, TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart_subset, TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart
statement: formalized
proof: formalized
---

# The normalized Morse lemma

On the whole source of a Morse chart,
`f y = f x - Σ_{i < λ} (ψ y)ᵢ² + Σ_{i ≥ λ} (ψ y)ᵢ²` in the normalized chart `ψ`, where `λ` is the
Morse index.

```lean
TauCeti.MorseChart.eq_quadratic_normalizedChart.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {M : Type u_2} [TopologicalSpace M] [ChartedSpace E M] {f : M → ℝ} {x : M}
  (φ : TauCeti.MorseChart E f x) [FiniteDimensional ℝ E] {y : M} (hy : y ∈ φ.toChart.source) :
  f y =
    f x +
      ∑ i,
        (if ↑i < TauCeti.manifoldMorseIndex (modelWithCornersSelf ℝ E) f x then -1 else 1) *
          (↑φ.normalizedChart.toPartialEquiv y).ofLp i ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse lemma on a manifold](../part-01/the-morse-lemma-on-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MorseChart.eq_quadratic_normalizedChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/NormalizedChart.html#TauCeti.MorseChart.eq_quadratic_normalizedChart).

## Other forms

**The normalized Morse lemma in a prescribed neighbourhood.** Formalized in Tau Ceti as [`TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/NormalizedChart.html#TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart_subset).

```lean
TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart_subset.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  {M : Type u_3} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] {f : M → ℝ} {x : M}
  (hf : ∀ᶠ (y : M) in nhds x, ContMDiffAt I (modelWithCornersSelf ℝ ℝ) (↑⊤) f y)
  (h : TauCeti.IsManifoldNondegenerateCriticalPoint I f x) {U : Set M} (hU : U ∈ nhds x) :
  ∃ ψ,
    x ∈ ψ.source ∧
      ψ.source ⊆ U ∧
        ↑ψ.toPartialEquiv x = 0 ∧
          ∀ y ∈ ψ.source,
            f y =
              f x +
                ∑ i,
                  (if ↑i < TauCeti.manifoldMorseIndex I f x then -1 else 1) *
                    (↑ψ.toPartialEquiv y).ofLp i ^ 2
```

**The normalized Morse lemma on a manifold.** Formalized in Tau Ceti as [`TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/NormalizedChart.html#TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart).

```lean
TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  {M : Type u_3} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] {f : M → ℝ} {x : M}
  (hf : ∀ᶠ (y : M) in nhds x, ContMDiffAt I (modelWithCornersSelf ℝ ℝ) (↑⊤) f y)
  (h : TauCeti.IsManifoldNondegenerateCriticalPoint I f x) :
  ∃ ψ,
    x ∈ ψ.source ∧
      ↑ψ.toPartialEquiv x = 0 ∧
        ∀ y ∈ ψ.source,
          f y =
            f x +
              ∑ i,
                (if ↑i < TauCeti.manifoldMorseIndex I f x then -1 else 1) *
                  (↑ψ.toPartialEquiv y).ofLp i ^ 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.MorseChart.eq_quadratic_normalizedChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/NormalizedChart.html#TauCeti.MorseChart.eq_quadratic_normalizedChart)
- [Source of `TauCeti.MorseChart.eq_quadratic_normalizedChart` in TauCeti/Geometry/Manifold/Morse/NormalizedChart.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/NormalizedChart.lean#L177)
