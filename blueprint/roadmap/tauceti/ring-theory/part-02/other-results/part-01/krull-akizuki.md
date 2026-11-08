---
declaration: theorem
origin: cited
lean: TauCeti.IsIntegralClosure.isNoetherianRing, TauCeti.integralClosure.isNoetherianRing
statement: formalized
proof: formalized
---

# Krull–Akizuki

Let `A` be a Noetherian domain of Krull dimension at most one with fraction
field `K`, and let `L` be a domain containing `A` that is a finite-dimensional `K`-vector space
compatibly with `A`, such as a finite extension of `K`. Then an integral closure `C` of `A` in `L`
is a Noetherian ring. No separability over `K` is assumed, and `C` need not be a finite
`A`-module.

```lean
TauCeti.IsIntegralClosure.isNoetherianRing.{u_1, u_2, u_3, u_4} {A : Type u_1} [CommRing A]
  [IsDomain A] [IsNoetherianRing A] [Ring.KrullDimLE 1 A] {L : Type u_2} [CommRing L] [IsDomain L]
  [Algebra A L] (K : Type u_3) [Field K] [Algebra A K] [IsFractionRing A K] [_root_.Module K L]
  [IsScalarTower A K L] [Module.Finite K L] (C : Type u_4) [CommRing C] [Algebra A C] [Algebra C L]
  [IsScalarTower A C L] [IsIntegralClosure C A L] : IsNoetherianRing C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Krull–Akizuki's length bound](../part-02/krull-akizukis-length-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsIntegralClosure.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.html#TauCeti.IsIntegralClosure.isNoetherianRing).

## Other forms

**Krull–Akizuki for Mathlib's `integralClosure`.** Formalized in Tau Ceti as [`TauCeti.integralClosure.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.html#TauCeti.integralClosure.isNoetherianRing).

```lean
TauCeti.integralClosure.isNoetherianRing.{u_1, u_2, u_3} {A : Type u_1} [CommRing A] [IsDomain A]
  [IsNoetherianRing A] [Ring.KrullDimLE 1 A] {L : Type u_2} [CommRing L] [IsDomain L] [Algebra A L]
  (K : Type u_3) [Field K] [Algebra A K] [IsFractionRing A K] [_root_.Module K L]
  [IsScalarTower A K L] [Module.Finite K L] : IsNoetherianRing ↥(integralClosure A L)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsIntegralClosure.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.html#TauCeti.IsIntegralClosure.isNoetherianRing)
- [Source of `TauCeti.IsIntegralClosure.isNoetherianRing` in TauCeti/RingTheory/IntegralClosure/NormalizationFinite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.lean#L321)
