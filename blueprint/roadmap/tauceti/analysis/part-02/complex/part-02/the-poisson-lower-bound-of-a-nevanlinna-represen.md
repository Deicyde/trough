---
declaration: theorem
origin: cited
lean: TauCeti.measureReal_Icc_le_of_eq_nevanlinnaKernel_add
statement: formalized
proof: formalized
---

# The Poisson lower bound of a Nevanlinna representation

The mass a Nevanlinna measure
gives to the interval of centre `u` and half-width `v` is at most `2 v` times the imaginary part
of the represented function at `u + i v`.

```lean
TauCeti.measureReal_Icc_le_of_eq_nevanlinnaKernel_add {F : ℂ → ℂ} {mu : MeasureTheory.Measure ℝ}
  {beta c : ℝ} [MeasureTheory.IsFiniteMeasure mu] (hbeta : 0 ≤ beta)
  (hrep :
    ∀ z ∈ UpperHalfPlane.upperHalfPlaneSet,
      F z = ↑beta * z + ∫ (x : ℝ), TauCeti.nevanlinnaKernel z x ∂mu + ↑c)
  (u : ℝ) {v : ℝ} (hv : 0 < v) :
  mu.real (Set.Icc (u - v) (u + v)) ≤ 2 * v * (F (↑u + ↑v * Complex.I)).im
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.measureReal_Icc_le_of_eq_nevanlinnaKernel_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pick/Boundary.html#TauCeti.measureReal_Icc_le_of_eq_nevanlinnaKernel_add).

## Sources

- [Tau Ceti documentation: `TauCeti.measureReal_Icc_le_of_eq_nevanlinnaKernel_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pick/Boundary.html#TauCeti.measureReal_Icc_le_of_eq_nevanlinnaKernel_add)
- [Source of `TauCeti.measureReal_Icc_le_of_eq_nevanlinnaKernel_add` in TauCeti/Analysis/Complex/Pick/Boundary.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Pick/Boundary.lean#L72)
