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
  [InnerProductSpace ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (hL : ZLattice.IsEven L) (hU : ZLattice.IsUnimodular L) : 8 ∣ Module.finrank ℝ E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Poisson's summation formula](../../../analysis/part-03/fourier/part-01/poissons-summation-formula.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.eight_dvd_finrank`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.html#ZLattice.IsEven.eight_dvd_finrank).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.eight_dvd_finrank`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.html#ZLattice.IsEven.eight_dvd_finrank)
- [Source of `ZLattice.IsEven.eight_dvd_finrank` in TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.lean#L109)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ThetaSeries/STATUS.md)
