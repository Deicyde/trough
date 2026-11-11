---
declaration: theorem
origin: cited
lean: Real.fourierInv_mul_convolution_eq
statement: formalized
proof: formalized
---

# The convolution theorem for the inverse Fourier transform

The inverse Fourier transform
of the convolution of two integrable functions is the product of their inverse Fourier
transforms.

```lean
Real.fourierInv_mul_convolution_eq.{u_1, u_2} {E : Type u_1} {R : Type u_2} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] [NormedRing R]
  [NormedSpace ℂ R] [IsScalarTower ℂ R R] [SMulCommClass ℂ R R] [CompleteSpace R] {f₁ f₂ : E → R}
  (hf₁ : MeasureTheory.Integrable f₁ MeasureTheory.volume)
  (hf₂ : MeasureTheory.Integrable f₂ MeasureTheory.volume) (x : E) :
  FourierTransformInv.fourierInv
      (MeasureTheory.convolution f₁ f₂ (ContinuousLinearMap.mul ℂ R) MeasureTheory.volume) x =
    FourierTransformInv.fourierInv f₁ x * FourierTransformInv.fourierInv f₂ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Real.fourierInv_mul_convolution_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Convolution.html#Real.fourierInv_mul_convolution_eq).

## Sources

- [Tau Ceti documentation: `Real.fourierInv_mul_convolution_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Convolution.html#Real.fourierInv_mul_convolution_eq)
- [Source of `Real.fourierInv_mul_convolution_eq` in TauCeti/Analysis/Fourier/Convolution.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/Convolution.lean#L36)
