---
declaration: theorem
origin: cited
lean: TauCeti.UniversalForms.cycleCocycle_trace
statement: formalized
proof: formalized
---

# Every cyclic cocycle is the character of a universal-form cycle

the cyclic cocycle of the
cycle `(⨁ m, Ωᵐ, d, ∫_φ, ι)` is `φ`.

```lean
TauCeti.UniversalForms.cycleCocycle_trace.{u_1, u_2, u_3} {k : Type u_1} {A : Type u_2}
  {M : Type u_3} [CommRing k] [NonUnitalRing A] [_root_.Module k A] [AddCommGroup M]
  [_root_.Module k M] {n : ℕ} [IsScalarTower k A A] [SMulCommClass k A A]
  (φ : ↥(TauCeti.cyclicCocycles k A M n)) : TauCeti.cycleCocycle ⋯ ⋯ ⋯ = φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalForms.cycleCocycle_trace`](https://taucetiproject.org/docs/TauCeti/NoncommutativeGeometry/UniversalDifferential/Cycle.html#TauCeti.UniversalForms.cycleCocycle_trace).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalForms.cycleCocycle_trace`](https://taucetiproject.org/docs/TauCeti/NoncommutativeGeometry/UniversalDifferential/Cycle.html#TauCeti.UniversalForms.cycleCocycle_trace)
- [Source of `TauCeti.UniversalForms.cycleCocycle_trace` in TauCeti/NoncommutativeGeometry/UniversalDifferential/Cycle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NoncommutativeGeometry/UniversalDifferential/Cycle.lean#L303)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
