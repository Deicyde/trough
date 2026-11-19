---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.thetaSeries_realModel_leechLattice_eq_E₄_cube_sub_mul_discriminant
statement: formalized
proof: formalized
---

# The theta series of the Leech lattice is `E₄³ - 720 Δ`

```lean
TauCeti.IntegralLattice.thetaSeries_realModel_leechLattice_eq_E₄_cube_sub_mul_discriminant
  (τ : UpperHalfPlane) :
  ZLattice.thetaSeries (TauCeti.leechLattice.realModel TauCeti.isPosDef_leechLattice) τ =
    ModularForm.E₄ τ ^ 3 - 720 * ModularForm.discriminant τ
```

## Depends on

- [TauCeti.ConstructionA.lattice](../../../linear-algebra/part-01/algebraic-codes-and-code-lattice-constructions/tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](../../part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Proof depends on

- [Even overlattices correspond to quadratic-isotropic subgroups](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/even-overlattices-correspond-to-quadratic-isotro.md)
- [The Leech lattice has no roots](../../../linear-algebra/part-01/niemeier-glue-data-and-explicit-leech-constructi/the-leech-lattice-has-no-roots.md)
- [The theta series of an even unimodular lattice is a level-one modular form](the-theta-series-of-an-even-unimodular-lattice-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.thetaSeries_realModel_leechLattice_eq_E₄_cube_sub_mul_discriminant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Leech.html#TauCeti.IntegralLattice.thetaSeries_realModel_leechLattice_eq_E%E2%82%84_cube_sub_mul_discriminant).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.thetaSeries_realModel_leechLattice_eq_E₄_cube_sub_mul_discriminant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Leech.html#TauCeti.IntegralLattice.thetaSeries_realModel_leechLattice_eq_E%E2%82%84_cube_sub_mul_discriminant)
- [Source of `TauCeti.IntegralLattice.thetaSeries_realModel_leechLattice_eq_E₄_cube_sub_mul_discriminant` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Leech.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/ThetaSeries/Leech.lean#L79)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ThetaSeries/STATUS.md)
