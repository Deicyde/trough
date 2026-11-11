---
declaration: theorem
origin: cited
lean: TauCeti.CompletedInjectiveTensor.range_toOperator
statement: formalized
proof: formalized
---

# TauCeti.CompletedInjectiveTensor.range_toOperator

The completed injective tensor product represents exactly the operator-norm closure of
the finite-rank operators.

```lean
TauCeti.CompletedInjectiveTensor.range_toOperator.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] :
  Set.range ⇑(TauCeti.CompletedInjectiveTensor.toOperator 𝕜 E F) = closure {T | (↑T).HasFiniteRange}
```

## Depends on

- [TauCeti.CompletedInjectiveTensor](tauceti-completedinjectivetensor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CompletedInjectiveTensor.range_toOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/TensorProduct/Approximable.html#TauCeti.CompletedInjectiveTensor.range_toOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.CompletedInjectiveTensor.range_toOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/TensorProduct/Approximable.html#TauCeti.CompletedInjectiveTensor.range_toOperator)
- [Source of `TauCeti.CompletedInjectiveTensor.range_toOperator` in TauCeti/Analysis/Normed/Module/TensorProduct/Approximable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/TensorProduct/Approximable.lean#L186)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
