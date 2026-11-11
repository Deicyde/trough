---
declaration: theorem
origin: cited
lean: TauCeti.IsManifoldNondegenerateCriticalPoint.nonempty_morseChart
statement: formalized
proof: formalized
---

# The Morse lemma on a manifold

At a nondegenerate critical point `x` of a function `f`
that is smooth at every point of a neighbourhood of `x`, on a manifold modelled on a
finite-dimensional real normed space `E`, there is a Morse chart: a chart `ψ` of the maximal atlas,
centred at `x`, and a linear change of coordinates `L : E ≃ (Fin n → ℝ)` such that on the source
of `ψ`

`f y = f x + (1/2) Σᵢ wᵢ (L (ψ y))ᵢ²`,

where every weight `wᵢ` is `-1` or `1` and the number of negative weights is the manifold Morse
index of `f` at `x`.

```lean
TauCeti.IsManifoldNondegenerateCriticalPoint.nonempty_morseChart.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {M : Type u_2} [TopologicalSpace M] [ChartedSpace E M]
  {f : M → ℝ} {x : M} [FiniteDimensional ℝ E] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  (hf :
    ∀ᶠ (y : M) in nhds x,
      ContMDiffAt (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ ℝ) (↑⊤) f y)
  (h : TauCeti.IsManifoldNondegenerateCriticalPoint (modelWithCornersSelf ℝ E) f x) :
  Nonempty (TauCeti.MorseChart E f x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local Morse lemma](../../../../analysis/part-02/calculus/part-01/the-local-morse-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsManifoldNondegenerateCriticalPoint.nonempty_morseChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Lemma.html#TauCeti.IsManifoldNondegenerateCriticalPoint.nonempty_morseChart).

## Sources

- [Tau Ceti documentation: `TauCeti.IsManifoldNondegenerateCriticalPoint.nonempty_morseChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Lemma.html#TauCeti.IsManifoldNondegenerateCriticalPoint.nonempty_morseChart)
- [Source of `TauCeti.IsManifoldNondegenerateCriticalPoint.nonempty_morseChart` in TauCeti/Geometry/Manifold/Morse/Lemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Lemma.lean#L394)
