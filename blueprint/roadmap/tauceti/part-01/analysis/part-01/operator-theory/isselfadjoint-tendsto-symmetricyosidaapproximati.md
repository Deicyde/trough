---
declaration: theorem
origin: cited
lean: IsSelfAdjoint.tendsto_symmetricYosidaApproximation_apply
statement: formalized
proof: formalized
---

# IsSelfAdjoint.tendsto_symmetricYosidaApproximation_apply

The symmetric approximations converge to the original operator on its domain.

```lean
IsSelfAdjoint.tendsto_symmetricYosidaApproximation_apply.{u_1} {H : Type u_1} [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A)
  (x : ↥A.domain) :
  Filter.Tendsto (fun r => (A.symmetricYosidaApproximation r) ↑x) (Filter.cocompact ℝ) (nhds (↑A x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSelfAdjoint.tendsto_symmetricYosidaApproximation_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/Yosida.html#IsSelfAdjoint.tendsto_symmetricYosidaApproximation_apply).

## Sources

- [Tau Ceti documentation: `IsSelfAdjoint.tendsto_symmetricYosidaApproximation_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/Yosida.html#IsSelfAdjoint.tendsto_symmetricYosidaApproximation_apply)
- [Source of `IsSelfAdjoint.tendsto_symmetricYosidaApproximation_apply` in TauCeti/Analysis/InnerProductSpace/LinearPMap/Yosida.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/LinearPMap/Yosida.lean#L182)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorTheory/STATUS.md)
