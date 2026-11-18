---
declaration: theorem
origin: cited
lean: TauCeti.fourier_twoPiHermiteFunctionLp
statement: formalized
proof: formalized
---

# The Fourier eigenrelation for the unitary Fourier transform of `L²(ℝ; ℂ)`

The `n`-th
rescaled Hermite function is an eigenvector of `MeasureTheory.Lp.fourierTransformₗᵢ` with
eigenvalue `(-i)ⁿ`.

```lean
TauCeti.fourier_twoPiHermiteFunctionLp (n : ℕ) :
  FourierTransform.fourier (TauCeti.twoPiHermiteFunctionLp ℂ n) =
    (-Complex.I) ^ n • TauCeti.twoPiHermiteFunctionLp ℂ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fourier eigenfunction theorem](fourier-eigenfunction-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.fourier_twoPiHermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/HilbertBasis.html#TauCeti.fourier_twoPiHermiteFunctionLp).

## Sources

- [Tau Ceti documentation: `TauCeti.fourier_twoPiHermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/HilbertBasis.html#TauCeti.fourier_twoPiHermiteFunctionLp)
- [Source of `TauCeti.fourier_twoPiHermiteFunctionLp` in TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/HilbertBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/HilbertBasis.lean#L332)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalL2Bases/STATUS.md)
