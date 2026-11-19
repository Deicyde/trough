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

- [Poisson's summation formula](../../../analysis/part-03/fourier/part-01/poissons-summation-formula.md)
- [The rank of an even unimodular lattice is divisible by `8`](the-rank-of-an-even-unimodular-lattice-is-divisi.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.thetaForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.html#ZLattice.thetaForm).

## Sources

- [Tau Ceti documentation: `ZLattice.thetaForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.html#ZLattice.thetaForm)
- [Source of `ZLattice.thetaForm` in TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/ThetaSeries/LevelOne.lean#L135)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ThetaSeries/STATUS.md)
