---
declaration: theorem
origin: cited
lean: ZLattice.IsIntegral.det_eq_card_discriminantGroup
statement: formalized
proof: formalized
---

# ZLattice.IsIntegral.det_eq_card_discriminantGroup

For an integral lattice `L`, the determinant is the order of the discriminant group
`L^∨ ⧸ L`. In particular it is a positive integer.

```lean
ZLattice.IsIntegral.det_eq_card_discriminantGroup.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {L : Submodule ℤ E} [DiscreteTopology ↥L] [IsZLattice ℝ L] (h : ZLattice.IsIntegral L) :
  ZLattice.det L = ↑(Nat.card (ZLattice.DiscriminantGroup L))
```

## Depends on

- [ZLattice.dual](zlattice-dual.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsIntegral.det_eq_card_discriminantGroup`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Determinant.html#ZLattice.IsIntegral.det_eq_card_discriminantGroup).

## Sources

- [Tau Ceti documentation: `ZLattice.IsIntegral.det_eq_card_discriminantGroup`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Determinant.html#ZLattice.IsIntegral.det_eq_card_discriminantGroup)
- [Source of `ZLattice.IsIntegral.det_eq_card_discriminantGroup` in TauCeti/Algebra/Module/ZLattice/Determinant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/Determinant.lean#L259)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
