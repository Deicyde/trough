---
declaration: theorem
origin: cited
lean: RootPairing.dotAlternatization_one, TauCeti.weylDenominator_eq_weylNumerator_zero
statement: formalized
proof: formalized
---

# The Weyl denominator identity for a root datum

`∑_{w ∈ W} sgn(w) e^{-(ρ - w ρ)} = ∏_{α > 0} (1 - e^{-α})`,

where `ρ - w ρ = ∑_{β > 0, w⁻¹ β < 0} β`. Unlike `TauCeti.weylDenominator_eq_weylNumerator_zero`,
this needs neither `ρ` to be a weight nor the roots to span.

```lean
RootPairing.dotAlternatization_one.{u_1, u_2, u_3} {ι : Type u_1} {M : Type u_2} {N : Type u_3}
  [AddCommGroup M] [AddCommGroup N] (P : RootPairing ι ℤ M N) [Finite ι] (b : P.Base) [P.IsReduced]
  [Fintype ↥P.weylGroup] : (P.dotAlternatization b) 1 = TauCeti.weylDenominator P b
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy-Schwarz against a majorant](../bilinear-form/cauchy-schwarz-against-a-majorant.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.dotAlternatization_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Integral.html#RootPairing.dotAlternatization_one).

## Other forms

**The Weyl denominator identity.** Formalized in Tau Ceti as [`TauCeti.weylDenominator_eq_weylNumerator_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Identity.html#TauCeti.weylDenominator_eq_weylNumerator_zero).

```lean
TauCeti.weylDenominator_eq_weylNumerator_zero.{u, v, w, x} {ι : Type u} {R : Type v} {M : Type w}
  {N : Type x} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] (P : RootPairing ι R M N) [Finite ι] (b : P.Base) [LinearOrder R]
  [IsStrictOrderedRing R] [Invertible 2] [P.IsCrystallographic] [P.IsReduced] [P.IsRootSystem]
  [Fintype ↥P.weylGroup] : TauCeti.weylDenominator P b = TauCeti.weylNumerator P b 0
```

## Sources

- [Tau Ceti documentation: `RootPairing.dotAlternatization_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Integral.html#RootPairing.dotAlternatization_one)
- [Source of `RootPairing.dotAlternatization_one` in TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/Weyl/Denominator/Integral.lean#L281)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
