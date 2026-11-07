---
declaration: def
origin: cited
lean: TauCeti.cyclicCohomology.selfEquiv
statement: formalized
---

# TauCeti.cyclicCohomology.selfEquiv

If multiplication by `2` is injective on `M`, then `HCⁿ(R; M) ≅ M` in every even degree `n`,
by the class of the product cochain. In particular `HC²ᵏ(ℂ) ≅ ℂ`.

```lean
TauCeti.cyclicCohomology.selfEquiv.{u, u_1} (R : Type u) (M : Type u_1) [CommRing R]
  [AddCommGroup M] [_root_.Module R M] {n : ℕ} (hn : Even n) (h2 : IsSMulRegular M 2) :
  M ≃ₗ[R] ↑(TauCeti.cyclicCohomology R R M n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicCohomology.selfEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/GroundRing.html#TauCeti.cyclicCohomology.selfEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicCohomology.selfEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/GroundRing.html#TauCeti.cyclicCohomology.selfEquiv)
- [Source of `TauCeti.cyclicCohomology.selfEquiv` in TauCeti/RingTheory/CyclicCohomology/GroundRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/GroundRing.lean#L295)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
