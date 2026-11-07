---
declaration: theorem
origin: cited
lean: TauCeti.isZero_cyclicCohomology_self_of_odd
statement: formalized
proof: formalized
---

# TauCeti.isZero\_cyclicCohomology\_self\_of\_odd

The cyclic cohomology of the ground ring vanishes in odd degree.

```lean
TauCeti.isZero_cyclicCohomology_self_of_odd.{u, u_1} (R : Type u) (M : Type u_1) [CommRing R]
  [AddCommGroup M] [_root_.Module R M] {n : ℕ} (hn : Odd n) :
  CategoryTheory.Limits.IsZero (TauCeti.cyclicCohomology R R M n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isZero_cyclicCohomology_self_of_odd`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/GroundRing.html#TauCeti.isZero_cyclicCohomology_self_of_odd).

## Sources

- [Tau Ceti documentation: `TauCeti.isZero_cyclicCohomology_self_of_odd`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/GroundRing.html#TauCeti.isZero_cyclicCohomology_self_of_odd)
- [Source of `TauCeti.isZero_cyclicCohomology_self_of_odd` in TauCeti/RingTheory/CyclicCohomology/GroundRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/GroundRing.lean#L192)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
