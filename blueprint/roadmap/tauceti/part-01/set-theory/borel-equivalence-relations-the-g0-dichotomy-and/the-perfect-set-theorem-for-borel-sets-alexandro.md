---
declaration: theorem
origin: cited
lean: MeasurableSet.exists_nat_bool_injection_of_not_countable
statement: formalized
proof: formalized
---

# The perfect set theorem for Borel sets (Alexandrov–Hausdorff)

An uncountable Borel
subset of a Polish space contains the range of a continuous injection of Cantor space.

```lean
MeasurableSet.exists_nat_bool_injection_of_not_countable.{u} {X : Type u} [TopologicalSpace X]
  [PolishSpace X] [MeasurableSpace X] [BorelSpace X] {s : Set X} (hs : MeasurableSet s)
  (hunc : ¬s.Countable) : ∃ f, Set.range f ⊆ s ∧ Continuous f ∧ Function.Injective f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasurableSet.exists_nat_bool_injection_of_not_countable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Perfect.html#MeasurableSet.exists_nat_bool_injection_of_not_countable).

## Sources

- [Tau Ceti documentation: `MeasurableSet.exists_nat_bool_injection_of_not_countable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Perfect.html#MeasurableSet.exists_nat_bool_injection_of_not_countable)
- [Source of `MeasurableSet.exists_nat_bool_injection_of_not_countable` in TauCeti/MeasureTheory/Constructions/Polish/Perfect.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Constructions/Polish/Perfect.lean#L49)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)
