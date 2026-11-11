---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.eight_dvd_finrank
statement: formalized
proof: formalized
---

# The rank of an even unimodular lattice is divisible by `8`

```lean
ZLattice.IsEven.eight_dvd_finrank.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L]
  [IsZLattice ℝ L] (hL : ZLattice.IsEven L) (hU : ZLattice.IsUnimodular L) : 8 ∣ Module.finrank ℝ E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inversion law of theta series](the-inversion-law-of-theta-series.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.eight_dvd_finrank`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.html#ZLattice.IsEven.eight_dvd_finrank).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.eight_dvd_finrank`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.html#ZLattice.IsEven.eight_dvd_finrank)
- [Source of `ZLattice.IsEven.eight_dvd_finrank` in TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.lean#L108)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
