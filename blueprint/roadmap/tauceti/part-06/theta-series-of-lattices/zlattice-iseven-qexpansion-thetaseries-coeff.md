---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.qExpansion_thetaSeries_coeff
statement: formalized
proof: formalized
---

# ZLattice.IsEven.qExpansion\_thetaSeries\_coeff

The coefficients of the `q`-expansion of the theta series of an even lattice: the `m`-th
coefficient in `q = exp (2 π i τ)` is the number `r_L(2m)` of vectors of half-norm `m`.

```lean
ZLattice.IsEven.qExpansion_thetaSeries_coeff.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  {L : Submodule ℤ E} [NormedSpace ℝ E] [FiniteDimensional ℝ E] [DiscreteTopology ↥L]
  (hL : ZLattice.IsEven L) (m : ℕ) :
  (PowerSeries.coeff m) (UpperHalfPlane.qExpansion 1 (ZLattice.thetaSeries L)) =
    ↑(ZLattice.representationNumber L (2 * ↑m))
```

## Depends on

- [ZLattice.IsEven](zlattice-iseven.md)
- [ZLattice.representationNumber](zlattice-representationnumber.md)
- [ZLattice.thetaSeries](zlattice-thetaseries.md)

## Proof depends on

- [ZLattice.thetaCoset](zlattice-thetacoset.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.qExpansion_thetaSeries_coeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/QExpansion.html#ZLattice.IsEven.qExpansion_thetaSeries_coeff).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.qExpansion_thetaSeries_coeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/QExpansion.html#ZLattice.IsEven.qExpansion_thetaSeries_coeff)
- [Source of `ZLattice.IsEven.qExpansion_thetaSeries_coeff` in TauCeti/NumberTheory/ModularForms/ThetaSeries/QExpansion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ThetaSeries/QExpansion.lean#L155)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
