---
declaration: theorem
origin: cited
lean: SchwartzMap.norm_fourierInv_toL2_eq
statement: formalized
proof: formalized
---

# Plancherel's theorem for the inverse Fourier transform of Schwartz functions

```lean
SchwartzMap.norm_fourierInv_toL2_eq.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] (f : SchwartzMap E F) :
  ‖(FourierTransformInv.fourierInv f).toLp 2 MeasureTheory.volume‖ = ‖f.toLp 2 MeasureTheory.volume‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SchwartzMap.norm_fourierInv_toL2_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/Fourier.html#SchwartzMap.norm_fourierInv_toL2_eq).

## Sources

- [Tau Ceti documentation: `SchwartzMap.norm_fourierInv_toL2_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/Fourier.html#SchwartzMap.norm_fourierInv_toL2_eq)
- [Source of `SchwartzMap.norm_fourierInv_toL2_eq` in TauCeti/Analysis/Distribution/SchwartzSpace/Fourier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/SchwartzSpace/Fourier.lean#L329)
