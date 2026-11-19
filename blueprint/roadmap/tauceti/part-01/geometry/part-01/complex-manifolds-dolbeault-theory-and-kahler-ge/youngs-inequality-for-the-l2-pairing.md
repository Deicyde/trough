---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.neg_add_le_two_mul_integralTopForm_inner
statement: formalized
proof: formalized
---

# Young's inequality for the `L²` pairing

on an oriented Riemannian manifold of positive
dimension `m = k + l`, compactly supported smooth `k`-forms satisfy
`-(∫_M |α|² vol + ∫_M |β|² vol) ≤ 2 ∫_M ⟨α, β⟩ vol`, from `0 ≤ ∫_M |α + β|² vol`.

```lean
TauCeti.SmoothForm.neg_add_le_two_mul_integralTopForm_inner.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {m k l : ℕ} [NeZero m]
  (o : TauCeti.Manifold.Orientation I M (Fin m)) (hkl : k + l = m)
  {α β : TauCeti.SmoothForm I M ℝ k} (hα : α ∈ TauCeti.compactlySupportedForms I M k)
  (hβ : β ∈ TauCeti.compactlySupportedForms I M k) :
  -((TauCeti.integralTopForm o fun x =>
          ((TauCeti.alternatingFormInner (TangentSpace I x) k) (↑α x)) (↑α x) •
            TauCeti.riemannianVolumeForm o x) +
        TauCeti.integralTopForm o fun x =>
          ((TauCeti.alternatingFormInner (TangentSpace I x) k) (↑β x)) (↑β x) •
            TauCeti.riemannianVolumeForm o x) ≤
    2 *
      TauCeti.integralTopForm o fun x =>
        ((TauCeti.alternatingFormInner (TangentSpace I x) k) (↑α x)) (↑β x) •
          TauCeti.riemannianVolumeForm o x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.SmoothForm.hodgeStar](tauceti-smoothform-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.neg_add_le_two_mul_integralTopForm_inner`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Codifferential.html#TauCeti.SmoothForm.neg_add_le_two_mul_integralTopForm_inner).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.neg_add_le_two_mul_integralTopForm_inner`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Codifferential.html#TauCeti.SmoothForm.neg_add_le_two_mul_integralTopForm_inner)
- [Source of `TauCeti.SmoothForm.neg_add_le_two_mul_integralTopForm_inner` in TauCeti/Geometry/Manifold/Riemannian/Codifferential.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Codifferential.lean#L829)
