---
declaration: def
origin: cited
lean: TauCeti.linearDixmierTrace
statement: formalized
---

# The linear Dixmier trace on `L^(1,∞)`

For a dilation-invariant generalized limit `ω`,
`TauCeti.complexDixmierTrace` restricts to a `ℂ`-linear functional on the logarithmic ideal
`((logarithmic ℂ).operatorGauge E E).finiteSubmodule`.

```lean
TauCeti.linearDixmierTrace.{u_3} (E : Type u_3) [NormedAddCommGroup E] [InnerProductSpace ℂ E]
  [CompleteSpace E] {ω : TauCeti.GeneralizedLimit} (hω : ω.IsDilationInvariant) :
  ↥((TauCeti.OperatorIdealFamily.logarithmic ℂ).operatorGauge E E).finiteSubmodule →ₗ[ℂ] ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ky Fan triangle inequality](../../../analysis/part-03/operator-ideal/ky-fan-triangle-inequality.md)
- [Ky Fan two-sided ideal inequality](../../../analysis/part-03/operator-ideal/ky-fan-two-sided-ideal-inequality.md)
- [Ky Fan's maximum principle](../../../analysis/part-03/operator-ideal/ky-fans-maximum-principle.md)
- [TauCeti.Complexification](../../../analysis/part-01/one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.linearDixmierTrace`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.html#TauCeti.linearDixmierTrace).

## Sources

- [Tau Ceti documentation: `TauCeti.linearDixmierTrace`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.html#TauCeti.linearDixmierTrace)
- [Source of `TauCeti.linearDixmierTrace` in TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.lean#L448)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
