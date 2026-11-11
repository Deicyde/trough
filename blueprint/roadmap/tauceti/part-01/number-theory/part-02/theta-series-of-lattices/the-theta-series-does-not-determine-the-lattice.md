---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.not_forall_exists_map_eq_of_thetaSeries_eq
statement: formalized
proof: formalized
---

# The theta series does not determine the lattice

There are even unimodular full lattices
`L ⊆ E` and `M ⊆ F` with `Θ_L = Θ_M` such that no linear isometry `E ≃ F` carries `L` onto `M`:
the real models of `E₈ ⊕ E₈` and `D₁₆⁺`, whose theta series are both `E₄²`.

```lean
TauCeti.IntegralLattice.not_forall_exists_map_eq_of_thetaSeries_eq :
  ¬∀ (E F : Type) [inst : NormedAddCommGroup E] [inst_1 : InnerProductSpace ℝ E]
      [FiniteDimensional ℝ E] [inst_3 : NormedAddCommGroup F] [inst_4 : InnerProductSpace ℝ F]
      [FiniteDimensional ℝ F] (L : Submodule ℤ E) (M : Submodule ℤ F) [inst_6 : DiscreteTopology ↥L]
      [IsZLattice ℝ L] [inst_8 : DiscreteTopology ↥M] [IsZLattice ℝ M],
      ZLattice.IsEven L →
        ZLattice.IsUnimodular L →
          ZLattice.IsEven M →
            ZLattice.IsUnimodular M →
              ZLattice.thetaSeries L = ZLattice.thetaSeries M →
                ∃ f, Submodule.map (↑(LinearEquiv.restrictScalars ℤ f.toLinearEquiv)) L = M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.FiniteQuadraticModule](../../part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)
- [TauCeti.IntegralLattice.realModel](tauceti-integrallattice-realmodel.md)
- [The theta series of an even unimodular lattice is a level-one modular form](the-theta-series-of-an-even-unimodular-lattice-i.md)
- [ZLattice.ratModel](zlattice-ratmodel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.not_forall_exists_map_eq_of_thetaSeries_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/RankSixteen.html#TauCeti.IntegralLattice.not_forall_exists_map_eq_of_thetaSeries_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.not_forall_exists_map_eq_of_thetaSeries_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/RankSixteen.html#TauCeti.IntegralLattice.not_forall_exists_map_eq_of_thetaSeries_eq)
- [Source of `TauCeti.IntegralLattice.not_forall_exists_map_eq_of_thetaSeries_eq` in TauCeti/NumberTheory/ModularForms/ThetaSeries/RankSixteen.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ThetaSeries/RankSixteen.lean#L83)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
