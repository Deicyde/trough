---
declaration: structure
origin: cited
lean: TauCeti.ProjectiveTensor
statement: formalized
---

# TauCeti.ProjectiveTensor

The algebraic tensor product `E ⊗[𝕜] F` carrying the projective seminorm.

This wrapper distinguishes the projective seminorm from other norms on the same algebraic tensor
product, such as the injective norm or the Hilbert-space norm of inner product spaces.

```lean
TauCeti.ProjectiveTensor.{u_1, u_2, u_3} (𝕜 : Type u_1) (E : Type u_2) (F : Type u_3)
  [NormedField 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [SeminormedAddCommGroup F]
  [NormedSpace 𝕜 F] : Type (max u_2 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ProjectiveTensor`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/TensorProduct/ProjectiveSeminorm.html#TauCeti.ProjectiveTensor).

## Sources

- [Tau Ceti documentation: `TauCeti.ProjectiveTensor`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/TensorProduct/ProjectiveSeminorm.html#TauCeti.ProjectiveTensor)
- [Source of `TauCeti.ProjectiveTensor` in TauCeti/Analysis/Normed/Module/TensorProduct/ProjectiveSeminorm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/TensorProduct/ProjectiveSeminorm.lean#L232)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
