---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le, TauCeti.Manifold.exists_lintegral_exp_mul_abs_rpow_le
statement: formalized
proof: formalized
---

# Trudinger's inequality near a point

Every point `c` of a manifold without boundary, of
dimension `n ≥ 2`, with a continuous Riemannian metric, has a neighbourhood `V` with constants
`β > 0` and `C` such that `∫_V exp (β |u| ^ (n / (n - 1))) dV ≤ C` for every `C¹` function `u`
with `‖∇u‖_{Lⁿ} + ‖u‖_{Lⁿ} ≤ 1`.

```lean
TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [LindelofSpace M] (hn : 2 ≤ Module.finrank ℝ E) (c : M) :
  ∃ V ∈ nhds c,
    ∃ β > 0,
      ∃ C,
        ∀ (u : M → ℝ),
          ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
            MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖)
                    (↑(Module.finrank ℝ E)) (TauCeti.riemannianVolume I M) +
                  MeasureTheory.eLpNorm u (↑(Module.finrank ℝ E)) (TauCeti.riemannianVolume I M) ≤
                1 →
              ∫⁻ (x : M) in V,
                  ENNReal.ofReal
                    (Real.exp
                      (β *
                        |u x| ^
                          (↑(Module.finrank ℝ E) /
                            (↑(Module.finrank ℝ E) - 1)))) ∂TauCeti.riemannianVolume I M ≤
                ↑C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Trudinger's inequality on `W^{1,n}_0(Ω)`](../../../../analysis/part-02/sobolev/part-02/trudingers-inequality-on-w-1-n-0.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Trudinger.html#TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le).

## Other forms

**Trudinger's inequality on a closed Riemannian manifold.** Formalized in Tau Ceti as [`TauCeti.Manifold.exists_lintegral_exp_mul_abs_rpow_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Trudinger.html#TauCeti.Manifold.exists_lintegral_exp_mul_abs_rpow_le).

```lean
TauCeti.Manifold.exists_lintegral_exp_mul_abs_rpow_le.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [CompactSpace M] (hn : 2 ≤ Module.finrank ℝ E) :
  ∃ β > 0,
    ∃ C,
      ∀ (u : M → ℝ),
        ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
          MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖)
                  (↑(Module.finrank ℝ E)) (TauCeti.riemannianVolume I M) +
                MeasureTheory.eLpNorm u (↑(Module.finrank ℝ E)) (TauCeti.riemannianVolume I M) ≤
              1 →
            ∫⁻ (x : M),
                ENNReal.ofReal
                  (Real.exp
                    (β *
                      |u x| ^
                        (↑(Module.finrank ℝ E) /
                          (↑(Module.finrank ℝ E) - 1)))) ∂TauCeti.riemannianVolume I M ≤
              ↑C
```

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Trudinger.html#TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le)
- [Source of `TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le` in TauCeti/Geometry/Manifold/Riemannian/Trudinger.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Trudinger.lean#L82)
