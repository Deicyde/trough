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

- [Ky Fan triangle inequality](../../../analysis/part-04/operator-ideal/ky-fan-triangle-inequality.md)
- [Ky Fan two-sided ideal inequality](../../../analysis/part-04/operator-ideal/ky-fan-two-sided-ideal-inequality.md)
- [Ky Fan's maximum principle](../../../analysis/part-04/operator-ideal/ky-fans-maximum-principle.md)
- [TauCeti.Complexification](../../../analysis/part-02/one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.linearDixmierTrace`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.html#TauCeti.linearDixmierTrace).

## Sources

- [Tau Ceti documentation: `TauCeti.linearDixmierTrace`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.html#TauCeti.linearDixmierTrace)
- [Source of `TauCeti.linearDixmierTrace` in TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.lean#L448)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
