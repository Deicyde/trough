---
declaration: theorem
origin: cited
lean: TauCeti.cyclicCohomology.evenPairing_units_conj
statement: formalized
proof: formalized
---

# Conjugation invariance of the even pairing

Conjugating an idempotent by a unit does not
change its even pairing with cyclic cohomology.

```lean
TauCeti.cyclicCohomology.evenPairing_units_conj.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2}
  {M : Type u_3} [Field R] [CharZero R] [Ring A] [Algebra R A] [AddCommGroup M] [_root_.Module R M]
  (u : Aˣ) {e : A} (he : IsIdempotentElem e) (hue : IsIdempotentElem (↑u * e * ↑u⁻¹)) (m : ℕ) :
  TauCeti.cyclicCohomology.evenPairing (↑u * e * ↑u⁻¹) hue m =
    TauCeti.cyclicCohomology.evenPairing e he m
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicCohomology.evenPairing_units_conj`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/EvenPairing/Invariance.html#TauCeti.cyclicCohomology.evenPairing_units_conj).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicCohomology.evenPairing_units_conj`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/EvenPairing/Invariance.html#TauCeti.cyclicCohomology.evenPairing_units_conj)
- [Source of `TauCeti.cyclicCohomology.evenPairing_units_conj` in TauCeti/RingTheory/CyclicCohomology/EvenPairing/Invariance.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/EvenPairing/Invariance.lean#L173)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
