---
declaration: theorem
origin: cited
lean: SetRel.exists_measurableSet_isIndependent_superset
statement: formalized
proof: formalized
---

# The Kechris–Solecki–Todorcevic lemma

In a Hausdorff space with its Borel σ-algebra, an
analytic independent set of an analytic relation is contained in a Borel independent set.

```lean
SetRel.exists_measurableSet_isIndependent_superset.{u_1} {X : Type u_1} {G : SetRel X X} {A : Set X}
  [TopologicalSpace X] [T2Space X] [MeasurableSpace X] [BorelSpace X]
  (hG : MeasureTheory.AnalyticSet G) (hA : MeasureTheory.AnalyticSet A) (hind : G.IsIndependent A) :
  ∃ B, MeasurableSet B ∧ A ⊆ B ∧ G.IsIndependent B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SetRel.exists_measurableSet_isIndependent_superset`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/BorelColoring.html#SetRel.exists_measurableSet_isIndependent_superset).

## Sources

- [Tau Ceti documentation: `SetRel.exists_measurableSet_isIndependent_superset`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/BorelColoring.html#SetRel.exists_measurableSet_isIndependent_superset)
- [Source of `SetRel.exists_measurableSet_isIndependent_superset` in TauCeti/SetTheory/Descriptive/BorelColoring.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/SetTheory/Descriptive/BorelColoring.lean#L183)
