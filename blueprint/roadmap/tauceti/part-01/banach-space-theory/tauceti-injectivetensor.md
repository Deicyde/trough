---
declaration: structure
origin: cited
lean: TauCeti.InjectiveTensor
statement: formalized
---

# TauCeti.InjectiveTensor

The algebraic tensor product `E ⊗[𝕜] F` carrying the injective seminorm.

This wrapper distinguishes the injective seminorm from other norms on the same algebraic tensor
product, such as the projective norm or the Hilbert-space norm of inner product spaces.

```lean
TauCeti.InjectiveTensor.{u_1, u_2, u_3} (𝕜 : Type u_1) (E : Type u_2) (F : Type u_3)
  [NontriviallyNormedField 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [SeminormedAddCommGroup F] [NormedSpace 𝕜 F] : Type (max u_2 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.InjectiveTensor`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/TensorProduct/InjectiveSeminorm.html#TauCeti.InjectiveTensor).

## Sources

- [Tau Ceti documentation: `TauCeti.InjectiveTensor`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/TensorProduct/InjectiveSeminorm.html#TauCeti.InjectiveTensor)
- [Source of `TauCeti.InjectiveTensor` in TauCeti/Analysis/Normed/Module/TensorProduct/InjectiveSeminorm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/TensorProduct/InjectiveSeminorm.lean#L326)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
