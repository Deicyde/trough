---
declaration: theorem
origin: cited
lean: MeasureTheory.Integrable.eLpNorm_fourier_le
statement: formalized
proof: formalized
---

# The Hausdorff–Young inequality

For `1 ≤ p ≤ 2` the Fourier integral of an integrable
complex function satisfies `‖𝓕 f‖_{p'} ≤ ‖f‖_p`, where `p' = p.conjExponent` is the conjugate
exponent.

```lean
MeasureTheory.Integrable.eLpNorm_fourier_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {f : E → ℂ}
  (hf : MeasureTheory.Integrable f MeasureTheory.volume) {p : ENNReal} (hp₁ : 1 ≤ p) (hp₂ : p ≤ 2) :
  MeasureTheory.eLpNorm (FourierTransform.fourier f) p.conjExponent MeasureTheory.volume ≤
    MeasureTheory.eLpNorm f p MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Plancherel's theorem on `L¹ ∩ L²`](plancherels-theorem-on-l1-l2.md)
- [The Riesz–Thorin interpolation theorem](../../../measure-theory/integral/part-02/the-riesz-thorin-interpolation-theorem.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Integrable.eLpNorm_fourier_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/HausdorffYoung.html#MeasureTheory.Integrable.eLpNorm_fourier_le).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Integrable.eLpNorm_fourier_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/HausdorffYoung.html#MeasureTheory.Integrable.eLpNorm_fourier_le)
- [Source of `MeasureTheory.Integrable.eLpNorm_fourier_le` in TauCeti/Analysis/Fourier/HausdorffYoung.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/HausdorffYoung.lean#L134)
