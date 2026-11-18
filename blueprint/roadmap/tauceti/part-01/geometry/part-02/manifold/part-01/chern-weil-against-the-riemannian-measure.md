---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.integral_inner_self_eq_two_mul_sub
statement: formalized
proof: formalized
---

# Chern–Weil against the Riemannian measure

On an oriented Riemannian manifold of dimension
`k + k` with `k` even, a compactly supported smooth `k`-form `α` has
`∫ |α|² = 2 ∫ |α⁺|² - ∫_M α ∧ α`, with the energies integrated against the Riemannian volume
measure. This combines
`TauCeti.SmoothForm.integralTopForm_inner_self_smul_riemannianVolumeForm_eq_add` and
`TauCeti.SmoothForm.integralTopForm_wedge_self`.

```lean
TauCeti.SmoothForm.integral_inner_self_eq_two_mul_sub.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [MeasurableSpace M] [BorelSpace M] [LindelofSpace M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {k : ℕ}
  (o : TauCeti.Manifold.Orientation I M (Fin (k + k))) (hk : Even k)
  {α : TauCeti.SmoothForm I M ℝ k} (hα : α ∈ TauCeti.compactlySupportedForms I M k) :
  ∫ (x : M),
      ((TauCeti.alternatingFormInner (TangentSpace I x) k) (↑α x))
        (↑α x) ∂TauCeti.riemannianVolume I M =
    2 *
        ∫ (x : M),
          ((TauCeti.alternatingFormInner (TangentSpace I x) k)
              (↑((TauCeti.SmoothForm.selfDualPart o) α) x))
            (↑((TauCeti.SmoothForm.selfDualPart o) α) x) ∂TauCeti.riemannianVolume I M -
      TauCeti.integralTopForm o (TauCeti.RoughForm.wedge ↑α ↑α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.SmoothForm.hodgeStar](../../../part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/tauceti-smoothform-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.integral_inner_self_eq_two_mul_sub`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/SelfDual/Measure.html#TauCeti.SmoothForm.integral_inner_self_eq_two_mul_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.integral_inner_self_eq_two_mul_sub`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/SelfDual/Measure.html#TauCeti.SmoothForm.integral_inner_self_eq_two_mul_sub)
- [Source of `TauCeti.SmoothForm.integral_inner_self_eq_two_mul_sub` in TauCeti/Geometry/Manifold/Riemannian/SelfDual/Measure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/SelfDual/Measure.lean#L49)
