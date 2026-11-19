---
declaration: theorem
origin: cited
lean: TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary
statement: formalized
proof: formalized
---

# The mod-two Morse boundary squares to zero

For a Morse function on a compact
boundaryless manifold and a Morse–Smale adapted pseudo-gradient, `∂ ∘ ∂ = 0`.

```lean
TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary.{u_1, u_2}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  [CompactSpace M] [T2Space M] {f : M → ℝ} {X : (x : M) → TangentSpace (modelWithCornersSelf ℝ E) x}
  {hX : TauCeti.IsAdaptedPseudoGradient f X} (h : hX.IsMorseSmale)
  (hf : TauCeti.IsMorse (modelWithCornersSelf ℝ E) f) : h.morseBoundary hf ∘ₗ h.morseBoundary hf = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../../geometry/part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/Differential.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/Differential.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary)
- [Source of `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary` in TauCeti/Geometry/Manifold/Morse/Boundary/Differential.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Boundary/Differential.lean#L109)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HeegaardFloer/STATUS.md)
