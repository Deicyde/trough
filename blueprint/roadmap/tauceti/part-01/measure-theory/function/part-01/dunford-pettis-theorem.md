---
declaration: theorem
origin: cited
lean: MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_unifIntegrable, MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_forall_setIntegral_le, MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_uniformIntegrable, MeasureTheory.Lp.isCompact_closure_toWeakSpace_of_uniformIntegrable, MeasureTheory.Lp.uniformIntegrable_of_isCompact_closure_toWeakSpace
statement: formalized
proof: formalized
---

# Dunford–Pettis theorem

For a finite measure, a subset of scalar `L¹` has weakly compact
closure exactly when it is norm bounded and uniformly integrable.

```lean
MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_unifIntegrable.{u_1, u_2}
  {α : Type u_1} {𝕜 : Type u_2} [RCLike 𝕜] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α}
  [MeasureTheory.IsFiniteMeasure μ] {A : Set ↥(MeasureTheory.Lp 𝕜 1 μ)} :
  IsCompact (closure (⇑(toWeakSpace 𝕜 ↥(MeasureTheory.Lp 𝕜 1 μ)) '' A)) ↔
    Bornology.IsBounded A ∧ MeasureTheory.UnifIntegrable (fun f => ↑↑↑f) 1 μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Grothendieck's lemma](../../../analysis/part-01/banach-space-theory/part-02/grothendiecks-lemma.md)
- [Milman–Pettis theorem](../../../analysis/part-02/convex/milman-pettis-theorem.md)
- [Šmulian's theorem](../../../analysis/part-01/banach-space-theory/part-02/smulians-theorem.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_unifIntegrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/L1Space/WeakCompact.html#MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_unifIntegrable).

## Other forms

**Dunford–Pettis theorem, classical form.** Formalized in Tau Ceti as [`MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_forall_setIntegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/L1Space/WeakCompact.html#MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_forall_setIntegral_le).

```lean
MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_forall_setIntegral_le.{u_1, u_2}
  {α : Type u_1} {𝕜 : Type u_2} [RCLike 𝕜] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α}
  [MeasureTheory.IsFiniteMeasure μ] {A : Set ↥(MeasureTheory.Lp 𝕜 1 μ)} :
  IsCompact (closure (⇑(toWeakSpace 𝕜 ↥(MeasureTheory.Lp 𝕜 1 μ)) '' A)) ↔
    Bornology.IsBounded A ∧
      ∀ ε > 0,
        ∃ δ > 0,
          ∀ f ∈ A,
            ∀ (s : Set α), MeasurableSet s → μ s ≤ ENNReal.ofReal δ → ∫ (x : α) in s, ‖↑↑f x‖ ∂μ ≤ ε
```

**Dunford–Pettis theorem.** Formalized in Tau Ceti as [`MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_uniformIntegrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/L1Space/WeakCompact.html#MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_uniformIntegrable).

```lean
MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_uniformIntegrable.{u_1, u_2} {α : Type u_1}
  {𝕜 : Type u_2} [RCLike 𝕜] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α}
  [MeasureTheory.IsFiniteMeasure μ] {A : Set ↥(MeasureTheory.Lp 𝕜 1 μ)} :
  IsCompact (closure (⇑(toWeakSpace 𝕜 ↥(MeasureTheory.Lp 𝕜 1 μ)) '' A)) ↔
    MeasureTheory.UniformIntegrable (fun f => ↑↑↑f) 1 μ
```

**Dunford–Pettis theorem, sufficiency.** Formalized in Tau Ceti as [`MeasureTheory.Lp.isCompact_closure_toWeakSpace_of_uniformIntegrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/L1Space/WeakCompact.html#MeasureTheory.Lp.isCompact_closure_toWeakSpace_of_uniformIntegrable).

```lean
MeasureTheory.Lp.isCompact_closure_toWeakSpace_of_uniformIntegrable.{u_1, u_2} {α : Type u_1}
  {𝕜 : Type u_2} [RCLike 𝕜] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α}
  [MeasureTheory.IsFiniteMeasure μ] {A : Set ↥(MeasureTheory.Lp 𝕜 1 μ)}
  (hA : MeasureTheory.UniformIntegrable (fun f => ↑↑↑f) 1 μ) :
  IsCompact (closure (⇑(toWeakSpace 𝕜 ↥(MeasureTheory.Lp 𝕜 1 μ)) '' A))
```

**Dunford–Pettis theorem, necessity.** Formalized in Tau Ceti as [`MeasureTheory.Lp.uniformIntegrable_of_isCompact_closure_toWeakSpace`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/L1Space/WeakCompact.html#MeasureTheory.Lp.uniformIntegrable_of_isCompact_closure_toWeakSpace).

```lean
MeasureTheory.Lp.uniformIntegrable_of_isCompact_closure_toWeakSpace.{u_1, u_2} {α : Type u_1}
  {𝕜 : Type u_2} [RCLike 𝕜] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α}
  {A : Set ↥(MeasureTheory.Lp 𝕜 1 μ)}
  (hA : IsCompact (closure (⇑(toWeakSpace 𝕜 ↥(MeasureTheory.Lp 𝕜 1 μ)) '' A))) :
  MeasureTheory.UniformIntegrable (fun f => ↑↑↑f) 1 μ
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_unifIntegrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/L1Space/WeakCompact.html#MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_unifIntegrable)
- [Source of `MeasureTheory.Lp.isCompact_closure_toWeakSpace_iff_isBounded_and_unifIntegrable` in TauCeti/MeasureTheory/Function/L1Space/WeakCompact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/L1Space/WeakCompact.lean#L215)
