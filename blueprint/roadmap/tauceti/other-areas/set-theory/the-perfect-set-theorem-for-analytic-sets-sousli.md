---
declaration: theorem
origin: cited
lean: MeasureTheory.AnalyticSet.exists_nat_bool_injection_of_not_countable
statement: formalized
proof: formalized
---

# The perfect set theorem for analytic sets (Souslin)

An uncountable analytic subset of a
Hausdorff space contains the range of a continuous injection of Cantor space.

```lean
MeasureTheory.AnalyticSet.exists_nat_bool_injection_of_not_countable.{u} {X : Type u}
  [TopologicalSpace X] [T2Space X] {s : Set X} (hs : MeasureTheory.AnalyticSet s)
  (hunc : ¬s.Countable) : ∃ f, Set.range f ⊆ s ∧ Continuous f ∧ Function.Injective f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.AnalyticSet.exists_nat_bool_injection_of_not_countable`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/PerfectSet.html#MeasureTheory.AnalyticSet.exists_nat_bool_injection_of_not_countable).

## Sources

- [Tau Ceti documentation: `MeasureTheory.AnalyticSet.exists_nat_bool_injection_of_not_countable`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/PerfectSet.html#MeasureTheory.AnalyticSet.exists_nat_bool_injection_of_not_countable)
- [Source of `MeasureTheory.AnalyticSet.exists_nat_bool_injection_of_not_countable` in TauCeti/SetTheory/Descriptive/PerfectSet.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/SetTheory/Descriptive/PerfectSet.lean#L99)
