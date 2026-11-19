---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.integral_norm_sq_le_mul_add_mul_integral_of_laplaceBeltrami
statement: formalized
proof: formalized
---

# The integrated Weitzenböck inequality for `α`

On a compact Riemannian manifold without
boundary, with a `C¹` Riemannian metric, let `α` and `Dα` be sections of families of seminormed
groups, standing for `α` and `∇_a α`, such that `|α|²` is of class `C²` and `|∇_a α|²` is
continuous, satisfying the projected Weitzenböck inequality
`-Δ|α|² / 2 + |∇_a α|² - (r / 4) (1 - |α|²) |α|² ≤ K₁` with the Laplace–Beltrami operator
`Δ = div ∘ grad`. Then

`∫ |∇_a α|² ≤ K₁ Vol(M) + (r / 4) ∫ (1 - |α|²) |α|²`

for the Riemannian volume.

```lean
TauCeti.SeibergWitten.integral_norm_sq_le_mul_add_mul_integral_of_laplaceBeltrami.{u_1, u_2, u_3,
    u_4, u_6}
  {r : ℝ} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [CompactSpace M] [IsManifold I (↑⊤) M]
  [MeasurableSpace M] [BorelSpace M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {F₁ : M → Type u_6} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (F₁ x)] {α : (x : M) → A x} {Dα : (x : M) → F₁ x} {K₁ : ℝ}
  (hα : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖α x‖ ^ 2)
  (hDα : Continuous fun x => ‖Dα x‖ ^ 2)
  (hW :
    ∀ (x : M),
      -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖α y‖ ^ 2) x / 2) + ‖Dα x‖ ^ 2 -
          r / 4 * (1 - ‖α x‖ ^ 2) * ‖α x‖ ^ 2 ≤
        K₁) :
  ∫ (x : M), ‖Dα x‖ ^ 2 ∂TauCeti.riemannianVolume I M ≤
    K₁ * TauCeti.riemannianTotalVolume I M +
      r / 4 * ∫ (x : M), (1 - ‖α x‖ ^ 2) * ‖α x‖ ^ 2 ∂TauCeti.riemannianVolume I M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The divergence theorem on a manifold without boundary](../../../../geometry/part-02/manifold/part-01/the-divergence-theorem-on-a-manifold-without-bou.md)
- [The Koszul formula](../../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.integral_norm_sq_le_mul_add_mul_integral_of_laplaceBeltrami`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.html#TauCeti.SeibergWitten.integral_norm_sq_le_mul_add_mul_integral_of_laplaceBeltrami).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.integral_norm_sq_le_mul_add_mul_integral_of_laplaceBeltrami`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.html#TauCeti.SeibergWitten.integral_norm_sq_le_mul_add_mul_integral_of_laplaceBeltrami)
- [Source of `TauCeti.SeibergWitten.integral_norm_sq_le_mul_add_mul_integral_of_laplaceBeltrami` in TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.lean#L338)
