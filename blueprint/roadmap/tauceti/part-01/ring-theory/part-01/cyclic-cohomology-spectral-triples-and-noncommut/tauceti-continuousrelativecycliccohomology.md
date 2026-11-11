---
declaration: abbrev
origin: cited
lean: TauCeti.continuousRelativeCyclicCohomology
statement: formalized
---

# TauCeti.continuousRelativeCyclicCohomology

Relative continuous cyclic cohomology with the quotient topology on relative cocycles
modulo actual relative coboundaries.

```lean
TauCeti.continuousRelativeCyclicCohomology.{u_1, u_2, u_3} (𝕜 : Type u_1) (A : Type u_2)
  (M : Type u_3) [NormedField 𝕜] [NonUnitalRing A] [_root_.Module 𝕜 A] [IsScalarTower 𝕜 A A]
  [SMulCommClass 𝕜 A A] [TopologicalSpace A] [AddCommGroup M] [_root_.Module 𝕜 M]
  [TopologicalSpace M] [IsTopologicalAddGroup M] [ContinuousConstSMul 𝕜 M] [IsTopologicalAddGroup A]
  [ContinuousMul A] [ContinuousSMul 𝕜 A] (n : ℕ) : Type (max (max u_1 u_2) u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuousRelativeCyclicCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Continuous/Relative.html#TauCeti.continuousRelativeCyclicCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.continuousRelativeCyclicCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Continuous/Relative.html#TauCeti.continuousRelativeCyclicCohomology)
- [Source of `TauCeti.continuousRelativeCyclicCohomology` in TauCeti/RingTheory/CyclicCohomology/Continuous/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/Continuous/Relative.lean#L377)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
