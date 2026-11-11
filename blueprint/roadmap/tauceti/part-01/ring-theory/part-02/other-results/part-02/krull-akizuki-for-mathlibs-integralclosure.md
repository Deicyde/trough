---
declaration: theorem
origin: cited
lean: TauCeti.integralClosure.isNoetherianRing, TauCeti.IsIntegralClosure.isNoetherianRing
statement: formalized
proof: formalized
---

# Krull–Akizuki for Mathlib's `integralClosure`

The specialisation of
`TauCeti.IsIntegralClosure.isNoetherianRing` to the integral closure of `A` in `L` as a
subalgebra.

```lean
TauCeti.integralClosure.isNoetherianRing.{u_1, u_2, u_3} {A : Type u_1} [CommRing A] [IsDomain A]
  [IsNoetherianRing A] [Ring.KrullDimLE 1 A] {L : Type u_2} [CommRing L] [IsDomain L] [Algebra A L]
  (K : Type u_3) [Field K] [Algebra A K] [IsFractionRing A K] [_root_.Module K L]
  [IsScalarTower A K L] [Module.Finite K L] : IsNoetherianRing ↥(integralClosure A L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Krull–Akizuki's length bound](krull-akizukis-length-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integralClosure.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.html#TauCeti.integralClosure.isNoetherianRing).

## Other forms

**Krull–Akizuki.** Formalized in Tau Ceti as [`TauCeti.IsIntegralClosure.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.html#TauCeti.IsIntegralClosure.isNoetherianRing).

```lean
TauCeti.IsIntegralClosure.isNoetherianRing.{u_1, u_2, u_3, u_4} {A : Type u_1} [CommRing A]
  [IsDomain A] [IsNoetherianRing A] [Ring.KrullDimLE 1 A] {L : Type u_2} [CommRing L] [IsDomain L]
  [Algebra A L] (K : Type u_3) [Field K] [Algebra A K] [IsFractionRing A K] [_root_.Module K L]
  [IsScalarTower A K L] [Module.Finite K L] (C : Type u_4) [CommRing C] [Algebra A C] [Algebra C L]
  [IsScalarTower A C L] [IsIntegralClosure C A L] : IsNoetherianRing C
```

## Sources

- [Tau Ceti documentation: `TauCeti.integralClosure.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.html#TauCeti.integralClosure.isNoetherianRing)
- [Source of `TauCeti.integralClosure.isNoetherianRing` in TauCeti/RingTheory/IntegralClosure/NormalizationFinite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.lean#L311)
