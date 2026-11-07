---
declaration: def
origin: cited
lean: TauCeti.Khovanov.quantumGrading
statement: formalized
---

# TauCeti.Khovanov.quantumGrading

The **quantum grading** of the Khovanov Frobenius algebra `R[ε]`: the basis vector `1` spans
degree `1`, the basis vector `ε` spans degree `-1`, and every other degree is zero. It is the
grading of the free module on the basis `1, ε` by `TauCeti.Khovanov.quantumDegree`, transported
to `R[ε]`.

```lean
TauCeti.Khovanov.quantumGrading.{u} (R : Type u) [CommRing R] :
  TauCeti.InternalGrading R (DualNumber R) ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Khovanov.quantumGrading`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/QuantumGrading.html#TauCeti.Khovanov.quantumGrading).

## Sources

- [Tau Ceti documentation: `TauCeti.Khovanov.quantumGrading`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/QuantumGrading.html#TauCeti.Khovanov.quantumGrading)
- [Source of `TauCeti.Khovanov.quantumGrading` in TauCeti/KnotTheory/Khovanov/QuantumGrading.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Khovanov/QuantumGrading.lean#L88)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/KhovanovHomology/STATUS.md)
