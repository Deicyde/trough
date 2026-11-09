---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient
statement: formalized
proof: formalized
---

# The Poincaré–Wirtinger inequality on a closed Riemannian manifold

Let `1 ≤ p < ∞`, on a
compact connected manifold without boundary with a continuous Riemannian metric. There is a
constant `C` such that `‖u - ⨍ u‖_{Lᵖ} ≤ C ‖∇u‖_{Lᵖ}` for every `C¹` function `u`, where `⨍ u` is
the mean of `u` with respect to the Riemannian volume.

```lean
TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [CompactSpace M] [PreconnectedSpace M] {p : ENNReal} (hp : 1 ≤ p) (hp' : p ≠ ⊤) :
  ∃ C,
    ∀ (u : M → ℝ),
      ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
        MeasureTheory.eLpNorm (fun x => u x - ⨍ (y : M), u y ∂TauCeti.riemannianVolume I M) p
            (TauCeti.riemannianVolume I M) ≤
          ↑C *
            MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖) p
              (TauCeti.riemannianVolume I M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's bound on an average](../../../../measure-theory/integral/part-01/holders-bound-on-an-average.md)
- [The Poincaré–Wirtinger inequality on a ball](../../../../analysis/part-02/sobolev/part-02/the-poincare-wirtinger-inequality-on-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Poincare.html#TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Poincare.html#TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient)
- [Source of `TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient` in TauCeti/Geometry/Manifold/Riemannian/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Poincare.lean#L167)
