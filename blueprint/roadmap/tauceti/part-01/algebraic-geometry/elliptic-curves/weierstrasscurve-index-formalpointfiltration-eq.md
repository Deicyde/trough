---
declaration: theorem
origin: cited
lean: WeierstrassCurve.index_formalPointFiltration_eq_mul_tamagawaNumber
statement: formalized
proof: formalized
---

# WeierstrassCurve.index_formalPointFiltration_eq_mul_tamagawaNumber

On a minimal equation the component-group factor in the formal-level index is the
local Tamagawa number.

```lean
WeierstrassCurve.index_formalPointFiltration_eq_mul_tamagawaNumber.{u_1, u_2} {A : Type u_1}
  [CommRing A] [IsDedekindDomain A] {F : Type u_2} [Field F] [Algebra A F] [IsFractionRing A F]
  (u : IsDedekindDomain.HeightOneSpectrum A)
  (C : WeierstrassCurve ↥(IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegers F u))
  [(C.baseChange (IsDedekindDomain.HeightOneSpectrum.adicCompletion F u)).IsElliptic]
  [WeierstrassCurve.IsMinimal (↥(IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegers F u))
      (C.baseChange (IsDedekindDomain.HeightOneSpectrum.adicCompletion F u))]
  (k : ℕ) :
  (WeierstrassCurve.formalPointFiltration u C (k + 1)).index =
    Nat.card
            (IsLocalRing.ResidueField
              ↥(IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegers F u)) ^
          k *
        Nat.card
          ((WeierstrassCurve.integralModel (↥Valued.v.valuationSubring)
                    (C.baseChange (IsDedekindDomain.HeightOneSpectrum.adicCompletion F u))).map
                (IsLocalRing.residue ↥Valued.v.valuationSubring)).toAffine.Point *
      (C.baseChange (IsDedekindDomain.HeightOneSpectrum.adicCompletion F u)).tamagawaNumber Valued.v
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.index_formalPointFiltration_eq_mul_tamagawaNumber`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Point/Index.html#WeierstrassCurve.index_formalPointFiltration_eq_mul_tamagawaNumber).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.index_formalPointFiltration_eq_mul_tamagawaNumber`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Point/Index.html#WeierstrassCurve.index_formalPointFiltration_eq_mul_tamagawaNumber)
- [Source of `WeierstrassCurve.index_formalPointFiltration_eq_mul_tamagawaNumber` in TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Point/Index.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Point/Index.lean#L118)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCurves/STATUS.md)
