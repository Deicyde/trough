---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.exists_mem_nhds_eLpNorm_restrict_le_mul_eLpNorm_mgradient_add, TauCeti.Manifold.exists_eLpNorm_le_mul_eLpNorm_mgradient_two_add, TauCeti.Manifold.exists_integral_abs_rpow_rpow_le_mul_integral_mgradient_sq_add, TauCeti.Manifold.exists_eLpNorm_le_mul_eLpNorm_mgradient_add
statement: formalized
proof: formalized
---

# The Sobolev inequality near a point

Let `1 ≤ p` and let `p'` be the Sobolev conjugate
exponent, `1 / p' = 1 / p - 1 / n`, on a manifold without boundary of dimension `n > 0` with a
continuous Riemannian metric. Every point `c` has a neighbourhood `V` with a constant `C` such that
`‖u‖_{L^{p'}(V)} ≤ C (‖∇u‖_{Lᵖ} + ‖u‖_{Lᵖ})` for every `C¹` function `u`.

```lean
TauCeti.Manifold.exists_mem_nhds_eLpNorm_restrict_le_mul_eLpNorm_mgradient_add.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [LindelofSpace M] {p p' : NNReal} (hp : 1 ≤ p) (hn : 0 < Module.finrank ℝ E)
  (hp' : (↑p')⁻¹ = ↑p⁻¹ - (↑(Module.finrank ℝ E))⁻¹) (c : M) :
  ∃ V ∈ nhds c,
    ∃ C,
      ∀ (u : M → ℝ),
        ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
          MeasureTheory.eLpNorm u (↑p') ((TauCeti.riemannianVolume I M).restrict V) ≤
            ↑C *
              (MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖) (↑p)
                  (TauCeti.riemannianVolume I M) +
                MeasureTheory.eLpNorm u (↑p) (TauCeti.riemannianVolume I M))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.exists_mem_nhds_eLpNorm_restrict_le_mul_eLpNorm_mgradient_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Basic.html#TauCeti.Manifold.exists_mem_nhds_eLpNorm_restrict_le_mul_eLpNorm_mgradient_add).

## Other forms

**The Sobolev inequality for `H¹` on a closed Riemannian manifold.** Formalized in Tau Ceti as [`TauCeti.Manifold.exists_eLpNorm_le_mul_eLpNorm_mgradient_two_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Basic.html#TauCeti.Manifold.exists_eLpNorm_le_mul_eLpNorm_mgradient_two_add).

```lean
TauCeti.Manifold.exists_eLpNorm_le_mul_eLpNorm_mgradient_two_add.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [CompactSpace M] (hn : 2 < Module.finrank ℝ E) :
  ∃ C,
    ∀ (u : M → ℝ),
      ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
        MeasureTheory.eLpNorm u
            (ENNReal.ofReal (2 * ↑(Module.finrank ℝ E) / (↑(Module.finrank ℝ E) - 2)))
            (TauCeti.riemannianVolume I M) ≤
          ↑C *
            (MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖) 2
                (TauCeti.riemannianVolume I M) +
              MeasureTheory.eLpNorm u 2 (TauCeti.riemannianVolume I M))
```

**The Sobolev inequality for `H¹` with integrals.** Formalized in Tau Ceti as [`TauCeti.Manifold.exists_integral_abs_rpow_rpow_le_mul_integral_mgradient_sq_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Basic.html#TauCeti.Manifold.exists_integral_abs_rpow_rpow_le_mul_integral_mgradient_sq_add).

```lean
TauCeti.Manifold.exists_integral_abs_rpow_rpow_le_mul_integral_mgradient_sq_add.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [CompactSpace M] (hn : 2 < Module.finrank ℝ E) :
  ∃ K,
    0 < K ∧
      ∀ (u : M → ℝ),
        ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
          (∫ (x : M),
                |u x| ^
                  (2 * ↑(Module.finrank ℝ E) /
                    (↑(Module.finrank ℝ E) - 2)) ∂TauCeti.riemannianVolume I M) ^
              (2 / (2 * ↑(Module.finrank ℝ E) / (↑(Module.finrank ℝ E) - 2))) ≤
            K *
              (∫ (x : M), ‖TauCeti.Manifold.mgradient I u x‖ ^ 2 ∂TauCeti.riemannianVolume I M +
                ∫ (x : M), u x ^ 2 ∂TauCeti.riemannianVolume I M)
```

**The Sobolev inequality on a closed Riemannian manifold.** Formalized in Tau Ceti as [`TauCeti.Manifold.exists_eLpNorm_le_mul_eLpNorm_mgradient_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Basic.html#TauCeti.Manifold.exists_eLpNorm_le_mul_eLpNorm_mgradient_add).

```lean
TauCeti.Manifold.exists_eLpNorm_le_mul_eLpNorm_mgradient_add.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [CompactSpace M] {p p' : NNReal} (hp : 1 ≤ p) (hn : 0 < Module.finrank ℝ E)
  (hp' : (↑p')⁻¹ = ↑p⁻¹ - (↑(Module.finrank ℝ E))⁻¹) :
  ∃ C,
    ∀ (u : M → ℝ),
      ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
        MeasureTheory.eLpNorm u (↑p') (TauCeti.riemannianVolume I M) ≤
          ↑C *
            (MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖) (↑p)
                (TauCeti.riemannianVolume I M) +
              MeasureTheory.eLpNorm u (↑p) (TauCeti.riemannianVolume I M))
```

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.exists_mem_nhds_eLpNorm_restrict_le_mul_eLpNorm_mgradient_add`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Basic.html#TauCeti.Manifold.exists_mem_nhds_eLpNorm_restrict_le_mul_eLpNorm_mgradient_add)
- [Source of `TauCeti.Manifold.exists_mem_nhds_eLpNorm_restrict_le_mul_eLpNorm_mgradient_add` in TauCeti/Geometry/Manifold/Riemannian/Sobolev/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Basic.lean#L81)
