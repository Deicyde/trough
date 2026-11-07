---
declaration: theorem
origin: cited
lean: ZLattice.IsIntegral.thetaSeries_dual_eq_sum
statement: formalized
proof: formalized
---

# ZLattice.IsIntegral.thetaSeries\_dual\_eq\_sum

For an integral lattice `L`, the theta series of the dual lattice is the sum of the coset theta
series over the finite discriminant group `L^∨ ⧸ L`: `Θ_{L^∨} = ∑_{γ ∈ A_L} θ_γ`. The discriminant
group of an integral lattice is finite (`IsIntegral.finite_discriminantGroup`), so a `Fintype`
instance is always available.

```lean
ZLattice.IsIntegral.thetaSeries_dual_eq_sum.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {L : Submodule ℤ E} [FiniteDimensional ℝ E] [DiscreteTopology ↥L]
  [IsZLattice ℝ L] (h : ZLattice.IsIntegral L) [Fintype (ZLattice.DiscriminantGroup L)]
  (τ : UpperHalfPlane) :
  ZLattice.thetaSeries (ZLattice.dual L) τ = ∑ γ, ZLattice.thetaCosetClass L γ τ
```

## Depends on

- [ZLattice.dual](zlattice-dual.md)
- [ZLattice.thetaCoset](zlattice-thetacoset.md)
- [ZLattice.thetaSeries](zlattice-thetaseries.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsIntegral.thetaSeries_dual_eq_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/DiscriminantGroup.html#ZLattice.IsIntegral.thetaSeries_dual_eq_sum).

## Sources

- [Tau Ceti documentation: `ZLattice.IsIntegral.thetaSeries_dual_eq_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/DiscriminantGroup.html#ZLattice.IsIntegral.thetaSeries_dual_eq_sum)
- [Source of `ZLattice.IsIntegral.thetaSeries_dual_eq_sum` in TauCeti/NumberTheory/ModularForms/ThetaSeries/DiscriminantGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ThetaSeries/DiscriminantGroup.lean#L147)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
