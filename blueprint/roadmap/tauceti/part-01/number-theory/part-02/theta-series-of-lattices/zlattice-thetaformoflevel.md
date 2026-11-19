---
declaration: def
origin: cited
lean: ZLattice.thetaFormOfLevel
statement: formalized
---

# ZLattice.thetaFormOfLevel

The theta series of an even full lattice of rank `2k`, as a modular form on
`Γ₁(level L)` of weight `k`. Its character-space membership is
`ZLattice.thetaFormOfLevel_mem_modFormCharSpace`.

```lean
ZLattice.thetaFormOfLevel.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L] [IsZLattice ℝ L] {k : ℕ}
  (hL : ZLattice.IsEven L) (hk : Module.finrank ℝ E = 2 * k) :
  ModularForm
    (Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ)
      (CongruenceSubgroup.Gamma1 (ZLattice.level L)))
    ↑k
```

## Depends on

- [ZLattice.level](zlattice-level.md)

## Proof depends on

- [The Hecke–Schoeneberg transformation law](the-hecke-schoeneberg-transformation-law.md)
- [Poisson's summation formula](../../../analysis/part-03/fourier/part-01/poissons-summation-formula.md)
- [TauCeti.IntegralLattice](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym](zlattice-iseven-gausssum-eq-sqrt-card-mul-jacobi.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.thetaFormOfLevel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/GeneralLevel.html#ZLattice.thetaFormOfLevel).

## Sources

- [Tau Ceti documentation: `ZLattice.thetaFormOfLevel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/GeneralLevel.html#ZLattice.thetaFormOfLevel)
- [Source of `ZLattice.thetaFormOfLevel` in TauCeti/NumberTheory/ModularForms/ThetaSeries/GeneralLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/ThetaSeries/GeneralLevel.lean#L102)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ThetaSeries/STATUS.md)
