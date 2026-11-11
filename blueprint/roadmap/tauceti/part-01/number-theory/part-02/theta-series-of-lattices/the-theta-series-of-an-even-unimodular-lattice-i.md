---
declaration: def
origin: cited
lean: ZLattice.thetaForm
statement: formalized
---

# The theta series of an even unimodular lattice is a level-one modular form

if `L` is
even unimodular and `dim E = 2k`, then `Θ_L` is a modular form of weight `k` for `SL(2, ℤ)`. Its
coercion is `thetaSeries L` (`ZLattice.coe_thetaForm`).

```lean
ZLattice.thetaForm.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L] [IsZLattice ℝ L] {k : ℕ}
  (hL : ZLattice.IsEven L) (hU : ZLattice.IsUnimodular L) (hk : Module.finrank ℝ E = 2 * k) :
  ModularForm (Matrix.SpecialLinearGroup.mapGL ℝ).range ↑k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inversion law of theta series](the-inversion-law-of-theta-series.md)
- [The rank of an even unimodular lattice is divisible by `8`](the-rank-of-an-even-unimodular-lattice-is-divisi.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.thetaForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.html#ZLattice.thetaForm).

## Sources

- [Tau Ceti documentation: `ZLattice.thetaForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.html#ZLattice.thetaForm)
- [Source of `ZLattice.thetaForm` in TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.lean#L130)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
