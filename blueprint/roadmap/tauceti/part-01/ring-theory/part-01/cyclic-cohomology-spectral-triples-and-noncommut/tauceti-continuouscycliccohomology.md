---
declaration: abbrev
origin: cited
lean: TauCeti.continuousCyclicCohomology
statement: formalized
---

# TauCeti.continuousCyclicCohomology

Continuous cyclic cohomology of a unital topological algebra, with the quotient topology
on cocycles modulo actual coboundaries. This is the `M`-valued theory `HCⁿ(A; M)`;
for `𝕜 = M = ℂ` it is Connes' continuous `HCⁿ(A)`.

```lean
TauCeti.continuousCyclicCohomology.{u_1, u_2, u_3} (𝕜 : Type u_1) (A : Type u_2) (M : Type u_3)
  [NormedField 𝕜] [Ring A] [Algebra 𝕜 A] [TopologicalSpace A] [ContinuousMul A] [AddCommGroup M]
  [_root_.Module 𝕜 M] [TopologicalSpace M] [IsTopologicalAddGroup M] [ContinuousConstSMul 𝕜 M]
  (n : ℕ) : Type (max u_2 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuousCyclicCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Continuous/Cohomology.html#TauCeti.continuousCyclicCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.continuousCyclicCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Continuous/Cohomology.html#TauCeti.continuousCyclicCohomology)
- [Source of `TauCeti.continuousCyclicCohomology` in TauCeti/RingTheory/CyclicCohomology/Continuous/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/Continuous/Cohomology.lean#L269)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
