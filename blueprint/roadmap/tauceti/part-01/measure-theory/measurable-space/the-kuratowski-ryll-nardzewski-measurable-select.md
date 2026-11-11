---
declaration: theorem
origin: cited
lean: TauCeti.exists_measurable_forall_mem
statement: formalized
proof: formalized
---

# The Kuratowski–Ryll-Nardzewski measurable selection theorem

A map `M` from a measurable
space to the nonempty closed subsets of a Polish space, which is weakly measurable in the sense that
`{z | M z ∩ U ≠ ∅}` is measurable for every open `U`, has a measurable selection.

```lean
TauCeti.exists_measurable_forall_mem.{u_1, u_2} {Z : Type u_1} {X : Type u_2} [MeasurableSpace Z]
  [TopologicalSpace X] [PolishSpace X] [MeasurableSpace X] [BorelSpace X] {M : Z → Set X}
  (hclosed : ∀ (z : Z), IsClosed (M z)) (hne : ∀ (z : Z), (M z).Nonempty)
  (hM : ∀ (U : Set X), IsOpen U → MeasurableSet {z | (M z ∩ U).Nonempty}) :
  ∃ f, Measurable f ∧ ∀ (z : Z), f z ∈ M z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_measurable_forall_mem`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/MeasurableSpace/Selection.html#TauCeti.exists_measurable_forall_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_measurable_forall_mem`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/MeasurableSpace/Selection.html#TauCeti.exists_measurable_forall_mem)
- [Source of `TauCeti.exists_measurable_forall_mem` in TauCeti/MeasureTheory/MeasurableSpace/Selection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/MeasurableSpace/Selection.lean#L148)
