---
declaration: def
origin: cited
lean: HahnModule.residueDualContinuousLinearEquiv
statement: formalized
---

# HahnModule.residueDualContinuousLinearEquiv

Residue pairing is a homeomorphism and linear equivalence for the lattice topology on
`V*((t))` and the annihilator topology on the continuous dual of `V((t))`.

```lean
HahnModule.residueDualContinuousLinearEquiv.{u_1, u_2} (R : Type u_1) (V : Type u_2) [CommRing R]
  [AddCommGroup V] [_root_.Module R V] [TopologicalSpace R] [DiscreteTopology R] :
  HahnModule ℤ R (Module.Dual R V) ≃L[R] HahnModule ℤ R V →L[R] R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HahnModule.residueDualContinuousLinearEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/ContinuousDual/AnnihilatorTopology.html#HahnModule.residueDualContinuousLinearEquiv).

## Sources

- [Tau Ceti documentation: `HahnModule.residueDualContinuousLinearEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/ContinuousDual/AnnihilatorTopology.html#HahnModule.residueDualContinuousLinearEquiv)
- [Source of `HahnModule.residueDualContinuousLinearEquiv` in TauCeti/RingTheory/LaurentSeries/ContinuousDual/AnnihilatorTopology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/ContinuousDual/AnnihilatorTopology.lean#L154)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
