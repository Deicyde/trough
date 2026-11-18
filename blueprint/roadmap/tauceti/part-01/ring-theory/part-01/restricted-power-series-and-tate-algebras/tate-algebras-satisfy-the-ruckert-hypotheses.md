---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.isRueckert_polynomialToRestricted
statement: formalized
proof: formalized
---

# Tate algebras satisfy the Rückert hypotheses

The inclusion of polynomials over the
Tate algebra `T = K⟨X₁, …, Xₙ⟩` into the Tate algebra `T⟨Y⟩` in one more variable satisfies the
Rückert hypotheses for the Weierstrass polynomials: the monic polynomials over `T` which are
distinguished of their degree at the unit radius.

```lean
TauCeti.MvPowerSeries.isRueckert_polynomialToRestricted.{u_1, u_2} {K : Type u_1} [NormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {σ : Type u_2} [Finite σ] :
  (↑(TauCeti.PowerSeries.polynomialToRestricted 1)).IsRueckert
    {p | p.Monic ∧ TauCeti.PowerSeries.IsDistinguished 1 p.natDegree ↑p}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsNormMulUnit](tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](the-weierstrass-division-estimate-bosch-guntzer.md)
- [Weierstrass preparation](../../part-02/power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.isRueckert_polynomialToRestricted`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Rueckert.html#TauCeti.MvPowerSeries.isRueckert_polynomialToRestricted).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.isRueckert_polynomialToRestricted`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Rueckert.html#TauCeti.MvPowerSeries.isRueckert_polynomialToRestricted)
- [Source of `TauCeti.MvPowerSeries.isRueckert_polynomialToRestricted` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Rueckert.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Rueckert.lean#L53)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
