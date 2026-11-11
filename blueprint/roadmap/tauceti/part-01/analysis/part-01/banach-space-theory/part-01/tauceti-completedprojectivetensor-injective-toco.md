---
declaration: theorem
origin: cited
lean: TauCeti.CompletedProjectiveTensor.injective_toContinuousLinearMap_of_hasApproximationProperty
statement: formalized
proof: formalized
---

# TauCeti.CompletedProjectiveTensor.injective_toContinuousLinearMap_of_hasApproximationProperty

If the Banach space `F` has the approximation property, the canonical operator
`E* ⊗̂π F → (E →L[𝕜] F)` is injective: every nuclear operator `E → F` has a unique representing
tensor.

```lean
TauCeti.CompletedProjectiveTensor.injective_toContinuousLinearMap_of_hasApproximationProperty.{u_1,
    u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F]
  (hF : TauCeti.HasApproximationProperty 𝕜 F) :
  Function.Injective ⇑(TauCeti.CompletedProjectiveTensor.toContinuousLinearMap 𝕜 E F)
```

## Depends on

- [TauCeti.CompletedProjectiveTensor](tauceti-completedprojectivetensor.md)

## Proof depends on

- [TauCeti.CompletedInjectiveTensor](tauceti-completedinjectivetensor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CompletedProjectiveTensor.injective_toContinuousLinearMap_of_hasApproximationProperty`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.html#TauCeti.CompletedProjectiveTensor.injective_toContinuousLinearMap_of_hasApproximationProperty).

## Sources

- [Tau Ceti documentation: `TauCeti.CompletedProjectiveTensor.injective_toContinuousLinearMap_of_hasApproximationProperty`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.html#TauCeti.CompletedProjectiveTensor.injective_toContinuousLinearMap_of_hasApproximationProperty)
- [Source of `TauCeti.CompletedProjectiveTensor.injective_toContinuousLinearMap_of_hasApproximationProperty` in TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.lean#L176)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
