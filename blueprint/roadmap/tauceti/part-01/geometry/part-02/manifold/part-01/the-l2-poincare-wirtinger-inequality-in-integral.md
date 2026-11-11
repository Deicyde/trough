---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.exists_integral_sq_sub_average_le_mul_integral_norm_sq_mgradient
statement: formalized
proof: formalized
---

# The `L²` Poincaré–Wirtinger inequality in integral form

On a compact connected manifold
without boundary with a continuous Riemannian metric, there is a constant `C` such that
`∫ (u - ⨍ u)² dV ≤ C ∫ ‖∇u‖² dV` for every `C¹` function `u`.

```lean
TauCeti.Manifold.exists_integral_sq_sub_average_le_mul_integral_norm_sq_mgradient.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [CompactSpace M] [PreconnectedSpace M] :
  ∃ C,
    ∀ (u : M → ℝ),
      ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
        ∫ (x : M),
            (u x - ⨍ (y : M), u y ∂TauCeti.riemannianVolume I M) ^ 2 ∂TauCeti.riemannianVolume I M ≤
          ↑C * ∫ (x : M), ‖TauCeti.Manifold.mgradient I u x‖ ^ 2 ∂TauCeti.riemannianVolume I M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré–Wirtinger inequality on `H¹(M)`](../part-02/the-poincare-wirtinger-inequality-on-h1-m.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.exists_integral_sq_sub_average_le_mul_integral_norm_sq_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Poincare.html#TauCeti.Manifold.exists_integral_sq_sub_average_le_mul_integral_norm_sq_mgradient).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.exists_integral_sq_sub_average_le_mul_integral_norm_sq_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Poincare.html#TauCeti.Manifold.exists_integral_sq_sub_average_le_mul_integral_norm_sq_mgradient)
- [Source of `TauCeti.Manifold.exists_integral_sq_sub_average_le_mul_integral_norm_sq_mgradient` in TauCeti/Geometry/Manifold/Riemannian/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Poincare.lean#L195)
