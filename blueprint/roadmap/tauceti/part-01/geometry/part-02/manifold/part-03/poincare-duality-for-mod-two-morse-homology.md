---
declaration: theorem
origin: cited
lean: TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_neg
statement: formalized
proof: formalized
---

# Poincaré duality for mod-two Morse homology

On a compact boundaryless manifold of
dimension `m`, for `k ≤ m`, the mod-two Morse homology of `-f` and `-X` in degree `k` has the
dimension of the mod-two Morse homology of `f` and `X` in degree `m - k`.

```lean
TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_neg.{u_1, u_2}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  [CompactSpace M] [T2Space M] {f : M → ℝ} {X : (x : M) → TangentSpace (modelWithCornersSelf ℝ E) x}
  {hX : TauCeti.IsAdaptedPseudoGradient f X} (h : hX.IsMorseSmale)
  (hf : TauCeti.IsMorse (modelWithCornersSelf ℝ E) f) {k : ℕ} (hk : k ≤ Module.finrank ℝ E) :
  Module.finrank (ZMod 2) ↑(HomologicalComplex.homology (⋯.morseComplex ⋯) k) =
    Module.finrank (ZMod 2)
      ↑(HomologicalComplex.homology (h.morseComplex hf) (Module.finrank ℝ E - k))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The mod-two Morse boundary squares to zero](../../../../analysis/part-01/analytic-heegaard-floer-homology/the-mod-two-morse-boundary-squares-to-zero.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_neg`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/Duality.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_neg).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_neg`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/Duality.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_neg)
- [Source of `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_neg` in TauCeti/Geometry/Manifold/Morse/Boundary/Duality.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Boundary/Duality.lean#L185)
