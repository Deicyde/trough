---
declaration: theorem
origin: cited
lean: MeasureTheory.Integrable.eLpNorm_fourier_two_eq
statement: formalized
proof: formalized
---

# Plancherel's theorem on `L¹ ∩ L²`

The Fourier integral of an integrable, square
integrable function has the same `L²` norm as the function.

```lean
MeasureTheory.Integrable.eLpNorm_fourier_two_eq.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] {f : E → F}
  (hf : MeasureTheory.Integrable f MeasureTheory.volume)
  (hf₂ : MeasureTheory.MemLp f 2 MeasureTheory.volume) :
  MeasureTheory.eLpNorm (FourierTransform.fourier f) 2 MeasureTheory.volume =
    MeasureTheory.eLpNorm f 2 MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Integrable.eLpNorm_fourier_two_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/LpSpace.html#MeasureTheory.Integrable.eLpNorm_fourier_two_eq).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Integrable.eLpNorm_fourier_two_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/LpSpace.html#MeasureTheory.Integrable.eLpNorm_fourier_two_eq)
- [Source of `MeasureTheory.Integrable.eLpNorm_fourier_two_eq` in TauCeti/Analysis/Fourier/LpSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/LpSpace.lean#L68)
