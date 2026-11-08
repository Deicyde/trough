---
declaration: theorem
origin: cited
lean: SetRel.exists_measurableSet_isIndependent_superset, SimpleGraph.g0_dichotomy
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

## Proof depends on

- [Miller's independence lemma](millers-independence-lemma.md)

## Lean

Formalized in Tau Ceti as [`SetRel.exists_measurableSet_isIndependent_superset`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/BorelColoring.html#SetRel.exists_measurableSet_isIndependent_superset).

## Other forms

**The Kechris–Solecki–Todorcevic G₀ dichotomy.** Formalized in Tau Ceti as [`SimpleGraph.g0_dichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GZeroDichotomy.html#SimpleGraph.g0_dichotomy).

```lean
SimpleGraph.g0_dichotomy.{u_1} {X : Type u_1} [TopologicalSpace X] [PolishSpace X]
  [MeasurableSpace X] [BorelSpace X] (G : SimpleGraph X)
  (hG : MeasureTheory.AnalyticSet {p | G.Adj p.1 p.2}) :
  Xor (∃ c, Measurable ⇑c) (∃ φ, Continuous ⇑φ)
```

## Sources

- [Tau Ceti documentation: `SetRel.exists_measurableSet_isIndependent_superset`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/BorelColoring.html#SetRel.exists_measurableSet_isIndependent_superset)
- [Source of `SetRel.exists_measurableSet_isIndependent_superset` in TauCeti/SetTheory/Descriptive/BorelColoring.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/SetTheory/Descriptive/BorelColoring.lean#L183)
