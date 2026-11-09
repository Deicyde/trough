---
declaration: theorem
origin: cited
lean: TauCeti.aestronglyMeasurable_iff_forall_inner, TauCeti.aestronglyMeasurable_strongDual_iff_forall_apply
statement: formalized
proof: formalized
---

# Pettis' theorem in a separable inner product space

A function into a separable inner
product space is almost everywhere strongly measurable exactly when it is weakly measurable, that
is, when each of its coordinates `t ↦ ⟪v, h t⟫` is almost everywhere strongly measurable.

```lean
TauCeti.aestronglyMeasurable_iff_forall_inner.{u_1, u_2, u_3} {α : Type u_1} {𝕜 : Type u_2}
  {E : Type u_3} {x✝ : MeasurableSpace α} {μ : MeasureTheory.Measure α} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [TopologicalSpace.SeparableSpace E] {h : α → E} :
  MeasureTheory.AEStronglyMeasurable h μ ↔
    ∀ (v : E), MeasureTheory.AEStronglyMeasurable (fun t => inner 𝕜 v (h t)) μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.aestronglyMeasurable_iff_forall_inner`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/StronglyMeasurable/Pettis.html#TauCeti.aestronglyMeasurable_iff_forall_inner).

## Other forms

**Pettis' theorem for the dual of a separable Hilbert space.** Formalized in Tau Ceti as [`TauCeti.aestronglyMeasurable_strongDual_iff_forall_apply`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/StronglyMeasurable/Pettis.html#TauCeti.aestronglyMeasurable_strongDual_iff_forall_apply).

```lean
TauCeti.aestronglyMeasurable_strongDual_iff_forall_apply.{u_1, u_2, u_3} {α : Type u_1}
  {𝕜 : Type u_2} {E : Type u_3} {x✝ : MeasurableSpace α} {μ : MeasureTheory.Measure α} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [TopologicalSpace.SeparableSpace E]
  [CompleteSpace E] {g : α → StrongDual 𝕜 E} :
  MeasureTheory.AEStronglyMeasurable g μ ↔
    ∀ (v : E), MeasureTheory.AEStronglyMeasurable (fun t => (g t) v) μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.aestronglyMeasurable_iff_forall_inner`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/StronglyMeasurable/Pettis.html#TauCeti.aestronglyMeasurable_iff_forall_inner)
- [Source of `TauCeti.aestronglyMeasurable_iff_forall_inner` in TauCeti/MeasureTheory/Function/StronglyMeasurable/Pettis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/StronglyMeasurable/Pettis.lean#L67)
