---
declaration: theorem
origin: cited
lean: Real.fourier_convolution_eq
statement: formalized
proof: formalized
---

# The convolution theorem for a real kernel

For an integrable real kernel `k` and an
integrable `f`, the Fourier transform of `k ⋆ f` is `𝓕 k • 𝓕 f`, with `k` viewed as complex
valued.

```lean
Real.fourier_convolution_eq.{u_1, u_3} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] {k : E → ℝ} {f : E → F}
  (hk : MeasureTheory.Integrable k MeasureTheory.volume)
  (hf : MeasureTheory.Integrable f MeasureTheory.volume) (ξ : E) :
  FourierTransform.fourier
      (MeasureTheory.convolution k f (ContinuousLinearMap.lsmul ℝ ℝ) MeasureTheory.volume) ξ =
    FourierTransform.fourier (fun x => ↑(k x)) ξ • FourierTransform.fourier f ξ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Real.fourier_convolution_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Convolution.html#Real.fourier_convolution_eq).

## Sources

- [Tau Ceti documentation: `Real.fourier_convolution_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Convolution.html#Real.fourier_convolution_eq)
- [Source of `Real.fourier_convolution_eq` in TauCeti/Analysis/Fourier/Convolution.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Convolution.lean#L47)
