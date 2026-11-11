---
declaration: theorem
origin: cited
lean: Convex.logConcave_measure_preimage_prodMk
statement: formalized
proof: formalized
---

# Brunn's principle, in log-concave form

For a measurable convex set `s ⊆ E × F` and a
measure `ν` with the Prékopa–Leindler property at every weight, the measure of the slices,
`x ↦ ν (Prod.mk x ⁻¹' s)`, is log-concave.

```lean
Convex.logConcave_measure_preimage_prodMk.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [MeasurableSpace E] [AddCommMonoid E] [_root_.Module ℝ E] [MeasurableSpace F] [AddCommMonoid F]
  [_root_.Module ℝ F] {ν : MeasureTheory.Measure F}
  (hν : ∀ ⦃θ : ℝ⦄, 0 ≤ θ → θ ≤ 1 → ν.HasPrekopaLeindler θ) {s : Set (E × F)} (hs : MeasurableSet s)
  (hsc : Convex ℝ s) : TauCeti.LogConcave fun x => ν (Prod.mk x ⁻¹' s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Convex.logConcave_measure_preimage_prodMk`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler.html#Convex.logConcave_measure_preimage_prodMk).

## Sources

- [Tau Ceti documentation: `Convex.logConcave_measure_preimage_prodMk`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler.html#Convex.logConcave_measure_preimage_prodMk)
- [Source of `Convex.logConcave_measure_preimage_prodMk` in TauCeti/MeasureTheory/Integral/PrekopaLeindler.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/PrekopaLeindler.lean#L481)
