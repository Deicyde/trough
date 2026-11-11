---
declaration: theorem
origin: cited
lean: TauCeti.IsInjectiveEnvelope.bijective_applyₗ_of_finite
statement: formalized
proof: formalized
---

# TauCeti.IsInjectiveEnvelope.bijective_applyₗ_of_finite

Matlis biduality for finitely generated modules over a complete Noetherian local ring:
the canonical evaluation map is bijective.

```lean
TauCeti.IsInjectiveEnvelope.bijective_applyₗ_of_finite.{u, v, w} {R : Type u} [CommRing R]
  [IsLocalRing R] [IsNoetherianRing R] {E : Type v} [AddCommGroup E] [_root_.Module R E]
  [Small.{v, u} R] {ι : IsLocalRing.ResidueField R →ₗ[R] E} (hι : TauCeti.IsInjectiveEnvelope ι)
  [IsAdicComplete (IsLocalRing.maximalIdeal R) R] (M : Type w) [AddCommGroup M] [_root_.Module R M]
  [Module.Finite R M] : Function.Bijective ⇑LinearMap.applyₗ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsInjectiveEnvelope.bijective_applyₗ_of_finite`](https://taucetiproject.org/docs/TauCeti/RingTheory/MatlisDuality/Finite.html#TauCeti.IsInjectiveEnvelope.bijective_apply%E2%82%97_of_finite).

## Sources

- [Tau Ceti documentation: `TauCeti.IsInjectiveEnvelope.bijective_applyₗ_of_finite`](https://taucetiproject.org/docs/TauCeti/RingTheory/MatlisDuality/Finite.html#TauCeti.IsInjectiveEnvelope.bijective_apply%E2%82%97_of_finite)
- [Source of `TauCeti.IsInjectiveEnvelope.bijective_applyₗ_of_finite` in TauCeti/RingTheory/MatlisDuality/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MatlisDuality/Finite.lean#L78)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
