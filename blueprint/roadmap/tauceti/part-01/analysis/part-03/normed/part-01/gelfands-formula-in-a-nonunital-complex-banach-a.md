---
declaration: theorem
origin: cited
lean: TauCeti.spectralRadius_eq_gelfandRadius_toLp_inr
statement: formalized
proof: formalized
---

# Gelfand's formula in a nonunital complex Banach algebra

the spectral radius of `a`,
computed from its quasispectrum, is the Gelfand radius of its image in the ℓ¹ unitization.

```lean
TauCeti.spectralRadius_eq_gelfandRadius_toLp_inr.{u_1} {A : Type u_1} [NonUnitalNormedRing A]
  [NormedSpace ℂ A] [IsScalarTower ℂ A A] [SMulCommClass ℂ A A] [CompleteSpace A] (a : A) :
  spectralRadius ℂ a = ENNReal.ofReal (gelfandRadius (WithLp.toLp 1 ↑a))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.spectralRadius_eq_gelfandRadius_toLp_inr`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/GelfandRadius.html#TauCeti.spectralRadius_eq_gelfandRadius_toLp_inr).

## Sources

- [Tau Ceti documentation: `TauCeti.spectralRadius_eq_gelfandRadius_toLp_inr`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/GelfandRadius.html#TauCeti.spectralRadius_eq_gelfandRadius_toLp_inr)
- [Source of `TauCeti.spectralRadius_eq_gelfandRadius_toLp_inr` in TauCeti/Analysis/Normed/Algebra/GelfandRadius.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Algebra/GelfandRadius.lean#L74)
