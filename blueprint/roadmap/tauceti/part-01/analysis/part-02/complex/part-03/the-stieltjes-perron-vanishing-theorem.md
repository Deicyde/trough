---
declaration: theorem
origin: cited
lean: TauCeti.measure_Icc_eq_zero_of_eq_nevanlinnaKernel_add
statement: formalized
proof: formalized
---

# The Stieltjes--Perron vanishing theorem

A Nevanlinna measure gives no mass to a compact
interval over which the imaginary part of the represented function is continuous up to the real
axis and vanishes there.  Continuity is asked for on the closed rectangle of any positive height
`d` over the interval, as a function holomorphic near the interval supplies it.

```lean
TauCeti.measure_Icc_eq_zero_of_eq_nevanlinnaKernel_add {F : ℂ → ℂ} {mu : MeasureTheory.Measure ℝ}
  {beta c : ℝ} [MeasureTheory.IsFiniteMeasure mu]
  (hrep :
    ∀ z ∈ UpperHalfPlane.upperHalfPlaneSet,
      F z = ↑beta * z + ∫ (x : ℝ), TauCeti.nevanlinnaKernel z x ∂mu + ↑c)
  {a b d : ℝ} (hab : a < b) (hd : 0 < d)
  (hcont : ContinuousOn (fun z => (F z).im) (Set.Icc a b ×ℂ Set.Icc 0 d))
  (hzero : ∀ u ∈ Set.Icc a b, (F ↑u).im = 0) : mu (Set.Icc a b) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poisson lower bound of a Nevanlinna representation](the-poisson-lower-bound-of-a-nevanlinna-represen.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.measure_Icc_eq_zero_of_eq_nevanlinnaKernel_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pick/Boundary.html#TauCeti.measure_Icc_eq_zero_of_eq_nevanlinnaKernel_add).

## Sources

- [Tau Ceti documentation: `TauCeti.measure_Icc_eq_zero_of_eq_nevanlinnaKernel_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pick/Boundary.html#TauCeti.measure_Icc_eq_zero_of_eq_nevanlinnaKernel_add)
- [Source of `TauCeti.measure_Icc_eq_zero_of_eq_nevanlinnaKernel_add` in TauCeti/Analysis/Complex/Pick/Boundary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Pick/Boundary.lean#L176)
