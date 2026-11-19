---
declaration: theorem
origin: cited
lean: TauCeti.UnitAddTorus.hasSum_norm_sq_mFourierCoeff
statement: formalized
proof: formalized
---

# Parseval's identity in `L²(𝕋ᵈ)`

the squared norm of `f` is the sum of the squared norms of
its Fourier coefficients.

```lean
TauCeti.UnitAddTorus.hasSum_norm_sq_mFourierCoeff.{u_1} {d : Type u_1} [Fintype d]
  (f : ↥(MeasureTheory.Lp ℂ 2 MeasureTheory.volume)) :
  HasSum (fun n => ‖UnitAddTorus.mFourierCoeff (↑↑f) n‖ ^ 2) (‖f‖ ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitAddTorus.hasSum_norm_sq_mFourierCoeff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Torus/Multiplier.html#TauCeti.UnitAddTorus.hasSum_norm_sq_mFourierCoeff).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitAddTorus.hasSum_norm_sq_mFourierCoeff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Torus/Multiplier.html#TauCeti.UnitAddTorus.hasSum_norm_sq_mFourierCoeff)
- [Source of `TauCeti.UnitAddTorus.hasSum_norm_sq_mFourierCoeff` in TauCeti/Analysis/Fourier/Torus/Multiplier.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Torus/Multiplier.lean#L73)
