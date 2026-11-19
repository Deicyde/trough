---
declaration: theorem
origin: cited
lean: TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_le
statement: formalized
proof: formalized
---

# The weak Morse inequality for Morse homology

The mod-two Morse homology in degree `n` has
dimension at most the number of critical points of index `n`.

```lean
TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_le.{u_1, u_2}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  [CompactSpace M] [T2Space M] {f : M → ℝ} {X : (x : M) → TangentSpace (modelWithCornersSelf ℝ E) x}
  {hX : TauCeti.IsAdaptedPseudoGradient f X} (h : hX.IsMorseSmale)
  (hf : TauCeti.IsMorse (modelWithCornersSelf ℝ E) f) (n : ℕ) :
  Module.finrank (ZMod 2) ↑(HomologicalComplex.homology (h.morseComplex hf) n) ≤
    (TauCeti.criticalCount (modelWithCornersSelf ℝ E) f n).toNat
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The mod-two Morse boundary squares to zero](../../../../analysis/part-01/analytic-heegaard-floer-homology/the-mod-two-morse-boundary-squares-to-zero.md)
- [The weak Morse inequality](../../../../algebra/part-02/homology/the-weak-morse-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/ChainComplex.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_le).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/ChainComplex.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_le)
- [Source of `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.finrank_homology_morseComplex_le` in TauCeti/Geometry/Manifold/Morse/Boundary/ChainComplex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Boundary/ChainComplex.lean#L237)
