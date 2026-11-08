---
declaration: theorem
origin: cited
lean: TauCeti.fourier_twoPiHermiteFunction
statement: formalized
proof: formalized
---

# Fourier eigenfunction theorem

For Mathlib's `exp (-2πixξ)` convention, the rescaled
Hermite function `Φₙ(x) = √(√(2π)) ψₙ(√(2π)x)` has eigenvalue `(-i)ⁿ`.

```lean
TauCeti.fourier_twoPiHermiteFunction (n : ℕ) :
  (FourierTransform.fourier fun x => ↑(TauCeti.twoPiHermiteFunction n x)) = fun x =>
    (-Complex.I) ^ n * ↑(TauCeti.twoPiHermiteFunction n x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fourier_twoPiHermiteFunction`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/Basic.html#TauCeti.fourier_twoPiHermiteFunction).

## Sources

- [Tau Ceti documentation: `TauCeti.fourier_twoPiHermiteFunction`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/Basic.html#TauCeti.fourier_twoPiHermiteFunction)
- [Source of `TauCeti.fourier_twoPiHermiteFunction` in TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/Basic.lean#L431)
