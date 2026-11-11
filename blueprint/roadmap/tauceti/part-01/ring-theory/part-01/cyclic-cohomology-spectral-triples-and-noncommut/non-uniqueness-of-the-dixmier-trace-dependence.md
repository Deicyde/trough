---
declaration: theorem
origin: cited
lean: TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable
statement: formalized
proof: formalized
---

# Non-uniqueness of the Dixmier trace (`ω`-dependence)

On `ℓ²(ℕ, ℂ)` there exists a
positive operator in `L^(1,∞)` that is not Dixmier measurable: two dilation-invariant generalized
limits assign it strictly different Dixmier traces.

```lean
TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable :
  ∃ T,
    T.IsPositive ∧
      T ∈
          ((TauCeti.OperatorIdealFamily.logarithmic ℂ).operatorGauge ↥(lp (fun x => ℂ) 2)
              ↥(lp (fun x => ℂ) 2)).finiteSubmodule ∧
        ¬TauCeti.IsDixmierMeasurable T
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ky Fan triangle inequality](../../../analysis/part-03/operator-ideal/ky-fan-triangle-inequality.md)
- [Ky Fan two-sided ideal inequality](../../../analysis/part-03/operator-ideal/ky-fan-two-sided-ideal-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Measurable.html#TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Measurable.html#TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable)
- [Source of `TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable` in TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Measurable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Measurable.lean#L678)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
