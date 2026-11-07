---
declaration: theorem
origin: cited
lean: TauCeti.continuous_continuousConnesB
statement: formalized
proof: formalized
---

# TauCeti.continuous\_continuousConnesB

Connes' operator is continuous for bounded convergence of cochains.

```lean
TauCeti.continuous_continuousConnesB.{u_1, u_2, u_3} (𝕜 : Type u_1) (A : Type u_2) (M : Type u_3)
  [NormedField 𝕜] [AddCommGroup A] [_root_.Module 𝕜 A] [TopologicalSpace A] [ContinuousSMul 𝕜 A]
  [One A] [AddCommGroup M] [_root_.Module 𝕜 M] [TopologicalSpace M] [IsTopologicalAddGroup M]
  [ContinuousConstSMul 𝕜 M] (n : ℕ) : Continuous ⇑(TauCeti.continuousConnesB 𝕜 A M n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_continuousConnesB`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OperatorTopology.html#TauCeti.continuous_continuousConnesB).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_continuousConnesB`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OperatorTopology.html#TauCeti.continuous_continuousConnesB)
- [Source of `TauCeti.continuous_continuousConnesB` in TauCeti/RingTheory/CyclicCohomology/OperatorTopology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/OperatorTopology.lean#L230)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
