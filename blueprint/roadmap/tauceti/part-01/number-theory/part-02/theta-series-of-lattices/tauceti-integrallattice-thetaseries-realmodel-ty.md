---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.thetaSeries_realModel_typeARootLattice_two_eq_tsum
statement: formalized
proof: formalized
---

# TauCeti.IntegralLattice.thetaSeries_realModel_typeARootLattice_two_eq_tsum

The classical expansion `Θ_{A₂}(τ) = 1 + 6 ∑_{m ≥ 1} (∑_{d ∣ m} (-3 / d)) q^m`,
where `q = exp (2 π i τ)`.

```lean
TauCeti.IntegralLattice.thetaSeries_realModel_typeARootLattice_two_eq_tsum (τ : UpperHalfPlane) :
  ZLattice.thetaSeries ((TauCeti.IntegralLattice.typeARootLattice 2).realModel ⋯) τ =
    1 +
      6 *
        ∑' (m : ℕ),
          (∑ d ∈ (m + 1).divisors, ↑(TauCeti.kroneckerSym (-3) ↑d)) *
            Function.Periodic.qParam 1 ↑τ ^ (m + 1)
```

## Depends on

- [TauCeti.IntegralLattice](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Proof depends on

- [Classical Sturm bound for finite-index subgroups of `SL(2, ℤ)`](../modular-forms/classical-sturm-bound-for-finite-index-subgroups.md)
- [ZLattice.level](zlattice-level.md)
- [ZLattice.thetaFormOfLevel](zlattice-thetaformoflevel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.thetaSeries_realModel_typeARootLattice_two_eq_tsum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/A2.html#TauCeti.IntegralLattice.thetaSeries_realModel_typeARootLattice_two_eq_tsum).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.thetaSeries_realModel_typeARootLattice_two_eq_tsum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/A2.html#TauCeti.IntegralLattice.thetaSeries_realModel_typeARootLattice_two_eq_tsum)
- [Source of `TauCeti.IntegralLattice.thetaSeries_realModel_typeARootLattice_two_eq_tsum` in TauCeti/NumberTheory/ModularForms/ThetaSeries/A2.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/ThetaSeries/A2.lean#L192)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ThetaSeries/STATUS.md)
