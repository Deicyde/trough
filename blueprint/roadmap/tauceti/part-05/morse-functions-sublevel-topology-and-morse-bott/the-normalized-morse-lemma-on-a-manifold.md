---
declaration: theorem
origin: cited
lean: TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart
statement: formalized
proof: formalized
---

# The normalized Morse lemma on a manifold

At a nondegenerate critical point `x` of a
function `f` which is smooth near `x`, on a manifold with a boundaryless model, there is a partial
diffeomorphism `ψ` onto an open subset of `EuclideanSpace ℝ (Fin m)`, `m = dim M`, with
`ψ x = 0` and

`f y = f x - Σ_{i < λ} (ψ y)ᵢ² + Σ_{i ≥ λ} (ψ y)ᵢ²`

on its whole source, where `λ` is the manifold Morse index of `f` at `x`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/NormalizedChart.html#TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart).

## Sources

- [Tau Ceti documentation: `TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/NormalizedChart.html#TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart)
- [Source of `TauCeti.IsManifoldNondegenerateCriticalPoint.exists_normalized_morseChart` in TauCeti/Geometry/Manifold/Morse/NormalizedChart.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/NormalizedChart.lean#L191)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
