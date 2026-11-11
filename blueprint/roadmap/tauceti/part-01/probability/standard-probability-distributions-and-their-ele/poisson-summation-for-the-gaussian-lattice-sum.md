---
declaration: theorem
origin: cited
lean: Real.gaussianLatticeSum_eq_fourier
statement: formalized
proof: formalized
---

# Poisson summation for the Gaussian lattice sum

`Z(c, s)` is the absolutely convergent
Fourier series with coefficients `sqrt (2π) |s| exp (-2π²s²n²)`.

```lean
Real.gaussianLatticeSum_eq_fourier (c s : ℝ) :
  c.gaussianLatticeSum s =
    √(2 * Real.pi) * |s| *
      ∑' (n : ℤ), Real.exp (-2 * Real.pi ^ 2 * s ^ 2 * ↑n ^ 2) * Real.cos (2 * Real.pi * ↑n * c)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Real.gaussianLatticeSum_eq_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.gaussianLatticeSum_eq_fourier).

## Sources

- [Tau Ceti documentation: `Real.gaussianLatticeSum_eq_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.gaussianLatticeSum_eq_fourier)
- [Source of `Real.gaussianLatticeSum_eq_fourier` in TauCeti/Analysis/SpecialFunctions/Gaussian/PoissonSummation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Gaussian/PoissonSummation.lean#L125)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StandardDistributions/STATUS.md)
