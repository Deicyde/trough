---
declaration: theorem
origin: cited
lean: Matrix.wassersteinEDist_two_spectralMeasure_sq_le
statement: formalized
proof: formalized
---

# Spectral Wasserstein bound, squared form

The squared `W₂` distance between the
empirical spectral measures is at most the normalized squared Frobenius distance.

```lean
Matrix.wassersteinEDist_two_spectralMeasure_sq_le.{u_1, u_2} {n : Type u_1} {𝕜 : Type u_2}
  [Fintype n] [DecidableEq n] [Nonempty n] [RCLike 𝕜] (A B : Matrix n n 𝕜) (hA : A.IsHermitian)
  (hB : B.IsHermitian) :
  TauCeti.wassersteinEDist 2 ↑(A.spectralMeasure hA) ↑(B.spectralMeasure hB) ^ 2 ≤
    ENNReal.ofReal (‖A - B‖ ^ 2 / ↑(Fintype.card n))
```

## Depends on

- [TauCeti.Probability.empiricalFiniteMeasure](../../../probability/random-matrices/tauceti-probability-empiricalfinitemeasure.md)

## Proof depends on

- [The Hoffman–Wielandt inequality for Hermitian matrices](../../../probability/random-matrices/the-hoffman-wielandt-inequality-for-hermitian-ma.md)

## Lean

Formalized in Tau Ceti as [`Matrix.wassersteinEDist_two_spectralMeasure_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/SpectralMeasure/Wasserstein.html#Matrix.wassersteinEDist_two_spectralMeasure_sq_le).

## Sources

- [Tau Ceti documentation: `Matrix.wassersteinEDist_two_spectralMeasure_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/SpectralMeasure/Wasserstein.html#Matrix.wassersteinEDist_two_spectralMeasure_sq_le)
- [Source of `Matrix.wassersteinEDist_two_spectralMeasure_sq_le` in TauCeti/Analysis/Matrix/SpectralMeasure/Wasserstein.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/SpectralMeasure/Wasserstein.lean#L100)
