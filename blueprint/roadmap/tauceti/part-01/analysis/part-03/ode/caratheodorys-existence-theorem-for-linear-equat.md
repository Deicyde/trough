---
declaration: theorem
origin: cited
lean: TauCeti.exists_continuousOn_eq_forall_mem_Icc_eq_picard
statement: formalized
proof: formalized
---

# Carathéodory's existence theorem for linear equations

Let `M : ℝ → E →L[ℝ] E` be almost
everywhere strongly measurable and essentially bounded on `(a, b)`, and let `F : ℝ → E` be
integrable on `(a, b)`. Then the linear equation `x' = M(t) x + F(t)` with `x(a) = x₀` has a
solution in Carathéodory's sense: a curve `x` continuous on `[a, b]` with `x a = x₀` and
`x t = x₀ + ∫ s in a..t, (M s (x s) + F s)` for every `t ∈ [a, b]`.

```lean
TauCeti.exists_continuousOn_eq_forall_mem_Icc_eq_picard.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {M : ℝ → E →L[ℝ] E} {F : ℝ → E} {a b K : ℝ} [CompleteSpace E]
  (hM : MeasureTheory.AEStronglyMeasurable M (MeasureTheory.volume.restrict (Set.Ioo a b)))
  (hK : ∀ᵐ (t : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo a b), ‖M t‖ ≤ K)
  (hF : MeasureTheory.IntegrableOn F (Set.Ioo a b) MeasureTheory.volume) (x₀ : E) :
  ∃ x,
    ContinuousOn x (Set.Icc a b) ∧
      x a = x₀ ∧ ∀ t ∈ Set.Icc a b, x t = ODE.picard (fun s y => (M s) y + F s) a x₀ x t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_continuousOn_eq_forall_mem_Icc_eq_picard`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Caratheodory.html#TauCeti.exists_continuousOn_eq_forall_mem_Icc_eq_picard).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_continuousOn_eq_forall_mem_Icc_eq_picard`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Caratheodory.html#TauCeti.exists_continuousOn_eq_forall_mem_Icc_eq_picard)
- [Source of `TauCeti.exists_continuousOn_eq_forall_mem_Icc_eq_picard` in TauCeti/Analysis/ODE/Caratheodory.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/ODE/Caratheodory.lean#L191)
