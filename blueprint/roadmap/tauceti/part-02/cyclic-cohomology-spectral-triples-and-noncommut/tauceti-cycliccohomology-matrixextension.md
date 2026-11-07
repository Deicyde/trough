---
declaration: def
origin: cited
lean: TauCeti.cyclicCohomology.matrixExtension
statement: formalized
---

# TauCeti.cyclicCohomology.matrixExtension

The map `HCⁿ(A; M) → HCⁿ(Matrix ι ι A; M)` on cyclic cohomology induced by matrix extension of
cyclic cocycles.

```lean
TauCeti.cyclicCohomology.matrixExtension.{u_4, u_5, u_6, u_7} {R : Type u_4} {A : Type u_5}
  (M : Type u_6) [AddCommGroup M] (ι : Type u_7) [Fintype ι] (n : ℕ) [CommRing R]
  [_root_.Module R M] [Ring A] [Algebra R A] [DecidableEq ι] :
  ↑(TauCeti.cyclicCohomology R A M n) →ₗ[R] ↑(TauCeti.cyclicCohomology R (Matrix ι ι A) M n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicCohomology.matrixExtension`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Matrix.html#TauCeti.cyclicCohomology.matrixExtension).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicCohomology.matrixExtension`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Matrix.html#TauCeti.cyclicCohomology.matrixExtension)
- [Source of `TauCeti.cyclicCohomology.matrixExtension` in TauCeti/RingTheory/CyclicCohomology/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/Matrix.lean#L497)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
