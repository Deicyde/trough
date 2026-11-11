---
declaration: theorem
origin: cited
lean: MeasureTheory.Integrable.exists_convexOn_superlinear_integrable
statement: formalized
proof: formalized
---

# De la Vallée Poussin's lemma

Every integrable function `f` remains integrable after
composing its norm with some convex, monotone function `Φ` with `Φ 0 = 0` that grows
superlinearly, `Φ t / t → ∞`.

```lean
MeasureTheory.Integrable.exists_convexOn_superlinear_integrable.{u_1, u_2} {α : Type u_1}
  {F : Type u_2} [MeasurableSpace α] [NormedAddCommGroup F] {μ : MeasureTheory.Measure α}
  {f : α → F} (hf : MeasureTheory.Integrable f μ) :
  ∃ Φ,
    Φ 0 = 0 ∧
      Monotone Φ ∧
        ConvexOn ℝ Set.univ Φ ∧
          Filter.Tendsto (fun t => Φ t / t) Filter.atTop Filter.atTop ∧
            MeasureTheory.Integrable (fun a => Φ ‖f a‖) μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Integrable.exists_convexOn_superlinear_integrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DeLaValleePoussin.html#MeasureTheory.Integrable.exists_convexOn_superlinear_integrable).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Integrable.exists_convexOn_superlinear_integrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DeLaValleePoussin.html#MeasureTheory.Integrable.exists_convexOn_superlinear_integrable)
- [Source of `MeasureTheory.Integrable.exists_convexOn_superlinear_integrable` in TauCeti/MeasureTheory/Function/DeLaValleePoussin.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/DeLaValleePoussin.lean#L116)
