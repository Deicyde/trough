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

- [Ky Fan triangle inequality](../../../analysis/part-04/operator-ideal/ky-fan-triangle-inequality.md)
- [Ky Fan two-sided ideal inequality](../../../analysis/part-04/operator-ideal/ky-fan-two-sided-ideal-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Measurable.html#TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Measurable.html#TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable)
- [Source of `TauCeti.exists_isPositive_mem_logarithmic_not_isDixmierMeasurable` in TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Measurable.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Measurable.lean#L678)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
