---
declaration: abbrev
origin: cited
lean: TauCeti.CompletedProjectiveTensor
statement: formalized
---

# TauCeti.CompletedProjectiveTensor

The completed projective tensor product `E ⊗̂π F`: the completion of the algebraic tensor
product `E ⊗[𝕜] F` for the projective norm.

```lean
TauCeti.CompletedProjectiveTensor.{u_1, u_2, u_3} (𝕜 : Type u_1) (E : Type u_2) (F : Type u_3)
  [NontriviallyNormedField 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [SeminormedAddCommGroup F] [NormedSpace 𝕜 F] : Type (max u_3 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CompletedProjectiveTensor`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/TensorProduct/Completion.html#TauCeti.CompletedProjectiveTensor).

## Sources

- [Tau Ceti documentation: `TauCeti.CompletedProjectiveTensor`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/TensorProduct/Completion.html#TauCeti.CompletedProjectiveTensor)
- [Source of `TauCeti.CompletedProjectiveTensor` in TauCeti/Analysis/Normed/Module/TensorProduct/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/TensorProduct/Completion.lean#L81)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
