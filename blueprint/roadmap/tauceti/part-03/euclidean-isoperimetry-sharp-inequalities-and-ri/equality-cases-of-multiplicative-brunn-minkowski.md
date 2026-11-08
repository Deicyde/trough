---
declaration: theorem
origin: cited
lean: Convex.volume_smul_add_smul_eq_iff
statement: formalized
proof: formalized
---

# Equality cases of multiplicative Brunn–Minkowski for convex bodies

Let `K` and `L` be
compact convex sets of positive volume and `0 < θ < 1`. Then
`volume ((1 - θ) • K + θ • L) = volume K ^ (1 - θ) * volume L ^ θ` exactly when `L` is a translate
of `K`.

```lean
Convex.volume_smul_add_smul_eq_iff.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {K L : Set E}
  (hK : Convex ℝ K) (hKc : IsCompact K) (hK0 : MeasureTheory.volume K ≠ 0) (hL : Convex ℝ L)
  (hLc : IsCompact L) (hL0 : MeasureTheory.volume L ≠ 0) {θ : ℝ} (hθ₀ : 0 < θ) (hθ₁ : θ < 1) :
  MeasureTheory.volume ((1 - θ) • K + θ • L) =
      MeasureTheory.volume K ^ (1 - θ) * MeasureTheory.volume L ^ θ ↔
    ∃ v, L = v +ᵥ K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.hasPrekopaLeindler_volume](tauceti-hasprekopaleindler-volume.md)

## Lean

Formalized in Tau Ceti as [`Convex.volume_smul_add_smul_eq_iff`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Homothety.html#Convex.volume_smul_add_smul_eq_iff).

## Sources

- [Tau Ceti documentation: `Convex.volume_smul_add_smul_eq_iff`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Homothety.html#Convex.volume_smul_add_smul_eq_iff)
- [Source of `Convex.volume_smul_add_smul_eq_iff` in TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Homothety.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Homothety.lean#L136)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Isoperimetry/STATUS.md)
