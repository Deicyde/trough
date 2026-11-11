---
declaration: theorem
origin: cited
lean: InnerProductSpace.finrank_pointSpectralSubspace_Iio_continuousLinearMapOfBilin, InnerProductSpace.finrank_pointSpectralSubspace_Ioi_continuousLinearMapOfBilin
statement: formalized
proof: formalized
---

# Sylvester's law of inertia, spectrally

The negative index of inertia of a symmetric real
bilinear form on a finite-dimensional inner product space is the dimension of the negative
spectral subspace of its Riesz operator.

```lean
InnerProductSpace.finrank_pointSpectralSubspace_Iio_continuousLinearMapOfBilin.{u_1} {W : Type u_1}
  [NormedAddCommGroup W] [InnerProductSpace ℝ W] [FiniteDimensional ℝ W] {B : W →L[ℝ] W →L[ℝ] ℝ}
  (hB : ∀ (v w : W), (B v) w = (B w) v) :
  Module.finrank ℝ
      ↥(Module.End.pointSpectralSubspace (↑(InnerProductSpace.continuousLinearMapOfBilin B))
          (Set.Iio 0)) =
    sigNeg (LinearMap.BilinMap.toQuadraticMap B.toBilinForm)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`InnerProductSpace.finrank_pointSpectralSubspace_Iio_continuousLinearMapOfBilin`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Spectral/Inertia.html#InnerProductSpace.finrank_pointSpectralSubspace_Iio_continuousLinearMapOfBilin).

## Other forms

**Sylvester's law of inertia, spectrally, positive part.** Formalized in Tau Ceti as [`InnerProductSpace.finrank_pointSpectralSubspace_Ioi_continuousLinearMapOfBilin`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Spectral/Inertia.html#InnerProductSpace.finrank_pointSpectralSubspace_Ioi_continuousLinearMapOfBilin).

```lean
InnerProductSpace.finrank_pointSpectralSubspace_Ioi_continuousLinearMapOfBilin.{u_1} {W : Type u_1}
  [NormedAddCommGroup W] [InnerProductSpace ℝ W] [FiniteDimensional ℝ W] {B : W →L[ℝ] W →L[ℝ] ℝ}
  (hB : ∀ (v w : W), (B v) w = (B w) v) :
  Module.finrank ℝ
      ↥(Module.End.pointSpectralSubspace (↑(InnerProductSpace.continuousLinearMapOfBilin B))
          (Set.Ioi 0)) =
    sigPos (LinearMap.BilinMap.toQuadraticMap B.toBilinForm)
```

## Sources

- [Tau Ceti documentation: `InnerProductSpace.finrank_pointSpectralSubspace_Iio_continuousLinearMapOfBilin`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Spectral/Inertia.html#InnerProductSpace.finrank_pointSpectralSubspace_Iio_continuousLinearMapOfBilin)
- [Source of `InnerProductSpace.finrank_pointSpectralSubspace_Iio_continuousLinearMapOfBilin` in TauCeti/Analysis/InnerProductSpace/Spectral/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Spectral/Inertia.lean#L131)
