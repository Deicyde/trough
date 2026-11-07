---
declaration: theorem
origin: cited
lean: TauCeti.exists_isInjectiveEnvelope
statement: formalized
proof: formalized
---

# Existence of injective envelopes

Every module has an injective envelope, in its own
universe.

```lean
TauCeti.exists_isInjectiveEnvelope.{u, v} (R : Type u) [Ring R] (M : Type v) [AddCommGroup M]
  [_root_.Module R M] [Small.{v, u} R] : ∃ Q x x_1 i, TauCeti.IsInjectiveEnvelope i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isInjectiveEnvelope`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Injective/Envelope/Existence.html#TauCeti.exists_isInjectiveEnvelope).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isInjectiveEnvelope`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Injective/Envelope/Existence.html#TauCeti.exists_isInjectiveEnvelope)
- [Source of `TauCeti.exists_isInjectiveEnvelope` in TauCeti/Algebra/Module/Injective/Envelope/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/Injective/Envelope/Existence.lean#L107)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
